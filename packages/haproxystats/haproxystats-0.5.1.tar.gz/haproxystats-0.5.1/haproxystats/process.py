# vim:fenc=utf-8
# pylint: disable=too-many-locals
# pylint: disable=too-many-branches
"""Processes statistics from HAProxy and pushes them to Graphite.

Usage:
    haproxystats-process [-f <file>] [-d <dir>] [-p | -P]

Options:
    -f, --file <file>  configuration file with settings
                       [default: /etc/haproxystats.conf]
    -d, --dir <dir>    directory with additional configuration files
    -p, --print        show default settings
    -P, --print-conf   show configuration
    -h, --help         show this screen
    -v, --version      show version
"""
import os
import multiprocessing
import signal
import logging
import glob
import copy
import re
import sys
import time
import shutil
import socket
import fileinput
from collections import defaultdict
from configparser import ConfigParser, ExtendedInterpolation, ParsingError
from threading import Lock, Thread
from docopt import docopt
import pyinotify
import pandas

from haproxystats import __version__ as VERSION
from haproxystats import DEFAULT_OPTIONS
from haproxystats.utils import (dispatcher, GraphiteHandler, get_files,
                                FileHandler, EventHandler, concat_csv,
                                FILE_SUFFIX_INFO, FILE_SUFFIX_STAT,
                                load_file_content, configuration_check,
                                read_write_access, check_metrics,
                                daemon_percentage_metrics, send_wlc,
                                calculate_percentage_per_column,
                                calculate_percentage_per_row)
from haproxystats.metrics import (DAEMON_AVG_METRICS, DAEMON_METRICS,
                                  SERVER_AVG_METRICS, SERVER_METRICS,
                                  BACKEND_AVG_METRICS, BACKEND_METRICS,
                                  FRONTEND_METRICS)

LOG_FORMAT = ('%(asctime)s [%(process)d] [%(processName)-11s] '
              '[%(funcName)-20s] %(levelname)-8s %(message)s')
logging.basicConfig(format=LOG_FORMAT)
log = logging.getLogger('root')  # pylint: disable=I0011,C0103

watcher = pyinotify.WatchManager()  # pylint: disable=I0011,C0103
# watched events
MASK = pyinotify.IN_CREATE | pyinotify.IN_MOVED_TO  # pylint: disable=no-member

STOP_SIGNAL = 'STOP'


class Checker(Thread):
    """Check the liveness of consumer"""
    def __init__(self, consumers, interval):
        """Initialization.

        Arguments:
            consumers (list): A list of consumers(multiprocessing.Process obj)
            interval (float): How often to run the check
        """
        super(Checker, self).__init__()
        self.daemon = True
        self.consumers = consumers
        self.interval = interval

    def run(self):
        """Terminate main program if at least one consumer isn't alive"""
        while True:
            alive_consumers = 0
            for consumer in self.consumers:
                if not consumer.is_alive():
                    log.critical("consumer %s is dead", consumer.name)
                else:
                    alive_consumers += 1
                    log.debug("consumer %s is alive", consumer.name)
            if alive_consumers < len(self.consumers):
                log.critical("terminating myself as %s consumers are dead",
                             len(self.consumers) - alive_consumers)
                os.kill(os.getpid(), signal.SIGTERM)

            time.sleep(self.interval)

class Consumer(multiprocessing.Process):
    """Process statistics and dispatch them to handlers."""

    # Cache results of the get_metric_paths() function call
    path_cache = {
        'frontend': {},
        'backend': {},
        'server': {}
    }

    # Store compiled patterns declared in the 'frontend-groups' and
    # 'backend-groups' config sections
    metric_patterns = {
        'frontend': [],
        'backend': [],
        'server': [],
    }

    def __init__(self, tasks, config):
        """Initialization.

        Arguments:
            tasks (queue): A queue from which we consume items.
            config (obj): A configParser object which holds configuration.
        """
        multiprocessing.Process.__init__(self)
        self.tasks = tasks
        self.config = config
        self.local_store = None
        self.file_handler = None
        self.timestamp = None  # The time that statistics were retrieved

        # Build graphite path (<namespace>.<hostname>.haproxy)
        graphite_tree = []
        graphite_tree.append(self.config.get('graphite', 'namespace'))
        if self.config.getboolean('graphite', 'prefix-hostname'):
            if self.config.getboolean('graphite', 'fqdn'):
                graphite_tree.append(socket.gethostname().replace('.', '_'))
            else:
                graphite_tree.append(socket.gethostname().split('.')[0])
        graphite_tree.append('haproxy')
        self.graphite_path = '.'.join(graphite_tree)

        # Compile regex patterns for metric groups
        if self.config.has_option('graphite', 'group-namespace'):
            self.build_metric_patterns()
            self.double_writes =\
                self.config.getboolean('graphite',
                                       'group-namespace-double-writes')
        else:
            self.double_writes = False


    def run(self):
        """Consume item from queue and process it.

        It is the target function of Process class. Consumes items from
        the queue, processes data which are pulled down by haproxystats-pull
        program and uses Pandas to perform all computations of statistics.

        It exits when it receives STOP_SIGNAL as item.

        To avoid orphan processes on the system, it must be robust against
        failures and try very hard recover from failures.
        """
        if self.config.has_section('local-store'):
            self.local_store = self.config.get('local-store', 'dir')
            self.file_handler = FileHandler()
            dispatcher.register('open', self.file_handler.open)
            dispatcher.register('send', self.file_handler.send)
            dispatcher.register('flush', self.file_handler.flush)
            dispatcher.register('loop', self.file_handler.loop)

        timeout = self.config.getfloat('graphite', 'timeout')
        connect_timeout = self.config.getfloat('graphite',
                                               'connect-timeout',
                                               fallback=timeout)
        write_timeout = self.config.getfloat('graphite',
                                             'write-timeout',
                                             fallback=timeout)
        graphite = GraphiteHandler(
            server=self.config.get('graphite', 'server'),
            port=self.config.getint('graphite', 'port'),
            connect_timeout=connect_timeout,
            write_timeout=write_timeout,
            retries=self.config.getint('graphite', 'retries'),
            interval=self.config.getfloat('graphite', 'interval'),
            delay=self.config.getfloat('graphite', 'delay'),
            backoff=self.config.getfloat('graphite', 'backoff'),
            queue_size=self.config.getint('graphite', 'queue-size')
        )
        dispatcher.register('open', graphite.open)
        dispatcher.register('send', graphite.send)

        dispatcher.signal('open')

        try:
            while True:
                log.info('waiting for item from the queue')
                incoming_dir = self.tasks.get()
                log.info('received item %s', incoming_dir)
                if incoming_dir == STOP_SIGNAL:
                    break
                start_time = time.time()

                # incoming_dir => /var/lib/haproxystats/incoming/1454016646
                # timestamp => 1454016646
                self.timestamp = os.path.basename(incoming_dir)

                # update filename for file handler.
                # This *does not* error if a file handler is not registered.
                dispatcher.signal('loop',
                                  local_store=self.local_store,
                                  timestamp=self.timestamp)

                self.process_stats(incoming_dir)

                # This flushes data to file
                dispatcher.signal('flush')

                # Remove directory as data have been successfully processed.
                log.debug('removing %s', incoming_dir)
                try:
                    shutil.rmtree(incoming_dir)
                except (FileNotFoundError, PermissionError, OSError) as exc:
                    log.critical('failed to remove directory %s with:%s. '
                                 'This should not have happened as it means '
                                 'another worker processed data from this '
                                 'directory or something/someone removed the '
                                 'directory!', incoming_dir, exc)
                elapsed_time = time.time() - start_time
                log.info('total wall clock time in seconds %.3f', elapsed_time)
                data = ("{p}.haproxystats.{m} {v} {t}\n"
                        .format(p=self.graphite_path,
                                m='TotalWallClockTime',
                                v="{t:.3f}".format(t=elapsed_time),
                                t=self.timestamp))
                dispatcher.signal('send', data=data)
                log.info('finished with %s', incoming_dir)
        except KeyboardInterrupt:
            log.critical('Ctrl-C received')

        return

    @send_wlc(output=dispatcher, name='AllStats')
    def process_stats(self, pathname):
        """Delegate the processing of statistics to other functions.

        Arguments:
            pathname (str): Directory where statistics from HAProxy are saved.
        """
        # statistics for HAProxy daemon and for frontend/backend/server have
        # different format and haproxystats-pull save them using a different
        # file suffix, so we can distinguish them easier.
        files = get_files(pathname, FILE_SUFFIX_INFO)
        if not files:
            log.warning("%s directory doesn't contain any files with HAProxy "
                        "daemon statistics", pathname)
        else:
            self.haproxy_stats(files)
        files = get_files(pathname, FILE_SUFFIX_STAT)

        if not files:
            log.warning("%s directory doesn't contain any files with site "
                        "statistics", pathname)
        else:
            self.sites_stats(files)

    @send_wlc(output=dispatcher, name='HAProxy')
    def haproxy_stats(self, files):
        """Process statistics for HAProxy daemon.

        Arguments:
            files (list): A list of files which contain the output of 'show
            info' command on the stats socket.
        """
        cnt_metrics = 1  # a metric counter
        log.info('processing statistics for HAProxy daemon')
        log.debug('processing files %s', ' '.join(files))
        raw_info_stats = defaultdict(list)
        # Parse raw data and build a data structure, input looks like:
        #     Name: HAProxy
        #     Version: 1.6.3-4d747c-52
        #     Release_date: 2016/02/25
        #     Nbproc: 4
        #     Uptime_sec: 59277
        #     SslFrontendSessionReuse_pct: 0
        #     ....
        with fileinput.input(files=files) as file_input:
            for line in file_input:
                if ': ' in line:
                    key, value = line.split(': ', 1)
                    try:
                        numeric_value = int(value)
                    except ValueError:
                        pass
                    else:
                        raw_info_stats[key].append(numeric_value)

        if not raw_info_stats:
            log.error('failed to parse daemon statistics')
            return
        else:
            # Here is where Pandas enters and starts its magic.
            try:
                dataframe = pandas.DataFrame(raw_info_stats)
            except ValueError as exc:
                log.error('failed to create Pandas object for daemon '
                          'statistics %s', exc)
                return

            sums = dataframe.loc[:, DAEMON_METRICS].sum()
            avgs = dataframe.loc[:, DAEMON_AVG_METRICS].mean()
            cnt_metrics += sums.size + avgs.size

            # Pandas did all the hard work, let's join above tables and extract
            # statistics
            for values in pandas.concat([sums, avgs], axis=0).items():
                data = ("{p}.daemon.{m} {v} {t}\n"
                        .format(p=self.graphite_path,
                                m=values[0].replace('.', '_'),
                                v=values[1],
                                t=self.timestamp))
                dispatcher.signal('send', data=data)

            dataframe['CpuUsagePct'] = (dataframe.loc[:, 'Idle_pct']
                                        .map(lambda x: (x * -1) + 100))
            if dataframe.loc[:, 'Idle_pct'].size > 1:
                log.info('calculating percentiles for CpuUsagePct')
                percentiles = (dataframe.loc[:, 'CpuUsagePct']
                               .quantile(q=[0.25, 0.50, 0.75, 0.95, 0.99],
                                         interpolation='nearest'))
                for per in percentiles.items():
                    # per[0] = index => [0.25, 0.50, 0.75, 0.95, 0.99]
                    # per[1] = percentile value
                    cnt_metrics += 1
                    data = ("{p}.daemon.{m} {v} {t}\n"
                            .format(p=self.graphite_path,
                                    m=("{:.2f}PercentileCpuUsagePct"
                                       .format(per[0]).split('.')[1]),
                                    v=per[1],
                                    t=self.timestamp))
                    dispatcher.signal('send', data=data)

                cnt_metrics += 1
                data = ("{p}.daemon.{m} {v} {t}\n"
                        .format(p=self.graphite_path,
                                m="StdCpuUsagePct",
                                v=dataframe.loc[:, 'CpuUsagePct'].std(),
                                t=self.timestamp))
                dispatcher.signal('send', data=data)

            if self.config.getboolean('process', 'calculate-percentages'):
                for metric in daemon_percentage_metrics():
                    cnt_metrics += 1
                    log.info('calculating percentage for %s', metric.name)
                    try:
                        value = calculate_percentage_per_column(dataframe,
                                                                metric)
                    except KeyError:
                        log.warning("metric %s doesn't exist", metric.name)
                    else:
                        data = ("{p}.daemon.{m} {v} {t}\n"
                                .format(p=self.graphite_path,
                                        m=metric.title,
                                        v=value,
                                        t=self.timestamp))
                        dispatcher.signal('send', data=data)

            if self.config.getboolean('process', 'per-process-metrics'):
                log.info("processing statistics per daemon")
                indexed_by_worker = dataframe.set_index('Process_num')
                metrics_per_worker = (indexed_by_worker
                                      .loc[:, DAEMON_METRICS
                                           + ['CpuUsagePct']
                                           + DAEMON_AVG_METRICS])
                cnt_metrics += metrics_per_worker.size

                for worker, row in metrics_per_worker.iterrows():
                    for values in row.iteritems():
                        data = ("{p}.daemon.process.{w}.{m} {v} {t}\n"
                                .format(p=self.graphite_path,
                                        w=worker,
                                        m=values[0].replace('.', '_'),
                                        v=values[1],
                                        t=self.timestamp))
                        dispatcher.signal('send', data=data)

                if self.config.getboolean('process', 'calculate-percentages'):
                    for metric in daemon_percentage_metrics():
                        log.info('calculating percentage for %s per daemon',
                                 metric.name)
                        _percentages = (metrics_per_worker
                                        .loc[:, [metric.limit, metric.name]]
                                        .apply(calculate_percentage_per_row,
                                               axis=1,
                                               args=(metric,)))

                        cnt_metrics += _percentages.size
                        for worker, row in _percentages.iterrows():
                            for values in row.iteritems():
                                data = ("{p}.daemon.process.{w}.{m} {v} {t}\n"
                                        .format(p=self.graphite_path,
                                                w=worker,
                                                m=values[0].replace('.', '_'),
                                                v=values[1],
                                                t=self.timestamp))
                                dispatcher.signal('send', data=data)

            data = ("{p}.haproxystats.MetricsHAProxy {v} {t}\n"
                    .format(p=self.graphite_path,
                            v=cnt_metrics,
                            t=self.timestamp))
            dispatcher.signal('send', data=data)

            log.info('number of HAProxy metrics %s', cnt_metrics)
            log.info('finished processing statistics for HAProxy daemon')

    def sites_stats(self, files):
        """Process statistics for frontends/backends/servers.

        Arguments:
            files (list): A list of files which contain the output of 'show
            stat' command on the stats socket of HAProxy.
        """
        log.info('processing statistics for sites')
        log.debug('processing files %s', ' '.join(files))
        log.debug('merging multiple csv files to one Pandas data frame')
        data_frame = concat_csv(files)
        excluded_backends = []

        if data_frame is not None:
            # Perform some sanitization on the raw data
            if '# pxname' in data_frame.columns:
                log.debug('replace "# pxname" column with  "pxname"')
                data_frame.rename(columns={'# pxname': 'pxname'}, inplace=True)
            if 'Unnamed: 62' in data_frame.columns:
                log.debug('remove "Unnamed: 62" column')
                try:
                    data_frame.drop(labels=['Unnamed: 62'],
                                    axis=1,
                                    inplace=True)
                except ValueError as error:
                    log.warning("failed to drop 'Unnamed: 62' column with: %s",
                                error)
            # Sanitize the values for pxname (frontend's/backend's names) and
            # svname (server's names) columns by replacing dots with
            # underscores because Graphite uses the dot in the namespace.
            data_frame['pxname_'] = (data_frame.pxname
                                     .apply(lambda value:
                                            value.replace('.', '_')))
            data_frame['svname_'] = (data_frame.svname
                                     .apply(lambda value:
                                            value.replace('.', '_')))

            data_frame.drop('pxname', axis=1, inplace=True)
            data_frame.drop('svname', axis=1, inplace=True)

            if not isinstance(data_frame, pandas.DataFrame):
                log.warning('Pandas data frame was not created')
                return
            if len(data_frame.index) == 0:
                log.error('Pandas data frame is empty')
                return

            # For some metrics HAProxy returns nothing, so we replace them
            # with zeros
            data_frame.fillna(0, inplace=True)

            self.process_frontends(data_frame)

            exclude_backends_file = self.config.get('process',
                                                    'exclude-backends',
                                                    fallback=None)
            if exclude_backends_file is not None:
                excluded_backends = load_file_content(exclude_backends_file)
                log.info('excluding backends %s', excluded_backends)
                # replace dots in backend names
                excluded_backends[:] = [x.replace('.', '_')
                                        for x in excluded_backends]

            filter_backend = ~data_frame['pxname_'].isin(excluded_backends)

            self.process_backends(data_frame, filter_backend)
            self.process_servers(data_frame, filter_backend)
            log.info('finished processing statistics for sites')
        else:
            log.error('failed to process statistics for sites')

    @send_wlc(output=dispatcher, name='Frontends')
    def process_frontends(self, data_frame):
        """Process statistics for frontends.

        Arguments:
            data_frame (obj): A pandas data_frame ready for processing.
        """
        # Filtering for Pandas
        cnt_metrics = 1
        log.debug('processing statistics for frontends')
        is_frontend = data_frame['svname_'] == 'FRONTEND'
        excluded_frontends = []
        metrics = self.config.get('process', 'frontend-metrics', fallback=None)

        if metrics is not None:
            metrics = metrics.split(' ')
        else:
            metrics = FRONTEND_METRICS
        log.debug('metric names for frontends %s', metrics)

        exclude_frontends_file = self.config.get('process',
                                                 'exclude-frontends',
                                                 fallback=None)
        if exclude_frontends_file is not None:
            excluded_frontends = load_file_content(exclude_frontends_file)
            log.info('excluding frontends %s', excluded_frontends)
            # replace dots in frontend names
            excluded_frontends[:] = [x.replace('.', '_')
                                     for x in excluded_frontends]
        filter_frontend = (~data_frame['pxname_']
                           .isin(excluded_frontends))

        frontend_stats = (data_frame[is_frontend & filter_frontend]
                          .loc[:, ['pxname_'] + metrics])

        # Group by frontend name and sum values for each column
        frontend_aggr_stats = frontend_stats.groupby(['pxname_']).sum()
        cnt_metrics += frontend_aggr_stats.size
        for index, row in frontend_aggr_stats.iterrows():
            paths = self.get_metric_paths('frontend', index)
            for i in row.iteritems():
                datapoints = [
                    "{p}.frontend.{f}.{m} {v} {t}\n"
                    .format(p=path,
                            f=index,
                            m=i[0],
                            v=i[1],
                            t=self.timestamp) for path in paths
                ]
                for datapoint in datapoints:
                    dispatcher.signal('send', data=datapoint)

        data = ("{p}.haproxystats.MetricsFrontend {v} {t}\n"
                .format(p=self.graphite_path,
                        v=cnt_metrics,
                        t=self.timestamp))
        dispatcher.signal('send', data=data)
        log.info('number of frontend metrics %s', cnt_metrics)

        log.debug('finished processing statistics for frontends')

    @send_wlc(output=dispatcher, name='Backends')
    def process_backends(self, data_frame, filter_backend):
        """Process statistics for backends.

        Arguments:
            data_frame (obj): A pandas data_frame ready for processing.
            filter_backend: A filter to apply on data_frame.
        """
        cnt_metrics = 1
        log.debug('processing statistics for backends')
        # Filtering for Pandas
        is_backend = data_frame['svname_'] == 'BACKEND'

        metrics = self.config.get('process', 'backend-metrics', fallback=None)
        if metrics is not None:
            metrics = metrics.split(' ')
        else:
            metrics = BACKEND_METRICS
        log.debug('metric names for backends %s', metrics)
        # Get rows only for backends. For some metrics we need the sum and
        # for others the average, thus we split them.
        stats_sum = (data_frame[is_backend & filter_backend]
                     .loc[:, ['pxname_'] + metrics])
        stats_avg = (data_frame[is_backend & filter_backend]
                     .loc[:, ['pxname_'] + BACKEND_AVG_METRICS])

        aggr_sum = stats_sum.groupby(['pxname_'], as_index=False).sum()
        aggr_avg = stats_avg.groupby(['pxname_'], as_index=False).mean()
        merged_stats = pandas.merge(aggr_sum, aggr_avg, on='pxname_')

        rows, columns = merged_stats.shape
        cnt_metrics += rows * (columns - 1)  # minus the index

        for _, row in merged_stats.iterrows():
            backend = row[0]
            paths = self.get_metric_paths('backend', backend)
            for i in row[1:].iteritems():
                datapoints = [
                    "{p}.backend.{b}.{m} {v} {t}\n"
                    .format(p=path,
                            b=backend,
                            m=i[0],
                            v=i[1],
                            t=self.timestamp) for path in paths
                ]
                for datapoint in datapoints:
                    dispatcher.signal('send', data=datapoint)

        data = ("{p}.haproxystats.MetricsBackend {v} {t}\n"
                .format(p=self.graphite_path,
                        v=cnt_metrics,
                        t=self.timestamp))
        dispatcher.signal('send', data=data)

        log.info('number of backend metrics %s', cnt_metrics)
        log.debug('finished processing statistics for backends')

    @send_wlc(output=dispatcher, name='Servers')
    def process_servers(self, data_frame, filter_backend):
        """Process statistics for servers.

        Arguments:
            data_frame (obj): A pandas data_frame ready for processing.
            filter_backend: A filter to apply on data_frame.
        """
        cnt_metrics = 1
        # A filter for rows with stats for servers
        is_server = data_frame['type'] == 2

        log.debug('processing statistics for servers')

        server_metrics = self.config.get('process',
                                         'server-metrics',
                                         fallback=None)
        if server_metrics is not None:
            server_metrics = server_metrics.split(' ')
        else:
            server_metrics = SERVER_METRICS
        log.debug('metric names for servers %s', server_metrics)
        # Get rows only for servers. For some metrics we need the sum and
        # for others the average, thus we split them.
        stats_sum = (data_frame[is_server & filter_backend]
                     .loc[:, ['pxname_', 'svname_'] + server_metrics])
        stats_avg = (data_frame[is_server & filter_backend]
                     .loc[:, ['pxname_', 'svname_'] + SERVER_AVG_METRICS])
        servers = (data_frame[is_server & filter_backend]
                   .loc[:, ['pxname_', 'svname_']])

        # Calculate the number of configured servers in a backend
        tot_servers = (servers
                       .groupby(['pxname_'])
                       .agg({'svname_': pandas.Series.nunique}))
        aggr_sum = (stats_sum
                    .groupby(['pxname_', 'svname_'], as_index=False)
                    .sum())
        aggr_avg = (stats_avg
                    .groupby(['pxname_', 'svname_'], as_index=False)
                    .mean())
        merged_stats = pandas.merge(aggr_sum,
                                    aggr_avg,
                                    on=['svname_', 'pxname_'])
        rows, columns = merged_stats.shape
        cnt_metrics += rows * (columns - 2)
        for backend, row in tot_servers.iterrows():
            cnt_metrics += 1
            paths = self.get_metric_paths('backend', backend)
            datapoints = [
                "{p}.backend.{b}.{m} {v} {t}\n"
                .format(p=path,
                        b=backend,
                        m='TotalServers',
                        v=row[0],
                        t=self.timestamp) for path in paths
            ]
            for datapoint in datapoints:
                dispatcher.signal('send', data=datapoint)

        for _, row in merged_stats.iterrows():
            backend = row[0]
            server = row[1]
            paths = self.get_metric_paths('backend', backend)
            for i in row[2:].iteritems():
                datapoints = [
                    "{p}.backend.{b}.server.{s}.{m} {v} {t}\n"
                    .format(p=path,
                            b=backend,
                            s=server,
                            m=i[0],
                            v=i[1],
                            t=self.timestamp) for path in paths
                ]
                for datapoint in datapoints:
                    dispatcher.signal('send', data=datapoint)

        if self.config.getboolean('process', 'aggr-server-metrics'):
            log.info('aggregate stats for servers across all backends')
            # Produce statistics for servers across all backends
            stats_sum = (data_frame[is_server]
                         .loc[:, ['svname_'] + SERVER_METRICS])
            stats_avg = (data_frame[is_server]
                         .loc[:, ['svname_'] + SERVER_AVG_METRICS])
            aggr_sum = (stats_sum
                        .groupby(['svname_'], as_index=False)
                        .sum())
            aggr_avg = (stats_avg
                        .groupby(['svname_'], as_index=False)
                        .mean())
            merged_stats = pandas.merge(aggr_sum, aggr_avg, on=['svname_'])
            rows, columns = merged_stats.shape
            cnt_metrics += rows * (columns - 1)  # minus the index

            for _, row in merged_stats.iterrows():
                server = row[0]
                paths = self.get_metric_paths('server', server)
                for i in row[1:].iteritems():
                    datapoints = [
                        "{p}.server.{s}.{m} {v} {t}\n"
                        .format(p=path,
                                s=server,
                                m=i[0],
                                v=i[1],
                                t=self.timestamp) for path in paths
                    ]
                    for datapoint in datapoints:
                        dispatcher.signal('send', data=datapoint)

        data = ("{p}.haproxystats.MetricsServer {v} {t}\n"
                .format(p=self.graphite_path,
                        v=cnt_metrics,
                        t=self.timestamp))
        dispatcher.signal('send', data=data)

        log.info('number of server metrics %s', cnt_metrics)
        log.debug('finished processing statistics for servers')


    def build_metric_patterns(self):
        """Compile regexes from frontend- backend- and server-groups config.

        Builds a list of pairs (pattern_name, regex) to be used when sending
        metrics. When a frontend, backend or server matches a given pattern, the
        string in pattern_name can be inserted into the metric.

        This list is stored in the class variable 'metric_patterns'.
        """
        # Don't let Consumer instances run this at the same time
        lock = Lock()
        with lock:
            for (section, patterns) in Consumer.metric_patterns.items():
                # Run only once
                if patterns:
                    return
                config_section = "{}-groups".format(section)
                if config_section not in self.config.sections():
                    continue
                for (name, pattern) in self.config.items(config_section):
                    # Skip items inherited from the [DEFAULTS] section
                    if name in self.config.defaults():
                        continue
                    try:
                        regex = re.compile(pattern)
                    except re.error as error:
                        log.error('faied to compile %s pattern %s. Error: %s',
                                  config_section, name, error)
                    else:
                        Consumer.metric_patterns[section].append((name, regex))
            log.debug('built metric patterns %s', Consumer.metric_patterns)


    def get_metric_paths(self, section, section_name):
        """Return the graphite path(s) of a metric.

        When the name of a frontend or backend matches a given pattern, the
        returned graphite path will include the name of the pattern, prefixed by
        a string defined in the 'group-namespace' config setting. The list of
        patterns and their names are defined in the 'frontend-groups',
        'backend-groups' and 'server-groups' config sections.

        Additionally, if the config option 'group-namespace-double-writes' is
        true, this function will return the default graphite path as well,
        so every datapoint may be sent to graphite on both paths.

        If no groups are defined, or if there is no match for the given
        frontend/backend name, it returns only the default graphite path.

        If two or more patterns match a frontend/backend name, only one will be
        used: the first one declared in the config file.

        Arguments:
            section (str): Either 'frontend', 'backend' or 'server'.
            section_name (str): The name of said frontend/backend/server.
        """
        group = None
        for (pattern_name, pattern) in Consumer.metric_patterns[section]:
            if pattern.search(section_name):
                group = pattern_name
                break
        if group is None:
            return [self.graphite_path]
        try:
            path = Consumer.path_cache[section][section_name]
        except KeyError:
            # cache miss
            group_namespace = self.config.get('graphite', 'group-namespace')
            path = "{}.{}.{}".format(self.graphite_path, group_namespace, group)
            Consumer.path_cache[section][section_name] = path
        if self.double_writes:
            return [path, self.graphite_path]
        else:
            return [path]


def main():
    """Parse CLI arguments and launches main program."""
    args = docopt(__doc__, version=VERSION)

    config = ConfigParser(interpolation=ExtendedInterpolation())
    # Set defaults for all sections
    config.read_dict(copy.copy(DEFAULT_OPTIONS))
    try:
        config.read(args['--file'])
    except ParsingError as exc:
        sys.exit(str(exc))

    config_dir = args['--dir']
    if config_dir is not None:
        if not os.path.isdir(config_dir):
            raise ValueError("{d} directory with .conf files doesn't exist"
                             .format(d=config_dir))
        else:
            config_files = glob.glob(os.path.join(config_dir, '*.conf'))
            try:
                config.read(config_files)
            except ParsingError as exc:
                sys.exit(str(exc))

    incoming_dir = config.get('process', 'src-dir')

    if args['--print']:
        for section in sorted(DEFAULT_OPTIONS):
            if section == 'pull':
                continue
            print("[{}]".format(section))
            for key, value in sorted(DEFAULT_OPTIONS[section].items()):
                print("{k} = {v}".format(k=key, v=value))
            print()
        sys.exit(0)
    if args['--print-conf']:
        for section in sorted(config):
            if section == 'pull':
                continue
            print("[{}]".format(section))
            for key, value in sorted(config[section].items()):
                print("{k} = {v}".format(k=key, v=value))
            print()
        sys.exit(0)

    try:
        configuration_check(config, 'paths')
        configuration_check(config, 'process')
        configuration_check(config, 'graphite')
        read_write_access(config.get('process', 'src-dir'))
        check_metrics(config)
    except ValueError as exc:
        sys.exit(str(exc))

    tasks = multiprocessing.Queue()
    handler = EventHandler(tasks=tasks)
    notifier = pyinotify.Notifier(watcher, handler)
    num_consumers = config.getint('process', 'workers')
    incoming_dir = config.get('process', 'src-dir')

    loglevel =\
        config.get('process', 'loglevel').upper()  # pylint: disable=no-member
    log.setLevel(getattr(logging, loglevel, None))

    log.info('haproxystats-processs %s version started', VERSION)
    # process incoming data which were retrieved while processing was stopped
    for pathname in glob.iglob(incoming_dir + '/*'):
        if os.path.isdir(pathname):
            log.info('putting %s in queue', pathname)
            tasks.put(pathname)

    def shutdown(signalnb=None, frame=None):
        """Signal processes to exit.

        It adds STOP_SIGNAL to the queue, which causes processes to exit in a
        clean way.

        Arguments:
            signalnb (int): The ID of signal
            frame (obj): Frame object at the time of receiving the signal
        """
        log.info('received %s at %s', signalnb, frame)
        notifier.stop()
        for _ in range(num_consumers):
            log.info('sending stop signal to worker')
            tasks.put(STOP_SIGNAL)
        log.info('waiting for workers to finish their work')
        for consumer in consumers:
            consumer.join()
        log.info('exiting')
        sys.exit(0)

    # Register our graceful shutdown process to termination signals
    signal.signal(signal.SIGHUP, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    # Add our watcher
    while True:
        try:
            log.info('adding a watch for %s', incoming_dir)
            watcher.add_watch(incoming_dir, MASK, quiet=False, rec=False)
        except pyinotify.WatchManagerError as error:
            log.error('received error (%s), going to retry in few seconds',
                      error)
            time.sleep(3)
        else:
            break

    log.info('creating %d consumers', num_consumers)
    consumers = [Consumer(tasks, config) for i in range(num_consumers)]
    for consumer in consumers:
        consumer.start()

    _thread = Checker(
        consumers, config.getfloat('process', 'liveness-check-interval')
    )
    _thread.start()
    log.info('watching %s directory for incoming data', incoming_dir)
    notifier.loop(daemonize=False)


if __name__ == '__main__':
    main()

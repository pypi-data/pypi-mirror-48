"""Provide constants for grouping metric names.

There are seperated groups for frontend, backend, servers and haproxy daemon.
Metric names are the field names contained in the HAProxy statistics.
"""
from collections import namedtuple

DAEMON_METRICS = [
    'CompressBpsIn',
    'CompressBpsOut',
    'CompressBpsRateLim',
    'ConnRate',
    'ConnRateLimit',
    'CumConns',
    'CumReq',
    'CumSslConns',
    'CurrConns',
    'CurrSslConns',
    'Hard_maxconn',
    'MaxConnRate',
    'MaxSessRate',
    'MaxSslConns',
    'MaxSslRate',
    'MaxZlibMemUsage',
    'Maxconn',
    'Maxpipes',
    'Maxsock',
    'Memmax_MB',
    'PipesFree',
    'PipesUsed',
    'Run_queue',
    'SessRate',
    'SessRateLimit',
    'SslBackendKeyRate',
    'SslBackendMaxKeyRate',
    'SslCacheLookups',
    'SslCacheMisses',
    'SslFrontendKeyRate',
    'SslFrontendMaxKeyRate',
    'SslFrontendSessionReuse_pct',
    'SslRate',
    'SslRateLimit',
    'Tasks',
    'Ulimit-n',
    'ZlibMemUsage',
]

DAEMON_AVG_METRICS = ['Idle_pct', 'Uptime_sec']

COMMON = [
    'bin',
    'bout',
    'dresp',
    'hrsp_1xx',
    'hrsp_2xx',
    'hrsp_3xx',
    'hrsp_4xx',
    'hrsp_5xx',
    'hrsp_other',
    'rate',
    'rate_max',
    'scur',
    'slim',
    'smax',
    'stot'
]

SERVER_METRICS = [
    'chkfail',
    'chkdown',
    'cli_abrt',
    'econ',
    'eresp',
    'lbtot',
    'qcur',
    'qmax',
    'srv_abrt',
    'wredis',
    'wretr'
] + COMMON

SERVER_AVG_METRICS = ['ctime', 'qtime', 'rtime', 'throttle', 'ttime', 'weight']

BACKEND_METRICS = [
    'chkdown',
    'cli_abrt',
    'comp_byp',
    'comp_in',
    'comp_out',
    'comp_rsp',
    'downtime',
    'dreq',
    'econ',
    'eresp',
    'intercepted',
    'lbtot',
    'qcur',
    'qmax',
    'req_tot',
    'srv_abrt',
    'wredis',
    'wretr',
] + COMMON

BACKEND_AVG_METRICS = [
    'act',
    'bck',
    'rtime',
    'ctime',
    'qtime',
    'ttime',
    'weight'
]

FRONTEND_METRICS = [
    'comp_byp',
    'comp_in',
    'comp_out',
    'comp_rsp',
    'conn_rate',
    'conn_rate_max',
    'conn_tot',
    'dcon',
    'dses',
    'dreq',
    'ereq',
    'intercepted',
    'rate_lim',
    'req_rate',
    'req_rate_max',
    'req_tot'
] + COMMON

MetricNamesPercentage = namedtuple('MetricsNamesPercentage',
                                   ['name', 'limit', 'title'])

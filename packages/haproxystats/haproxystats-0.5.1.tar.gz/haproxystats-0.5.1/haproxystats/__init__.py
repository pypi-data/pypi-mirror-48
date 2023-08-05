# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
"""A collection of Python tools to process HAProxy statistics."""
__title__ = 'haproxystats'
__author__ = 'Pavlos Parissis'
__license__ = 'Apache 2.0'
__version__ = '0.5.1'
__copyright__ = 'Copyright 2016 Pavlos Parissis <pavlos.parissis@gmail.com'

DEFAULT_OPTIONS = {
    'DEFAULT': {
        'retries': 2,
        'timeout': 1,
        'interval': 2,
        'loglevel': 'info',
    },
    'paths': {
        'base-dir': '/var/lib/haproxystats',
    },
    'pull': {
        'retries': 1,
        'timeout': 0.1,
        'interval': 0.5,
        'pull-timeout': 2,
        'pull-interval': 10,
        'buffer-limit': 6291456,
        'dst-dir': '/var/lib/haproxystats/incoming',
        'tmp-dst-dir': '/var/lib/haproxystats/incoming.tmp',
        'workers': 8,
        'queue-size': 360,
    },
    'process': {
        'workers': '4',
        'src-dir': '/var/lib/haproxystats/incoming',
        'aggr-server-metrics': 'false',
        'per-process-metrics': 'false',
        'calculate-percentages': 'false',
        'liveness-check-interval': 10,
    },
    'graphite': {
        'server': '127.0.0.1',
        'port': 3002,
        'retries': 3,
        'interval': 1.8,
        'connect-timeout': 1.0,
        'write-timeout': 1.0,
        'delay': 10,
        'backoff': 2,
        'namespace': 'loadbalancers',
        'prefix-hostname': 'true',
        'fqdn': 'true',
        'queue-size': 1000000
    },
}

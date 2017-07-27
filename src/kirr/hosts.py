from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', 'kirr.hostsconf.urls', name='wildcard'),
)

'''
	It may change in next few years to 
form kirr.hostsconf import urls as reduced_urls
host_patterns = patterns=[
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', 'kirr.hostsconf.urls', name='wildcard'),
]
'''
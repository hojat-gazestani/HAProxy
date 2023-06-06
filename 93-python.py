#!/usr/bin/python3

from haproxyadmin import haproxy

#hap = haproxy.HAProxy(socket='127.0.0.1:9999')
hap = haproxy.HAProxy(socket_file='/run/haproxy/admin.sock')

frontends = hap.frontends()

for frontend in frontends:
    print(frontend.name, frontend.requests, frontend.process_nb)


#!/usr/bin/python3

# pip install haproxyadmin
from haproxyadmin import haproxy

hap = haproxy.HAProxy(socket_dir='/run/haproxy/admin.sock')

frontends = hap.frontends()

for frontend in frontends:
    print(frontend.name, frontend.requests. frontend.proccess_nb)

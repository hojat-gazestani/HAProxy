#!/usr/bin/python3

from haproxyadmin import haproxy

hap = haproxy.HAProxy(socket_file='/run/haproxy/admin.sock')

frontends = hap.frontends()
backends = hap.backends()

for frontend in frontends:
    if frontend.name == 'Italy':
        print("Frontend: {}".format(frontend.name))
        for server in frontend.servers():
            print("  Server: {} ({})".format(server.name, server.address))

for backend in backends:
    if backend.name == 'myapps':
        print("Backend: {}".format(backend.name))
        for server in backend.servers():
            print("  Server: {} ({})".format(server.name, server.address))

#!/usr/bin/python3

from haproxyadmin import haproxy

hap = haproxy.HAProxy(socket_file='/run/haproxy/admin.sock')

frontends = hap.frontends()
backends = hap.backends()

for frontend in frontends:
    if frontend.name == 'Italy':
        print("Frontend: {}".format(frontend.name))
        backend_name = frontend.default_backend
        for backend in backends:
            if backend.name == backend_name:
                for server in backend.servers():
                    print("  Server: {} ({})".format(server.name, server.address))
                break

for backend in backends:
    if backend.name == 'myapps':
        print("Backend: {}".format(backend.name))
        for server in backend.servers():
            print("  Server: {} ({})".format(server.name, server.address))

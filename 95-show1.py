#!/usr/bin/python3

# from haproxyadmin import haproxy

# hap = haproxy.HAProxy(socket_file='/run/haproxy/admin.sock')

# frontends = hap.frontends()
# backends = hap.backends()

# for frontend in frontends:
#     if frontend.name == 'Italy':
#         print("Frontend: {}".format(frontend.name))
#         backend_name = frontend.default_backend
#         for backend in backends:
#             if backend.name == backend_name:
#                 for server in backend.servers():
#                     print("  Server: {} ({})".format(server.name, server.address))
#                 break

# for backend in backends:
#     if backend.name == 'myapps':
#         print("Backend: {}".format(backend.name))
#         for server in backend.servers():
#             print("  Server: {} ({})".format(server.name, server.address))

#!/usr/bin/python3

from haproxyadmin import haproxy

hap = haproxy.HAProxy(socket_file='/run/haproxy/admin.sock')

frontends = hap.frontends()
backends = hap.backends()

for frontend in frontends:
    if frontend.name == 'Italy':
        print("Frontend: {}".format(frontend.name))
        backend_name = None
        for line in frontend.raw_data.split('\n'):
            if line.startswith('default_backend'):
                backend_name = line.split(' ')[1]
                break
        if backend_name:
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


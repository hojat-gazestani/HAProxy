#!/usr/bin/python3

from haproxyadmin import haproxy

hap = haproxy.HAProxy(socket_file='/run/haproxy/admin.sock')

backends = hap.backends()

for backend in backends:
    if backend.name == 'myapps':
        print("Backend: {}".format(backend.name))
        for stick_table in backend.stick_tables():
            print("  Sticky Table: {}".format(stick_table.name))
            for record in stick_table.records():
                print("    Record: {}".format(record.key))


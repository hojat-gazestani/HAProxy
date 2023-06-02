global
	log         127.0.0.1:1514 local0

defaults
	log	global
	mode	http
    timeout connect 5000
    timeout client  50000
    timeout server  50000


frontend graylog
	bind *:80
	use_backend graylog

backend graylog
	server localsrv 127.0.0.1:9000

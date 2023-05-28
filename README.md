# HAProxy
Microservice project toturail

docker ps --format "{{.ID}}\t{{.Image}}\t{{.Ports}}" | awk -F '->|:' '/tcp/{print $1"\t"$2"\t"$3":"$4}'

 for i in {1..100}; do curl localhost &&sleep 1 && echo; done;

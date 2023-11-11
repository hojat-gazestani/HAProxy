
# HAproxy

```sh
sudo apt-get install haproxy -y

sudo vi /etc/haproxy/haproxy.cfg
listen stats
    bind :9000
    stats enable
    mode http
    stats uri /stats
    stats hide-version
    stats realm Haproxy\ Statistics
    stats auth admin:P@$$w0rd

frontend ourwebsitefrontend
    bind *:80
    mode http
    default_backend ourwebsiteendpoint

backend ourwebsiteendpoint
    server backend_server 172.2.2.5:3000
```


# Prometheus
```sh
sudo wget https://github.com/prometheus/prometheus/releases/download/v2.20.1/prometheus-2.20.1.linux-amd64.tar.gz
tar -xzf prometheus-2.20.1.linux-amd64.tar.gz
mv prometheus-2.20.1.linux-amd64.tar.gz prometheus
cp prometheus /opt/

vim /opt/prometheus/prometheus.yml
global:
  scrape_interval: 15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 15s # Evaluate rules every 15 seconds. The default is every 1 minute.

alerting:
  alertmanagers:
    - static_configs:
        - targets:
          # - alertmanager:9093

rule_files:

scrape_configs:

  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]
  - job_name: "haproxy"
    static_configs:
      - targets: ["localhost:9101"]



sudo systemctl daemon-reload
sudo systemctl start prometheus
sudo systemctl enable prometheus
```

# HAproxy node exporter
```sh
sudo wget https://github.com/prometheus/haproxy_exporter/releases/download/v0.8.0/haproxy_exporter-0.8.0.linux-amd64.tar.gz
tar -xzf haproxy_exporter-0.8.0.linux-amd64.tar.gz
sudo mv haproxy_exporter-0.8.0.linux-amd64.tar.gz haproxy_exporter
sudo cp haproxy_exporter/haproxy_exporter /usr/bin/

sudo vim /lib/systemd/system/prometheus-haproxy-exporter.service
[Unit]
Description=Prometheus exporter for HAProxy
Documentation=https://github.com/prometheus/haproxy_exporter

[Service]
Restart=on-failure
User=prometheus
EnvironmentFile=/etc/default/prometheus-haproxy-exporter
ExecStart=/usr/bin/prometheus-haproxy-exporter $ARGS

[Install]
WantedBy=multi-user.target

sudo systemctl start haproxy_exporter
sudo systemctl enable haproxy_exporter

sudo vim /etc/default/prometheus-haproxy-exporter
ARGS=""
  --haproxy.scrape-uri="http://localhost:9000/stats?stats;csv"
```

# Grafana
```sh
sudo apt-get install -y apt-transport-https
sudo apt-get install -y software-properties-common wget
wget -q -O — https://packages.grafana.com/gpg.key | sudo apt-key add -
echo “deb https://packages.grafana.com/oss/deb stable main” | sudo tee -a /etc/apt/sources.list.d/grafana.list
sudo apt-get update
sudo apt-get install grafana
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
```

# Add data store
```sh
add data store

prometheus
name: haproxy_test
URL: http://localhost:9090

```

##########

## Install and Configure HAProxy Exporter

```sh
sudo groupadd prometheus
sudo useradd --system -s /sbin/nologin -g prometheus prometheus

sudo firewall-cmd --permanent --add-port=9101/tcp
sudo firewall-cmd --reload

wget -q https://github.com/prometheus/haproxy_exporter/releases/download/v0.15.0/haproxy_exporter-0.15.0.linux-amd64.tar.gz
sudo tar --strip-components=1 -xf haproxy_exporter-0.15.0.linux-amd64.tar.gz -C /usr/local/bin/
sudo chown -R root: /usr/local/bin/
```

```sh
sudo vim /etc/systemd/system/haproxy_exporter.service
[Unit]
Description=Prometheus
Documentation=https://github.com/prometheus/haproxy_exporter
Wants=network-online.target
After=network-online.target

[Service]
Type=simple
User=prometheus
Group=prometheus
ExecReload=/bin/kill -HUP $MAINPID
ExecStart=/usr/local/bin/haproxy_exporter \
  --haproxy.pid-file=/var/run/haproxy.pid \
  --haproxy.timeout=20s \
  --web.listen-address=0.0.0.0:9101 \
  --web.telemetry-path=/metrics \
  --haproxy.scrape-uri='http://admin:P@$$w0rd@172.2.2.5:80/stats;csv'

SyslogIdentifier=prometheus
Restart=always

[Install]
WantedBy=multi-user.target
```

```sh
sudo chown -R root: /etc/systemd/system/haproxy_exporter.service
sudo chmod 0644 /etc/systemd/system/haproxy_exporter.service

sudo systemctl daemon-reload
sudo systemctl enable --now haproxy_exporter
```

## Configure HAProxy Server to Export Statistics
```sh
sudo vim /etc/haproxy/haproxy.cfg
listen stats 
    bind 10.11.1.30:8080
    mode http
    stats enable
    stats uri /
    stats refresh 30s
    stats realm HAProxy\ Statistics
    stats auth admin:P@$$w0rd
```

```sh
sudo systemctl restart haproxy
```

## Configure Prometheus Scraping

```sh
  - job_name: 'haproxy'
    static_configs:
      - targets: ['10.11.1.30:9101']
```

## Add Grafana Dashboard for HAProxy

```sh
dashboadid: 367
```
# Nginx by Zabbix agent template description

Get metrics from stub status module using Zabbix agent running on Linux
https://nginx.ru/en/docs/http/ngx_http_stub_status_module.html

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/384765-discussion-thread-for-official-zabbix-template-nginx

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Nginx process discovery ](#discovery_nginx_process_discovery)

<a name="items"></a>

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Service response time | no description | net.tcp.service.perf[http,"{$NGINX.STUB_STATUS.HOST}","{$NGINX.STUB_STATUS.PORT}"] | no type | no delay |
| Service status | no description | net.tcp.service[http,"{$NGINX.STUB_STATUS.HOST}","{$NGINX.STUB_STATUS.PORT}"] | no type | no delay |
| Connections accepted per second | The total number of accepted client connections. | nginx.connections.accepted.rate | DEPENDENT | 0 |
| Connections active | The current number of active client connections including waiting connections. | nginx.connections.active | DEPENDENT | 0 |
| Connections dropped per second | The total number of dropped client connections. | nginx.connections.dropped.rate | DEPENDENT | 0 |
| Connections handled per second | The total number of handled connections. Generally, the parameter value is the same as for the accepted connections, unless some resource limits have been reached (for example, the `worker_connections limit`). | nginx.connections.handled.rate | DEPENDENT | 0 |
| Connections reading | The current number of connections where Nginx is reading the request header. | nginx.connections.reading | DEPENDENT | 0 |
| Connections waiting | The current number of idle client connections waiting for a request. | nginx.connections.waiting | DEPENDENT | 0 |
| Connections writing | The current number of connections where Nginx is writing a response back to the client. | nginx.connections.writing | DEPENDENT | 0 |
| Requests total | The total number of client requests. | nginx.requests.total | DEPENDENT | 0 |
| Requests per second | The total number of client requests. | nginx.requests.total.rate | DEPENDENT | 0 |
| Version | no description | nginx.version | DEPENDENT | 0 |
| Get processes summary | The aggregated data of summary metrics for all processes. | proc.get[{$NGINX.PROCESS.NAME.PARAMETER},,,summary] | no type | no delay |
| Get stub status page | The following status information is provided:<br>`Active connections` - the current number of active client connections including waiting connections.<br>`Accepted` - the total number of accepted client connections.<br>`Handled` - the total number of handled connections. Generally, the parameter value is the same as for the accepted connections, unless some resource limits have been reached (for example, the `worker_connections` limit).<br>`Requests` - the total number of client requests.<br>`Reading` - the current number of connections where Nginx is reading the request header.<br>`Writing` - the current number of connections where Nginx is writing a response back to the client.<br>`Waiting` - the current number of idle client connections waiting for a request.<br><br>See also [Module ngx_http_stub_status_module](https://nginx.org/en/docs/http/ngx_http_stub_status_module.html). | web.page.get["{$NGINX.STUB_STATUS.HOST}","{$NGINX.STUB_STATUS.PATH}","{$NGINX.STUB_STATUS.PORT}"] | no type | no delay |


<a name="macros"></a>

## Macros
| macro | value |
| ------------- |------------- |
| {$NGINX.DROP_RATE.MAX.WARN} | 1 |
| {$NGINX.PROCESS.NAME.PARAMETER} | no value |
| {$NGINX.PROCESS_NAME} | nginx |
| {$NGINX.RESPONSE_TIME.MAX.WARN} | 10 |
| {$NGINX.STUB_STATUS.HOST} | localhost |
| {$NGINX.STUB_STATUS.PATH} | basic_status |
| {$NGINX.STUB_STATUS.PORT} | 80 |


<a name="triggers"></a>

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Version has changed | INFO | The Nginx version has changed. Acknowledge to close the problem manually. | last(/Nginx by Zabbix agent/nginx.version,#1)<>last(/Nginx by Zabbix agent/nginx.version,#2) and length(last(/Nginx by Zabbix agent/nginx.version))>0 | [{"tag": "scope", "value": "notice"}] | no url |


<a name="discoveries"></a>

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Nginx process discovery | nginx.proc.discovery | The discovery of Nginx process summary. | DEPENDENT | no lifetime | 0 |


<a name="discovery_nginx_process_discovery" />

## Discovery Nginx process discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Get process data | The summary metrics aggregated by a process {#NGINX.NAME}. | nginx.proc.get[{#NGINX.NAME}] | DEPENDENT |
| Number of running processes | The number of running processes {#NGINX.NAME}. | nginx.proc.num[{#NGINX.NAME}] | DEPENDENT |
| Memory usage, % | The percentage of real memory used by a process {#NGINX.NAME}. | nginx.proc.pmem[{#NGINX.NAME}] | DEPENDENT |
| Memory usage (rss) | The summary of resident set size memory used by a process {#NGINX.NAME} expressed in bytes. | nginx.proc.rss[{#NGINX.NAME}] | DEPENDENT |
| Memory usage (vsize) | The summary of virtual memory used by a process {#NGINX.NAME} expressed in bytes. | nginx.proc.vmem[{#NGINX.NAME}] | DEPENDENT |
| CPU utilization | The percentage of the CPU utilization by a process {#NGINX.NAME}. | proc.cpu.util[{#NGINX.NAME}] | no type |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Process is not running | HIGH | no description | last(/Nginx by Zabbix agent/nginx.proc.num[{#NGINX.NAME}])=0 | [{"tag": "scope", "value": "availability"}] | no url |
| Failed to fetch stub status page | WARNING | Zabbix has not received any data for items for the last 30 minutes. | (find(/Nginx by Zabbix agent/web.page.get["{$NGINX.STUB_STATUS.HOST}","{$NGINX.STUB_STATUS.PATH}","{$NGINX.STUB_STATUS.PORT}"],,"iregexp","HTTP\\/[\\d.]+\\s+200")=0 or<br>nodata(/Nginx by Zabbix agent/web.page.get["{$NGINX.STUB_STATUS.HOST}","{$NGINX.STUB_STATUS.PATH}","{$NGINX.STUB_STATUS.PORT}"],30m)) and last(/Nginx by Zabbix agent/nginx.proc.num[{#NGINX.NAME}])>0 | [{"tag": "scope", "value": "availability"}] | no url |
| High connections drop rate | WARNING | The rate of dropping connections has been greater than {$NGINX.DROP_RATE.MAX.WARN} for the last 5 minutes. | min(/Nginx by Zabbix agent/nginx.connections.dropped.rate,5m) > {$NGINX.DROP_RATE.MAX.WARN} and last(/Nginx by Zabbix agent/nginx.proc.num[{#NGINX.NAME}])>0 | [{"tag": "scope", "value": "performance"}] | no url |
| Service is down | AVERAGE | no description | last(/Nginx by Zabbix agent/net.tcp.service[http,"{$NGINX.STUB_STATUS.HOST}","{$NGINX.STUB_STATUS.PORT}"])=0 and last(/Nginx by Zabbix agent/nginx.proc.num[{#NGINX.NAME}])>0 | [{"tag": "scope", "value": "availability"}] | no url |
| Service response time is too high | WARNING | no description | min(/Nginx by Zabbix agent/net.tcp.service.perf[http,"{$NGINX.STUB_STATUS.HOST}","{$NGINX.STUB_STATUS.PORT}"],5m)>{$NGINX.RESPONSE_TIME.MAX.WARN} and last(/Nginx by Zabbix agent/nginx.proc.num[{#NGINX.NAME}])>0 | [{"tag": "scope", "value": "performance"}] | no url |

# Nginx by HTTP template description

This template is developed to monitor Nginx by Zabbix that works without any external scripts.
Most of the metrics are collected in one go, thanks to Zabbix bulk data collection.

The template collects metrics by polling the module 'ngx_http_stub_status_module' with HTTP agent remotely:
https://nginx.ru/en/docs/http/ngx_http_stub_status_module.html

Active connections: 291
server accepts handled requests
16630948 16630948 31070465
Reading: 6 Writing: 179 Waiting: 106

Setup:

1. See the setup instructions for 'ngx_http_stub_status_module':
https://nginx.ru/en/docs/http/ngx_http_stub_status_module.html

Test the availability of the 'http_stub_status_module' with 'nginx -V 2>&1 | grep -o with-http_stub_status_module'.

Example configuration of Nginx:

location = /basic_status {
    stub_status;
    allow <IP of your Zabbix server/proxy>;
    deny all;
}

2. Set the hostname or IP address of the Nginx host or Nginx container in the '{$NGINX.STUB_STATUS.HOST}' macro. You can also change the status page port in the '{$NGINX.STUB_STATUS.PORT}' macro, the status page scheme in the '{$NGINX.STUB_STATUS.SCHEME}' macro and the status page path in the '{$NGINX.STUB_STATUS.PATH}' macro if necessary.

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/384765-discussion-thread-for-official-zabbix-template-nginx

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Service response time | no description | net.tcp.service.perf[http,"{$NGINX.STUB_STATUS.HOST}","{$NGINX.STUB_STATUS.PORT}"] | SIMPLE | no delay |
| Service status | no description | net.tcp.service[http,"{$NGINX.STUB_STATUS.HOST}","{$NGINX.STUB_STATUS.PORT}"] | SIMPLE | no delay |
| Connections accepted per second | The total number of accepted client connections. | nginx.connections.accepted.rate | DEPENDENT | 0 |
| Connections active | The current number of active client connections including waiting connections. | nginx.connections.active | DEPENDENT | 0 |
| Connections dropped per second | The total number of dropped client connections. | nginx.connections.dropped.rate | DEPENDENT | 0 |
| Connections handled per second | The total number of handled connections. Generally, the parameter value is the same as for the accepted connections, unless some resource limits have been reached (for example, the `worker_connections limit`). | nginx.connections.handled.rate | DEPENDENT | 0 |
| Connections reading | The current number of connections where Nginx is reading the request header. | nginx.connections.reading | DEPENDENT | 0 |
| Connections waiting | The current number of idle client connections waiting for a request. | nginx.connections.waiting | DEPENDENT | 0 |
| Connections writing | The current number of connections where Nginx is writing a response back to the client. | nginx.connections.writing | DEPENDENT | 0 |
| Get stub status page | The following status information is provided:<br>`Active connections` - the current number of active client connections including waiting connections.<br>`Accepted` - the total number of accepted client connections.<br>`Handled` - the total number of handled connections. Generally, the parameter value is the same as for the accepted connections, unless some resource limits have been reached (for example, the `worker_connections` limit).<br>`Requests` - the total number of client requests.<br>`Reading` - the current number of connections where Nginx is reading the request header.<br>`Writing` - the current number of connections where Nginx is writing a response back to the client.<br>`Waiting` - the current number of idle client connections waiting for a request.<br><br>See also [Module ngx_http_stub_status_module](https://nginx.org/en/docs/http/ngx_http_stub_status_module.html). | nginx.get_stub_status | HTTP_AGENT | no delay |
| Requests total | The total number of client requests. | nginx.requests.total | DEPENDENT | 0 |
| Requests per second | The total number of client requests. | nginx.requests.total.rate | DEPENDENT | 0 |
| Version | no description | nginx.version | DEPENDENT | 0 |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$NGINX.DROP_RATE.MAX.WARN} | 1 |
| {$NGINX.RESPONSE_TIME.MAX.WARN} | 10 |
| {$NGINX.STUB_STATUS.HOST} | <SET STUB_STATUS HOST> |
| {$NGINX.STUB_STATUS.PATH} | basic_status |
| {$NGINX.STUB_STATUS.PORT} | 80 |
| {$NGINX.STUB_STATUS.SCHEME} | http |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Service response time is too high | WARNING | no description | min(/Nginx by HTTP/net.tcp.service.perf[http,"{$NGINX.STUB_STATUS.HOST}","{$NGINX.STUB_STATUS.PORT}"],5m)>{$NGINX.RESPONSE_TIME.MAX.WARN} | [{"tag": "scope", "value": "performance"}] | no url |
| Service is down | AVERAGE | no description | last(/Nginx by HTTP/net.tcp.service[http,"{$NGINX.STUB_STATUS.HOST}","{$NGINX.STUB_STATUS.PORT}"])=0 | [{"tag": "scope", "value": "availability"}] | no url |
| High connections drop rate | WARNING | The rate of dropping connections has been greater than {$NGINX.DROP_RATE.MAX.WARN} for the last 5 minutes. | min(/Nginx by HTTP/nginx.connections.dropped.rate,5m) > {$NGINX.DROP_RATE.MAX.WARN} | [{"tag": "scope", "value": "performance"}] | no url |
| Failed to fetch stub status page | WARNING | Zabbix has not received any data for items for the last 30 minutes. | find(/Nginx by HTTP/nginx.get_stub_status,,"iregexp","HTTP\\/[\\d.]+\\s+200")=0 or<br>nodata(/Nginx by HTTP/nginx.get_stub_status,30m)=1 | [{"tag": "scope", "value": "availability"}] | no url |
| Version has changed | INFO | The Nginx version has changed. Acknowledge to close the problem manually. | last(/Nginx by HTTP/nginx.version,#1)<>last(/Nginx by HTTP/nginx.version,#2) and length(last(/Nginx by HTTP/nginx.version))>0 | [{"tag": "scope", "value": "notice"}] | no url |

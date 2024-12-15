# PHP-FPM by Zabbix agent template description

Get PHP-FPM metrics using Zabbix agent running on Linux.

Note that depending on your OS distribution, the PHP-FPM process name may vary. Please, check the actual name in the line "Name" from /proc/<pid>/status file (https://www.zabbix.com/documentation/7.0/manual/appendix/items/proc_mem_num_notes) and change {$PHP_FPM.PROCESS.NAME.PARAMETER} macro if needed.

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery PHP-FPM process discovery ](#discovery_php-fpm_process_discovery)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Accepted connections per second | The number of accepted requests per second. | php-fpm.conn_accepted.rate | DEPENDENT | 0 |
| Listen queue | The current number of connections that have been initiated but not yet accepted. | php-fpm.listen_queue | DEPENDENT | 0 |
| Listen queue, len | The size of the socket queue of pending connections. | php-fpm.listen_queue_len | DEPENDENT | 0 |
| Listen queue, max | The maximum number of requests in the queue of pending connections since this FPM pool was started. | php-fpm.listen_queue_max | DEPENDENT | 0 |
| Queue usage | The utilization of the queue. | php-fpm.listen_queue_usage | CALCULATED | no delay |
| Max children reached | The number of times that `pm.max_children` has been reached since the PHP-FPM pool was started. | php-fpm.max_children | DEPENDENT | 0 |
| Pool name | The name of the current pool. | php-fpm.name | DEPENDENT | 0 |
| Ping | no description | php-fpm.ping | DEPENDENT | 0 |
| Processes, active | The total number of active processes. | php-fpm.processes_active | DEPENDENT | 0 |
| Processes, idle | The total number of idle processes. | php-fpm.processes_idle | DEPENDENT | 0 |
| Processes, max active | The highest value of "active processes" since the PHP-FPM server was started. | php-fpm.processes_max_active | DEPENDENT | 0 |
| Processes, total | The total number of server processes currently running. | php-fpm.processes_total | DEPENDENT | 0 |
| Process manager | The method used by the process manager to control the number of child processes for this pool. | php-fpm.process_manager | DEPENDENT | 0 |
| Slow requests | The number of requests that has exceeded your `request_slowlog_timeout` value. | php-fpm.slow_requests | DEPENDENT | 0 |
| Start time | The time when this pool was started. | php-fpm.start_time | DEPENDENT | 0 |
| Uptime | It indicates how long has this pool been running. | php-fpm.uptime | DEPENDENT | 0 |
| Version | The current version of the PHP. You can get it from the HTTP-Header "X-Powered-By"; it may not work if you have changed the default HTTP-headers. | php-fpm.version | DEPENDENT | 0 |
| Get processes summary | The aggregated data of summary metrics for all processes. | proc.get[{$PHP_FPM.PROCESS.NAME.PARAMETER},,,summary] | no type | no delay |
| php-fpm_ping | no description | web.page.get["{$PHP_FPM.HOST}","{$PHP_FPM.PING.PAGE}","{$PHP_FPM.PORT}"] | no type | no delay |
| Get status page | no description | web.page.get["{$PHP_FPM.HOST}","{$PHP_FPM.STATUS.PAGE}?json","{$PHP_FPM.PORT}"] | no type | no delay |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$PHP_FPM.HOST} | localhost |
| {$PHP_FPM.PING.PAGE} | ping |
| {$PHP_FPM.PING.REPLY} | pong |
| {$PHP_FPM.PORT} | 80 |
| {$PHP_FPM.PROCESS.NAME.PARAMETER} | no value |
| {$PHP_FPM.PROCESS_NAME} | php-fpm |
| {$PHP_FPM.QUEUE.WARN.MAX} | 80 |
| {$PHP_FPM.STATUS.PAGE} | status |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Queue utilization is high | WARNING | The queue for this pool has reached `{$PHP_FPM.QUEUE.WARN.MAX}%` of its maximum capacity. <br>Items in the queue represent the current number of connections that have been initiated on this pool but not yet accepted. | min(/PHP-FPM by Zabbix agent/php-fpm.listen_queue_usage,15m) > {$PHP_FPM.QUEUE.WARN.MAX} | [{"tag": "scope", "value": "capacity"}] | no url |
| Manager changed | INFO | The PHP-FPM manager has changed. Acknowledge to close the problem manually. | last(/PHP-FPM by Zabbix agent/php-fpm.process_manager,#1)<>last(/PHP-FPM by Zabbix agent/php-fpm.process_manager,#2) | [{"tag": "scope", "value": "notice"}] | no url |
| Detected slow requests | WARNING | The PHP-FPM has detected a slow request. <br>The slow request means that it took more time to execute than expected (defined in the configuration of your pool). | min(/PHP-FPM by Zabbix agent/php-fpm.slow_requests,#3)>0 | [{"tag": "scope", "value": "performance"}] | no url |
| Pool has been restarted | INFO | Uptime is less than 10 minutes. | last(/PHP-FPM by Zabbix agent/php-fpm.uptime)<10m | [{"tag": "scope", "value": "notice"}] | no url |
| Version has changed | INFO | The PHP-FPM version has changed. Acknowledge to close the problem manually. | last(/PHP-FPM by Zabbix agent/php-fpm.version,#1)<>last(/PHP-FPM by Zabbix agent/php-fpm.version,#2) and length(last(/PHP-FPM by Zabbix agent/php-fpm.version))>0 | [{"tag": "scope", "value": "notice"}] | no url |


<a name="discoveries" />

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| PHP-FPM process discovery | php-fpm.proc.discovery | The discovery of the PHP-FPM summary processes. | DEPENDENT | no lifetime | 0 |


<a name="discovery_php-fpm_process_discovery" />

## Discovery PHP-FPM process discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Get process data | The summary metrics aggregated by a process `{#PHP_FPM.NAME}`. | php-fpm.proc.get[{#PHP_FPM.NAME}] | DEPENDENT |
| Number of running processes | The number of running processes `{#PHP_FPM.NAME}`. | php-fpm.proc.num[{#PHP_FPM.NAME}] | DEPENDENT |
| Memory usage, % | The percentage of real memory used by a process `{#PHP_FPM.NAME}`. | php-fpm.proc.pmem[{#PHP_FPM.NAME}] | DEPENDENT |
| Memory usage (rss) | The summary of resident set size memory used by a process `{#PHP_FPM.NAME}` expressed in bytes. | php-fpm.proc.rss[{#PHP_FPM.NAME}] | DEPENDENT |
| Memory usage (vsize) | The summary of virtual memory used by a process `{#PHP_FPM.NAME}` expressed in bytes. | php-fpm.proc.vmem[{#PHP_FPM.NAME}] | DEPENDENT |
| CPU utilization | The percentage of the CPU utilization by a process `{#PHP_FPM.NAME}`. | proc.cpu.util[{#PHP_FPM.NAME}] | no type |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Process is not running | HIGH | no description | last(/PHP-FPM by Zabbix agent/php-fpm.proc.num[{#PHP_FPM.NAME}])=0 | [{"tag": "scope", "value": "availability"}] | no url |
| Failed to fetch info data | INFO | Zabbix has not received any data for items for the last 30 minutes. | nodata(/PHP-FPM by Zabbix agent/php-fpm.uptime,30m)=1 and last(/PHP-FPM by Zabbix agent/php-fpm.proc.num[{#PHP_FPM.NAME}])>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Service is down | HIGH | no description | (last(/PHP-FPM by Zabbix agent/php-fpm.ping)=0 or nodata(/PHP-FPM by Zabbix agent/php-fpm.ping,3m)=1) and last(/PHP-FPM by Zabbix agent/php-fpm.proc.num[{#PHP_FPM.NAME}])>0 | [{"tag": "scope", "value": "availability"}] | no url |

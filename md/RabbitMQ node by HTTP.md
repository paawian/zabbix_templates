# RabbitMQ node by HTTP template description

This template is developed to monitor the messaging broker RabbitMQ node by Zabbix that works without any external scripts.
Most of the metrics are collected in one go, thanks to Zabbix bulk data collection.

The template collects metrics by polling RabbitMQ management plugin with HTTP agent remotely.

Setup:

1. Enable the RabbitMQ management plugin. See the RabbitMQ documentation for the instructions:
https://www.rabbitmq.com/management.html

2. Create a user to monitor the service:

rabbitmqctl add_user zbx_monitor <PASSWORD>
rabbitmqctl set_permissions  -p / zbx_monitor "" "" ".*"
rabbitmqctl set_user_tags zbx_monitor monitoring

3. Set the hostname or IP address of the RabbitMQ node host in the '{$RABBITMQ.API.HOST}' macro. You can also change the port in the '{$RABBITMQ.API.PORT}' macro and the scheme in the '{$RABBITMQ.API.SCHEME}' macro if necessary.

4. Set the user name and password in the macros '{$RABBITMQ.API.USER}' and '{$RABBITMQ.API.PASSWORD}'.

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/387226-discussion-thread-for-official-zabbix-template-rabbitmq

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Health Check 3.8.9- discovery ](#discovery_health_check_3.8.9-_discovery)
  * [Discovery Health Check 3.8.10+ discovery ](#discovery_health_check_3.8.10+_discovery)
  * [Discovery Queues discovery ](#discovery_queues_discovery)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Service response time | no description | net.tcp.service.perf["{$RABBITMQ.API.SCHEME}","{$RABBITMQ.API.HOST}","{$RABBITMQ.API.PORT}"] | SIMPLE | no delay |
| Service ping | no description | net.tcp.service["{$RABBITMQ.API.SCHEME}","{$RABBITMQ.API.HOST}","{$RABBITMQ.API.PORT}"] | SIMPLE | no delay |
| Get nodes | The HTTP API endpoint that returns metrics of the nodes. | rabbitmq.get_nodes | HTTP_AGENT | no delay |
| Get node overview | The HTTP API endpoint that returns cluster-wide metrics. | rabbitmq.get_node_overview | HTTP_AGENT | no delay |
| Get queues | The HTTP API endpoint that returns metrics of the queues metrics. | rabbitmq.get_queues | HTTP_AGENT | no delay |
| Free disk space | The current free disk space. | rabbitmq.node.disk_free | DEPENDENT | 0 |
| Disk free alarm | It checks whether the node has a disk alarm or not. | rabbitmq.node.disk_free_alarm | DEPENDENT | 0 |
| Disk free limit | The free space limit of a disk expressed in bytes. | rabbitmq.node.disk_free_limit | DEPENDENT | 0 |
| Used file descriptors | The descriptors of the used file. | rabbitmq.node.fd_used | DEPENDENT | 0 |
| Memory alarm | It checks whether the host has a memory alarm or not. | rabbitmq.node.mem_alarm | DEPENDENT | 0 |
| Memory limit | The memory usage with high watermark properties expressed in bytes. | rabbitmq.node.mem_limit | DEPENDENT | 0 |
| Memory used | The memory usage expressed in bytes. | rabbitmq.node.mem_used | DEPENDENT | 0 |
| Management plugin version | The version of the management plugin in use. | rabbitmq.node.overview.management_version | DEPENDENT | 0 |
| RabbitMQ version | The version of the RabbitMQ on the node, which processed this request. | rabbitmq.node.overview.rabbitmq_version | DEPENDENT | 0 |
| Number of network partitions | The number of network partitions, which this node "sees". | rabbitmq.node.partitions | DEPENDENT | 0 |
| Is running | It "sees" whether the node is running or not. | rabbitmq.node.running | DEPENDENT | 0 |
| Runtime run queue | The average number of Erlang processes waiting to run. | rabbitmq.node.run_queue | DEPENDENT | 0 |
| Sockets available | The file descriptors available for use as sockets. | rabbitmq.node.sockets_total | DEPENDENT | 0 |
| Sockets used | The number of file descriptors used as sockets. | rabbitmq.node.sockets_used | DEPENDENT | 0 |
| Uptime | Uptime expressed in milliseconds. | rabbitmq.node.uptime | DEPENDENT | 0 |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$RABBITMQ.API.HOST} | <SET NODE API HOST> |
| {$RABBITMQ.API.PASSWORD} | zabbix |
| {$RABBITMQ.API.PORT} | 15672 |
| {$RABBITMQ.API.SCHEME} | http |
| {$RABBITMQ.API.USER} | zbx_monitor |
| {$RABBITMQ.CLUSTER.NAME} | rabbit |
| {$RABBITMQ.LLD.FILTER.QUEUE.MATCHES} | .* |
| {$RABBITMQ.LLD.FILTER.QUEUE.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$RABBITMQ.MESSAGES.MAX.WARN} | 1000 |
| {$RABBITMQ.RESPONSE_TIME.MAX.WARN} | 10 |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Service response time is too high | WARNING | no description | min(/RabbitMQ node by HTTP/net.tcp.service.perf["{$RABBITMQ.API.SCHEME}","{$RABBITMQ.API.HOST}","{$RABBITMQ.API.PORT}"],5m)>{$RABBITMQ.RESPONSE_TIME.MAX.WARN} | [{"tag": "scope", "value": "performance"}] | no url |
| Service is down | AVERAGE | no description | last(/RabbitMQ node by HTTP/net.tcp.service["{$RABBITMQ.API.SCHEME}","{$RABBITMQ.API.HOST}","{$RABBITMQ.API.PORT}"])=0 | [{"tag": "scope", "value": "availability"}] | no url |
| Failed to fetch nodes data | WARNING | Zabbix has not received any data for items for the last 30 minutes. | nodata(/RabbitMQ node by HTTP/rabbitmq.get_nodes,30m)=1 | [{"tag": "scope", "value": "availability"}] | no url |
| Free disk space alarm | AVERAGE | For more details see [Free Disk Space Alarms](https://www.rabbitmq.com/disk-alarms.html). | last(/RabbitMQ node by HTTP/rabbitmq.node.disk_free_alarm)=1 | [{"tag": "scope", "value": "performance"}] | no url |
| Memory alarm | AVERAGE | For more details see [Memory Alarms](https://www.rabbitmq.com/memory.html). | last(/RabbitMQ node by HTTP/rabbitmq.node.mem_alarm)=1 | [{"tag": "scope", "value": "performance"}] | no url |
| Version has changed | INFO | RabbitMQ version has changed. Acknowledge to close the problem manually. | last(/RabbitMQ node by HTTP/rabbitmq.node.overview.rabbitmq_version,#1)<>last(/RabbitMQ node by HTTP/rabbitmq.node.overview.rabbitmq_version,#2) and length(last(/RabbitMQ node by HTTP/rabbitmq.node.overview.rabbitmq_version))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Number of network partitions is too high | WARNING | For more details see [Detecting Network Partitions](https://www.rabbitmq.com/partitions.html#detecting). | min(/RabbitMQ node by HTTP/rabbitmq.node.partitions,5m)>0 | [{"tag": "scope", "value": "performance"}] | no url |
| Node is not running | AVERAGE | RabbitMQ node is not running. | max(/RabbitMQ node by HTTP/rabbitmq.node.running,5m)=0 | [{"tag": "scope", "value": "availability"}] | no url |
| Host has been restarted | INFO | Uptime is less than 10 minutes. | last(/RabbitMQ node by HTTP/rabbitmq.node.uptime)<10m | [{"tag": "scope", "value": "notice"}] | no url |


<a name="discoveries" />

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Health Check 3.8.9- discovery | rabbitmq.healthcheck.v389.discovery | Specific metrics for the versions: up to and including 3.8.4. | DEPENDENT | no lifetime | 0 |
| Health Check 3.8.10+ discovery | rabbitmq.healthcheck.v3810.discovery | Specific metrics for the versions: up to and including 3.8.10. | DEPENDENT | no lifetime | 0 |
| Queues discovery | rabbitmq.queues.discovery | The metrics for an individual queue. | DEPENDENT | no lifetime | 0 |


<a name="discovery_health_check_3.8.9-_discovery" />

## Discovery Health Check 3.8.9- discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Healthcheck{#SINGLETON} | It checks whether the RabbitMQ application is running; and whether the channels and queues can be listed successfully; and that no alarms are in effect. | rabbitmq.healthcheck[{#SINGLETON}] | HTTP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Node healthcheck failed | AVERAGE | For more details see [Health Checks](https://www.rabbitmq.com/monitoring.html#health-checks). | last(/RabbitMQ node by HTTP/rabbitmq.healthcheck[{#SINGLETON}])=0 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discovery_health_check_3.8.10+_discovery" />

## Discovery Health Check 3.8.10+ discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Healthcheck: expiration date on the certificates{#SINGLETON} | It checks the expiration date on the certificates for every listener configured to use the Transport Layer Security (TLS).<br>It responds with a status code `200 OK` if all the certificates are valid (have not expired).<br>Otherwise, it responds with a status code `503 Service Unavailable`. | rabbitmq.healthcheck.certificate_expiration[{#SINGLETON}] | HTTP_AGENT |
| Healthcheck: local alarms in effect on this node{#SINGLETON} | It responds with a status code `200 OK` if there are no alarms in effect in the cluster.<br>Otherwise, it responds with a status code `503 Service Unavailable`. | rabbitmq.healthcheck.local_alarms[{#SINGLETON}] | HTTP_AGENT |
| Healthcheck: classic mirrored queues without synchronized mirrors online{#SINGLETON} | It checks if there are classic mirrored queues without synchronized mirrors online (queues that would potentially lose data if the target node is shut down).<br>It responds with a status code `200 OK` if there are no such classic mirrored queues.<br>Otherwise, it responds with a status code `503 Service Unavailable`. | rabbitmq.healthcheck.mirror_sync[{#SINGLETON}] | HTTP_AGENT |
| Healthcheck: queues with minimum online quorum{#SINGLETON} | It checks if there are quorum queues with minimum online quorum (queues that would lose their quorum and availability if the target node is shut down).<br>It responds with a status code `200 OK` if there are no such quorum queues.<br>Otherwise, it responds with a status code `503 Service Unavailable`. | rabbitmq.healthcheck.quorum[{#SINGLETON}] | HTTP_AGENT |
| Healthcheck: virtual hosts on this node{#SINGLETON} | It responds with It responds with a status code `200 OK` if all virtual hosts are running on the target node.<br>Otherwise it responds with a status code `503 Service Unavailable`. | rabbitmq.healthcheck.virtual_hosts[{#SINGLETON}] | HTTP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| There are valid TLS certificates expiring in the next month | AVERAGE | This is the default API endpoint path: http://{$RABBITMQ.API.HOST}:{$RABBITMQ.API.PORT}/api/index.html. | last(/RabbitMQ node by HTTP/rabbitmq.healthcheck.certificate_expiration[{#SINGLETON}])=0 | [{"tag": "scope", "value": "notice"}] | no url |
| There are active alarms in the node | AVERAGE | This is the default API endpoint path: http://{$RABBITMQ.API.HOST}:{$RABBITMQ.API.PORT}/api/index.html. | last(/RabbitMQ node by HTTP/rabbitmq.healthcheck.local_alarms[{#SINGLETON}])=0 | [{"tag": "scope", "value": "notice"}] | no url |
| There are queues that could potentially lose data if this node goes offline. | AVERAGE | This is the default API endpoint path: http://{$RABBITMQ.API.HOST}:{$RABBITMQ.API.PORT}/api/index.html. | last(/RabbitMQ node by HTTP/rabbitmq.healthcheck.mirror_sync[{#SINGLETON}])=0 | [{"tag": "scope", "value": "notice"}] | no url |
| There are queues that would lose their quorum and availability if this node is shut down. | AVERAGE | This is the default API endpoint path: http://{$RABBITMQ.API.HOST}:{$RABBITMQ.API.PORT}/api/index.html. | last(/RabbitMQ node by HTTP/rabbitmq.healthcheck.quorum[{#SINGLETON}])=0 | [{"tag": "scope", "value": "notice"}] | no url |
| There are not running virtual hosts | AVERAGE | This is the default API endpoint path: http://{$RABBITMQ.API.HOST}:{$RABBITMQ.API.PORT}/api/index.html. | last(/RabbitMQ node by HTTP/rabbitmq.healthcheck.virtual_hosts[{#SINGLETON}])=0 | [{"tag": "scope", "value": "notice"}] | no url |


<a name="discovery_queues_discovery" />

## Discovery Queues discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Queue [{#VHOST}][{#QUEUE}]: Get data | The HTTP API endpoint that returns [{#VHOST}][{#QUEUE}] queue metrics | rabbitmq.get_exchanges["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Consumers | The number of consumers. | rabbitmq.queue.consumers["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Memory | The bytes of memory consumed by the Erlang process associated with the queue, including stack, heap and internal structures. | rabbitmq.queue.memory["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Messages acknowledged per second | The number of messages (per second) delivered to clients and acknowledged. | rabbitmq.queue.messages.ack.rate["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Messages acknowledged | The number of messages delivered to clients and acknowledged. | rabbitmq.queue.messages.ack["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Messages delivered per second | The count of messages (per second) delivered to consumers in acknowledgement mode. | rabbitmq.queue.messages.deliver.rate["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Messages delivered | The count of messages delivered to consumers in acknowledgement mode. | rabbitmq.queue.messages.deliver["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Sum of messages delivered per second | The rate of delivery per second. The sum of messages delivered (per second) to consumers: in acknowledgement mode and in no-acknowledgement mode; delivered to consumers in response to `basic.get`: in acknowledgement mode and in no-acknowledgement mode. | rabbitmq.queue.messages.deliver_get.rate["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Sum of messages delivered | The sum of messages delivered to consumers: in acknowledgement mode and in no-acknowledgement mode; delivered to consumers in response to the `basic.get`: in acknowledgement mode and in no-acknowledgement mode. | rabbitmq.queue.messages.deliver_get["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Messages published per second | The rate of published messages per second. | rabbitmq.queue.messages.publish.rate["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Messages published | The count of published messages. | rabbitmq.queue.messages.publish["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Messages per second | The count of total messages per second in the queue. | rabbitmq.queue.messages.rate["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Messages redelivered per second | The rate of messages redelivered per second. | rabbitmq.queue.messages.redeliver.rate["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Messages redelivered | The count of subset of messages in the `deliver_get` queue with the `redelivered` flag set. | rabbitmq.queue.messages.redeliver["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Messages total | The count of total messages in the queue. | rabbitmq.queue.messages["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Messages ready per second | The number of messages per second ready to be delivered to clients. | rabbitmq.queue.messages_ready.rate["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Messages ready | The number of messages ready to be delivered to clients. | rabbitmq.queue.messages_ready["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Messages unacknowledged per second | The number of messages per second delivered to clients but not yet acknowledged. | rabbitmq.queue.messages_unacknowledged.rate["{#VHOST}/{#QUEUE}"] | DEPENDENT |
| Queue [{#VHOST}][{#QUEUE}]: Messages unacknowledged | The number of messages delivered to clients but not yet acknowledged. | rabbitmq.queue.messages_unacknowledged["{#VHOST}/{#QUEUE}"] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Too many messages in queue [{#VHOST}][{#QUEUE}] | WARNING | no description | min(/RabbitMQ node by HTTP/rabbitmq.queue.messages["{#VHOST}/{#QUEUE}"],5m)>{$RABBITMQ.MESSAGES.MAX.WARN:"{#QUEUE}"} | [{"tag": "scope", "value": "performance"}] | no url |


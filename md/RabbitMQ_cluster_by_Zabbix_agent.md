# RabbitMQ cluster by Zabbix agent template description

Get cluster metrics from RabbitMQ management plugin provided an HTTP-based API using Zabbix agent.

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/387226-discussion-thread-for-official-zabbix-template-rabbitmq

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Exchanges discovery ](#discovery_exchanges_discovery)
  * [Discovery Health Check 3.8.10+ discovery ](#discovery_health_check_3.8.10+_discovery)

<a name="items"></a>

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Messages acknowledged | The number of messages delivered to clients and acknowledged. | rabbitmq.overview.messages.ack | DEPENDENT | 0 |
| Messages acknowledged per second | The rate of messages (per second) delivered to clients and acknowledged. | rabbitmq.overview.messages.ack.rate | DEPENDENT | 0 |
| Messages confirmed | The count of confirmed messages. | rabbitmq.overview.messages.confirm | DEPENDENT | 0 |
| Messages confirmed per second | The rate of messages confirmed per second. | rabbitmq.overview.messages.confirm.rate | DEPENDENT | 0 |
| Messages delivered | The sum of messages delivered to consumers: in acknowledgement mode and in no-acknowledgement mode; delivered to consumers in response to the `basic.get`: in acknowledgement mode and in no-acknowledgement mode. | rabbitmq.overview.messages.deliver_get | DEPENDENT | 0 |
| Messages delivered per second | The rate of the sum of messages (per second) delivered to consumers: in acknowledgement mode and in no-acknowledgement mode; delivered to consumers in response to the `basic.get`: in acknowledgement mode and in no-acknowledgement mode. | rabbitmq.overview.messages.deliver_get.rate | DEPENDENT | 0 |
| Messages published | The count of published messages. | rabbitmq.overview.messages.publish | DEPENDENT | 0 |
| Messages published per second | The rate of messages published per second. | rabbitmq.overview.messages.publish.rate | DEPENDENT | 0 |
| Messages publish_in | The count of messages published from the channels into this overview. | rabbitmq.overview.messages.publish_in | DEPENDENT | 0 |
| Messages publish_in per second | The rate of messages (per second) published from the channels into this overview. | rabbitmq.overview.messages.publish_in.rate | DEPENDENT | 0 |
| Messages publish_out | The count of messages published from this overview into queues. | rabbitmq.overview.messages.publish_out | DEPENDENT | 0 |
| Messages publish_out per second | The rate of messages (per second) published from this overview into queues. | rabbitmq.overview.messages.publish_out.rate | DEPENDENT | 0 |
| Messages returned redeliver | The count of subset of messages in the `deliver_get`, which had the `redelivered` flag set. | rabbitmq.overview.messages.redeliver | DEPENDENT | 0 |
| Messages returned redeliver per second | The rate of subset of messages (per second) in the `deliver_get`, which had the `redelivered` flag set. | rabbitmq.overview.messages.redeliver.rate | DEPENDENT | 0 |
| Messages returned unroutable | The count of messages returned to a publisher as unroutable. | rabbitmq.overview.messages.return_unroutable | DEPENDENT | 0 |
| Messages returned unroutable per second | The rate of messages (per second) returned to a publisher as unroutable. | rabbitmq.overview.messages.return_unroutable.rate | DEPENDENT | 0 |
| Channels total | The total number of channels. | rabbitmq.overview.object_totals.channels | DEPENDENT | 0 |
| Connections total | The total number of connections. | rabbitmq.overview.object_totals.connections | DEPENDENT | 0 |
| Consumers total | The total number of consumers. | rabbitmq.overview.object_totals.consumers | DEPENDENT | 0 |
| Exchanges total | The total number of exchanges. | rabbitmq.overview.object_totals.exchanges | DEPENDENT | 0 |
| Queues total | The total number of queues. | rabbitmq.overview.object_totals.queues | DEPENDENT | 0 |
| Messages total | The total number of messages (ready, plus unacknowledged). | rabbitmq.overview.queue_totals.messages | DEPENDENT | 0 |
| Messages ready for delivery | The number of messages ready for delivery. | rabbitmq.overview.queue_totals.messages.ready | DEPENDENT | 0 |
| Messages unacknowledged | The number of unacknowledged messages. | rabbitmq.overview.queue_totals.messages.unacknowledged | DEPENDENT | 0 |
| Get exchanges | The HTTP API endpoint that returns exchanges metrics. | web.page.get["{$RABBITMQ.API.SCHEME}://{$RABBITMQ.API.USER}:{$RABBITMQ.API.PASSWORD}@{$RABBITMQ.API.CLUSTER_HOST}:{$RABBITMQ.API.PORT}/api/exchanges"] | no type | no delay |
| Get overview | The HTTP API endpoint that returns cluster-wide metrics. | web.page.get["{$RABBITMQ.API.SCHEME}://{$RABBITMQ.API.USER}:{$RABBITMQ.API.PASSWORD}@{$RABBITMQ.API.CLUSTER_HOST}:{$RABBITMQ.API.PORT}/api/overview"] | no type | no delay |


<a name="macros"></a>

## Macros
| macro | value |
| ------------- |------------- |
| {$RABBITMQ.API.CLUSTER_HOST} | 127.0.0.1 |
| {$RABBITMQ.API.PASSWORD} | zabbix |
| {$RABBITMQ.API.PORT} | 15672 |
| {$RABBITMQ.API.SCHEME} | http |
| {$RABBITMQ.API.USER} | zbx_monitor |
| {$RABBITMQ.LLD.FILTER.EXCHANGE.MATCHES} | .* |
| {$RABBITMQ.LLD.FILTER.EXCHANGE.NOT_MATCHES} | CHANGE_IF_NEEDED |


<a name="triggers"></a>

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Failed to fetch overview data | WARNING | Zabbix has not received any data for items for the last 30 minutes. | nodata(/RabbitMQ cluster by Zabbix agent/web.page.get["{$RABBITMQ.API.SCHEME}://{$RABBITMQ.API.USER}:{$RABBITMQ.API.PASSWORD}@{$RABBITMQ.API.CLUSTER_HOST}:{$RABBITMQ.API.PORT}/api/overview"],30m)=1 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discoveries"></a>

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Exchanges discovery | rabbitmq.exchanges.discovery | The metrics for an individual exchange. | DEPENDENT | no lifetime | 0 |
| Health Check 3.8.10+ discovery | rabbitmq.healthcheck.v3810.discovery | Specific metrics for the versions: up to and including 3.8.10. | DEPENDENT | no lifetime | 0 |


<a name="discovery_exchanges_discovery"></a>

## Discovery Exchanges discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Messages acknowledged per second | The rate of messages (per second) delivered to clients and acknowledged. | rabbitmq.exchange.messages.ack.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Messages acknowledged | The number of messages delivered to clients and acknowledged. | rabbitmq.exchange.messages.ack["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Messages confirmed per second | The rate of messages confirmed per second. | rabbitmq.exchange.messages.confirm.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Messages confirmed | The count of confirmed messages. | rabbitmq.exchange.messages.confirm["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Messages delivered per second | The rate of the sum of messages (per second) delivered to consumers: in acknowledgement mode and in no-acknowledgement mode; delivered to consumers in response to the `basic.get`: in acknowledgement mode and in no-acknowledgement mode. | rabbitmq.exchange.messages.deliver_get.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Messages delivered | The sum of messages delivered to consumers: in acknowledgement mode and in no-acknowledgement mode; delivered to consumers in response to the `basic.get`: in acknowledgement mode and in no-acknowledgement mode. | rabbitmq.exchange.messages.deliver_get["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Messages published per second | The rate of messages published per second. | rabbitmq.exchange.messages.publish.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Messages published | The count of published messages. | rabbitmq.exchange.messages.publish["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Messages publish_in per second | The rate of messages (per second) published from the channels into this overview. | rabbitmq.exchange.messages.publish_in.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Messages publish_in | The count of messages published from the channels into this overview. | rabbitmq.exchange.messages.publish_in["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Messages publish_out per second | The rate of messages (per second) published from this overview into queues. | rabbitmq.exchange.messages.publish_out.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Messages publish_out | The count of messages published from this overview into queues. | rabbitmq.exchange.messages.publish_out["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange {#VHOST}/{#EXCHANGE}/{#TYPE}: Messages redelivered per second | The rate of subset of messages (per second) in the `deliver_get`, which had the `redelivered` flag set. | rabbitmq.exchange.messages.redeliver.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Messages redelivered | The count of subset of messages in the `deliver_get`, which had the `redelivered` flag set. | rabbitmq.exchange.messages.redeliver["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Messages returned unroutable per second | The rate of messages (per second) returned to a publisher as unroutable. | rabbitmq.exchange.messages.return_unroutable.rate["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Messages returned unroutable | The count of messages returned to a publisher as unroutable. | rabbitmq.exchange.messages.return_unroutable["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |
| Exchange [{#VHOST}][{#EXCHANGE}][{#TYPE}]: Get data | The HTTP API endpoint that returns [{#VHOST}][{#EXCHANGE}][{#TYPE}] exchanges metrics | rabbitmq.get_exchanges["{#VHOST}/{#EXCHANGE}/{#TYPE}"] | DEPENDENT |


<a name="discovery_health_check_3.8.10+_discovery"></a>

## Discovery Health Check 3.8.10+ discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Healthcheck: alarms in effect in the cluster{#SINGLETON} | It responds with a status code `200 OK` if there are no alarms in effect in the cluster.<br>Otherwise, it responds with a status code `503 Service Unavailable`. | web.page.get["{$RABBITMQ.API.SCHEME}://{$RABBITMQ.API.USER}:{$RABBITMQ.API.PASSWORD}@{$RABBITMQ.API.CLUSTER_HOST}:{$RABBITMQ.API.PORT}/api/health/checks/alarms{#SINGLETON}"] | no type |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| There are active alarms in the cluster | AVERAGE | This is the default API endpoint path: http://{$RABBITMQ.API.CLUSTER_HOST}:{$RABBITMQ.API.PORT}/api/index.html. | last(/RabbitMQ cluster by Zabbix agent/web.page.get["{$RABBITMQ.API.SCHEME}://{$RABBITMQ.API.USER}:{$RABBITMQ.API.PASSWORD}@{$RABBITMQ.API.CLUSTER_HOST}:{$RABBITMQ.API.PORT}/api/health/checks/alarms{#SINGLETON}"])=0 | [{"tag": "scope", "value": "notice"}] | no url |


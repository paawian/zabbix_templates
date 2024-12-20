# Kubernetes Controller manager by HTTP template description

Get Kubernetes Controller manager metrics by HTTP agent from Prometheus metrics endpoint.

Don't forget change macros {$KUBE.API.SERVER.URL}.
Some metrics may not be collected depending on your Kubernetes Controller manager instance version and configuration.

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Workqueue metrics discovery ](#discovery_workqueue_metrics_discovery)

<a name="items"></a>

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| REST Client requests: 2xx, rate | Number of HTTP requests with 2xx status code per second. | kubernetes.controller.client_http_requests_200.rate | DEPENDENT | 0 |
| REST Client requests: 3xx, rate | Number of HTTP requests with 3xx status code per second. | kubernetes.controller.client_http_requests_300.rate | DEPENDENT | 0 |
| REST Client requests: 4xx, rate | Number of HTTP requests with 4xx status code per second. | kubernetes.controller.client_http_requests_400.rate | DEPENDENT | 0 |
| REST Client requests: 5xx, rate | Number of HTTP requests with 5xx status code per second. | kubernetes.controller.client_http_requests_500.rate | DEPENDENT | 0 |
| CPU | Total user and system CPU usage ratio. | kubernetes.controller.cpu.util | DEPENDENT | 0 |
| Kubernetes Controller: Get Controller metrics | Get raw metrics from Controller instance /metrics endpoint. | kubernetes.controller.get_metrics | HTTP_AGENT | no delay |
| Goroutines | Number of goroutines that currently exist. | kubernetes.controller.go_goroutines | DEPENDENT | 0 |
| Go threads | Number of OS threads created. | kubernetes.controller.go_threads | DEPENDENT | 0 |
| Leader election status | Gauge of if the reporting system is master of the relevant lease, 0 indicates backup, 1 indicates master. | kubernetes.controller.leader_election_master_status | DEPENDENT | 0 |
| Fds max | Maximum allowed open file descriptors. | kubernetes.controller.max_fds | DEPENDENT | 0 |
| Fds open | Number of open file descriptors. | kubernetes.controller.open_fds | DEPENDENT | 0 |
| Resident memory, bytes | Resident memory size in bytes. | kubernetes.controller.process_resident_memory_bytes | DEPENDENT | 0 |
| Virtual memory, bytes | Virtual memory size in bytes. | kubernetes.controller.process_virtual_memory_bytes | DEPENDENT | 0 |


<a name="macros"></a>

## Macros
| macro | value |
| ------------- |------------- |
| {$KUBE.API.TOKEN} | no value |
| {$KUBE.CONTROLLER.HTTP.CLIENT.ERROR} | 2 |
| {$KUBE.CONTROLLER.SERVER.URL} | https://localhost:10257/metrics |


<a name="triggers"></a>

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Too many HTTP client errors | WARNING | "Kubernetes Controller manager is experiencing high error rate (with 5xx HTTP code). | min(/Kubernetes Controller manager by HTTP/kubernetes.controller.client_http_requests_500.rate,5m)>{$KUBE.CONTROLLER.HTTP.CLIENT.ERROR} | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discoveries"></a>

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Workqueue metrics discovery | kubernetes.controller.workqueue.discovery | no description | DEPENDENT | no lifetime | 0 |


<a name="discovery_workqueue_metrics_discovery"></a>

## Discovery Workqueue metrics discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| ["{#NAME}"]: Workqueue duration seconds bucket, {#LE} | How long in seconds processing an item from workqueue takes. | kubernetes.controller.duration_seconds_bucket[{#LE},"{#NAME}"] | DEPENDENT |
| ["{#NAME}"]: Queue duration seconds bucket, {#LE} | How long in seconds an item stays in workqueue before being requested. | kubernetes.controller.queue_duration_seconds_bucket[{#LE},"{#NAME}"] | DEPENDENT |
| ["{#NAME}"]: Workqueue adds total, rate | Total number of adds handled by workqueue per second. | kubernetes.controller.workqueue_adds_total["{#NAME}"] | DEPENDENT |
| ["{#NAME}"]: Workqueue depth | Current depth of workqueue. | kubernetes.controller.workqueue_depth["{#NAME}"] | DEPENDENT |
| ["{#NAME}"]: Workqueue longest running processor, sec | How many seconds has the longest running processor for workqueue been running. | kubernetes.controller.workqueue_longest_running_processor_seconds["{#NAME}"] | DEPENDENT |
| ["{#NAME}"]: Workqueue queue duration, 50p | 50 percentile of how long in seconds an item stays in workqueue before being requested. If there are no requests for 5 minute, item value will be discarded. | kubernetes.controller.workqueue_queue_duration_seconds_p50["{#NAME}"] | CALCULATED |
| ["{#NAME}"]: Workqueue queue duration, p90 | 90 percentile of how long in seconds an item stays in workqueue before being requested, by queue. | kubernetes.controller.workqueue_queue_duration_seconds_p90["{#NAME}"] | CALCULATED |
| ["{#NAME}"]: Workqueue queue duration, p95 | 95 percentile of how long in seconds an item stays in workqueue before being requested, by queue. | kubernetes.controller.workqueue_queue_duration_seconds_p95["{#NAME}"] | CALCULATED |
| ["{#NAME}"]: Workqueue queue duration, p99 | 99 percentile of how long in seconds an item stays in workqueue before being requested, by queue. | kubernetes.controller.workqueue_queue_duration_seconds_p99["{#NAME}"] | CALCULATED |
| ["{#NAME}"]: Workqueue retries, rate | Total number of retries handled by workqueue per second. | kubernetes.controller.workqueue_retries_total["{#NAME}"] | DEPENDENT |
| ["{#NAME}"]: Workqueue unfinished work, sec | How many seconds of work has done that is in progress and hasn't been observed by work_duration. Large values indicate stuck threads. One can deduce the number of stuck threads by observing the rate at which this increases. | kubernetes.controller.workqueue_unfinished_work_seconds["{#NAME}"] | DEPENDENT |
| ["{#NAME}"]: Workqueue work duration, 50p | 50 percentiles of how long in seconds processing an item from workqueue takes, by queue. | kubernetes.controller.workqueue_work_duration_seconds_p50["{#NAME}"] | CALCULATED |
| ["{#NAME}"]: Workqueue work duration, p90 | 90 percentile of how long in seconds processing an item from workqueue takes, by queue. | kubernetes.controller.workqueue_work_duration_seconds_p90["{#NAME}"] | CALCULATED |
| ["{#NAME}"]: Workqueue work duration, p95 | 95 percentile of how long in seconds processing an item from workqueue takes, by queue. | kubernetes.controller.workqueue_work_duration_seconds_p95["{#NAME}"] | CALCULATED |
| ["{#NAME}"]: Workqueue work duration, p99 | 99 percentile of how long in seconds processing an item from workqueue takes, by queue. | kubernetes.controller.workqueue_work_duration_seconds_p99["{#NAME}"] | CALCULATED |


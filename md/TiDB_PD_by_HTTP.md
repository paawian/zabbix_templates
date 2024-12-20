# TiDB PD by HTTP template description

The template to monitor PD server of TiDB cluster by Zabbix that works without any external scripts.
Most of the metrics are collected in one go, thanks to Zabbix bulk data collection.
Don't forget to change the macros {$PD.URL}, {$PD.PORT}.

Template `TiDB PD by HTTP` — collects metrics by HTTP agent from PD /metrics endpoint and from monitoring API.

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Cluster metrics discovery ](#discovery_cluster_metrics_discovery)
  * [Discovery gRPC commands discovery ](#discovery_grpc_commands_discovery)
  * [Discovery Region discovery ](#discovery_region_discovery)
  * [Discovery Region labels discovery ](#discovery_region_labels_discovery)
  * [Discovery Region status discovery ](#discovery_region_status_discovery)
  * [Discovery Running scheduler discovery ](#discovery_running_scheduler_discovery)

<a name="items"></a>

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Get cluster metrics | Get cluster metrics. | pd.cluster_status.get_metrics | DEPENDENT | 0 |
| Get instance metrics | Get TiDB PD instance metrics. | pd.get_metrics | HTTP_AGENT | no delay |
| Get instance status | Get TiDB PD instance status info. | pd.get_status | HTTP_AGENT | no delay |
| gRPC Commands total, rate | The rate at which gRPC commands are completed. | pd.grpc_command.rate | DEPENDENT | 0 |
| Get gRPC command metrics | Get gRPC command metrics. | pd.grpc_commands.get_metrics | DEPENDENT | 0 |
| Get region metrics | Get region metrics. | pd.regions.get_metrics | DEPENDENT | 0 |
| Get region label metrics | Get region label metrics. | pd.region_labels.get_metrics | DEPENDENT | 0 |
| Get region status metrics | Get region status metrics. | pd.region_status.get_metrics | DEPENDENT | 0 |
| Get scheduler metrics | Get scheduler metrics. | pd.scheduler.get_metrics | DEPENDENT | 0 |
| Status | Status of PD instance. | pd.status | DEPENDENT | 0 |
| Uptime | The runtime of each PD instance. | pd.uptime | DEPENDENT | 0 |
| Version | Version of the PD instance. | pd.version | DEPENDENT | 0 |


<a name="macros"></a>

## Macros
| macro | value |
| ------------- |------------- |
| {$PD.MISS_REGION.MAX.WARN} | 100 |
| {$PD.PORT} | 2379 |
| {$PD.STORAGE_USAGE.MAX.WARN} | 80 |
| {$PD.URL} | localhost |


<a name="triggers"></a>

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Instance is not responding | AVERAGE | no description | last(/TiDB PD by HTTP/pd.status)=0 | [{"tag": "scope", "value": "availability"}] | no url |
| has been restarted | INFO | Uptime is less than 10 minutes. | last(/TiDB PD by HTTP/pd.uptime)<10m | [{"tag": "scope", "value": "notice"}] | no url |
| Version has changed | INFO | PD version has changed. Acknowledge to close the problem manually. | last(/TiDB PD by HTTP/pd.version,#1)<>last(/TiDB PD by HTTP/pd.version,#2) and length(last(/TiDB PD by HTTP/pd.version))>0 | [{"tag": "scope", "value": "notice"}] | no url |


<a name="discoveries"></a>

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Cluster metrics discovery | pd.cluster.discovery | Discovery cluster specific metrics. | DEPENDENT | no lifetime | 0 |
| gRPC commands discovery | pd.grpc_command.discovery | Discovery grpc commands specific metrics. | DEPENDENT | no lifetime | 0 |
| Region discovery | pd.region.discovery | Discovery region specific metrics. | DEPENDENT | no lifetime | 0 |
| Region labels discovery | pd.region_labels.discovery | Discovery region labels specific metrics. | DEPENDENT | no lifetime | 0 |
| Region status discovery | pd.region_status.discovery | Discovery region status specific metrics. | DEPENDENT | no lifetime | 0 |
| Running scheduler discovery | pd.scheduler.discovery | Discovery scheduler specific metrics. | DEPENDENT | no lifetime | 0 |


<a name="discovery_cluster_metrics_discovery"></a>

## Discovery Cluster metrics discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Number of regions | The total count of cluster Regions. | pd.cluster_status.leader_count[{#SINGLETON}] | DEPENDENT |
| Current peer count | The current count of all cluster peers. | pd.cluster_status.region_count[{#SINGLETON}] | DEPENDENT |
| Storage capacity | The total storage capacity for this TiDB cluster. | pd.cluster_status.storage_capacity[{#SINGLETON}] | DEPENDENT |
| Storage size | The storage size that is currently used by the TiDB cluster. | pd.cluster_status.storage_size[{#SINGLETON}] | DEPENDENT |
| Disconnect stores | The count of disconnected stores. | pd.cluster_status.store_disconnected[{#SINGLETON}] | DEPENDENT |
| Down stores | The count of down stores. | pd.cluster_status.store_down[{#SINGLETON}] | DEPENDENT |
| Lowspace stores | The count of low space stores. | pd.cluster_status.store_low_space[{#SINGLETON}] | DEPENDENT |
| Offline stores | no description | pd.cluster_status.store_offline[{#SINGLETON}] | DEPENDENT |
| Tombstone stores | The count of tombstone stores. | pd.cluster_status.store_tombstone[{#SINGLETON}] | DEPENDENT |
| Unhealth stores | The count of unhealthy stores. | pd.cluster_status.store_unhealth[{#SINGLETON}] | DEPENDENT |
| Normal stores | The count of healthy storage instances. | pd.cluster_status.store_up[{#SINGLETON}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| There are disconnected TiKV nodes | WARNING | PD does not receive a TiKV heartbeat within 20 seconds. Normally a TiKV heartbeat comes in every 10 seconds. | last(/TiDB PD by HTTP/pd.cluster_status.store_disconnected[{#SINGLETON}])>0 | [{"tag": "scope", "value": "availability"}] | no url |
| There are offline TiKV nodes | AVERAGE | PD has not received a TiKV heartbeat for a long time. | last(/TiDB PD by HTTP/pd.cluster_status.store_down[{#SINGLETON}])>0 | [{"tag": "scope", "value": "availability"}] | no url |
| There are low space TiKV nodes | AVERAGE | Indicates that there is no sufficient space on the TiKV node. | last(/TiDB PD by HTTP/pd.cluster_status.store_low_space[{#SINGLETON}])>0 | [{"tag": "scope", "value": "capacity"}] | no url |
| Current storage usage is too high | WARNING | Over {$PD.STORAGE_USAGE.MAX.WARN}% of the cluster space is occupied. | min(/TiDB PD by HTTP/pd.cluster_status.storage_size[{#SINGLETON}],5m)/last(/TiDB PD by HTTP/pd.cluster_status.storage_capacity[{#SINGLETON}])*100>{$PD.STORAGE_USAGE.MAX.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |


<a name="discovery_grpc_commands_discovery"></a>

## Discovery gRPC commands discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| gRPC Commands: {#GRPC_METHOD}, rate | The rate per command type at which gRPC commands are completed. | pd.grpc_command.rate[{#GRPC_METHOD}] | DEPENDENT |


<a name="discovery_region_discovery"></a>

## Discovery Region discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Region heartbeat: error, rate | The count of heartbeats with the error status per second. | pd.region_heartbeat.error.rate[{#STORE_ADDRESS}] | DEPENDENT |
| Get metrics: {#STORE_ADDRESS} | Get region metrics for {#STORE_ADDRESS}. | pd.region_heartbeat.get_metrics[{#STORE_ADDRESS}] | DEPENDENT |
| Region heartbeat: active, rate | The count of heartbeats with the ok status per second. | pd.region_heartbeat.ok.rate[{#STORE_ADDRESS}] | DEPENDENT |
| Region schedule push: total, rate | no description | pd.region_heartbeat.push.err.rate[{#STORE_ADDRESS}] | DEPENDENT |
| Region heartbeat: total, rate | The count of heartbeats reported to PD per instance per second. | pd.region_heartbeat.rate[{#STORE_ADDRESS}] | DEPENDENT |


<a name="discovery_region_labels_discovery"></a>

## Discovery Region labels discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Regions label: {#TYPE} | The number of Regions in different label levels. | pd.region_labels[{#TYPE}] | DEPENDENT |


<a name="discovery_region_status_discovery"></a>

## Discovery Region status discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Regions status: {#TYPE} | The health status of Regions indicated via the count of unusual Regions including pending peers, down peers, extra peers, offline peers, missing peers, learner peers and incorrect namespaces. | pd.region_status[{#TYPE}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| There are unresponsive peers | WARNING | The number of Regions with an unresponsive peer reported by the Raft leader. | min(/TiDB PD by HTTP/pd.region_status[{#TYPE}],5m)>0 | [{"tag": "scope", "value": "availability"}] | no url |
| Too many missed regions | WARNING | The number of Region replicas is smaller than the value of max-replicas. When a TiKV machine is down and its downtime exceeds max-down-time, it usually leads to missing replicas for some Regions during a period of time. When a TiKV node is made offline, it might result in a small number of Regions with missing replicas. | min(/TiDB PD by HTTP/pd.region_status[{#TYPE}],5m)>{$PD.MISS_REGION.MAX.WARN} | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discovery_running_scheduler_discovery"></a>

## Discovery Running scheduler discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Scheduler status: {#KIND} | The current running schedulers. | pd.scheduler[{#KIND}] | DEPENDENT |


# Veeam Backup and Replication by HTTP template description

This template is designed to monitor Veeam Backup and Replication.

NOTE: The RESTful API may not be available for some editions, see (https://www.veeam.com/licensing-pricing.html) for more details.

Setup:
  1. Create a user to monitor the service or use an existing read-only account.
  See (https://helpcenter.veeam.com/docs/backup/vbr_rest/reference/vbr-rest-v1-rev2.html?ver=110#tag/Login/operation/CreateToken!path=grant_type&t=request) for more details. 
  2. Link the template to a host.
  3. Configure the following macros: {$VEEAM.API.URL}, {$VEEAM.USER}, and {$VEEAM.PASSWORD}.

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Jobs states discovery ](#discovery_jobs_states_discovery)
  * [Discovery Proxies discovery ](#discovery_proxies_discovery)
  * [Discovery Repositories discovery ](#discovery_repositories_discovery)
  * [Discovery Sessions discovery ](#discovery_sessions_discovery)

<a name="items"></a>

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Get errors | The errors from API requests. | veeam.get.errors | DEPENDENT | 0 |
| Get metrics | The result of API requests is expressed in the JSON. | veeam.get.metrics | SCRIPT | 5m |


<a name="macros"></a>

## Macros
| macro | value |
| ------------- |------------- |
| {$CREATED.AFTER} | 7 |
| {$JOB.NAME.MATCHES} | .* |
| {$JOB.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$JOB.STATUS.MATCHES} | .* |
| {$JOB.STATUS.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$JOB.TYPE.MATCHES} | .* |
| {$JOB.TYPE.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$PROXIES.NAME.MATCHES} | .* |
| {$PROXIES.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$PROXIES.TYPE.MATCHES} | .* |
| {$PROXIES.TYPE.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$REPOSITORIES.NAME.MATCHES} | .* |
| {$REPOSITORIES.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$REPOSITORIES.TYPE.MATCHES} | .* |
| {$REPOSITORIES.TYPE.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$SESSION.NAME.MATCHES} | .* |
| {$SESSION.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$SESSION.TYPE.MATCHES} | .* |
| {$SESSION.TYPE.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$VEEAM.API.URL} | https://localhost:9419 |
| {$VEEAM.DATA.TIMEOUT} | 10 |
| {$VEEAM.HTTP.PROXY} | no value |
| {$VEEAM.PASSWORD} | no value |
| {$VEEAM.USER} | no value |


<a name="triggers"></a>

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| There are errors in requests to API | AVERAGE | Zabbix has received errors in response to API requests. | length(last(/Veeam Backup and Replication by HTTP/veeam.get.errors))>0 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discoveries"></a>

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Jobs states discovery | veeam.job.state.discovery | Discovery of the jobs states. | DEPENDENT | no lifetime | 0 |
| Proxies discovery | veeam.proxies.discovery | Discovery of proxies. | DEPENDENT | no lifetime | 0 |
| Repositories discovery | veeam.repositories.discovery | Discovery of repositories. | DEPENDENT | no lifetime | 0 |
| Sessions discovery | veeam.sessions.discovery | Discovery of sessions. | DEPENDENT | no lifetime | 0 |


<a name="discovery_jobs_states_discovery" />

## Discovery Jobs states discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Job states [{#NAME}] [{#TYPE}]: Last result | The result of the session. The enums used: `None`, `Success`, `Warning`, `Failed`. | veeam.jobs.last.result[{#ID}] | DEPENDENT |
| Job states [{#NAME}] [{#TYPE}]: Get data | Gets raw data from the job states with the name `[{#NAME}]`. | veeam.jobs.states.raw[{#ID}] | DEPENDENT |
| Job states [{#NAME}] [{#TYPE}]: Status | The current status of the job. The enums used: `running`, `inactive`, `disabled`. | veeam.jobs.status[{#ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Last result job failed | AVERAGE | no description | find(/Veeam Backup and Replication by HTTP/veeam.jobs.last.result[{#ID}],,"like","Failed")=1 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discovery_proxies_discovery" />

## Discovery Proxies discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Proxy [{#NAME}] [{#TYPE}]: Max Task Count | The maximum number of concurrent tasks. | veeam.proxy.maxtask[{#NAME}] | DEPENDENT |
| Proxy [{#NAME}] [{#TYPE}]: Get data | Gets raw data collected by the proxy with the name `[{#NAME}]`, `[{#TYPE}]`. | veeam.proxy.raw[{#NAME}] | DEPENDENT |
| Proxy [{#NAME}] [{#TYPE}]: Host name | The name of the proxy server. | veeam.proxy.server.name[{#NAME}] | DEPENDENT |
| Server [{#NAME}]: Get data | Gets raw data collected by the proxy server. | veeam.proxy.server.raw[{#NAME}] | DEPENDENT |
| Proxy [{#NAME}] [{#TYPE}]: Host type | The type of the proxy server. | veeam.proxy.server.type[{#NAME}] | DEPENDENT |


<a name="discovery_repositories_discovery" />

## Discovery Repositories discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Repository [{#NAME}] [{#TYPE}]: Get data | Gets raw data from repository with the name: `[{#NAME}]`, `[{#TYPE}]`. | veeam.repositories.raw[{#NAME}] | DEPENDENT |
| Repository [{#NAME}] [{#TYPE}]: Used space [{#PATH}] | Used space by repositories expressed in gigabytes (GB). | veeam.repository.capacity[{#NAME}] | DEPENDENT |
| Repository [{#NAME}] [{#TYPE}]: Free space [{#PATH}] | Free space of repositories expressed in gigabytes (GB). | veeam.repository.free.space[{#NAME}] | DEPENDENT |


<a name="discovery_sessions_discovery" />

## Discovery Sessions discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Session [{#NAME}] [{#TYPE}]: Message | A message that explains the session result. | veeam.sessions.message[{#ID}] | DEPENDENT |
| Session progress percent [{#NAME}] [{#TYPE}] | The progress of the session expressed as percentage. | veeam.sessions.progress.percent[{#ID}] | DEPENDENT |
| Session [{#NAME}] [{#TYPE}]: Get data | Gets raw data from session with the name: `[{#NAME}]`, `[{#TYPE}]`. | veeam.sessions.raw[{#ID}] | DEPENDENT |
| Session [{#NAME}] [{#TYPE}]: Result | The result of the session. The enums used: `None`, `Success`, `Warning`, `Failed`. | veeam.sessions.result[{#ID}] | DEPENDENT |
| Session [{#NAME}] [{#TYPE}]: State | The state of the session. The enums used: `Stopped`, `Starting`, `Stopping`, `Working`, `Pausing`, `Resuming`, `WaitingTape`, `Idle`, `Postprocessing`, `WaitingRepository`, `WaitingSlot`. | veeam.sessions.state[{#ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Last result session failed | AVERAGE | no description | find(/Veeam Backup and Replication by HTTP/veeam.sessions.result[{#ID}],,"like","Failed")=1 | [{"tag": "scope", "value": "availability"}] | no url |

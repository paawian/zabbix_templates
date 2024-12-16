# Microsoft SharePoint by HTTP template description

Overview:
Template receives data via HTTP Agent.
Setup:
Create a new host.
Define macros according to your Sharepoint web portal.
It is recommended to fill in the values of the filter macros to avoid getting redundant data.

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Directory discovery ](#discovery_directory_discovery)

<a name="items"></a>

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Get directory structure | Used to get directory structure information | sharepoint.get_dir | SCRIPT | {$SHAREPOINT.GET_INTERVAL} |
| Get directory structure: Status | HTTP response (status) code. Indicates whether the HTTP request was successfully completed. Additional information is available in the server log file. | sharepoint.get_dir.status | DEPENDENT | 0 |
| Get directory structure: Exec time | The time taken to execute the script for obtaining the data structure (in ms). Less is better. | sharepoint.get_dir.time | DEPENDENT | 0 |
| Health score | This item specifies a value between 0 and 10, where 0 represents a low load and a high ability to process requests and 10 represents a high load and that the server is throttling requests to maintain adequate throughput. | sharepoint.health_score | HTTP_AGENT | no delay |


<a name="macros"></a>

## Macros
| macro | value |
| ------------- |------------- |
| {$SHAREPOINT.GET_INTERVAL} | 1m |
| {$SHAREPOINT.LLD.FILTER.FULL_PATH.MATCHES} | ^/ |
| {$SHAREPOINT.LLD.FILTER.FULL_PATH.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$SHAREPOINT.LLD.FILTER.NAME.MATCHES} | .* |
| {$SHAREPOINT.LLD.FILTER.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$SHAREPOINT.LLD.FILTER.TYPE.MATCHES} | FOLDER |
| {$SHAREPOINT.LLD.FILTER.TYPE.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$SHAREPOINT.LLD_INTERVAL} | 3h |
| {$SHAREPOINT.MAX_HEALTH_SCORE} | 5 |
| {$SHAREPOINT.PASSWORD} | no value |
| {$SHAREPOINT.ROOT} | /Shared Documents |
| {$SHAREPOINT.URL} | no value |
| {$SHAREPOINT.USER} | no value |


<a name="triggers"></a>

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Error getting directory structure. | WARNING | Error getting directory structure. Check the Zabbix server log for more details. | last(/Microsoft SharePoint by HTTP/sharepoint.get_dir.status)<>200 | [{"tag": "scope", "value": "availability"}] | no url |
| Server responds slowly to API request | WARNING | no description | last(/Microsoft SharePoint by HTTP/sharepoint.get_dir.time)>2000 | [{"tag": "scope", "value": "performance"}] | no url |
| Bad health score | AVERAGE | no description | last(/Microsoft SharePoint by HTTP/sharepoint.health_score)>"{$SHAREPOINT.MAX_HEALTH_SCORE}" | [{"tag": "scope", "value": "performance"}] | no url |


<a name="discoveries"></a>

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Directory discovery | sharepoint.directory.discovery | no description | SCRIPT | no lifetime | {$SHAREPOINT.LLD_INTERVAL} |


<a name="discovery_directory_discovery" />

## Discovery Directory discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Created ({#SHAREPOINT.LLD.FULL_PATH}) | Date of creation:<br>{#SHAREPOINT.LLD.FULL_PATH} | sharepoint.created["{#SHAREPOINT.LLD.FULL_PATH}"] | DEPENDENT |
| Modified ({#SHAREPOINT.LLD.FULL_PATH}) | Date of change:<br>{#SHAREPOINT.LLD.FULL_PATH} | sharepoint.modified["{#SHAREPOINT.LLD.FULL_PATH}"] | DEPENDENT |
| Size ({#SHAREPOINT.LLD.FULL_PATH}) | Size of:<br>{#SHAREPOINT.LLD.FULL_PATH} | sharepoint.size["{#SHAREPOINT.LLD.FULL_PATH}"] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Sharepoint object is changed | INFO | Updated date of modification of folder / file | last(/Microsoft SharePoint by HTTP/sharepoint.modified["{#SHAREPOINT.LLD.FULL_PATH}"],#1)<>last(/Microsoft SharePoint by HTTP/sharepoint.modified["{#SHAREPOINT.LLD.FULL_PATH}"],#2) | [{"tag": "scope", "value": "notice"}] | no url |

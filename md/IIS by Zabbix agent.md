# IIS by Zabbix agent template description

Get metrics from IIS using Zabbix agent running on Windows.

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/401862-discussion-thread-for-official-zabbix-template-internet-information-services

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Application pools discovery ](#discovery_application_pools_discovery)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| {$IIS.PORT} port ping | no description | net.tcp.service[{$IIS.SERVICE},,{$IIS.PORT}] | SIMPLE | no delay |
| Anonymous users per second | The number of requests from users over an anonymous connection per second. Average per minute. | perf_counter_en["\Web Service(_Total)\Anonymous Users/sec", 60] | no type | no delay |
| Bytes Received per second | The average rate per minute at which data bytes are received by the service at the Application Layer. Does not include protocol headers or control bytes. | perf_counter_en["\Web Service(_Total)\Bytes Received/sec", 60] | no type | no delay |
| Bytes Sent per second | The average rate per minute at which data bytes are sent by the service. | perf_counter_en["\Web Service(_Total)\Bytes Sent/sec", 60] | no type | no delay |
| Bytes Total per second | The average rate per minute of total bytes/sec transferred by the Web service (sum of bytes sent/sec and bytes received/sec). | perf_counter_en["\Web Service(_Total)\Bytes Total/Sec", 60] | no type | no delay |
| Method CGI requests per second | The rate of CGI requests that are simultaneously being processed by the Web service. Average per minute. | perf_counter_en["\Web Service(_Total)\CGI Requests/Sec", 60] | no type | no delay |
| Connection attempts per second | The average rate per minute that connections using the Web service are being attempted. The count is the average for all Web sites combined. | perf_counter_en["\Web Service(_Total)\Connection Attempts/Sec", 60] | no type | no delay |
| Method COPY requests per second | The rate of HTTP requests made using the COPY method. Copy requests are used for copying files and directories. Average per minute. | perf_counter_en["\Web Service(_Total)\Copy Requests/Sec", 60] | no type | no delay |
| Current connections | The number of active connections. | perf_counter_en["\Web Service(_Total)\Current Connections"] | no type | no delay |
| Method DELETE requests per second | The rate of HTTP requests using the DELETE method made. Average per minute. | perf_counter_en["\Web Service(_Total)\Delete Requests/Sec", 60] | no type | no delay |
| Method GET requests per second | The rate of HTTP requests made using the GET method. GET requests are generally used for basic file retrievals or image maps, though they can be used with forms. Average per minute. | perf_counter_en["\Web Service(_Total)\Get Requests/Sec", 60] | no type | no delay |
| Method HEAD requests per second | The rate of HTTP requests using the HEAD method made. HEAD requests generally indicate a client is querying the state of a document they already have to see if it needs to be refreshed. Average per minute. | perf_counter_en["\Web Service(_Total)\Head Requests/Sec", 60] | no type | no delay |
| Method ISAPI requests per second | The rate of ISAPI Extension requests that are simultaneously being processed by the Web service. Average per minute. | perf_counter_en["\Web Service(_Total)\ISAPI Extension Requests/Sec", 60] | no type | no delay |
| Locked errors per second | The rate of errors due to requests that couldn't be satisfied by the server because the requested document was locked. These are generally reported as an HTTP 423 error code to the client. Average per minute. | perf_counter_en["\Web Service(_Total)\Locked Errors/Sec", 60] | no type | no delay |
| Method LOCK requests per second | The rate of HTTP requests made using the LOCK method. Lock requests are used to lock a file for one user so that only that user can modify the file. Average per minute. | perf_counter_en["\Web Service(_Total)\Lock Requests/Sec", 60] | no type | no delay |
| Method MKCOL requests per second | The rate of HTTP requests using the MKCOL method made. Mkcol requests are used to create directories on the server. Average per minute. | perf_counter_en["\Web Service(_Total)\Mkcol Requests/Sec", 60] | no type | no delay |
| Method MOVE requests per second | The rate of HTTP requests using the MOVE method made. Move requests are used for moving files and directories. Average per minute. | perf_counter_en["\Web Service(_Total)\Move Requests/Sec", 60] | no type | no delay |
| NonAnonymous users per second | The number of requests from users over a non-anonymous connection per second. Average per minute. | perf_counter_en["\Web Service(_Total)\NonAnonymous Users/sec", 60] | no type | no delay |
| Not Found errors per second | The rate of errors due to requests that couldn't be satisfied by the server because the requested document could not be found. These are generally reported to the client with HTTP error code 404. Average per minute. | perf_counter_en["\Web Service(_Total)\Not Found Errors/Sec", 60] | no type | no delay |
| Method OPTIONS requests per second | The rate of HTTP requests using the OPTIONS method made. Average per minute. | perf_counter_en["\Web Service(_Total)\Options Requests/Sec", 60] | no type | no delay |
| Method Total Other requests per second | Total Other Request Methods is the number of HTTP requests that are not OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, MOVE, COPY, MKCOL, PROPFIND, PROPPATCH, SEARCH, LOCK or UNLOCK methods (since service startup). Average per minute. | perf_counter_en["\Web Service(_Total)\Other Request Methods/Sec", 60] | no type | no delay |
| Method POST requests per second | Rate of HTTP requests using POST method. Generally used for forms or gateway requests. Average per minute. | perf_counter_en["\Web Service(_Total)\Post Requests/Sec", 60] | no type | no delay |
| Method PROPFIND requests per second | The rate of HTTP requests using the PROPFIND method made. Propfind requests retrieve property values on files and directories. Average per minute. | perf_counter_en["\Web Service(_Total)\Propfind Requests/Sec", 60] | no type | no delay |
| Method PROPPATCH requests per second | The rate of HTTP requests using the PROPPATCH method made. Proppatch requests set property values on files and directories. Average per minute. | perf_counter_en["\Web Service(_Total)\Proppatch Requests/Sec", 60] | no type | no delay |
| Method PUT requests per second | The rate of HTTP requests using the PUT method made. Average per minute. | perf_counter_en["\Web Service(_Total)\Put Requests/Sec", 60] | no type | no delay |
| Method MS-SEARCH requests per second | The rate of HTTP requests using the MS-SEARCH method made. Search requests are used to query the server to find resources that match a set of conditions provided by the client. Average per minute. | perf_counter_en["\Web Service(_Total)\Search Requests/Sec", 60] | no type | no delay |
| Uptime | The service uptime expressed in seconds. | perf_counter_en["\Web Service(_Total)\Service Uptime"] | no type | no delay |
| Total connection attempts | The total number of connections to the Web or FTP service that have been attempted since service startup. The count is the total for all Web sites or FTP sites combined. | perf_counter_en["\Web Service(_Total)\Total Connection Attempts (all instances)"] | no type | no delay |
| Method Total requests per second | The rate of all HTTP requests received. Average per minute. | perf_counter_en["\Web Service(_Total)\Total Method Requests/Sec", 60] | no type | no delay |
| Method TRACE requests per second | The rate of HTTP requests using the TRACE method made. Average per minute. | perf_counter_en["\Web Service(_Total)\Trace Requests/Sec", 60] | no type | no delay |
| Method TRACE requests per second | The rate of HTTP requests using the UNLOCK method made. Unlock requests are used to remove locks from files. Average per minute. | perf_counter_en["\Web Service(_Total)\Unlock Requests/Sec", 60] | no type | no delay |
| Files cache hits percentage | The ratio of user-mode file cache hits to total cache requests (since service startup). Note: This value might be low if the Kernel URI cache hits percentage is high. | perf_counter_en["\Web Service Cache\File Cache Hits %"] | no type | no delay |
| File cache misses | The total number of unsuccessful lookups in the user-mode file cache since service startup. | perf_counter_en["\Web Service Cache\File Cache Misses"] | no type | no delay |
| URIs cache hits percentage | The ratio of user-mode URI Cache Hits to total cache requests (since service startup) | perf_counter_en["\Web Service Cache\URI Cache Hits %"] | no type | no delay |
| URI cache misses | The total number of unsuccessful lookups in the user-mode URI cache since service startup. | perf_counter_en["\Web Service Cache\URI Cache Misses"] | no type | no delay |
| World Wide Web Publishing Service (W3SVC) state | The World Wide Web Publishing Service (W3SVC) provides web connectivity and administration of websites through the IIS snap-in. If the World Wide Web Publishing Service stops, the operating system cannot serve any form of web request. This service was dependent on "Windows Process Activation Service". | service.info[W3SVC] | no type | no delay |
| Windows Process Activation Service (WAS) state | Windows Process Activation Service (WAS) is a tool for managing worker processes that contain applications that host Windows Communication Foundation (WCF) services. Worker processes handle requests that are sent to a Web Server for specific application pools. Each application pool sets boundaries for the applications it contains. | service.info[WAS] | no type | no delay |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$IIS.APPPOOL.MATCHES} | .+ |
| {$IIS.APPPOOL.MONITORED} | 1 |
| {$IIS.APPPOOL.NOT_MATCHES} | <CHANGE_IF_NEEDED> |
| {$IIS.PORT} | 80 |
| {$IIS.QUEUE.MAX.TIME} | 5m |
| {$IIS.QUEUE.MAX.WARN} | no value |
| {$IIS.SERVICE} | http |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Port {$IIS.PORT} is down | AVERAGE | no description | last(/IIS by Zabbix agent/net.tcp.service[{$IIS.SERVICE},,{$IIS.PORT}])=0 | [{"tag": "scope", "value": "availability"}] | no url |
| has been restarted | INFO | Uptime is less than 10 minutes. | last(/IIS by Zabbix agent/perf_counter_en["\Web Service(_Total)\Service Uptime"])<10m | [{"tag": "scope", "value": "notice"}] | no url |
| The World Wide Web Publishing Service (W3SVC) is not running | HIGH | The World Wide Web Publishing Service (W3SVC) is not in the running state. IIS cannot start. | last(/IIS by Zabbix agent/service.info[W3SVC])<>0 | [{"tag": "scope", "value": "availability"}] | no url |
| Windows process Activation Service (WAS) is not running | HIGH | Windows Process Activation Service (WAS) is not in the running state. IIS cannot start. | last(/IIS by Zabbix agent/service.info[WAS])<>0 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discoveries" />

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Application pools discovery | wmi.getall[root\webAdministration, select Name from ApplicationPool] | no description | no type | no lifetime | 1h |


<a name="discovery_application_pools_discovery" />

## Discovery Application pools discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| AppPool {#APPPOOL} state | The state of the application pool. | perf_counter_en["\APP_POOL_WAS({#APPPOOL})\Current Application Pool State"] | no type |
| {#APPPOOL} Uptime | The web application uptime period since the last restart. | perf_counter_en["\APP_POOL_WAS({#APPPOOL})\Current Application Pool Uptime"] | no type |
| AppPool {#APPPOOL} recycles | The number of times the application pool has been recycled since Windows Process Activation Service (WAS) started. | perf_counter_en["\APP_POOL_WAS({#APPPOOL})\Total Application Pool Recycles"] | no type |
| AppPool {#APPPOOL} current queue size | The number of requests in the queue. | perf_counter_en["\HTTP Service Request Queues({#APPPOOL})\CurrentQueueSize"] | no type |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Application pool {#APPPOOL} is not in Running state | HIGH | no description | last(/IIS by Zabbix agent/perf_counter_en["\APP_POOL_WAS({#APPPOOL})\Current Application Pool State"])<>3 and {$IIS.APPPOOL.MONITORED:"{#APPPOOL}"}=1 | [{"tag": "scope", "value": "availability"}] | no url |
| {#APPPOOL} has been restarted | INFO | Uptime is less than 10 minutes. | last(/IIS by Zabbix agent/perf_counter_en["\APP_POOL_WAS({#APPPOOL})\Current Application Pool Uptime"])<10m | [{"tag": "scope", "value": "notice"}] | no url |
| Application pool {#APPPOOL} has been recycled | INFO | no description | last(/IIS by Zabbix agent/perf_counter_en["\APP_POOL_WAS({#APPPOOL})\Total Application Pool Recycles"],#1)<>last(/IIS by Zabbix agent/perf_counter_en["\APP_POOL_WAS({#APPPOOL})\Total Application Pool Recycles"],#2) and {$IIS.APPPOOL.MONITORED:"{#APPPOOL}"}=1 | [{"tag": "scope", "value": "notice"}] | no url |
| Request queue of {#APPPOOL} is too large | WARNING | no description | min(/IIS by Zabbix agent/perf_counter_en["\HTTP Service Request Queues({#APPPOOL})\CurrentQueueSize"],{$IIS.QUEUE.MAX.TIME})>{$IIS.QUEUE.MAX.WARN} | [{"tag": "scope", "value": "performance"}] | no url |

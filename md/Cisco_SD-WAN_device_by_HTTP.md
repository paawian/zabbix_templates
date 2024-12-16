# Cisco SD-WAN device by HTTP template description

Get Cisco SD-WAN devices monitoring with script item usage to perform HTTP requests to Cisco SD-WAN API.
This template will be automatically connected to discovered entities with all required parameters pre-defined.

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Mounted filesystem discovery ](#discovery_mounted_filesystem_discovery)
  * [Discovery Network interfaces discovery ](#discovery_network_interfaces_discovery)
  * [Discovery Route discovery ](#discovery_route_discovery)

<a name="items"></a>

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Operating system architecture | The architecture of the operating system. | sd_wan.device.arch | DEPENDENT | 0 |
| Certificate validity | Validity status of the device certificate. | sd_wan.device.certificate_validity | DEPENDENT | 0 |
| Control connections | The number of control connections. | sd_wan.device.control_conn | DEPENDENT | 0 |
| Load average (1m avg) | The average number of processes being or waiting executed over past 1 minute. | sd_wan.device.cpu.load[avg1] | DEPENDENT | 0 |
| Load average (5m avg) | The average number of processes being or waiting executed over past 5 minutes. | sd_wan.device.cpu.load[avg5] | DEPENDENT | 0 |
| Load average (15m avg) | The average number of processes being or waiting executed over past 15 minutes. | sd_wan.device.cpu.load[avg15] | DEPENDENT | 0 |
| Number of CPUs | The total number of CPU. | sd_wan.device.cpu.num | DEPENDENT | 0 |
| CPU utilization | CPU utilization, expressed in %. | sd_wan.device.cpu.util | DEPENDENT | 0 |
| CPU idle time | The time the CPU has spent doing nothing. | sd_wan.device.cpu.util[idle] | DEPENDENT | 0 |
| CPU system time | The time the CPU has spent running the kernel and its processes. | sd_wan.device.cpu.util[system] | DEPENDENT | 0 |
| CPU user time | The time the CPU has spent running users' processes that are not niced. | sd_wan.device.cpu.util[user] | DEPENDENT | 0 |
| System name | The system host name. | sd_wan.device.hostname | DEPENDENT | 0 |
| Available memory | The amount of physical memory (in bytes) immediately available for the allocation to a process or for a system use in the device. | sd_wan.device.memory.avail | DEPENDENT | 0 |
| Memory (buffers) | The amount of physical memory (in bytes) used by the kernel buffers. | sd_wan.device.memory.buffers | DEPENDENT | 0 |
| Memory (cached) | The amount of physical memory (in bytes) used by the page cache and slabs. | sd_wan.device.memory.cached | DEPENDENT | 0 |
| Total memory | Total memory, expressed in bytes. | sd_wan.device.memory.total | DEPENDENT | 0 |
| Used memory | The amount of physical memory (in bytes) used by applications on the device. | sd_wan.device.memory.used | DEPENDENT | 0 |
| Memory utilization | Calculated percentage of the memory used, in %. | sd_wan.device.memory.util | CALCULATED | no delay |
| Model name | The model name of the device. | sd_wan.device.model | DEPENDENT | 0 |
| Operating system | The device operating system. | sd_wan.device.os | DEPENDENT | 0 |
| Number of processes | The total number of processes in any state. | sd_wan.device.proc.num | DEPENDENT | 0 |
| Device reachability | Reachability to the vManager and/or the entire network. | sd_wan.device.reachability | DEPENDENT | 0 |
| Device role | The device role in the network. | sd_wan.device.role | DEPENDENT | 0 |
| Serial Number | The device serial number. | sd_wan.device.serialnumber | DEPENDENT | 0 |
| Device state | The device current state. | sd_wan.device.state | DEPENDENT | 0 |
| Device state description | The description of the device current state. | sd_wan.device.state_descr | DEPENDENT | 0 |
| System uptime | The system uptime is calculated on the basis of boot time. | sd_wan.device.uptime | DEPENDENT | 0 |
| Version | The version of the device software. | sd_wan.device.version | DEPENDENT | 0 |
| Get device data | Item for gathering device data from Cisco SD-WAN API. | sd_wan.get.device | SCRIPT | no delay |
| Device data item errors | Item for gathering errors of the device item. | sd_wan.get.device.errors | DEPENDENT | 0 |
| Get interfaces data | Item for gathering device interfaces from Cisco SD-WAN API. | sd_wan.get.interfaces | SCRIPT | no delay |
| Device interfaces item errors | Item for gathering errors of the device interfaces. | sd_wan.get.interfaces.errors | DEPENDENT | 0 |
| Get routes data | Item for gathering device routes from Cisco SD-WAN API. | sd_wan.get.routes | SCRIPT | {$SDWAN.ROUTES.FREQUENCY} |
| Device routes item errors | Item for gathering errors of the device routes. | sd_wan.get.routes.errors | DEPENDENT | 0 |


<a name="macros"></a>

## Macros
| macro | value |
| ------------- |------------- |
| {$IFCONTROL} | 1 |
| {$SDWAN.API.URL} | no value |
| {$SDWAN.CPU.UTIL.CRIT} | 90 |
| {$SDWAN.DATA.TIMEOUT} | 15s |
| {$SDWAN.FS.PUSED.MAX.CRIT} | 90 |
| {$SDWAN.FS.PUSED.MAX.WARN} | 80 |
| {$SDWAN.HTTP_PROXY} | no value |
| {$SDWAN.IF.ERRORS.WARN} | 2 |
| {$SDWAN.IF.UTIL.MAX} | 90 |
| {$SDWAN.LA.PER.CPU.MAX.WARN} | 1.5 |
| {$SDWAN.LLD.FILTER.FSNAME.MATCHES} | .* |
| {$SDWAN.LLD.FILTER.FSNAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$SDWAN.LLD.FILTER.IFNAME.MATCHES} | .* |
| {$SDWAN.LLD.FILTER.IFNAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$SDWAN.MEMORY.AVAILABLE.MIN} | 100K |
| {$SDWAN.MEMORY.UTIL.MAX} | 90 |
| {$SDWAN.ROUTES.FREQUENCY} | 1h |
| {$SDWAN.TOKEN} | no value |


<a name="triggers"></a>

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Device certificate is invalid | WARNING | no description | last(/Cisco SD-WAN device by HTTP/sd_wan.device.certificate_validity)=1 | [{"tag": "scope", "value": "security"}] | no url |
| High CPU utilization | WARNING | CPU utilization is too high. The system might be slow to respond. | min(/Cisco SD-WAN device by HTTP/sd_wan.device.cpu.util,5m)>{$SDWAN.CPU.UTIL.CRIT} | [{"tag": "scope", "value": "performance"}] | no url |
| System name has changed | INFO | System name has changed. Ack to close. | last(/Cisco SD-WAN device by HTTP/sd_wan.device.hostname,#1)<>last(/Cisco SD-WAN device by HTTP/sd_wan.device.hostname,#2) and length(last(/Cisco SD-WAN device by HTTP/sd_wan.device.hostname))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| High memory utilization | AVERAGE | The system is running out of free memory. | min(/Cisco SD-WAN device by HTTP/sd_wan.device.memory.util,5m)>{$SDWAN.MEMORY.UTIL.MAX} | [{"tag": "scope", "value": "capacity"}, {"tag": "scope", "value": "performance"}] | no url |
| Operating system description has changed | INFO | Operating system description has changed. Possible reasons that system has been updated or replaced. Ack to close. | last(/Cisco SD-WAN device by HTTP/sd_wan.device.os,#1)<>last(/Cisco SD-WAN device by HTTP/sd_wan.device.os,#2) and length(last(/Cisco SD-WAN device by HTTP/sd_wan.device.os))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Device is not reachable | WARNING | Device is not reachable to the vManager and/or the entire network. | last(/Cisco SD-WAN device by HTTP/sd_wan.device.reachability)<>0 | [{"tag": "scope", "value": "availability"}] | no url |
| Device has been replaced | INFO | Device serial number has changed. Acknowledge to close the problem manually. | last(/Cisco SD-WAN device by HTTP/sd_wan.device.serialnumber,#1)<>last(/Cisco SD-WAN device by HTTP/sd_wan.device.serialnumber,#2) and length(last(/Cisco SD-WAN device by HTTP/sd_wan.device.serialnumber))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Device has been restarted | INFO | The host uptime is less than 10 minutes | last(/Cisco SD-WAN device by HTTP/sd_wan.device.uptime)<10m | [{"tag": "scope", "value": "notice"}] | no url |
| There are errors in the 'Get device data' metric | WARNING | no description | length(last(/Cisco SD-WAN device by HTTP/sd_wan.get.device.errors))>0 | [{"tag": "scope", "value": "availability"}] | no url |
| There are errors in the 'Get interfaces data' metric | WARNING | no description | length(last(/Cisco SD-WAN device by HTTP/sd_wan.get.interfaces.errors))>0 | [{"tag": "scope", "value": "availability"}] | no url |
| There are errors in the 'Get routes data' metric | WARNING | no description | length(last(/Cisco SD-WAN device by HTTP/sd_wan.get.routes.errors))>0 | [{"tag": "scope", "value": "availability"}] | no url |
| Device state is not green | AVERAGE | The device current state is not green. | last(/Cisco SD-WAN device by HTTP/sd_wan.device.state)<>0 and length(last(/Cisco SD-WAN device by HTTP/sd_wan.device.state_descr))>0 | [{"tag": "scope", "value": "availability"}] | no url |
| Lack of available memory | AVERAGE | no description | max(/Cisco SD-WAN device by HTTP/sd_wan.device.memory.avail,5m)<{$SDWAN.MEMORY.AVAILABLE.MIN} and last(/Cisco SD-WAN device by HTTP/sd_wan.device.memory.total)>0 | [{"tag": "scope", "value": "capacity"}, {"tag": "scope", "value": "performance"}] | no url |
| Load average is too high | AVERAGE | The load average per CPU is too high. The system might be slow to respond. | min(/Cisco SD-WAN device by HTTP/sd_wan.device.cpu.load[avg1],5m)/last(/Cisco SD-WAN device by HTTP/sd_wan.device.cpu.num)>{$SDWAN.LA.PER.CPU.MAX.WARN}<br>and last(/Cisco SD-WAN device by HTTP/sd_wan.device.cpu.load[avg5])>0<br>and last(/Cisco SD-WAN device by HTTP/sd_wan.device.cpu.load[avg15])>0 | [{"tag": "scope", "value": "performance"}] | no url |


<a name="discoveries"></a>

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Mounted filesystem discovery | sd_wan.fs.discovery | Discovering device filesystems from Cisco SD-WAN API. | DEPENDENT | no lifetime | 0 |
| Network interfaces discovery | sd_wan.interfaces.discovery | Discovering device interfaces from Cisco SD-WAN API. | DEPENDENT | no lifetime | 0 |
| Route discovery | sd_wan.routes.discovery | Discovering Application-Aware routes from Cisco SD-WAN API. | DEPENDENT | no lifetime | 0 |


<a name="discovery_mounted_filesystem_discovery" />

## Discovery Mounted filesystem discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| ["{#FSNAME}"]: Available space | The available size of the storage pool, in bytes. | sd_wan.device.fs.avail["{#FSNAME}"] | DEPENDENT |
| ["{#FSNAME}"]: Get data | Item for gathering data for the {#FSNAME} filesystem. | sd_wan.device.fs.get_data["{#FSNAME}"] | DEPENDENT |
| ["{#FSNAME}"]: Space utilization | Space utilization, expressed in %. | sd_wan.device.fs.pused["{#FSNAME}"] | DEPENDENT |
| ["{#FSNAME}"]: Total space | The size of the storage pool, in bytes. | sd_wan.device.fs.total["{#FSNAME}"] | DEPENDENT |
| ["{#FSNAME}"]: Used space | The used size of the dataset, in bytes. | sd_wan.device.fs.used["{#FSNAME}"] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| ["{#FSNAME}"]: Disk space is critically low | AVERAGE | Utilization of the space is above {$VFS.FS.PUSED.MAX.CRIT:"{{FSNAME}}"} | last(/Cisco SD-WAN device by HTTP/sd_wan.device.fs.pused["{#FSNAME}"])>{$SDWAN.FS.PUSED.MAX.CRIT:"{#FSNAME}"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "capacity"}] | no url |
| ["{#FSNAME}"]: Disk space is low | WARNING | Utilization of the space is above {$VFS.FS.PUSED.MAX.CRIT:"{{FSNAME}}"} | last(/Cisco SD-WAN device by HTTP/sd_wan.device.fs.pused["{#FSNAME}"])>{$SDWAN.FS.PUSED.MAX.WARN:"{#FSNAME}"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "capacity"}] | no url |


<a name="discovery_network_interfaces_discovery" />

## Discovery Network interfaces discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Interface ["{#IFNAME}"]: Admin status | Current admin status of the interface. | sd_wan.device.if.adm.status["{#IFKEY}"] | DEPENDENT |
| Interface ["{#IFNAME}"]: Get data | Item for gathering data for the {#IFNAME} interface. | sd_wan.device.if.get_data["{#IFKEY}"] | DEPENDENT |
| Interface ["{#IFNAME}"]: Inbound packets discarded | The number of inbound packets that were chosen to be discarded. | sd_wan.device.if.in.discards["{#IFKEY}"] | DEPENDENT |
| Interface ["{#IFNAME}"]: Inbound packets with errors | The number of inbound packets that were contain errors. | sd_wan.device.if.in.errors["{#IFKEY}"] | DEPENDENT |
| Interface ["{#IFNAME}"]: Inbound IPv6 packets discarded | The number of inbound IPv6 packets that were chosen to be discarded. | sd_wan.device.if.in.v6.discards["{#IFKEY}"] | DEPENDENT |
| Interface ["{#IFNAME}"]: Inbound IPv6 packets with errors | The number of inbound IPv4 packets that were contain errors. | sd_wan.device.if.in.v6.errors["{#IFKEY}"] | DEPENDENT |
| Interface ["{#IFNAME}"]: Bits received | The total number of octets received on the interface. | sd_wan.device.if.in["{#IFKEY}"] | DEPENDENT |
| Interface ["{#IFNAME}"]: Outbound packets discarded | The number of outbound packets that were chosen to be discarded. | sd_wan.device.if.out.discards["{#IFKEY}"] | DEPENDENT |
| Interface ["{#IFNAME}"]: Outbound packets with errors | The number of outbound packets that were contain errors. | sd_wan.device.if.out.errors["{#IFKEY}"] | DEPENDENT |
| Interface ["{#IFNAME}"]: Outbound IPv6 packets discarded | The number of outbound IPv6 packets that were chosen to be discarded. | sd_wan.device.if.out.v6.discards["{#IFKEY}"] | DEPENDENT |
| Interface ["{#IFNAME}"]: Outbound IPv6 packets with errors | The number of outbound IPv6 packets that were contain errors. | sd_wan.device.if.out.v6.errors["{#IFKEY}"] | DEPENDENT |
| Interface ["{#IFNAME}"]: Bits sent | The total number of octets transmitted out of the interface. | sd_wan.device.if.out["{#IFKEY}"] | DEPENDENT |
| Interface ["{#IFNAME}"]: Speed | Current bandwidth of the interface. | sd_wan.device.if.speed["{#IFKEY}"] | DEPENDENT |
| Interface ["{#IFNAME}"]: Operational status | Current operational status of the interface. | sd_wan.device.if.status["{#IFKEY}"] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Interface ["{#IFNAME}"]: Link down | AVERAGE | This trigger expression works as follows:<br>1. It can be triggered if the operational status is down.<br>2. `{$IFCONTROL:"{#IFNAME}"}=1` - a user can redefine context macro to value - 0. That marks this interface as not important. No new trigger will be fired if this interface is down.<br>3. `{TEMPLATE_NAME:METRIC.diff()}=1` - the trigger fires only if the operational status was up to (1) sometime before (so, it does not fire for the 'eternal off' interfaces).<br><br>WARNING: If closed manually, it will not fire again on the next poll because of .diff. | {$IFCONTROL:"{#IFNAME}"}=1 and last(/Cisco SD-WAN device by HTTP/sd_wan.device.if.status["{#IFKEY}"])=1 and (last(/Cisco SD-WAN device by HTTP/sd_wan.device.if.status["{#IFKEY}"],#1)<>last(/Cisco SD-WAN device by HTTP/sd_wan.device.if.status["{#IFKEY}"],#2)) | [{"tag": "scope", "value": "availability"}] | no url |
| Interface ["{#IFNAME}"]: Ethernet has changed to lower speed than it was before | INFO | This Ethernet connection has transitioned down from its known maximum speed. This might be a sign of autonegotiation issues. Acknowledge to close the problem manually. | change(/Cisco SD-WAN device by HTTP/sd_wan.device.if.speed["{#IFKEY}"])<0 and last(/Cisco SD-WAN device by HTTP/sd_wan.device.if.speed["{#IFKEY}"])>0<br>and<br>last(/Cisco SD-WAN device by HTTP/sd_wan.device.if.status["{#IFKEY}"])<>0 | [{"tag": "scope", "value": "capacity"}] | no url |
| Interface ["{#IFNAME}"]: High bandwidth usage | WARNING | The network interface utilization is close to its estimated maximum bandwidth. | (avg(/Cisco SD-WAN device by HTTP/sd_wan.device.if.in["{#IFKEY}"],15m)>({$SDWAN.IF.UTIL.MAX:"{#IFNAME}"}/100)*last(/Cisco SD-WAN device by HTTP/sd_wan.device.if.speed["{#IFKEY}"]) or<br>avg(/Cisco SD-WAN device by HTTP/sd_wan.device.if.out["{#IFKEY}"],15m)>({$SDWAN.IF.UTIL.MAX:"{#IFNAME}"}/100)*last(/Cisco SD-WAN device by HTTP/sd_wan.device.if.speed["{#IFKEY}"])) and<br>last(/Cisco SD-WAN device by HTTP/sd_wan.device.if.speed["{#IFKEY}"])>0 | [{"tag": "scope", "value": "performance"}] | no url |
| Interface ["{#IFNAME}"]: High error rate | WARNING | It recovers when it is below 80% of the `{$SDWAN.IF.ERRORS.WARN:"{#IFNAME}"}` threshold. | min(/Cisco SD-WAN device by HTTP/sd_wan.device.if.in.errors["{#IFKEY}"],5m)>{$SDWAN.IF.ERRORS.WARN:"{#IFNAME}"} <br>or min(/Cisco SD-WAN device by HTTP/sd_wan.device.if.out.errors["{#IFKEY}"],5m)>{$SDWAN.IF.ERRORS.WARN:"{#IFNAME}"} <br>or min(/Cisco SD-WAN device by HTTP/sd_wan.device.if.in.v6.errors["{#IFKEY}"],5m)>{$SDWAN.IF.ERRORS.WARN:"{#IFNAME}"} <br>or min(/Cisco SD-WAN device by HTTP/sd_wan.device.if.out.v6.errors["{#IFKEY}"],5m)>{$SDWAN.IF.ERRORS.WARN:"{#IFNAME}"} | [{"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_route_discovery" />

## Discovery Route discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Route [{#LOCAL} => {#REMOTE}]: Get data | Item for gathering data for the route {#LOCAL} => {#REMOTE}. | sd_wan.routes.get_data[{#LOCAL},{#REMOTE}] | DEPENDENT |
| Route [{#LOCAL} => {#REMOTE}]: Jitter | A change in the time it takes for a data packet to travel through the route. | sd_wan.routes.jitter[{#LOCAL},{#REMOTE}] | DEPENDENT |
| Route [{#LOCAL} => {#REMOTE}]: Latency | The amount of time it takes for a data packet to travel through the route. | sd_wan.routes.latency[{#LOCAL},{#REMOTE}] | DEPENDENT |
| Route [{#LOCAL} => {#REMOTE}]: Loss | Lost packets of data not reached the destination after being transmitted through the route. | sd_wan.routes.loss[{#LOCAL},{#REMOTE}] | DEPENDENT |

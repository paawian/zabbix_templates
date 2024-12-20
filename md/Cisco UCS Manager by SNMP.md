# Cisco UCS Manager by SNMP template description

This is a template for Cisco UCS Manager monitoring via Zabbix SNMP Agent that works without any external scripts.


MIBs used:
CISCO-UNIFIED-COMPUTING-COMPUTE-MIB
CISCO-UNIFIED-COMPUTING-EQUIPMENT-MIB
IF-MIB
HOST-RESOURCES-MIB
SNMPv2-MIB
CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB
CISCO-UNIFIED-COMPUTING-STORAGE-MIB

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/418396-discussion-thread-for-official-zabbix-templates-for-cisco

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Array controller cache discovery ](#discovery_array_controller_cache_discovery)
  * [Discovery Array controller discovery ](#discovery_array_controller_discovery)
  * [Discovery FAN discovery ](#discovery_fan_discovery)
  * [Discovery Network interface discovery ](#discovery_network_interface_discovery)
  * [Discovery Physical disk discovery ](#discovery_physical_disk_discovery)
  * [Discovery PSU discovery ](#discovery_psu_discovery)
  * [Discovery Temperature CPU discovery ](#discovery_temperature_cpu_discovery)
  * [Discovery Temperature discovery ](#discovery_temperature_discovery)
  * [Discovery Unit discovery ](#discovery_unit_discovery)
  * [Discovery Virtual disk discovery ](#discovery_virtual_disk_discovery)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| System contact details | MIB: SNMPv2-MIB<br>The textual identification of the contact person for this managed<br>node, together with information on how to contact this person.  If no contact<br>information is known, the value is the zero-length string. | cisco.ucs.contact[sysContact.0] | SNMP_AGENT | 15m |
| System description | MIB: SNMPv2-MIB<br>A textual description of the entity. This value should<br>include the full name and version identification of the system's hardware type, software operating-system, and<br>networking software. | cisco.ucs.descr[sysDescr.0] | SNMP_AGENT | 15m |
| Uptime (hardware) | MIB: HOST-RESOURCES-MIB<br>The amount of time since this host was last initialized.<br>Note that this is different from sysUpTime in the SNMPv2-MIB<br>[RFC1907] because sysUpTime is the uptime of the<br>network management portion of the system. | cisco.ucs.hw.uptime[hrSystemUptime.0] | SNMP_AGENT | 30s |
| System location | MIB: SNMPv2-MIB<br>The physical location of this node (e.g., `telephone closet,<br>3rd floor').  If the location is unknown, the value is the zero-length string. | cisco.ucs.location[sysLocation.0] | SNMP_AGENT | 15m |
| System name | MIB: SNMPv2-MIB<br>An administratively-assigned name for this managed node.By<br>convention, this is the node's fully-qualified domain name.  If the name is unknown,<br>the value is the zero-length string. | cisco.ucs.name[sysName.0] | SNMP_AGENT | 15m |
| Uptime (network) | MIB: SNMPv2-MIB<br>The time in seconds since the network management<br>portion of the system was last re-initialized. | cisco.ucs.net.uptime[sysUpTime.0] | SNMP_AGENT | 30s |
| System object ID | MIB: SNMPv2-MIB<br>The vendor's authoritative identification of the network management<br>subsystem contained in the entity.  This value is allocated within the SMI enterprises<br>subtree (1.3.6.1.4.1) and provides an easy and unambiguous means for determining 'what<br>kind of box' is being managed. For example, if vendor 'Flintstones, Inc.' was<br>assigned the subtree1.3.6.1.4.1.4242, it could assign the identifier 1.3.6.1.4.1.4242.1.1<br>to its 'Fred Router'. | cisco.ucs.objectid[sysObjectID.0] | SNMP_AGENT | 15m |
| SNMP traps (fallback) | The item is used to collect all SNMP traps unmatched by other snmptrap items | snmptrap.fallback | SNMP_TRAP | 0 |
| SNMP agent availability | Availability of SNMP checks on the host. The value of this item corresponds to availability icons in the host list.<br>Possible values:<br>0 - not available<br>1 - available<br>2 - unknown | zabbix[host,snmp,available] | INTERNAL | no delay |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$DISK.ARRAY.CACHE.BATTERY.STATUS.CRIT} | 2 |
| {$DISK.ARRAY.CACHE.BATTERY.STATUS.OK} | 1 |
| {$DISK.ARRAY.STATUS.CRIT:"inoperable"} | 2 |
| {$DISK.ARRAY.STATUS.OK:"operable"} | 1 |
| {$DISK.ARRAY.STATUS.WARN:"degraded"} | 3 |
| {$DISK.STATUS.CRIT:"bad"} | 16 |
| {$DISK.STATUS.CRIT:"predictiveFailure"} | 11 |
| {$DISK.STATUS.FAIL:"failed"} | 9 |
| {$FAN.STATUS.CRIT:"inoperable"} | 2 |
| {$FAN.STATUS.WARN:"degraded"} | 3 |
| {$HEALTH.STATUS.CRIT:"computeFailed"} | 30 |
| {$HEALTH.STATUS.CRIT:"configFailure"} | 33 |
| {$HEALTH.STATUS.CRIT:"inoperable"} | 60 |
| {$HEALTH.STATUS.CRIT:"unconfigFailure"} | 34 |
| {$HEALTH.STATUS.WARN:"diagnosticsFailed"} | 204 |
| {$HEALTH.STATUS.WARN:"powerProblem"} | 62 |
| {$HEALTH.STATUS.WARN:"testFailed"} | 35 |
| {$HEALTH.STATUS.WARN:"thermalProblem"} | 60 |
| {$HEALTH.STATUS.WARN:"voltageProblem"} | 62 |
| {$IF.ERRORS.WARN} | 2 |
| {$IFCONTROL} | 1 |
| {$NET.IFADMINSTATUS.MATCHES} | ^.* |
| {$NET.IFADMINSTATUS.NOT_MATCHES} | ^2$ |
| {$NET.IFALIAS.MATCHES} | .* |
| {$NET.IFALIAS.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$NET.IFDESCR.MATCHES} | .* |
| {$NET.IFDESCR.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$NET.IFNAME.MATCHES} | ^.*$ |
| {$NET.IFNAME.NOT_MATCHES} | (^Software Loopback Interface\|^NULL[0-9.]*$\|^[Ll]o[0-9.]*$\|^[Ss]ystem$\|^Nu[0-9.]*$\|^veth[0-9a-z]+$\|docker[0-9]+\|br-[a-z0-9]{12}\|sup-fc0) |
| {$NET.IFOPERSTATUS.MATCHES} | ^.*$ |
| {$NET.IFOPERSTATUS.NOT_MATCHES} | ^6$ |
| {$NET.IFTYPE.MATCHES} | .* |
| {$NET.IFTYPE.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$PSU.STATUS.CRIT:"inoperable"} | 2 |
| {$PSU.STATUS.WARN:"degraded"} | 3 |
| {$SNMP.TIMEOUT} | 5m |
| {$TEMP.MAX.CRIT:"Ambient"} | 35 |
| {$TEMP.MAX.WARN:"Ambient"} | 30 |
| {$VDISK.STATUS.OK:"equipped"} | 10 |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| System name has changed | INFO | The name of the system has changed. Acknowledge to close the problem manually. | last(/Cisco UCS Manager by SNMP/cisco.ucs.name[sysName.0],#1)<>last(/Cisco UCS Manager by SNMP/cisco.ucs.name[sysName.0],#2) and length(last(/Cisco UCS Manager by SNMP/cisco.ucs.name[sysName.0]))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| No SNMP data collection | WARNING | SNMP is not available for polling. Please check device connectivity and SNMP settings. | max(/Cisco UCS Manager by SNMP/zabbix[host,snmp,available],{$SNMP.TIMEOUT})=0 | [{"tag": "scope", "value": "availability"}] | no url |
| Host has been restarted | WARNING | Uptime is less than 10 minutes. | (last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.uptime[hrSystemUptime.0])>0 and last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.uptime[hrSystemUptime.0])<10m) or (last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.uptime[hrSystemUptime.0])=0 and last(/Cisco UCS Manager by SNMP/cisco.ucs.net.uptime[sysUpTime.0])<10m) | [{"tag": "scope", "value": "notice"}] | no url |


<a name="discoveries" />

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Array controller cache discovery | cisco.ucs.array.cache.discovery | Scanning table of Array controllers: CISCO-UNIFIED-COMPUTING-STORAGE-MIB::cucsStorageControllerTable. | SNMP_AGENT | no lifetime | 1h |
| Array controller discovery | cisco.ucs.array.discovery | Scanning table of Array controllers: CISCO-UNIFIED-COMPUTING-STORAGE-MIB::cucsStorageControllerTable. | SNMP_AGENT | no lifetime | 1h |
| FAN discovery | cisco.ucs.fan.discovery | no description | SNMP_AGENT | no lifetime | 1h |
| Network interface discovery | cisco.ucs.net.if.discovery | Discovering interfaces from IF-MIB. | SNMP_AGENT | no lifetime | 1h |
| Physical disk discovery | cisco.ucs.physicalDisk.discovery | Scanning table of physical drive entries CISCO-UNIFIED-COMPUTING-STORAGE-MIB::cucsStorageLocalDiskTable. | SNMP_AGENT | no lifetime | 1h |
| PSU discovery | cisco.ucs.psu.discovery | no description | SNMP_AGENT | no lifetime | 1h |
| Temperature CPU discovery | cisco.ucs.temp.cpu.discovery | no description | SNMP_AGENT | no lifetime | 1h |
| Temperature discovery | cisco.ucs.temp.discovery | no description | SNMP_AGENT | no lifetime | 1h |
| Unit discovery | cisco.ucs.unit.discovery | no description | SNMP_AGENT | no lifetime | 1h |
| Virtual disk discovery | cisco.ucs.virtualDisk.discovery | CISCO-UNIFIED-COMPUTING-STORAGE-MIB::cucsStorageLocalLunTable | SNMP_AGENT | no lifetime | 1h |


<a name="discovery_array_controller_cache_discovery" />

## Discovery Array controller cache discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#DISKARRAY_CACHE_LOCATION}: Disk array cache controller battery status | MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB | cisco.ucs.hw.diskarray.cache.battery.status[cucsStorageRaidBatteryOperability.{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#DISKARRAY_CACHE_LOCATION}: Disk array cache controller battery is in critical state! | AVERAGE | Please check the device for faults | last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.diskarray.cache.battery.status[cucsStorageRaidBatteryOperability.{#SNMPINDEX}])={$DISK.ARRAY.CACHE.BATTERY.STATUS.CRIT} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#DISKARRAY_CACHE_LOCATION}: Disk array cache controller battery is not in optimal state | WARNING | Please check the device for faults | last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.diskarray.cache.battery.status[cucsStorageRaidBatteryOperability.{#SNMPINDEX}])<>{$DISK.ARRAY.CACHE.BATTERY.STATUS.OK} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_array_controller_discovery" />

## Discovery Array controller discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#DISKARRAY_LOCATION}: Disk array controller model | MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB | cisco.ucs.hw.diskarray.model[cucsStorageControllerModel.{#SNMPINDEX}] | SNMP_AGENT |
| {#DISKARRAY_LOCATION}: Disk array controller status | MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB<br>Cisco UCS storage:RaidBattery:operability managed object property. | cisco.ucs.hw.diskarray.status[cucsStorageControllerOperState.{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#DISKARRAY_LOCATION}: Disk array controller is in critical state | HIGH | Please check the device for faults | last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.diskarray.status[cucsStorageControllerOperState.{#SNMPINDEX}])={$DISK.ARRAY.STATUS.CRIT:"inoperable"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#DISKARRAY_LOCATION}: Disk array controller is in warning state | AVERAGE | Please check the device for faults | last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.diskarray.status[cucsStorageControllerOperState.{#SNMPINDEX}])={$DISK.ARRAY.STATUS.WARN:"degraded"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#DISKARRAY_LOCATION}: Disk array controller is not in optimal state | WARNING | Please check the device for faults | last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.diskarray.status[cucsStorageControllerOperState.{#SNMPINDEX}])>{$DISK.ARRAY.STATUS.OK:"operable"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_fan_discovery" />

## Discovery FAN discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#FAN_LOCATION}: Fan status | MIB: CISCO-UNIFIED-COMPUTING-EQUIPMENT-MIB<br>Cisco UCS equipment:Fan:operState managed object property | cisco.ucs.sensor.fan.status[cucsEquipmentFanOperState.{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#FAN_LOCATION}: Fan is in critical state | AVERAGE | Please check the fan unit | last(/Cisco UCS Manager by SNMP/cisco.ucs.sensor.fan.status[cucsEquipmentFanOperState.{#SNMPINDEX}])={$FAN.STATUS.CRIT:"inoperable"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#FAN_LOCATION}: Fan is in warning state | WARNING | Please check the fan unit | last(/Cisco UCS Manager by SNMP/cisco.ucs.sensor.fan.status[cucsEquipmentFanOperState.{#SNMPINDEX}])={$FAN.STATUS.WARN:"degraded"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_network_interface_discovery" />

## Discovery Network interface discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Interface {#IFNAME}({#IFALIAS}): Interface description | MIB: IF-MIB<br>A textual string containing information about the<br>interface.  This string should include the name of the<br>manufacturer, the product name and the version of the<br>interface hardware/software. | cisco.ucs.if.descr[ifDescr.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Broadcast packets received | MIB: IF-MIB<br>The number of packets, delivered by this sub-layer to a<br>higher (sub-)layer, which were addressed to a broadcast<br>address at this sub-layer.  This object is a 64-bit version<br>of ifInBroadcastPkts.<br><br>Discontinuities in the value of this counter can occur at<br>re-initialization of the management system, and at other<br>times as indicated by the value of ifCounterDiscontinuityTime. | cisco.ucs.if.in.broadcast[ifHCInBroadcastPkts.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Inbound packets discarded | MIB: IF-MIB<br>The number of inbound packets which were chosen to be discarded<br>even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.<br>One possible reason for discarding such a packet could be to free up buffer space.<br>Discontinuities in the value of this counter can occur at re-initialization of the management system,<br>and at other times as indicated by the value of ifCounterDiscontinuityTime. | cisco.ucs.if.in.discards[ifInDiscards.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Inbound packets with errors | MIB: IF-MIB<br>For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character-oriented or fixed-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime. | cisco.ucs.if.in.errors[ifInErrors.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Multicast packets received | MIB: IF-MIB<br>The number of packets, delivered by this sub-layer to a<br>higher (sub-)layer, which were addressed to a multicast<br>address at this sub-layer.  For a MAC layer protocol, this<br>includes both Group and Functional addresses.  This object<br>is a 64-bit version of ifInMulticastPkts.<br><br>Discontinuities in the value of this counter can occur at<br>re-initialization of the management system, and at other<br>times as indicated by the value of ifCounterDiscontinuityTime. | cisco.ucs.if.in.multicast[ifHCInMulticastPkts.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Bits received | MIB: IF-MIB<br>The total number of octets received on the interface, including framing characters. This object is a 64-bit version of ifInOctets. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime. | cisco.ucs.if.in[ifHCInOctets.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Broadcast packets sent | MIB: IF-MIB<br>The total number of packets that higher-level protocols<br>requested be transmitted, and which were addressed to a<br>broadcast address at this sub-layer, including those that<br>were discarded or not sent.  This object is a 64-bit version<br>of ifOutBroadcastPkts.<br><br>Discontinuities in the value of this counter can occur at<br>re-initialization of the management system, and at other<br>times as indicated by the value of ifCounterDiscontinuityTime. | cisco.ucs.if.out.broadcast[ifHCOutBroadcastPkts.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Outbound packets discarded | MIB: IF-MIB<br>The number of outbound packets which were chosen to be discarded<br>even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.<br>One possible reason for discarding such a packet could be to free up buffer space.<br>Discontinuities in the value of this counter can occur at re-initialization of the management system,<br>and at other times as indicated by the value of ifCounterDiscontinuityTime. | cisco.ucs.if.out.discards[ifOutDiscards.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Outbound packets with errors | MIB: IF-MIB<br>For packet-oriented interfaces, the number of outbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character-oriented or fixed-length interfaces, the number of outbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime. | cisco.ucs.if.out.errors[ifOutErrors.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Multicast packets sent | MIB: IF-MIB<br>The total number of packets that higher-level protocols<br>requested be transmitted, and which were addressed to a<br>multicast address at this sub-layer, including those that<br>were discarded or not sent.  For a MAC layer protocol, this<br>includes both Group and Functional addresses.  This object<br>is a 64-bit version of ifOutMulticastPkts.<br><br>Discontinuities in the value of this counter can occur at<br>re-initialization of the management system, and at other<br>times as indicated by the value of ifCounterDiscontinuityTime. | cisco.ucs.if.out.multicast[ifHCOutMulticastPkts.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Bits sent | MIB: IF-MIB<br>The total number of octets transmitted out of the interface, including framing characters. This object is a 64-bit version of ifOutOctets.Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime. | cisco.ucs.if.out[ifHCOutOctets.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Speed | MIB: IF-MIB<br>An estimate of the interface's current bandwidth in units of 1,000,000 bits per second. If this object reports a value of `n' then the speed of the interface is somewhere in the range of `n-500,000' to`n+499,999'.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth. For a sub-layer which has no concept of bandwidth, this object should be zero. | cisco.ucs.if.speed[ifHighSpeed.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Operational status | MIB: IF-MIB<br>The current operational state of the interface.<br>- The testing(3) state indicates that no operational packet scan be passed<br>- If ifAdminStatus is down(2) then ifOperStatus should be down(2)<br>- If ifAdminStatus is changed to up(1) then ifOperStatus should change to up(1) if the interface is ready to transmit and receive network traffic<br>- It should change todormant(5) if the interface is waiting for external actions (such as a serial line waiting for an incoming connection)<br>- It should remain in the down(2) state if and only if there is a fault that prevents it from going to the up(1) state<br>- It should remain in the notPresent(6) state if the interface has missing(typically, hardware) components. | cisco.ucs.if.status[ifOperStatus.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Interface type | MIB: IF-MIB<br>The type of interface.<br>Additional values for ifType are assigned by the Internet Assigned Numbers Authority (IANA),<br>through updating the syntax of the IANAifType textual convention. | cisco.ucs.if.type[ifType.{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Interface {#IFNAME}({#IFALIAS}): Link down | AVERAGE | This trigger expression works as follows:<br>1. It can be triggered if the operations status is down.<br>2. `{$IFCONTROL:"{#IFNAME}"}=1` - a user can redefine context macro to value - 0. That marks this interface as not important. No new trigger will be fired if this interface is down.<br>3. `{TEMPLATE_NAME:METRIC.diff()}=1` - the trigger fires only if the operational status was up to (1) sometime before (so, do not fire for the 'eternal off' interfaces.)<br><br>WARNING: if closed manually - it will not fire again on the next poll, because of .diff. | {$IFCONTROL:"{#IFNAME}"}=1 and last(/Cisco UCS Manager by SNMP/cisco.ucs.if.status[ifOperStatus.{#SNMPINDEX}])=2 and (last(/Cisco UCS Manager by SNMP/cisco.ucs.if.status[ifOperStatus.{#SNMPINDEX}],#1)<>last(/Cisco UCS Manager by SNMP/cisco.ucs.if.status[ifOperStatus.{#SNMPINDEX}],#2)) | [{"tag": "scope", "value": "availability"}] | no url |
| Interface {#IFNAME}({#IFALIAS}): High error rate on {#IFNAME} | WARNING | Recovers when value below {$IF.ERRORS.WARN:"{#IFNAME}"} threshold. | min(/Cisco UCS Manager by SNMP/cisco.ucs.if.in.errors[ifInErrors.{#SNMPINDEX}],5m)>{$IF.ERRORS.WARN:"{#IFNAME}"}<br>or min(/Cisco UCS Manager by SNMP/cisco.ucs.if.out.errors[ifOutErrors.{#SNMPINDEX}],5m)>{$IF.ERRORS.WARN:"{#IFNAME}"} | [{"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_physical_disk_discovery" />

## Discovery Physical disk discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#DISK_LOCATION}: Physical disk media type | MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB<br>Cisco UCS storage:LocalDisk:deviceType managed object property. Actually returns 'HDD' or 'SSD'. | cisco.ucs.hw.physicaldisk.media_type[cucsStorageLocalDiskDeviceType.{#SNMPINDEX}] | SNMP_AGENT |
| {#DISK_LOCATION}: Physical disk model name | MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB<br>Cisco UCS storage:LocalDisk:model managed object property. | cisco.ucs.hw.physicaldisk.model[cucsStorageLocalDiskModel.{#SNMPINDEX}] | SNMP_AGENT |
| {#DISK_LOCATION}: Physical disk serial number | MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB<br>Cisco UCS storage:LocalDisk:serial managed object property. Actually returns part number code. | cisco.ucs.hw.physicaldisk.serialnumber[cucsStorageLocalDiskSerial.{#SNMPINDEX}] | SNMP_AGENT |
| {#DISK_LOCATION}: Disk size | MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB<br>Cisco UCS storage:LocalDisk:size managed object property. In MB. | cisco.ucs.hw.physicaldisk.size[cucsStorageLocalDiskSize.{#SNMPINDEX}] | SNMP_AGENT |
| {#DISK_LOCATION}: Physical disk status | MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB<br>Cisco UCS storage:LocalDisk:diskState managed object property. | cisco.ucs.hw.physicaldisk.status[cucsStorageLocalDiskDiskState.{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#DISK_LOCATION}: Disk has been replaced | INFO | Disk serial number has changed. Acknowledge to close the problem manually. | last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.physicaldisk.serialnumber[cucsStorageLocalDiskSerial.{#SNMPINDEX}],#1)<>last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.physicaldisk.serialnumber[cucsStorageLocalDiskSerial.{#SNMPINDEX}],#2) and length(last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.physicaldisk.serialnumber[cucsStorageLocalDiskSerial.{#SNMPINDEX}]))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| {#DISK_LOCATION}: Physical disk error | AVERAGE | Please check physical disk for warnings or errors | last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.physicaldisk.status[cucsStorageLocalDiskDiskState.{#SNMPINDEX}])={$DISK.STATUS.CRIT:"bad"} or last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.physicaldisk.status[cucsStorageLocalDiskDiskState.{#SNMPINDEX}])={$DISK.STATUS.CRIT:"predictiveFailure"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#DISK_LOCATION}: Physical disk failed | HIGH | Please check physical disk for warnings or errors | last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.physicaldisk.status[cucsStorageLocalDiskDiskState.{#SNMPINDEX}])={$DISK.STATUS.FAIL:"failed"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_psu_discovery" />

## Discovery PSU discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#PSU_LOCATION}: Power supply status | MIB: CISCO-UNIFIED-COMPUTING-EQUIPMENT-MIB<br>Cisco UCS equipment:Psu:operState managed object property | cisco.ucs.sensor.psu.status[cucsEquipmentPsuOperState.{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#PSU_LOCATION}: Power supply is in critical state | AVERAGE | Please check the power supply unit for errors | last(/Cisco UCS Manager by SNMP/cisco.ucs.sensor.psu.status[cucsEquipmentPsuOperState.{#SNMPINDEX}])={$PSU.STATUS.CRIT:"inoperable"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#PSU_LOCATION}: Power supply is in warning state | WARNING | Please check the power supply unit for errors | last(/Cisco UCS Manager by SNMP/cisco.ucs.sensor.psu.status[cucsEquipmentPsuOperState.{#SNMPINDEX}])={$PSU.STATUS.WARN:"degraded"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_temperature_cpu_discovery" />

## Discovery Temperature CPU discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#SENSOR_LOCATION}: Temperature | MIB: CISCO-UNIFIED-COMPUTING-PROCESSOR-MIB<br>Cisco UCS processor:EnvStats:temperature managed object property | cisco.ucs.sensor.temp.value[cucsProcessorEnvStatsTemperature.{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#SENSOR_LOCATION}: Temperature is above critical threshold | HIGH | This trigger uses temperature sensor values as well as temperature sensor status if available | avg(/Cisco UCS Manager by SNMP/cisco.ucs.sensor.temp.value[cucsProcessorEnvStatsTemperature.{#SNMPINDEX}],5m)>{$TEMP.MAX.CRIT:"CPU"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SENSOR_LOCATION}: Temperature is above warning threshold | WARNING | This trigger uses temperature sensor values as well as temperature sensor status if available | avg(/Cisco UCS Manager by SNMP/cisco.ucs.sensor.temp.value[cucsProcessorEnvStatsTemperature.{#SNMPINDEX}],5m)>{$TEMP.MAX.WARN:"CPU"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_temperature_discovery" />

## Discovery Temperature discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#SENSOR_LOCATION}.IOH: Temperature | MIB: CISCO-UNIFIED-COMPUTING-COMPUTE-MIB<br>Cisco UCS compute:RackUnitMbTempStats:ioh1Temp managed object property | cisco.ucs.sensor.temp.value[cucsComputeRackUnitMbTempSltatsIoh1Temp.{#SNMPINDEX}] | SNMP_AGENT |
| {#SENSOR_LOCATION}.Ambient: Temperature | MIB: CISCO-UNIFIED-COMPUTING-COMPUTE-MIB<br>Temperature readings of testpoint: {#SENSOR_LOCATION}.Ambient | cisco.ucs.sensor.temp.value[cucsComputeRackUnitMbTempStatsAmbientTemp.{#SNMPINDEX}] | SNMP_AGENT |
| {#SENSOR_LOCATION}.Front: Temperature | MIB: CISCO-UNIFIED-COMPUTING-COMPUTE-MIB<br>Cisco UCS compute:RackUnitMbTempStats:frontTemp managed object property | cisco.ucs.sensor.temp.value[cucsComputeRackUnitMbTempStatsFrontTemp.{#SNMPINDEX}] | SNMP_AGENT |
| {#SENSOR_LOCATION}.Rear: Temperature | MIB: CISCO-UNIFIED-COMPUTING-COMPUTE-MIB<br>Cisco UCS compute:RackUnitMbTempStats:rearTemp managed object property | cisco.ucs.sensor.temp.value[cucsComputeRackUnitMbTempStatsRearTemp.{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#SENSOR_LOCATION}.IOH: Temperature is above critical threshold | HIGH | This trigger uses temperature sensor values as well as temperature sensor status if available | avg(/Cisco UCS Manager by SNMP/cisco.ucs.sensor.temp.value[cucsComputeRackUnitMbTempSltatsIoh1Temp.{#SNMPINDEX}],5m)>{$TEMP.MAX.CRIT:"Ambient"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SENSOR_LOCATION}.IOH: Temperature is above warning threshold | WARNING | This trigger uses temperature sensor values as well as temperature sensor status if available | avg(/Cisco UCS Manager by SNMP/cisco.ucs.sensor.temp.value[cucsComputeRackUnitMbTempSltatsIoh1Temp.{#SNMPINDEX}],5m)>{$TEMP.MAX.WARN:"Ambient"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SENSOR_LOCATION}.Ambient: Temperature is above critical threshold | HIGH | This trigger uses temperature sensor values as well as temperature sensor status if available | avg(/Cisco UCS Manager by SNMP/cisco.ucs.sensor.temp.value[cucsComputeRackUnitMbTempStatsAmbientTemp.{#SNMPINDEX}],5m)>{$TEMP.MAX.CRIT:"Ambient"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SENSOR_LOCATION}.Ambient: Temperature is above warning threshold | WARNING | This trigger uses temperature sensor values as well as temperature sensor status if available | avg(/Cisco UCS Manager by SNMP/cisco.ucs.sensor.temp.value[cucsComputeRackUnitMbTempStatsAmbientTemp.{#SNMPINDEX}],5m)>{$TEMP.MAX.WARN:"Ambient"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SENSOR_LOCATION}.Front: Temperature is above critical threshold | HIGH | This trigger uses temperature sensor values as well as temperature sensor status if available | avg(/Cisco UCS Manager by SNMP/cisco.ucs.sensor.temp.value[cucsComputeRackUnitMbTempStatsFrontTemp.{#SNMPINDEX}],5m)>{$TEMP.MAX.CRIT:"Ambient"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SENSOR_LOCATION}.Front: Temperature is above warning threshold | WARNING | This trigger uses temperature sensor values as well as temperature sensor status if available | avg(/Cisco UCS Manager by SNMP/cisco.ucs.sensor.temp.value[cucsComputeRackUnitMbTempStatsFrontTemp.{#SNMPINDEX}],5m)>{$TEMP.MAX.WARN:"Ambient"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SENSOR_LOCATION}.Rear: Temperature is above critical threshold | HIGH | This trigger uses temperature sensor values as well as temperature sensor status if available | avg(/Cisco UCS Manager by SNMP/cisco.ucs.sensor.temp.value[cucsComputeRackUnitMbTempStatsRearTemp.{#SNMPINDEX}],5m)>{$TEMP.MAX.CRIT:"Ambient"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SENSOR_LOCATION}.Rear: Temperature is above warning threshold | WARNING | This trigger uses temperature sensor values as well as temperature sensor status if available | avg(/Cisco UCS Manager by SNMP/cisco.ucs.sensor.temp.value[cucsComputeRackUnitMbTempStatsRearTemp.{#SNMPINDEX}],5m)>{$TEMP.MAX.WARN:"Ambient"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_unit_discovery" />

## Discovery Unit discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#UNIT_LOCATION}: Hardware model name | MIB: CISCO-UNIFIED-COMPUTING-COMPUTE-MIB<br>Cisco UCS compute:RackUnit:model managed object property | cisco.ucs.hw.model[cucsComputeRackUnitModel.{#SNMPINDEX}] | SNMP_AGENT |
| {#UNIT_LOCATION}: Hardware serial number | MIB: CISCO-UNIFIED-COMPUTING-COMPUTE-MIB<br>Cisco UCS compute:RackUnit:serial managed object property | cisco.ucs.hw.serialnumber[cucsComputeRackUnitSerial.{#SNMPINDEX}] | SNMP_AGENT |
| {#UNIT_LOCATION}: Overall system health status | MIB: CISCO-UNIFIED-COMPUTING-COMPUTE-MIB<br>Cisco UCS compute:RackUnit:operState managed object property | cisco.ucs.status[cucsComputeRackUnitOperState.{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#UNIT_LOCATION}: Device has been replaced | INFO | Device serial number has changed. Acknowledge to close the problem manually. | last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.serialnumber[cucsComputeRackUnitSerial.{#SNMPINDEX}],#1)<>last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.serialnumber[cucsComputeRackUnitSerial.{#SNMPINDEX}],#2) and length(last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.serialnumber[cucsComputeRackUnitSerial.{#SNMPINDEX}]))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| {#UNIT_LOCATION}: System status is in critical state | HIGH | Please check the device for errors | last(/Cisco UCS Manager by SNMP/cisco.ucs.status[cucsComputeRackUnitOperState.{#SNMPINDEX}])={$HEALTH.STATUS.CRIT:"computeFailed"} or last(/Cisco UCS Manager by SNMP/cisco.ucs.status[cucsComputeRackUnitOperState.{#SNMPINDEX}])={$HEALTH.STATUS.CRIT:"configFailure"} or last(/Cisco UCS Manager by SNMP/cisco.ucs.status[cucsComputeRackUnitOperState.{#SNMPINDEX}])={$HEALTH.STATUS.CRIT:"unconfigFailure"} or last(/Cisco UCS Manager by SNMP/cisco.ucs.status[cucsComputeRackUnitOperState.{#SNMPINDEX}])={$HEALTH.STATUS.CRIT:"inoperable"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#UNIT_LOCATION}: System status is in warning state | WARNING | Please check the device for warnings | last(/Cisco UCS Manager by SNMP/cisco.ucs.status[cucsComputeRackUnitOperState.{#SNMPINDEX}])={$HEALTH.STATUS.WARN:"testFailed"} or last(/Cisco UCS Manager by SNMP/cisco.ucs.status[cucsComputeRackUnitOperState.{#SNMPINDEX}])={$HEALTH.STATUS.WARN:"thermalProblem"} or last(/Cisco UCS Manager by SNMP/cisco.ucs.status[cucsComputeRackUnitOperState.{#SNMPINDEX}])={$HEALTH.STATUS.WARN:"powerProblem"} or last(/Cisco UCS Manager by SNMP/cisco.ucs.status[cucsComputeRackUnitOperState.{#SNMPINDEX}])={$HEALTH.STATUS.WARN:"voltageProblem"} or last(/Cisco UCS Manager by SNMP/cisco.ucs.status[cucsComputeRackUnitOperState.{#SNMPINDEX}])={$HEALTH.STATUS.WARN:"diagnosticsFailed"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_virtual_disk_discovery" />

## Discovery Virtual disk discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#VDISK_LOCATION}: Layout type | MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB<br>Cisco UCS storage:LocalLun:type managed object property | cisco.ucs.hw.virtualdisk.layout[cucsStorageLocalLunType.{#SNMPINDEX}] | SNMP_AGENT |
| {#VDISK_LOCATION}: Disk size | MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB<br>Cisco UCS storage:LocalLun:size managed object property in MB. | cisco.ucs.hw.virtualdisk.size[cucsStorageLocalLunSize.{#SNMPINDEX}] | SNMP_AGENT |
| {#VDISK_LOCATION}: Status | MIB: CISCO-UNIFIED-COMPUTING-STORAGE-MIB<br>Cisco UCS storage:LocalLun:presence managed object property | cisco.ucs.hw.virtualdisk.status[cucsStorageLocalLunPresence.{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#VDISK_LOCATION}: Virtual disk is not in OK state | WARNING | Please check virtual disk for warnings or errors | last(/Cisco UCS Manager by SNMP/cisco.ucs.hw.virtualdisk.status[cucsStorageLocalLunPresence.{#SNMPINDEX}])<>{$VDISK.STATUS.OK:"equipped"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


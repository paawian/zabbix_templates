# Cisco Nexus 9000 Series by SNMP template description

Template Cisco Nexus 9000 Series
  
  MIBs used:
  CISCO-ENHANCED-MEMPOOL-MIB
  CISCO-ENTITY-FRU-CONTROL-MIB
  CISCO-ENTITY-SENSOR-MIB
  CISCO-PROCESS-MIB
  ENTITY-MIB
  EtherLike-MIB
  IF-MIB
  SNMPv2-MIB
  SNMP-FRAMEWORK-MIB
  CISCO-IMAGE-MIB

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/418396-discussion-thread-for-official-zabbix-templates-for-cisco

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery CPU discovery ](#discovery_cpu_discovery)
  * [Discovery Entity serial numbers discovery ](#discovery_entity_serial_numbers_discovery)
  * [Discovery Fan status discovery ](#discovery_fan_status_discovery)
  * [Discovery Memory discovery ](#discovery_memory_discovery)
  * [Discovery Network interfaces discovery ](#discovery_network_interfaces_discovery)
  * [Discovery EtherLike discovery ](#discovery_etherlike_discovery)
  * [Discovery PSU discovery ](#discovery_psu_discovery)
  * [Discovery Temperature sensors discovery ](#discovery_temperature_sensors_discovery)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| ICMP ping | no description | icmpping | SIMPLE | no delay |
| ICMP loss | no description | icmppingloss | SIMPLE | no delay |
| ICMP response time | no description | icmppingsec | SIMPLE | no delay |
| SNMP traps (fallback) | The item is used to collect all the SNMP traps unmatched by the other snmptrap items. | snmptrap.fallback | SNMP_TRAP | 0 |
| System contact details | MIB: SNMPv2-MIB.<br>The textual identification of the contact person for the managed node (or: this node), together with the contact information of this person. If no contact information is known, the value is a zero-length string. | system.contact | SNMP_AGENT | 1h |
| System description | MIB: SNMPv2-MIB.<br>The textual description of the entity. This value should include the full name and version identification number of the system's hardware type, software operating-system, and the networking software. | system.descr | SNMP_AGENT | 1h |
| Hardware model name | MIB: ENTITY-MIB. | system.hw.model | SNMP_AGENT | 1h |
| Hardware serial number | MIB: ENTITY-MIB. | system.hw.serialnumber | SNMP_AGENT | 1h |
| System location | MIB: SNMPv2-MIB.<br>The physical location of this node (e.g., telephone closet, the third floor).<br>If the location is unknown, the value is a zero-length string. | system.location | SNMP_AGENT | 1h |
| System name | MIB: SNMPv2-MIB.<br>The administratively-assigned name for this node. By convention, this is the node's fully-qualified domain name. If the name is unknown, the value is a zero-length string. | system.name | SNMP_AGENT | 1h |
| System object ID | MIB: SNMPv2-MIB.<br>The vendor's authoritative identification of the network management subsystem contained in the entity. This value is allocated within the SMI enterprise's subtree (1.3.6.1.4.1) and provides an easy and unambiguous means for determining "what kind of box" is being managed.<br>For example, if the vendor "Flintstones, Inc." was assigned the subtree 1.3.6.1.4.1.4242, it could assign the identifier 1.3.6.1.4.1.4242.1.1 to its "Fred Router". | system.objectid | SNMP_AGENT | no delay |
| Operating system | MIB: CISCO-IMAGE-MIB | system.sw.os | SNMP_AGENT | 1h |
| Uptime (snmp) | MIB: SNMP-FRAMEWORK-MIB::snmpEngineTime.<br>The number of seconds since the value of the `snmpEngineBoots` object has had a last change.<br>When incrementing this object's value would cause it to exceed its maximum, the `snmpEngineBoots` is incremented as if a re-initialization had occurred,<br>and this object's value consequently reverts to zero. | system.uptime | SNMP_AGENT | no delay |
| SNMP agent availability | no description | zabbix[host,snmp,available] | INTERNAL | no delay |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$CISCO.LLD.FILTER.FAN.NAME.MATCHES} | ^(?:Fan Module-\d+\|PowerSupply-\d+ Fan-\d+)$ |
| {$CISCO.LLD.FILTER.PSU.NAME.MATCHES} | ^(?:PowerSupply-\d+)$ |
| {$CPU.UTIL.CRIT} | 90 |
| {$ENT_CLASS.NOT_MATCHES} | 3 |
| {$ENT_SN.MATCHES} | .+ |
| {$ICMP_LOSS_WARN} | 20 |
| {$ICMP_RESPONSE_TIME_WARN} | 0.15 |
| {$IF.ERRORS.WARN} | 2 |
| {$IF.UTIL.MAX} | 90 |
| {$IFCONTROL} | 1 |
| {$MEMORY.UTIL.MAX} | 90 |
| {$NET.IF.IFADMINSTATUS.MATCHES} | ^.* |
| {$NET.IF.IFADMINSTATUS.NOT_MATCHES} | ^2$ |
| {$NET.IF.IFALIAS.MATCHES} | .* |
| {$NET.IF.IFALIAS.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$NET.IF.IFDESCR.MATCHES} | .* |
| {$NET.IF.IFDESCR.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$NET.IF.IFNAME.MATCHES} | ^.*$ |
| {$NET.IF.IFNAME.NOT_MATCHES} | (^Software Loopback Interface\|^NULL[0-9.]*$\|^[Ll]o[0-9.]*$\|^[Ss]ystem$\|^Nu[0-9.]*$\|^veth[0-9a-z]+$\|docker[0-9]+\|br-[a-z0-9]{12}) |
| {$NET.IF.IFOPERSTATUS.MATCHES} | ^.*$ |
| {$NET.IF.IFOPERSTATUS.NOT_MATCHES} | ^6$ |
| {$NET.IF.IFTYPE.MATCHES} | .* |
| {$NET.IF.IFTYPE.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$PSU.PROBLEM.STATES} | ^(1\|4\|5\|6\|7\|9\|10\|11\|12)$ |
| {$SNMP.TIMEOUT} | 5m |
| {$TEMP_CRIT} | 60 |
| {$TEMP_CRIT:regex:"BACK"} | 70 |
| {$TEMP_CRIT:regex:"CPU"} | 90 |
| {$TEMP_CRIT:regex:"FRONT"} | 80 |
| {$TEMP_CRIT:regex:"SUN1"} | 110 |
| {$TEMP_CRIT:regex:"Transceiver"} | 75 |
| {$TEMP_CRIT_LOW} | 5 |
| {$TEMP_WARN} | 50 |
| {$TEMP_WARN:regex:"BACK"} | 42 |
| {$TEMP_WARN:regex:"CPU"} | 80 |
| {$TEMP_WARN:regex:"FRONT"} | 70 |
| {$TEMP_WARN:regex:"SUN1"} | 90 |
| {$TEMP_WARN:regex:"Transceiver"} | 70 |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Unavailable by ICMP ping | HIGH | The last three attempts returned a timeout. Check the connectivity of a device. | max(/Cisco Nexus 9000 Series by SNMP/icmpping,#3)=0 | [{"tag": "scope", "value": "availability"}] | no url |
| High ICMP ping loss | WARNING | no description | min(/Cisco Nexus 9000 Series by SNMP/icmppingloss,5m)>{$ICMP_LOSS_WARN} and min(/Cisco Nexus 9000 Series by SNMP/icmppingloss,5m)<100 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| High ICMP ping response time | WARNING | no description | avg(/Cisco Nexus 9000 Series by SNMP/icmppingsec,5m)>{$ICMP_RESPONSE_TIME_WARN} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Device has been replaced | INFO | The serial number of a device has changed. Acknowledge to close the problem manually. | change(/Cisco Nexus 9000 Series by SNMP/system.hw.serialnumber)=1 and length(last(/Cisco Nexus 9000 Series by SNMP/system.hw.serialnumber))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| System name has changed | INFO | The system name has changed. Acknowledge to close the problem manually. | change(/Cisco Nexus 9000 Series by SNMP/system.name)=1 and length(last(/Cisco Nexus 9000 Series by SNMP/system.name))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Operating system description has changed | INFO | The description of the operating system has changed. Possible reasons that system has been updated or replaced. Acknowledge to close the problem manually. | change(/Cisco Nexus 9000 Series by SNMP/system.sw.os)=1 and length(last(/Cisco Nexus 9000 Series by SNMP/system.sw.os))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Device has been restarted or reinitialized | WARNING | The record of SNMP Boots has changed in less than 10 minutes. The restart of a device also counts. | last(/Cisco Nexus 9000 Series by SNMP/system.uptime)<10m | [{"tag": "scope", "value": "notice"}] | no url |
| No SNMP data collection | WARNING | SNMP is not available for polling. Check the connectivity of a device and SNMP settings. | max(/Cisco Nexus 9000 Series by SNMP/zabbix[host,snmp,available],{$SNMP.TIMEOUT})=0 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discoveries" />

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| CPU discovery | cpu.discovery | You must use CISCO-PROCESS-MIB and its object `cpmCPUTotal5minRev` from the table called `cpmCPUTotalTable`, and indexed with `cpmCPUTotalPhysicalIndex`.<br>The table `cpmCPUTotalTable` allows CISCO-PROCESS-MIB to keep the CPU statistics for different physical entities in the router, such as different CPU chips, a group of CPUs, or CPUs in different modules/cards.<br>In the case of a single CPU, the `cpmCPUTotalTable` has only one entry. | SNMP_AGENT | no lifetime | 1h |
| Entity serial numbers discovery | entity_sn.discovery | The discovery of serial numbers of the entities from ENTITY-MIB. | SNMP_AGENT | no lifetime | 1h |
| Fan status discovery | fan.status.discovery | The discovery of metrics for the fan's status from ENTITY-MIB and CISCO-ENTITY-FRU-CONTROL-MIB. | SNMP_AGENT | no lifetime | 1h |
| Memory discovery | memory.discovery | The discovery of `ciscoMemoryPoolTable` - the table that contains monitoring entries of the memory pool.<br>For more details see "How to Get Free and Largest Block of Contiguous Memory Using SNMP":<br>http://www.cisco.com/c/en/us/support/docs/ip/simple-network-management-protocol-snmp/15216-contiguous-memory.html | SNMP_AGENT | no lifetime | 1h |
| Network interfaces discovery | net.if.discovery | The discovery of interfaces from IF-MIB. | SNMP_AGENT | no lifetime | 1h |
| EtherLike discovery | net.if.duplex.discovery | The discovery of interfaces from IF-MIB and EtherLike-MIB. The interfaces that have up (1) operational status are discovered. | SNMP_AGENT | no lifetime | 1h |
| PSU discovery | psu.discovery | The discovery of power supplies from ENTITY-MIB and CISCO-ENTITY-FRU-CONTROL-MIB. | SNMP_AGENT | no lifetime | 1h |
| Temperature sensors discovery | temperature.discovery | The discovery of temperature sensors from CISCO-ENTITY-SENSOR-MIB and ENTITY-MIB. The sensors that have celsius (8) `entSensorType` are discovered. The scale of gathered values is taken from the `entSensorScale` and applied in item preprocessing. | SNMP_AGENT | no lifetime | 1h |


<a name="discovery_cpu_discovery" />

## Discovery CPU discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| #{#SNMPINDEX}: CPU utilization | MIB: CISCO-PROCESS-MIB<br>The object name: `cpmCPUTotal5minRev`<br><br>The MIB object `cpmCPUTotal5minRev` provides a more accurate view of the performance of the router over time than the MIB objects `cpmCPUTotal1minRev` and `cpmCPUTotal5secRev`. These MIB objects are not accurate because they look at the CPU with an interval of one minute and five seconds, respectively. These MIBs enable to monitor the trends and plan the capacity of your network. The recommended baseline rising threshold for the `cpmCPUTotal5minRev` is 90 percent. Depending on the platform, some routers that run at 90 percent, for example, 2500 series can exhibit performance degradation versus a high-end router, for example, the 7500 series, which can operate fine. | system.cpu.util[{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| #{#SNMPINDEX}: High CPU utilization | WARNING | The CPU utilization is too high. The system might be slow to respond. | min(/Cisco Nexus 9000 Series by SNMP/system.cpu.util[{#SNMPINDEX}],5m)>{$CPU.UTIL.CRIT} | [{"tag": "scope", "value": "capacity"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_entity_serial_numbers_discovery" />

## Discovery Entity serial numbers discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#ENT_NAME}: Hardware serial number | MIB: ENTITY-MIB.<br>The object name: `entPhysicalSerialNum`.<br>The vendor-specific serial number string for the physical entity. The preferred value is the serial number string actually printed on the component itself (if present). | system.hw.serialnumber[{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#ENT_NAME}: Device has been replaced | INFO | The device serial number has changed. Acknowledge to close the problem manually. | change(/Cisco Nexus 9000 Series by SNMP/system.hw.serialnumber[{#SNMPINDEX}])=1 and length(last(/Cisco Nexus 9000 Series by SNMP/system.hw.serialnumber[{#SNMPINDEX}]))>0 | [{"tag": "scope", "value": "notice"}] | no url |


<a name="discovery_fan_status_discovery" />

## Discovery Fan status discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#SNMPVALUE}: Fan operational status | MIB: CISCO-ENTITY-FRU-CONTROL-MIB.<br>The object name: `cefcFanTrayOperStatus`.<br>The operational state of the fan or a fan tray.<br>Possible values:<br>-  unknown (1) - unknown;<br>-  up (2) - powered on;<br>-  down (3) - powered down;<br>-  warning (4) - partial failure; needs replacement as soon as possible. | sensor.fan.status[{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#SNMPVALUE}: Fan is down | AVERAGE | The fan unit requires immediate attention. | last(/Cisco Nexus 9000 Series by SNMP/sensor.fan.status[{#SNMPINDEX}])=3 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SNMPVALUE}: Fan is in unknown state | INFO | The fan unit requires attention. | last(/Cisco Nexus 9000 Series by SNMP/sensor.fan.status[{#SNMPINDEX}])=1 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SNMPVALUE}: Fan is in warning state | WARNING | The fan unit requires attention. | last(/Cisco Nexus 9000 Series by SNMP/sensor.fan.status[{#SNMPINDEX}])=4 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_memory_discovery" />

## Discovery Memory discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#SNMPVALUE}: Free memory | MIB: CISCO-ENHANCED-MEMPOOL-MIB.<br>The object name: `cempMemPoolFree`.<br>It indicates the number of bytes from the memory pool that are currently unused on the physical entity. | vm.memory.free[{#SNMPINDEX}] | SNMP_AGENT |
| {#SNMPVALUE}: Used memory | MIB: CISCO-ENHANCED-MEMPOOL-MIB.<br>The object name: `cempMemPoolUsed`.<br>It indicates the number of bytes from the memory pool that are currently in use by applications on the physical entity. | vm.memory.used[{#SNMPINDEX}] | SNMP_AGENT |
| {#SNMPVALUE}: Memory utilization | The memory utilization expressed in %. | vm.memory.util[{#SNMPINDEX}] | CALCULATED |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#SNMPVALUE}: High memory utilization | AVERAGE | The system is running out of free memory. | min(/Cisco Nexus 9000 Series by SNMP/vm.memory.util[{#SNMPINDEX}],5m)>{$MEMORY.UTIL.MAX} | [{"tag": "scope", "value": "capacity"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_network_interfaces_discovery" />

## Discovery Network interfaces discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Interface {#IFNAME}({#IFALIAS}): Inbound packets discarded | MIB: IF-MIB.<br>The number of inbound packets, which were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.<br>One possible reason for discarding such a packet could be the necessity to free up the buffer space.<br>Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime. | net.if.in.discards[{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Inbound packets with errors | MIB: IF-MIB.<br>For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.<br>For character-oriented or fixed-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol.<br>Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime. | net.if.in.errors[{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Bits received | MIB: IF-MIB.<br>The total number of octets received on the interface, including framing characters. This object is a 64-bit version of ifInOctets.<br>Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime. | net.if.in[{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Outbound packets discarded | MIB: IF-MIB.<br>The number of outbound packets, which were chosen to be discarded, even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.<br>One possible reason for discarding such a packet could be to free up buffer space.<br>Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime. | net.if.out.discards[{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Outbound packets with errors | MIB: IF-MIB.<br>For packet-oriented interfaces, the number of outbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.<br>For character-oriented or fixed-length interfaces, the number of outbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol.<br>Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime. | net.if.out.errors[{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Bits sent | MIB: IF-MIB.<br>The total number of octets transmitted out of the interface, including framing characters. This object is a 64-bit version of the ifOutOctets.<br>Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of the ifCounterDiscontinuityTime. | net.if.out[{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Speed | MIB: IF-MIB.<br>An estimate of the interface's current bandwidth in units of 1,000,000 bits per second. If this object reports a value of "n", then the speed of the interface is somewhere in the range from n-500,000 to n+499,999.<br>For the interfaces, which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth.<br>For a sub-layer, which has no concept of bandwidth, this object should be zero. | net.if.speed[{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Operational status | MIB: IF-MIB.<br>The current operational state of the interface:<br>-  The testing (3) state indicates that no operational packet scan be passed.<br>-  If ifAdminStatus is down (2), then ifOperStatus should be down (2).<br>-  If ifAdminStatus is changed to up (1), then ifOperStatus should change to up (1), provided the interface is ready to transmit and receive network traffic.<br>-  It should change to dormant (5) if the interface is waiting for external actions, such as a serial line waiting for an incoming connection.<br>-  It should remain in the down (2) state if and only when there is a fault that prevents it from going to the up (1) state.<br>-  It should remain in the notPresent (6) state if the interface has missing components (typically, hardware). | net.if.status[{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Interface type | MIB: IF-MIB.<br>The type of an interface.<br>Additional values for ifType are assigned by the Internet Assigned Numbers Authority (IANA)<br>through updating the syntax of the IANAifType textual convention. | net.if.type[{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Interface {#IFNAME}({#IFALIAS}): High input error rate | WARNING | It recovers when it goes below 80% of the {$IF.ERRORS.WARN:"{#IFNAME}"} threshold. | min(/Cisco Nexus 9000 Series by SNMP/net.if.in.errors[{#SNMPINDEX}],5m)>{$IF.ERRORS.WARN:"{#IFNAME}"} | [{"tag": "scope", "value": "performance"}] | no url |
| Interface {#IFNAME}({#IFALIAS}): High output error rate | WARNING | It recovers when it goes below 80% of the {$IF.ERRORS.WARN:"{#IFNAME}"} threshold. | min(/Cisco Nexus 9000 Series by SNMP/net.if.out.errors[{#SNMPINDEX}],5m)>{$IF.ERRORS.WARN:"{#IFNAME}"} | [{"tag": "scope", "value": "performance"}] | no url |
| Interface {#IFNAME}({#IFALIAS}): Link down | AVERAGE | This trigger expression works as follows:<br>1. It can be triggered if the operations status is down.<br>2. Use $IFCONTROL macro with context "{#IFNAME}" to void trigger firing on specific interfaces. Values:<br>-  0 : Marks an interface as not important. Trigger does not fire when interface is down.<br>-  1 : Default value to fire the trigger when interface is down<br>3. change(//net.if.status[{#IFNAME}]) - condition prevents firing of trigger if status did not change. It helps in cases, when interfaces were initially down.<br>BEWARE, manual close will ceasefire until at least two status changes happens again! | {$IFCONTROL:"{#IFNAME}"}=1 <br>and last(/Cisco Nexus 9000 Series by SNMP/net.if.status[{#SNMPINDEX}])=2 <br>and change(/Cisco Nexus 9000 Series by SNMP/net.if.status[{#SNMPINDEX}]) | [{"tag": "scope", "value": "availability"}] | no url |
| Interface {#IFNAME}({#IFALIAS}): Ethernet has changed to lower speed than it was before | INFO | This Ethernet connection has transitioned down from its known maximum speed. This might be a sign of issues with autonegotiation. Acknowledge to close the problem manually. | change(/Cisco Nexus 9000 Series by SNMP/net.if.speed[{#SNMPINDEX}])<0 <br>and last(/Cisco Nexus 9000 Series by SNMP/net.if.speed[{#SNMPINDEX}])>0 <br>and find(/Cisco Nexus 9000 Series by SNMP/net.if.type[{#SNMPINDEX}],#1,"regexp","^(6\|7\|11\|62\|69\|117)$") <br>and last(/Cisco Nexus 9000 Series by SNMP/net.if.status[{#SNMPINDEX}])<>2 | [{"tag": "scope", "value": "performance"}] | no url |
| Interface {#IFNAME}({#IFALIAS}): High inbound bandwidth usage | WARNING | The utilization of the network interface is close to its estimated maximum bandwidth. | (avg(/Cisco Nexus 9000 Series by SNMP/net.if.in[{#SNMPINDEX}],15m)>({$IF.UTIL.MAX:"{#IFNAME}"}/100)*last(/Cisco Nexus 9000 Series by SNMP/net.if.speed[{#SNMPINDEX}])) and<br>last(/Cisco Nexus 9000 Series by SNMP/net.if.speed[{#SNMPINDEX}])>0 | [{"tag": "scope", "value": "performance"}] | no url |
| Interface {#IFNAME}({#IFALIAS}): High outbound bandwidth usage | WARNING | The utilization of the network interface is close to its estimated maximum bandwidth. | (avg(/Cisco Nexus 9000 Series by SNMP/net.if.out[{#SNMPINDEX}],15m)>({$IF.UTIL.MAX:"{#IFNAME}"}/100)*last(/Cisco Nexus 9000 Series by SNMP/net.if.speed[{#SNMPINDEX}])) and<br>last(/Cisco Nexus 9000 Series by SNMP/net.if.speed[{#SNMPINDEX}])>0 | [{"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_etherlike_discovery" />

## Discovery EtherLike discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Interface {#IFNAME}({#IFALIAS}): Duplex status | MIB: EtherLike-MIB.<br>The object name: dot3StatsDuplexStatus.<br>The current mode of operation of the MAC entity 'unknown' indicates that the current duplex mode could not be determined.<br>The management control of the duplex mode is accomplished through the MAU MIB. <br>When the interface does not support autonegotiation, or when autonegotiation is not enabled, the duplex mode is controlled using ifMauDefaultType.<br>When autonegotiation is supported and enabled, duplex mode is controlled using ifMauAutoNegAdvertisedBits.<br>In either case, the currently operating duplex mode is reflected in both: in this object and in ifMauType.<br>Note that this object provides redundant information with ifMauType.<br>Normally, redundant objects are discouraged. <br>However, in this instance, it allows the management application to determine the duplex status of an interface without having to know every possible value of ifMauType.<br>This was felt to be sufficiently valuable to justify the redundancy.<br>For the reference see: [IEEE 802.3 Std.], 30.3.1.1.32, aDuplexStatus. | net.if.duplex[{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Interface {#IFNAME}({#IFALIAS}): In half-duplex mode | WARNING | Check the autonegotiation settings and cabling. | last(/Cisco Nexus 9000 Series by SNMP/net.if.duplex[{#SNMPINDEX}])=2 | [{"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_psu_discovery" />

## Discovery PSU discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#SNMPVALUE}: Power supply status | MIB: CISCO-ENTITY-FRU-CONTROL-MIB.<br>The object name: cefcFRUPowerOperStatus.<br>The Operational field-replaceable unit (FRU) Status types.<br>The valid values are:<br>-  offEnvOther (1): FRU is powered off because of a problem not listed below;<br>-  on (2): FRU is powered on;<br>-  offAdmin (3): administratively off;<br>-  offDenied (4): FRU is powered off because available system power is insufficient;<br>-  offEnvPower (5): FRU is powered off because of a power problem in the FRU. For example, the FRU's power translation (DC-DC converter) or distribution failed;<br>-  offEnvTemp (6): FRU is powered off because of temperature problem;<br>-  offEnvFan (7): FRU is powered off because of fan problems;<br>-  failed (8): FRU is in failed state;<br>-  onButFanFail (9): FRU is on but fan has failed;<br>-  offCooling (10): FRU is powered off because of the system's insufficient cooling capacity;<br>-  offConnectorRating (11): FRU is powered off because of the system's connector rating exceeded;<br>-  onButInlinePowerFail (12): The FRU is on but no inline power is being delivered as the data/inline power component of the FRU has failed. | sensor.psu.status[{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#SNMPVALUE}: PSU is in failed state | HIGH | The FRU is in a failed state. | last(/Cisco Nexus 9000 Series by SNMP/sensor.psu.status[{#SNMPINDEX}])=8 | [{"tag": "scope", "value": "availability"}] | no url |
| {#SNMPVALUE}: PSU is off: Administratively | INFO | The FRU is administratively off. | last(/Cisco Nexus 9000 Series by SNMP/sensor.psu.status[{#SNMPINDEX}])=3 | [{"tag": "scope", "value": "availability"}] | no url |
| {#SNMPVALUE}: PSU is off or out of optimal state | AVERAGE | The PSU requires attention. Compare the current state from operational data with the table below:<br>-  offEnvOther (1): FRU is powered off because of a problem not listed below;<br>-  on (2): FRU is powered on;<br>-  offAdmin (3): administratively off;<br>-  offDenied (4): FRU is powered off because available system power is insufficient;<br>-  offEnvPower (5): FRU is powered off because of a power problem in the FRU. For example, the FRU's power translation (DC-DC converter) or distribution failed;<br>-  offEnvTemp (6): FRU is powered off because of temperature problem;<br>-  offEnvFan (7): FRU is powered off because of fan problems;<br>-  failed (8): FRU is in failed state;<br>-  onButFanFail (9): FRU is on but fan has failed;<br>-  offCooling (10): FRU is powered off because of the system's insufficient cooling capacity;<br>-  offConnectorRating (11): FRU is powered off because of the system's connector rating exceeded;<br>-  onButInlinePowerFail (12): The FRU is on but no inline power is being delivered as the data/inline power component of the FRU has failed. | find(/Cisco Nexus 9000 Series by SNMP/sensor.psu.status[{#SNMPINDEX}],#1,"regexp",{$PSU.PROBLEM.STATES}) | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discovery_temperature_sensors_discovery" />

## Discovery Temperature sensors discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#SNMPVALUE}: Temperature sensor status | MIB: CISCO-ENTITY-SENSOR-MIB.<br>The object name: entSensorStatus.<br>This variable indicates the present operational status of the sensor.<br>Possible values:<br>-  ok (1): means the agent can read the sensor value;<br>-  unavailable (2): means that the agent presently can not report the sensor value;<br>-  nonoperational (3) means that the agent believes the sensor is broken. The sensor could have a hard failure (e.g., disconnected wire), or a soft failure (e.g., out-of-range, jittery, or wildly fluctuating readings). | sensor.temp.status[{#SNMPINDEX}] | SNMP_AGENT |
| {#SNMPVALUE}: Temperature | MIB: CISCO-ENTITY-SENSOR-MIB.<br>The object name: entSensorValue.<br>This variable reports the most recent measurement seen by the sensor. | sensor.temp.value[{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#SNMPVALUE}: Temperature sensor is not available | WARNING | It means that the agent presently can not report the sensor value. | last(/Cisco Nexus 9000 Series by SNMP/sensor.temp.status[{#SNMPINDEX}])=2 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SNMPVALUE}: Temperature sensor is not operational | HIGH | It means that the agent considers that the sensor is broken. The sensor could have a hard failure (e.g., disconnected wire), or a soft failure (e.g., out-of-range, jittery, or wildly fluctuating readings). | last(/Cisco Nexus 9000 Series by SNMP/sensor.temp.status[{#SNMPINDEX}])=3 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SNMPVALUE}: Temperature is above critical threshold | HIGH | This trigger uses the values of the temperature sensor. | avg(/Cisco Nexus 9000 Series by SNMP/sensor.temp.value[{#SNMPINDEX}],5m)>{$TEMP_CRIT:"{#SNMPVALUE}"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SNMPVALUE}: Temperature is above warning threshold | WARNING | This trigger uses the values of the temperature sensor. | avg(/Cisco Nexus 9000 Series by SNMP/sensor.temp.value[{#SNMPINDEX}],5m)>{$TEMP_WARN:"{#SNMPVALUE}"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SNMPVALUE}: Temperature is too low | AVERAGE | no description | avg(/Cisco Nexus 9000 Series by SNMP/sensor.temp.value[{#SNMPINDEX}],5m)<{$TEMP_CRIT_LOW:"{#SNMPVALUE}"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


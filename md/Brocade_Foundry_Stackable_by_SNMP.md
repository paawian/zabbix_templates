# Brocade_Foundry Stackable by SNMP template description

Template Brocade Foundry Stackable

MIBs used:
FOUNDRY-SN-AGENT-MIB
HOST-RESOURCES-MIB
SNMPv2-MIB
FOUNDRY-SN-STACKING-MIB
IF-MIB

Known Issues:

  Description: Correct fan(returns fan status as 'other(1)' and temperature (returns 0) for the non-master Switches are not available in SNMP
  Version: Version 08.0.40b and above
  Device: ICX 7750 in stack

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Chassis Discovery ](#discovery_chassis_discovery)
  * [Discovery FAN Discovery ](#discovery_fan_discovery)
  * [Discovery Network interfaces discovery ](#discovery_network_interfaces_discovery)
  * [Discovery PSU Discovery ](#discovery_psu_discovery)
  * [Discovery Stack Discovery ](#discovery_stack_discovery)
  * [Discovery Temperature Discovery ](#discovery_temperature_discovery)

<a name="items"></a>

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| ICMP ping | no description | icmpping | SIMPLE | no delay |
| ICMP loss | no description | icmppingloss | SIMPLE | no delay |
| ICMP response time | no description | icmppingsec | SIMPLE | no delay |
| SNMP traps (fallback) | The item is used to collect all SNMP traps unmatched by other snmptrap items | snmptrap.fallback | SNMP_TRAP | 0 |
| System contact details | MIB: SNMPv2-MIB<br>The textual identification of the contact person for this managed node, together with information on how to contact this person.  If no contact information is known, the value is the zero-length string. | system.contact[sysContact.0] | SNMP_AGENT | 15m |
| CPU utilization | MIB: FOUNDRY-SN-AGENT-MIB<br>The statistics collection of 1 minute CPU utilization. | system.cpu.util[snAgGblCpuUtil1MinAvg.0] | SNMP_AGENT | no delay |
| System description | MIB: SNMPv2-MIB<br>A textual description of the entity. This value should<br>include the full name and version identification of the system's hardware type, software operating-system, and<br>networking software. | system.descr[sysDescr.0] | SNMP_AGENT | 15m |
| Firmware version | MIB: FOUNDRY-SN-AGENT-MIB<br>The version of the running software in the form 'major.minor.maintenance[letters]' | system.hw.firmware | SNMP_AGENT | 1h |
| Uptime (hardware) | MIB: HOST-RESOURCES-MIB<br>The amount of time since this host was last initialized. Note that this is different from sysUpTime in the SNMPv2-MIB [RFC1907] because sysUpTime is the uptime of the network management portion of the system. | system.hw.uptime[hrSystemUptime.0] | SNMP_AGENT | 30s |
| System location | MIB: SNMPv2-MIB<br>Physical location of the node (e.g., `equipment room`, `3rd floor`). If not provided, the value is a zero-length string. | system.location[sysLocation.0] | SNMP_AGENT | 15m |
| System name | MIB: SNMPv2-MIB<br>An administratively-assigned name for this managed node.By convention, this is the node's fully-qualified domain name.  If the name is unknown, the value is the zero-length string. | system.name | SNMP_AGENT | 15m |
| Uptime (network) | MIB: SNMPv2-MIB<br>Time (in hundredths of a second) since the network management portion of the system was last re-initialized. | system.net.uptime[sysUpTime.0] | SNMP_AGENT | 30s |
| System object ID | MIB: SNMPv2-MIB<br>The vendor's authoritative identification of the network management subsystem contained in the entity.  This value is allocated within the SMI enterprises subtree (1.3.6.1.4.1) and provides an easy and unambiguous means for determining`what kind of box' is being managed.  For example, if vendor`Flintstones, Inc.' was assigned the subtree1.3.6.1.4.1.4242, it could assign the identifier 1.3.6.1.4.1.4242.1.1 to its `Fred Router'. | system.objectid[sysObjectID.0] | SNMP_AGENT | 15m |
| Memory utilization | MIB: FOUNDRY-SN-AGENT-MIB<br>The system dynamic memory utilization, in unit of percentage.<br>Deprecated: Refer to snAgSystemDRAMUtil.<br>For NI platforms, refer to snAgentBrdMemoryUtil100thPercent. | vm.memory.util[snAgGblDynMemUtil.0] | SNMP_AGENT | no delay |
| SNMP agent availability | Availability of SNMP checks on the host. The value of this item corresponds to availability icons in the host list.<br>Possible values:<br>0 - not available<br>1 - available<br>2 - unknown | zabbix[host,snmp,available] | INTERNAL | no delay |


<a name="macros"></a>

## Macros
| macro | value |
| ------------- |------------- |
| {$CPU.UTIL.CRIT} | 90 |
| {$FAN_CRIT_STATUS} | 3 |
| {$FAN_OK_STATUS} | 2 |
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
| {$PSU_CRIT_STATUS} | 3 |
| {$PSU_OK_STATUS} | 2 |
| {$SNMP.TIMEOUT} | 5m |
| {$TEMP_CRIT} | 75 |
| {$TEMP_CRIT_LOW} | 5 |
| {$TEMP_WARN} | 65 |


<a name="triggers"></a>

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Unavailable by ICMP ping | HIGH | Last three attempts returned timeout.  Please check device connectivity. | max(/Brocade_Foundry Stackable by SNMP/icmpping,#3)=0 | [{"tag": "scope", "value": "availability"}] | no url |
| High ICMP ping loss | WARNING | no description | min(/Brocade_Foundry Stackable by SNMP/icmppingloss,5m)>{$ICMP_LOSS_WARN} and min(/Brocade_Foundry Stackable by SNMP/icmppingloss,5m)<100 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| High ICMP ping response time | WARNING | Average ICMP response time is too high. | avg(/Brocade_Foundry Stackable by SNMP/icmppingsec,5m)>{$ICMP_RESPONSE_TIME_WARN} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| High CPU utilization | WARNING | The CPU utilization is too high. The system might be slow to respond. | min(/Brocade_Foundry Stackable by SNMP/system.cpu.util[snAgGblCpuUtil1MinAvg.0],5m)>{$CPU.UTIL.CRIT} | [{"tag": "scope", "value": "performance"}] | no url |
| Firmware has changed | INFO | Firmware version has changed. Acknowledge to close the problem manually. | last(/Brocade_Foundry Stackable by SNMP/system.hw.firmware,#1)<>last(/Brocade_Foundry Stackable by SNMP/system.hw.firmware,#2) and length(last(/Brocade_Foundry Stackable by SNMP/system.hw.firmware))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| System name has changed | INFO | The name of the system has changed. Acknowledge to close the problem manually. | last(/Brocade_Foundry Stackable by SNMP/system.name,#1)<>last(/Brocade_Foundry Stackable by SNMP/system.name,#2) and length(last(/Brocade_Foundry Stackable by SNMP/system.name))>0 | [{"tag": "scope", "value": "notice"}, {"tag": "scope", "value": "security"}] | no url |
| High memory utilization | AVERAGE | The system is running out of free memory. | min(/Brocade_Foundry Stackable by SNMP/vm.memory.util[snAgGblDynMemUtil.0],5m)>{$MEMORY.UTIL.MAX} | [{"tag": "scope", "value": "capacity"}, {"tag": "scope", "value": "performance"}] | no url |
| No SNMP data collection | WARNING | SNMP is not available for polling. Please check device connectivity and SNMP settings. | max(/Brocade_Foundry Stackable by SNMP/zabbix[host,snmp,available],{$SNMP.TIMEOUT})=0 | [{"tag": "scope", "value": "availability"}] | no url |
| Host has been restarted | WARNING | Uptime is less than 10 minutes. | (last(/Brocade_Foundry Stackable by SNMP/system.hw.uptime[hrSystemUptime.0])>0 and last(/Brocade_Foundry Stackable by SNMP/system.hw.uptime[hrSystemUptime.0])<10m) or (last(/Brocade_Foundry Stackable by SNMP/system.hw.uptime[hrSystemUptime.0])=0 and last(/Brocade_Foundry Stackable by SNMP/system.net.uptime[sysUpTime.0])<10m) | [{"tag": "scope", "value": "notice"}] | no url |


<a name="discoveries"></a>

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Chassis Discovery | chassis.discovery | snChasUnitIndex: The index to chassis table. | SNMP_AGENT | no lifetime | 1h |
| FAN Discovery | fan.discovery | snChasFan2Table: A table of each fan information for each unit. Only installed fan appears in a table row. | SNMP_AGENT | no lifetime | 1h |
| Network interfaces discovery | net.if.discovery | Discovering interfaces from IF-MIB. | SNMP_AGENT | no lifetime | 1h |
| PSU Discovery | psu.discovery | snChasPwrSupply2Table: A table of each power supply information for each unit. Only installed power supply appears in a table row. | SNMP_AGENT | no lifetime | 1h |
| Stack Discovery | stack.discovery | Discovering snStackingConfigUnitTable for Model names | SNMP_AGENT | no lifetime | 1h |
| Temperature Discovery | temp.discovery | snAgentTemp2Table:Table to list temperatures of the modules in the device for each unit. This table is applicable to only those modules with temperature sensors. | SNMP_AGENT | no lifetime | 1h |


<a name="discovery_chassis_discovery" />

## Discovery Chassis Discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Unit {#SNMPVALUE}: Hardware serial number | MIB: FOUNDRY-SN-AGENT-MIB<br>The serial number of the chassis for each unit. If the serial number is unknown or unavailable then the value should be a zero length string. | system.hw.serialnumber[snChasUnitSerNum.{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Unit {#SNMPVALUE}: Device has been replaced | INFO | Device serial number has changed. Acknowledge to close the problem manually. | last(/Brocade_Foundry Stackable by SNMP/system.hw.serialnumber[snChasUnitSerNum.{#SNMPINDEX}],#1)<>last(/Brocade_Foundry Stackable by SNMP/system.hw.serialnumber[snChasUnitSerNum.{#SNMPINDEX}],#2) and length(last(/Brocade_Foundry Stackable by SNMP/system.hw.serialnumber[snChasUnitSerNum.{#SNMPINDEX}]))>0 | [{"tag": "scope", "value": "notice"}] | no url |


<a name="discovery_fan_discovery" />

## Discovery FAN Discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Unit {#FAN_UNIT} Fan {#FAN_INDEX}: Fan status | MIB: FOUNDRY-SN-AGENT-MIB | sensor.fan.status[snChasFan2OperStatus.{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Unit {#FAN_UNIT} Fan {#FAN_INDEX}: Fan is in critical state | AVERAGE | Please check the fan unit | count(/Brocade_Foundry Stackable by SNMP/sensor.fan.status[snChasFan2OperStatus.{#SNMPINDEX}],#1,"eq","{$FAN_CRIT_STATUS}")=1 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Unit {#FAN_UNIT} Fan {#FAN_INDEX}: Fan is not in normal state | INFO | Please check the fan unit | count(/Brocade_Foundry Stackable by SNMP/sensor.fan.status[snChasFan2OperStatus.{#SNMPINDEX}],#1,"ne","{$FAN_OK_STATUS}")=1 | [{"tag": "scope", "value": "notice"}] | no url |


<a name="discovery_network_interfaces_discovery" />

## Discovery Network interfaces discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Interface {#IFNAME}({#IFALIAS}): Inbound packets discarded | MIB: IF-MIB<br>The number of inbound packets which were chosen to be discarded<br>even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.<br>One possible reason for discarding such a packet could be to free up buffer space.<br>Discontinuities in the value of this counter can occur at re-initialization of the management system,<br>and at other times as indicated by the value of ifCounterDiscontinuityTime. | net.if.in.discards[ifInDiscards.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Inbound packets with errors | MIB: IF-MIB<br>For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character-oriented or fixed-length interfaces, the number of inbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime. | net.if.in.errors[ifInErrors.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Bits received | MIB: IF-MIB<br>The total number of octets received on the interface, including framing characters. This object is a 64-bit version of ifInOctets. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime. | net.if.in[ifHCInOctets.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Outbound packets discarded | MIB: IF-MIB<br>The number of outbound packets which were chosen to be discarded<br>even though no errors had been detected to prevent their being deliverable to a higher-layer protocol.<br>One possible reason for discarding such a packet could be to free up buffer space.<br>Discontinuities in the value of this counter can occur at re-initialization of the management system,<br>and at other times as indicated by the value of ifCounterDiscontinuityTime. | net.if.out.discards[ifOutDiscards.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Outbound packets with errors | MIB: IF-MIB<br>For packet-oriented interfaces, the number of outbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.  For character-oriented or fixed-length interfaces, the number of outbound transmission units that contained errors preventing them from being deliverable to a higher-layer protocol. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime. | net.if.out.errors[ifOutErrors.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Bits sent | MIB: IF-MIB<br>The total number of octets transmitted out of the interface, including framing characters. This object is a 64-bit version of ifOutOctets.Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime. | net.if.out[ifHCOutOctets.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Speed | MIB: IF-MIB<br>An estimate of the interface's current bandwidth in units of 1,000,000 bits per second. If this object reports a value of `n' then the speed of the interface is somewhere in the range of `n-500,000' to`n+499,999'.  For interfaces which do not vary in bandwidth or for those where no accurate estimation can be made, this object should contain the nominal bandwidth. For a sub-layer which has no concept of bandwidth, this object should be zero. | net.if.speed[ifHighSpeed.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Operational status | MIB: IF-MIB<br>The current operational state of the interface.<br>- The testing(3) state indicates that no operational packet scan be passed<br>- If ifAdminStatus is down(2) then ifOperStatus should be down(2)<br>- If ifAdminStatus is changed to up(1) then ifOperStatus should change to up(1) if the interface is ready to transmit and receive network traffic<br>- It should change todormant(5) if the interface is waiting for external actions (such as a serial line waiting for an incoming connection)<br>- It should remain in the down(2) state if and only if there is a fault that prevents it from going to the up(1) state<br>- It should remain in the notPresent(6) state if the interface has missing(typically, hardware) components. | net.if.status[ifOperStatus.{#SNMPINDEX}] | SNMP_AGENT |
| Interface {#IFNAME}({#IFALIAS}): Interface type | MIB: IF-MIB<br>The type of interface.<br>Additional values for ifType are assigned by the Internet Assigned Numbers Authority (IANA),<br>through updating the syntax of the IANAifType textual convention. | net.if.type[ifType.{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Interface {#IFNAME}({#IFALIAS}): Link down | AVERAGE | This trigger expression works as follows:<br>1. It can be triggered if the operations status is down.<br>2. `{$IFCONTROL:"{#IFNAME}"}=1` - a user can redefine the context macro to "0", marking this interface as not important. No new trigger will be fired if this interface is down.<br>3. `{TEMPLATE_NAME:METRIC.diff()}=1` - the trigger fires only if the operational status was up to (1) sometime before (so, does not fire for "eternal off" interfaces.)<br><br>WARNING: if closed manually - it will not fire again on the next poll, because of .diff. | {$IFCONTROL:"{#IFNAME}"}=1 and last(/Brocade_Foundry Stackable by SNMP/net.if.status[ifOperStatus.{#SNMPINDEX}])=2 and (last(/Brocade_Foundry Stackable by SNMP/net.if.status[ifOperStatus.{#SNMPINDEX}],#1)<>last(/Brocade_Foundry Stackable by SNMP/net.if.status[ifOperStatus.{#SNMPINDEX}],#2)) | [{"tag": "scope", "value": "availability"}] | no url |
| Interface {#IFNAME}({#IFALIAS}): Ethernet has changed to lower speed than it was before | INFO | This Ethernet connection has transitioned down from its known maximum speed. This might be a sign of autonegotiation issues. Acknowledge to close the problem manually. | change(/Brocade_Foundry Stackable by SNMP/net.if.speed[ifHighSpeed.{#SNMPINDEX}])<0 and last(/Brocade_Foundry Stackable by SNMP/net.if.speed[ifHighSpeed.{#SNMPINDEX}])>0<br>and (<br>last(/Brocade_Foundry Stackable by SNMP/net.if.type[ifType.{#SNMPINDEX}])=6 or<br>last(/Brocade_Foundry Stackable by SNMP/net.if.type[ifType.{#SNMPINDEX}])=7 or<br>last(/Brocade_Foundry Stackable by SNMP/net.if.type[ifType.{#SNMPINDEX}])=11 or<br>last(/Brocade_Foundry Stackable by SNMP/net.if.type[ifType.{#SNMPINDEX}])=62 or<br>last(/Brocade_Foundry Stackable by SNMP/net.if.type[ifType.{#SNMPINDEX}])=69 or<br>last(/Brocade_Foundry Stackable by SNMP/net.if.type[ifType.{#SNMPINDEX}])=117<br>)<br>and<br>(last(/Brocade_Foundry Stackable by SNMP/net.if.status[ifOperStatus.{#SNMPINDEX}])<>2) | [{"tag": "scope", "value": "performance"}] | no url |
| Interface {#IFNAME}({#IFALIAS}): High bandwidth usage | WARNING | The utilization of the network interface is close to its estimated maximum bandwidth. | (avg(/Brocade_Foundry Stackable by SNMP/net.if.in[ifHCInOctets.{#SNMPINDEX}],15m)>({$IF.UTIL.MAX:"{#IFNAME}"}/100)*last(/Brocade_Foundry Stackable by SNMP/net.if.speed[ifHighSpeed.{#SNMPINDEX}]) or<br>avg(/Brocade_Foundry Stackable by SNMP/net.if.out[ifHCOutOctets.{#SNMPINDEX}],15m)>({$IF.UTIL.MAX:"{#IFNAME}"}/100)*last(/Brocade_Foundry Stackable by SNMP/net.if.speed[ifHighSpeed.{#SNMPINDEX}])) and<br>last(/Brocade_Foundry Stackable by SNMP/net.if.speed[ifHighSpeed.{#SNMPINDEX}])>0 | [{"tag": "scope", "value": "performance"}] | no url |
| Interface {#IFNAME}({#IFALIAS}): High error rate | WARNING | It recovers when it is below 80% of the `{$IF.ERRORS.WARN:"{#IFNAME}"}` threshold. | min(/Brocade_Foundry Stackable by SNMP/net.if.in.errors[ifInErrors.{#SNMPINDEX}],5m)>{$IF.ERRORS.WARN:"{#IFNAME}"}<br>or min(/Brocade_Foundry Stackable by SNMP/net.if.out.errors[ifOutErrors.{#SNMPINDEX}],5m)>{$IF.ERRORS.WARN:"{#IFNAME}"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_psu_discovery" />

## Discovery PSU Discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Unit {#PSU_UNIT} PSU {#PSU_INDEX}: Power supply status | MIB: FOUNDRY-SN-AGENT-MIB | sensor.psu.status[snChasPwrSupply2OperStatus.{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Unit {#PSU_UNIT} PSU {#PSU_INDEX}: Power supply is in critical state | AVERAGE | Please check the power supply unit for errors | count(/Brocade_Foundry Stackable by SNMP/sensor.psu.status[snChasPwrSupply2OperStatus.{#SNMPINDEX}],#1,"eq","{$PSU_CRIT_STATUS}")=1 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Unit {#PSU_UNIT} PSU {#PSU_INDEX}: Power supply is not in normal state | INFO | Please check the power supply unit for errors | count(/Brocade_Foundry Stackable by SNMP/sensor.psu.status[snChasPwrSupply2OperStatus.{#SNMPINDEX}],#1,"ne","{$PSU_OK_STATUS}")=1 | [{"tag": "scope", "value": "notice"}] | no url |


<a name="discovery_stack_discovery" />

## Discovery Stack Discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Unit {#SNMPINDEX}: Hardware model name | MIB: FOUNDRY-SN-STACKING-MIB<br>A description of the configured/active system type for each unit. | system.hw.model[snStackingConfigUnitType.{#SNMPINDEX}] | SNMP_AGENT |


<a name="discovery_temperature_discovery" />

## Discovery Temperature Discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#SENSOR_DESCR}: Temperature | MIB: FOUNDRY-SN-AGENT-MIB<br>Temperature of the sensor represented by this row. Each unit is 0.5 degrees Celsius. | sensor.temp.value[snAgentTemp2Value.{#SNMPINDEX}] | SNMP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#SENSOR_DESCR}: Temperature is above critical threshold | HIGH | This trigger uses temperature sensor values as well as temperature sensor status if available | avg(/Brocade_Foundry Stackable by SNMP/sensor.temp.value[snAgentTemp2Value.{#SNMPINDEX}],5m)>{$TEMP_CRIT:"{#SENSOR_DESCR}"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SENSOR_DESCR}: Temperature is above warning threshold | WARNING | This trigger uses temperature sensor values as well as temperature sensor status if available | avg(/Brocade_Foundry Stackable by SNMP/sensor.temp.value[snAgentTemp2Value.{#SNMPINDEX}],5m)>{$TEMP_WARN:"{#SENSOR_DESCR}"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| {#SENSOR_DESCR}: Temperature is too low | AVERAGE | no description | avg(/Brocade_Foundry Stackable by SNMP/sensor.temp.value[snAgentTemp2Value.{#SNMPINDEX}],5m)<{$TEMP_CRIT_LOW:"{#SENSOR_DESCR}"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |

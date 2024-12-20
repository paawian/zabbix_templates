# Generic by SNMP template description

Template Module Generic

MIBs used:
HOST-RESOURCES-MIB
SNMPv2-MIB

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| ICMP ping | no description | icmpping | SIMPLE | no delay |
| ICMP loss | no description | icmppingloss | SIMPLE | no delay |
| ICMP response time | no description | icmppingsec | SIMPLE | no delay |
| SNMP traps (fallback) | The item is used to collect all SNMP traps unmatched by other snmptrap items | snmptrap.fallback | SNMP_TRAP | 0 |
| System contact details | MIB: SNMPv2-MIB<br>The textual identification of the contact person for this managed node, together with information on how to contact this person.  If no contact information is known, the value is the zero-length string. | system.contact[sysContact.0] | SNMP_AGENT | 15m |
| System description | MIB: SNMPv2-MIB<br>A textual description of the entity. This value should<br>include the full name and version identification of the system's hardware type, software operating-system, and<br>networking software. | system.descr[sysDescr.0] | SNMP_AGENT | 15m |
| Uptime (hardware) | MIB: HOST-RESOURCES-MIB<br>The amount of time since this host was last initialized. Note that this is different from sysUpTime in the SNMPv2-MIB [RFC1907] because sysUpTime is the uptime of the network management portion of the system. | system.hw.uptime[hrSystemUptime.0] | SNMP_AGENT | 30s |
| System location | MIB: SNMPv2-MIB<br>Physical location of the node (e.g., `equipment room`, `3rd floor`). If not provided, the value is a zero-length string. | system.location[sysLocation.0] | SNMP_AGENT | 15m |
| System name | MIB: SNMPv2-MIB<br>An administratively-assigned name for this managed node.By convention, this is the node's fully-qualified domain name.  If the name is unknown, the value is the zero-length string. | system.name | SNMP_AGENT | 15m |
| Uptime (network) | MIB: SNMPv2-MIB<br>Time (in hundredths of a second) since the network management portion of the system was last re-initialized. | system.net.uptime[sysUpTime.0] | SNMP_AGENT | 30s |
| System object ID | MIB: SNMPv2-MIB<br>The vendor's authoritative identification of the network management subsystem contained in the entity.  This value is allocated within the SMI enterprises subtree (1.3.6.1.4.1) and provides an easy and unambiguous means for determining`what kind of box' is being managed.  For example, if vendor`Flintstones, Inc.' was assigned the subtree1.3.6.1.4.1.4242, it could assign the identifier 1.3.6.1.4.1.4242.1.1 to its `Fred Router'. | system.objectid[sysObjectID.0] | SNMP_AGENT | 15m |
| SNMP agent availability | Availability of SNMP checks on the host. The value of this item corresponds to availability icons in the host list.<br>Possible values:<br>0 - not available<br>1 - available<br>2 - unknown | zabbix[host,snmp,available] | INTERNAL | no delay |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$ICMP_LOSS_WARN} | 20 |
| {$ICMP_RESPONSE_TIME_WARN} | 0.15 |
| {$SNMP.TIMEOUT} | 5m |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Unavailable by ICMP ping | HIGH | Last three attempts returned timeout.  Please check device connectivity. | max(/Generic by SNMP/icmpping,#3)=0 | [{"tag": "scope", "value": "availability"}] | no url |
| High ICMP ping loss | WARNING | no description | min(/Generic by SNMP/icmppingloss,5m)>{$ICMP_LOSS_WARN} and min(/Generic by SNMP/icmppingloss,5m)<100 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| High ICMP ping response time | WARNING | Average ICMP response time is too high. | avg(/Generic by SNMP/icmppingsec,5m)>{$ICMP_RESPONSE_TIME_WARN} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| System name has changed | INFO | The name of the system has changed. Acknowledge to close the problem manually. | last(/Generic by SNMP/system.name,#1)<>last(/Generic by SNMP/system.name,#2) and length(last(/Generic by SNMP/system.name))>0 | [{"tag": "scope", "value": "notice"}, {"tag": "scope", "value": "security"}] | no url |
| No SNMP data collection | WARNING | SNMP is not available for polling. Please check device connectivity and SNMP settings. | max(/Generic by SNMP/zabbix[host,snmp,available],{$SNMP.TIMEOUT})=0 | [{"tag": "scope", "value": "availability"}] | no url |
| Host has been restarted | WARNING | Uptime is less than 10 minutes. | (last(/Generic by SNMP/system.hw.uptime[hrSystemUptime.0])>0 and last(/Generic by SNMP/system.hw.uptime[hrSystemUptime.0])<10m) or (last(/Generic by SNMP/system.hw.uptime[hrSystemUptime.0])=0 and last(/Generic by SNMP/system.net.uptime[sysUpTime.0])<10m) | [{"tag": "scope", "value": "notice"}] | no url |


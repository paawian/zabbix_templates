# Zabbix agent active template description

Use this template instead of 'Zabbix agent' for agents running in active mode only.

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)

<a name="items"></a>

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Host name of Zabbix agent running | no description | agent.hostname | ZABBIX_ACTIVE | 1h |
| Zabbix agent ping | The agent always returns "1" for this item. May be used in combination with `nodata()` for the availability check. | agent.ping | ZABBIX_ACTIVE | no delay |
| Version of Zabbix agent running | no description | agent.version | ZABBIX_ACTIVE | 1h |
| Active agent availability | Availability of active checks on the host. The value of this item corresponds to availability icons in the host list.<br>Possible values:<br>0 - unknown<br>1 - available<br>2 - not available | zabbix[host,active_agent,available] | INTERNAL | no delay |


<a name="macros"></a>

## Macros
| macro | value |
| ------------- |------------- |
| {$AGENT.NODATA_TIMEOUT} | 30m |
| {$AGENT.TIMEOUT} | 5m |


<a name="triggers"></a>

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Zabbix agent is not available | AVERAGE | For active agents, `nodata()` with `agent.ping` is used with `{$AGENT.NODATA_TIMEOUT}` as a time threshold. | nodata(/Zabbix agent active/agent.ping,{$AGENT.NODATA_TIMEOUT})=1 | [{"tag": "scope", "value": "availability"}] | no url |
| Active checks are not available | HIGH | Active checks are considered unavailable. Agent has not sent a heartbeat for a prolonged time. | min(/Zabbix agent active/zabbix[host,active_agent,available],{$AGENT.TIMEOUT})=2 | [{"tag": "scope", "value": "availability"}] | no url |


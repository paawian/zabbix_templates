# Chassis by IPMI template description

Template for monitoring servers with BMC over IPMI that work without any external scripts.
All metrics are collected at once, thanks to Zabbix's bulk data collection. The template is available starting from Zabbix version 5.0.
It collects metrics by polling BMC remotely using an IPMI agent.


Known Issues:

  Description: If the BMC has a sensor with an empty threshold value, we get the LLD error "Cannot create trigger...".

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/398023-discussion-thread-for-official-zabbix-template-ipmi

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [discoveries](#discoveries)
  * [Discovery Discrete sensors discovery ](#discovery_discrete_sensors_discovery)
  * [Discovery Threshold sensors discovery ](#discovery_threshold_sensors_discovery)

<a name="items"></a>

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Get IPMI sensors | The master item that receives all sensors with values for LLD and dependent elements from BMC. | ipmi.get | IPMI | no delay |


<a name="macros"></a>

## Macros
| macro | value |
| ------------- |------------- |
| {$IPMI.PASSWORD} | no value |
| {$IPMI.SENSOR_TYPE.MATCHES} | .* |
| {$IPMI.SENSOR_TYPE.NOT_MATCHES} | invalid |
| {$IPMI.USER} | no value |


<a name="discoveries"></a>

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Discrete sensors discovery | ipmi.discrete.discovery | Discovery of the discrete IPMI sensors. | DEPENDENT | no lifetime | 0 |
| Threshold sensors discovery | ipmi.sensors.discovery | Discovery of the threshold IPMI sensors. | DEPENDENT | no lifetime | 0 |


<a name="discovery_discrete_sensors_discovery" />

## Discovery Discrete sensors discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#SENSOR_ID} | It is a state of the discrete IPMI sensor. | ipmi.state_text[{#SENSOR_ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#SENSOR_ID} value has changed | INFO | The trigger is informing about changes in a state of the discrete IPMI sensor. A problem generated by this trigger can be manually closed. | last(/Chassis by IPMI/ipmi.state_text[{#SENSOR_ID}],#1)<>last(/Chassis by IPMI/ipmi.state_text[{#SENSOR_ID}],#2) | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discovery_threshold_sensors_discovery" />

## Discovery Threshold sensors discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| {#SENSOR_ID}, {#SENSOR_UNIT} | It is a state of the threshold IPMI sensor. | ipmi.value[{#SENSOR_ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| {#SENSOR_ID} value is above critical high | HIGH | The trigger is informing that a value higher than the upper critical threshold has been reached. | min(/Chassis by IPMI/ipmi.value[{#SENSOR_ID}],5m)>{#SENSOR_HI_CRIT} | [{"tag": "scope", "value": "notice"}] | no url |
| {#SENSOR_ID} value is above non-critical high | WARNING | The trigger is informing that a value higher than the upper non-critical threshold has been reached. | min(/Chassis by IPMI/ipmi.value[{#SENSOR_ID}],5m)>{#SENSOR_HI_WARN} | [{"tag": "scope", "value": "notice"}] | no url |
| {#SENSOR_ID} value is above non-recoverable high | DISASTER | The trigger is informing that a value higher than the upper non-recoverable threshold has been reached. | min(/Chassis by IPMI/ipmi.value[{#SENSOR_ID}],5m)>{#SENSOR_HI_DISAST} | [{"tag": "scope", "value": "notice"}] | no url |
| {#SENSOR_ID} value is below critical low | HIGH | The trigger is informing that a value less than the lower critical threshold has been reached. | min(/Chassis by IPMI/ipmi.value[{#SENSOR_ID}],5m)<{#SENSOR_LO_CRIT} | [{"tag": "scope", "value": "notice"}] | no url |
| {#SENSOR_ID} value is below non-critical low | WARNING | The trigger is informing that a value less than the lower non-critical threshold has been reached. | min(/Chassis by IPMI/ipmi.value[{#SENSOR_ID}],5m)<{#SENSOR_LO_WARN} | [{"tag": "scope", "value": "notice"}] | no url |
| {#SENSOR_ID} value is below non-recoverable low | DISASTER | The trigger is informing that a value less than the lower non-recoverable threshold has been reached. | min(/Chassis by IPMI/ipmi.value[{#SENSOR_ID}],5m)<{#SENSOR_LO_DISAST} | [{"tag": "scope", "value": "notice"}] | no url |

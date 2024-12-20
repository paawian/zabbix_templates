# Cisco Meraki device by HTTP template description

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Uplinks loss and quality discovery ](#discovery_uplinks_loss_and_quality_discovery)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Get status | Item for gathering device status from Meraki API. | meraki.device.get.status | HTTP_AGENT | {$MERAKI.GET.STATUS.INTERVAL} |
| public IP | Device public IP<br>Network: {$NETWORK.ID}<br>MAC: {$MAC} | meraki.device.public.ip | DEPENDENT | 0 |
| status | Device operational status<br>Network: {$NETWORK.ID} <br>MAC: {$MAC} | meraki.device.status | DEPENDENT | 0 |
| Get device data | Item for gathering device data from Meraki API. | meraki.get.device | SCRIPT | {$MERAKI.UPLINK.LL.TIMESPAN} |
| Device data item errors | Item for gathering errors of the device item. | meraki.get.device.errors | DEPENDENT | 0 |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$MERAKI.API.URL} | api.meraki.com/api/v1 |
| {$MERAKI.DATA.TIMEOUT} | 60 |
| {$MERAKI.DEVICE.LATENCY} | 0.15 |
| {$MERAKI.DEVICE.LOSS} | 15 |
| {$MERAKI.DEVICE.LOSS.LATENCY.IP.MATCHES} | ^((25[0-5]\|(2[0-4]\|1\d\|[1-9]\|)\d)\.?\b){4}$ |
| {$MERAKI.DEVICE.LOSS.LATENCY.IP.NOT_MATCHES} | ^null$ |
| {$MERAKI.DEVICE.UPLINK.MATCHES} | .* |
| {$MERAKI.DEVICE.UPLINK.NOT_MATCHES} | ^null$ |
| {$MERAKI.GET.STATUS.INTERVAL} | 300 |
| {$MERAKI.HTTP_PROXY} | no value |
| {$MERAKI.TOKEN} | no value |
| {$MERAKI.UPLINK.LL.TIMESPAN} | 180 |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Status is not online | WARNING | no description | last(/Cisco Meraki device by HTTP/meraki.device.status)<>1 | [{"tag": "scope", "value": "availability"}] | no url |
| There are errors in 'Get device data' metric | WARNING | no description | length(last(/Cisco Meraki device by HTTP/meraki.get.device.errors))>0 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discoveries" />

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Uplinks loss and quality discovery | meraki.device.uplinks.discovery | no description | DEPENDENT | no lifetime | 0 |


<a name="discovery_uplinks_loss_and_quality_discovery" />

## Discovery Uplinks loss and quality discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Uplink [{#IP}]: [{#UPLINK}]: Latency | Latency of the device uplink. <br>Network: {#NETWORK.ID}. <br>Device serial: {#SERIAL}. | meraki.device.latency[{#IP},{#UPLINK}] | DEPENDENT |
| Uplink [{#IP}]: [{#UPLINK}]: Loss, % | Loss percent of the device uplink. <br>Network: {#NETWORK.ID}. <br>Device serial: {#SERIAL}. | meraki.device.loss.pct[{#IP},{#UPLINK}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Uplink [{#IP}]: [{#UPLINK}]: latency > {$MERAKI.DEVICE.LATENCY} | WARNING | no description | min(/Cisco Meraki device by HTTP/meraki.device.latency[{#IP},{#UPLINK}],#3)>{$MERAKI.DEVICE.LATENCY} | [{"tag": "scope", "value": "performance"}] | no url |
| Uplink [{#IP}]: [{#UPLINK}]: loss > {$MERAKI.DEVICE.LOSS}% | WARNING | no description | min(/Cisco Meraki device by HTTP/meraki.device.loss.pct[{#IP},{#UPLINK}],#3)>{$MERAKI.DEVICE.LOSS} | [{"tag": "scope", "value": "performance"}] | no url |


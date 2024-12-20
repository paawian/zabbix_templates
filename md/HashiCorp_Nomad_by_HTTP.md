# HashiCorp Nomad by HTTP template description

Discover HashiCorp Nomad servers and clients automatically.

Don't forget to change macro {$NOMAD.ENDPOINT.API.URL}, {$NOMAD.TOKEN} values.

You can discuss this template or leave feedback on our forum: https://www.zabbix.com/forum/zabbix-suggestions-and-feedback.

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)

<a name="items"></a>

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Client nodes API response | Client nodes API response message. | nomad.client.nodes.api.response | DEPENDENT | 0 |
| Nomad clients get | Nomad clients data in raw format. | nomad.client.nodes.get | HTTP_AGENT | 1h |
| Nomad clients count | Nomad clients count. | nomad.clients.count | DEPENDENT | 0 |
| Region | Current cluster region. | nomad.region | DEPENDENT | 0 |
| Server-related APIs response | Server-related (`operator/raft/configuration`, `agent/members`) APIs error response message. | nomad.server.api.response | DEPENDENT | 0 |
| Nomad servers get | Nomad servers data in raw format. | nomad.server.nodes.get | SCRIPT | 1h |
| Nomad servers count | Nomad servers count. | nomad.servers.count | DEPENDENT | 0 |


<a name="macros"></a>

## Macros
| macro | value |
| ------------- |------------- |
| {$NOMAD.API.RESPONSE.SUCCESS} | 200 |
| {$NOMAD.CLIENT.DC.MATCHES} | .* |
| {$NOMAD.CLIENT.DC.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$NOMAD.CLIENT.NAME.MATCHES} | .* |
| {$NOMAD.CLIENT.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$NOMAD.CLIENT.SCHEDULE.ELIGIBILITY.MATCHES} | .* |
| {$NOMAD.CLIENT.SCHEDULE.ELIGIBILITY.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$NOMAD.DATA.TIMEOUT} | 15s |
| {$NOMAD.ENDPOINT.API.URL} | http://localhost:4646 |
| {$NOMAD.HTTP.PROXY} | no value |
| {$NOMAD.SERVER.DC.MATCHES} | .* |
| {$NOMAD.SERVER.DC.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$NOMAD.SERVER.NAME.MATCHES} | .* |
| {$NOMAD.SERVER.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$NOMAD.TOKEN} | <PUT YOUR AUTH TOKEN> |


<a name="triggers"></a>

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Client nodes API connection has failed | AVERAGE | Client nodes API connection has failed.<br>Ensure that Nomad API URL and the necessary permissions have been defined correctly, check the service state and network connectivity between Nomad and Zabbix. | find(/HashiCorp Nomad by HTTP/nomad.client.nodes.api.response,,"like","{$NOMAD.API.RESPONSE.SUCCESS}")=0 | [{"tag": "scope", "value": "availability"}] | no url |
| Server-related API connection has failed | AVERAGE | Server-related API connection has failed.<br>Ensure that Nomad API URL and the necessary permissions have been defined correctly, check the service state and network connectivity between Nomad and Zabbix. | find(/HashiCorp Nomad by HTTP/nomad.server.api.response,,"like","{$NOMAD.API.RESPONSE.SUCCESS}")=0 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discoveries"></a>

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Clients discovery | nomad.clients.discovery | Client nodes discovery. | DEPENDENT | no lifetime | 0 |
| Servers discovery | nomad.servers.discovery | Server nodes discovery. | DEPENDENT | no lifetime | 0 |


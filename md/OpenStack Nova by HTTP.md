# OpenStack Nova by HTTP template description

Discovers and monitors project limits, servers, services, hypervisors, availability zones, hypervisors and tenants with OpenStack Compute API by HTTP using script and HTTP agent items.

This template receives token and service URL from parent host, therefore no additional configuration is necessary.

Read the template documentation prior to using this template.

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Nova: Availability zones discovery ](#discovery_nova:_availability_zones_discovery)
  * [Discovery Nova: Hypervisor discovery ](#discovery_nova:_hypervisor_discovery)
  * [Discovery Nova: Servers discovery ](#discovery_nova:_servers_discovery)
  * [Discovery Nova: Compute services discovery ](#discovery_nova:_compute_services_discovery)
  * [Discovery Nova: Tenant discovery ](#discovery_nova:_tenant_discovery)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Get availability zones | Gets a list of availability zones and its data. | openstack.nova.availability_zone.get | HTTP_AGENT | {$OPENSTACK.NOVA.INTERVAL.AVAILABILITY_ZONE} |
| Get hypervisors | Gets a list of hypervisors and its data. | openstack.nova.hypervisors.get | HTTP_AGENT | {$OPENSTACK.NOVA.INTERVAL.HYPERVISOR} |
| Get absolute limits | Gets absolute limits for the project. | openstack.nova.limits.get | HTTP_AGENT | {$OPENSTACK.NOVA.INTERVAL.LIMITS} |
| Instances count, current | Number of servers in each tenant. | openstack.nova.limits.instances.current | DEPENDENT | 0 |
| Instances count, free | Number of available servers for each tenant. | openstack.nova.limits.instances.free | CALCULATED | {$OPENSTACK.NOVA.INTERVAL.LIMITS} |
| Instances count, max | Number of allowed servers for each tenant. | openstack.nova.limits.instances.max | DEPENDENT | 0 |
| RAM usage, current | Amount of used server RAM. | openstack.nova.limits.ram.current | DEPENDENT | 0 |
| RAM usage, free | Amount of available server RAM. | openstack.nova.limits.ram.free | CALCULATED | {$OPENSTACK.NOVA.INTERVAL.LIMITS} |
| RAM usage, max | Amount of allowed server RAM. | openstack.nova.limits.ram.max | DEPENDENT | 0 |
| vCPUs usage, current | Number of used server cores in each tenant. | openstack.nova.limits.vcpu.current | DEPENDENT | 0 |
| vCPUs usage, free | Number of available server cores for each tenant. | openstack.nova.limits.vcpu.free | CALCULATED | {$OPENSTACK.NOVA.INTERVAL.LIMITS} |
| vCPUs usage, max | Number of allowed server cores for each tenant. | openstack.nova.limits.vcpu.max | DEPENDENT | 0 |
| Get servers | Gets a list of servers. | openstack.nova.servers.get | HTTP_AGENT | {$OPENSTACK.NOVA.INTERVAL.SERVERS} |
| Get compute services | Gets a list of compute services and its data. | openstack.nova.services.get | HTTP_AGENT | {$OPENSTACK.NOVA.INTERVAL.SERVICES} |
| Get tenants | Gets a list of tenants and its data. | openstack.nova.tenant.get | SCRIPT | {$OPENSTACK.NOVA.INTERVAL.TENANTS} |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$OPENSTACK.AVAILABILITY_ZONE.DISCOVERY.NAME.MATCHES} | .* |
| {$OPENSTACK.AVAILABILITY_ZONE.DISCOVERY.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$OPENSTACK.HTTP.PROXY} | no value |
| {$OPENSTACK.HYPERVISOR.DISCOVERY.HOSTNAME.MATCHES} | .* |
| {$OPENSTACK.HYPERVISOR.DISCOVERY.HOSTNAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$OPENSTACK.HYPERVISOR.DISCOVERY.IP.MATCHES} | .* |
| {$OPENSTACK.HYPERVISOR.DISCOVERY.IP.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$OPENSTACK.HYPERVISOR.DISCOVERY.TYPE.MATCHES} | .* |
| {$OPENSTACK.HYPERVISOR.DISCOVERY.TYPE.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$OPENSTACK.NOVA.CPU.UTIL.HIGH} | 90 |
| {$OPENSTACK.NOVA.CPU.UTIL.WARN} | 75 |
| {$OPENSTACK.NOVA.INSTANCES.UTIL.HIGH} | 90 |
| {$OPENSTACK.NOVA.INSTANCES.UTIL.WARN} | 75 |
| {$OPENSTACK.NOVA.INTERVAL.AVAILABILITY_ZONE} | 3m |
| {$OPENSTACK.NOVA.INTERVAL.HYPERVISOR} | 3m |
| {$OPENSTACK.NOVA.INTERVAL.LIMITS} | 3m |
| {$OPENSTACK.NOVA.INTERVAL.SERVERS} | 3m |
| {$OPENSTACK.NOVA.INTERVAL.SERVICES} | 3m |
| {$OPENSTACK.NOVA.INTERVAL.TENANTS} | 3m |
| {$OPENSTACK.NOVA.RAM.UTIL.HIGH} | 90 |
| {$OPENSTACK.NOVA.RAM.UTIL.WARN} | 75 |
| {$OPENSTACK.NOVA.SERVICE.URL} | no value |
| {$OPENSTACK.NOVA.TENANT.PERIOD} | m |
| {$OPENSTACK.SERVER.DISCOVERY.NAME.MATCHES} | .* |
| {$OPENSTACK.SERVER.DISCOVERY.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$OPENSTACK.SERVICES.DISCOVERY.BINARY.MATCHES} | .* |
| {$OPENSTACK.SERVICES.DISCOVERY.BINARY.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$OPENSTACK.SERVICES.DISCOVERY.HOST.MATCHES} | .* |
| {$OPENSTACK.SERVICES.DISCOVERY.HOST.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$OPENSTACK.TOKEN} | no value |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Current instances count is high | WARNING | Current instances count has exceeded {$OPENSTACK.NOVA.INSTANCES.UTIL.WARN}% of the max available instances count. | last(/OpenStack Nova by HTTP/openstack.nova.limits.instances.current) >= ({$OPENSTACK.NOVA.INSTANCES.UTIL.WARN} / 100 * last(/OpenStack Nova by HTTP/openstack.nova.limits.instances.max)) | [{"tag": "scope", "value": "capacity"}] | no url |
| Current instances count is too high | HIGH | Current instances count has exceeded {$OPENSTACK.NOVA.INSTANCES.UTIL.HIGH}% of the max available instances count. | last(/OpenStack Nova by HTTP/openstack.nova.limits.instances.current) >= ({$OPENSTACK.NOVA.INSTANCES.UTIL.HIGH} / 100 * last(/OpenStack Nova by HTTP/openstack.nova.limits.instances.max)) | [{"tag": "scope", "value": "capacity"}] | no url |
| Current RAM usage is high | WARNING | Current RAM usage has exceeded {$OPENSTACK.NOVA.RAM.UTIL.WARN}% of the max available RAM usage. | last(/OpenStack Nova by HTTP/openstack.nova.limits.ram.current) >= ({$OPENSTACK.NOVA.RAM.UTIL.WARN} / 100 * last(/OpenStack Nova by HTTP/openstack.nova.limits.ram.max)) | [{"tag": "scope", "value": "capacity"}] | no url |
| Current RAM usage is too high | HIGH | Current RAM usage has exceeded {$OPENSTACK.NOVA.RAM.UTIL.HIGH}% of the max available RAM usage. | last(/OpenStack Nova by HTTP/openstack.nova.limits.ram.current) >= ({$OPENSTACK.NOVA.RAM.UTIL.HIGH} / 100 * last(/OpenStack Nova by HTTP/openstack.nova.limits.ram.max)) | [{"tag": "scope", "value": "capacity"}] | no url |
| Current vCPU usage is high | WARNING | Current vCPU usage has exceeded {$OPENSTACK.NOVA.CPU.UTIL.WARN}% of the max available vCPU usage. | last(/OpenStack Nova by HTTP/openstack.nova.limits.vcpu.current) >= ({$OPENSTACK.NOVA.CPU.UTIL.WARN} / 100 * last(/OpenStack Nova by HTTP/openstack.nova.limits.vcpu.max)) | [{"tag": "scope", "value": "capacity"}] | no url |
| Current vCPU usage is too high | HIGH | Current vCPU usage has exceeded {$OPENSTACK.NOVA.CPU.UTIL.HIGH}% of the max available vCPU usage. | last(/OpenStack Nova by HTTP/openstack.nova.limits.vcpu.current) >= ({$OPENSTACK.NOVA.CPU.UTIL.HIGH} / 100 * last(/OpenStack Nova by HTTP/openstack.nova.limits.vcpu.max)) | [{"tag": "scope", "value": "capacity"}] | no url |


<a name="discoveries" />

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Nova: Availability zones discovery | openstack.nova.availability_zone.discovery | Discovers OpenStack Nova availability zones. | DEPENDENT | no lifetime | 0 |
| Nova: Hypervisor discovery | openstack.nova.hypervisors.discovery | Discovers OpenStack Nova hypervisors. | DEPENDENT | no lifetime | 0 |
| Nova: Servers discovery | openstack.nova.server.discovery | Discovers OpenStack Nova servers. | DEPENDENT | no lifetime | 0 |
| Nova: Compute services discovery | openstack.nova.services.discovery | Discovers OpenStack compute services. | DEPENDENT | no lifetime | 0 |
| Nova: Tenant discovery | openstack.nova.tenant.discovery | Discovers tenants and their usage data. | DEPENDENT | no lifetime | 0 |


<a name="discovery_nova:_availability_zones_discovery" />

## Discovery Nova: Availability zones discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Availability zone [{#ZONE_NAME}]: Host count | Count of hosts and service objects under single availability zone. | openstack.nova.availability_zone.host_count[{#ZONE_NAME}] | DEPENDENT |
| Availability zone [{#ZONE_NAME}]: Raw data | Raw data of the availability zone. | openstack.nova.availability_zone.raw[{#ZONE_NAME}] | DEPENDENT |
| Availability zone [{#ZONE_NAME}]: State | Current state of the availability zone. | openstack.nova.availability_zone.state[{#ZONE_NAME}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Availability zone [{#ZONE_NAME}]: Zone is unavailable | WARNING | Availability zone is not available. | last(/OpenStack Nova by HTTP/openstack.nova.availability_zone.state[{#ZONE_NAME}])=0 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discovery_nova:_hypervisor_discovery" />

## Discovery Nova: Hypervisor discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Hypervisor [{#ID}]:[{#HOSTNAME}]: Raw data | Raw data of the hypervisor. | openstack.nova.hypervisors.raw[{#ID}] | DEPENDENT |
| Hypervisor [{#ID}]:[{#HOSTNAME}]: State | State of the hypervisor. | openstack.nova.hypervisors.state[{#ID}] | DEPENDENT |
| Hypervisor [{#ID}]:[{#HOSTNAME}]: Status | Status of the hypervisor. | openstack.nova.hypervisors.status[{#ID}] | DEPENDENT |
| Hypervisor [{#ID}]:[{#HOSTNAME}]: Version | Hypervisor version. | openstack.nova.hypervisors.version[{#ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Hypervisor [{#ID}]:[{#HOSTNAME}]: State is "down" | WARNING | State of the hypervisor is "down". | last(/OpenStack Nova by HTTP/openstack.nova.hypervisors.state[{#ID}])=0 | [{"tag": "scope", "value": "availability"}] | no url |
| Hypervisor [{#ID}]:[{#HOSTNAME}]: Status is "disabled" | INFO | Status of the hypervisor is disabled. | last(/OpenStack Nova by HTTP/openstack.nova.hypervisors.status[{#ID}])=0 | [{"tag": "scope", "value": "availability"}] | no url |
| Hypervisor [{#ID}]:[{#HOSTNAME}]: Version has changed | INFO | Version of the hypervisor has changed. Acknowledge to close the problem manually. | last(/OpenStack Nova by HTTP/openstack.nova.hypervisors.version[{#ID}])<>last(/OpenStack Nova by HTTP/openstack.nova.hypervisors.version[{#ID}],#2) and length(last(/OpenStack Nova by HTTP/openstack.nova.hypervisors.version[{#ID}]))>0 | [{"tag": "scope", "value": "notice"}] | no url |


<a name="discovery_nova:_servers_discovery" />

## Discovery Nova: Servers discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Server [{#SERVER_ID}]:[{#SERVER_NAME}]: Status | Server status. | openstack.nova.server.status.get[{#SERVER_ID}] | HTTP_AGENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Server [{#SERVER_ID}]:[{#SERVER_NAME}]: Status has changed | INFO | Status of the server has changed. Acknowledge to close the problem manually. | last(/OpenStack Nova by HTTP/openstack.nova.server.status.get[{#SERVER_ID}])<>last(/OpenStack Nova by HTTP/openstack.nova.server.status.get[{#SERVER_ID}],#2) and length(last(/OpenStack Nova by HTTP/openstack.nova.server.status.get[{#SERVER_ID}]))>0 | [{"tag": "scope", "value": "availability"}] | no url |
| Server [{#SERVER_ID}]:[{#SERVER_NAME}]: Status is "ERROR" | HIGH | Server is in "ERROR" status. | last(/OpenStack Nova by HTTP/openstack.nova.server.status.get[{#SERVER_ID}])=5 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discovery_nova:_compute_services_discovery" />

## Discovery Nova: Compute services discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Compute service [{#HOST}]:[{#BINARY}]:[{#ID}]: Disabling reason | Reason for disabling a service. | openstack.nova.services.disabled.reason[{#ID}] | DEPENDENT |
| Compute service [{#HOST}]:[{#BINARY}]:[{#ID}]: Raw data | Raw data of the service. | openstack.nova.services.raw[{#ID}] | DEPENDENT |
| Compute service [{#HOST}]:[{#BINARY}]:[{#ID}]: State | State of the service. | openstack.nova.services.state[{#ID}] | DEPENDENT |
| Compute service [{#HOST}]:[{#BINARY}]:[{#ID}]: Status | Status of the service. | openstack.nova.services.status[{#ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Compute service [{#HOST}]:[{#BINARY}]:[{#ID}]: State is "down" | WARNING | State of the service is "down". | last(/OpenStack Nova by HTTP/openstack.nova.services.state[{#ID}])=0 | [{"tag": "scope", "value": "availability"}] | no url |
| Compute service [{#HOST}]:[{#BINARY}]:[{#ID}]: Status is "disabled" | INFO | Status of the server is disabled. Acknowledge to close the problem manually. | last(/OpenStack Nova by HTTP/openstack.nova.services.status[{#ID}])=0 and length(last(/OpenStack Nova by HTTP/openstack.nova.services.disabled.reason[{#ID}]))>=0 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discovery_nova:_tenant_discovery" />

## Discovery Nova: Tenant discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Tenant [{#TENANT_ID}]: Total disk usage | Total disk usage hours for the current tenant (project).<br>Multiplying the server disk size (in GiB) by hours the server exists, and then adding that all together for each server. | openstack.nova.tenant.disk_usage[{#TENANT_ID}] | DEPENDENT |
| Tenant [{#TENANT_ID}]: Raw data | Raw data of the tenant. | openstack.nova.tenant.raw[{#TENANT_ID}] | DEPENDENT |
| Tenant [{#TENANT_ID}]: Total hours | Total duration that the servers exist (in hours). | openstack.nova.tenant.total_hours[{#TENANT_ID}] | DEPENDENT |
| Tenant [{#TENANT_ID}]: Total memory usage | Total memory usage hours for the current tenant (project).<br>Multiplying the server memory size (in MiB) by hours the server exists, and then adding that all together for each server. | openstack.nova.tenant.total_memory_mb_usage[{#TENANT_ID}] | DEPENDENT |
| Tenant [{#TENANT_ID}]: Total vCPUs usage | Total vCPU usage hours for the current tenant (project).<br>Multiplying the number of virtual CPUs of the server by hours the server exists, and then adding that all together for each server. | openstack.nova.tenant.total_vcpu[{#TENANT_ID}] | DEPENDENT |


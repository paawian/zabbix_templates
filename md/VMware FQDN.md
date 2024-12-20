# VMware FQDN template description

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/

Note: To enable discovery of hardware sensors of VMware Hypervisors, set the macro '{$VMWARE.HV.SENSOR.DISCOVERY}' to the value 'true' on the discovered host level.

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [discoveries](#discoveries)
  * [Discovery Discover VMware clusters ](#discovery_discover_vmware_clusters)
  * [Discovery Discover VMware datastores ](#discovery_discover_vmware_datastores)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Event log | Collect VMware event log. See also: https://www.zabbix.com/documentation/7.0/manual/config/items/preprocessing/examples#filtering_vmware_event_log_records | vmware.eventlog[{$VMWARE.URL},skip] | SIMPLE | no delay |
| Full name | VMware service full name. | vmware.fullname[{$VMWARE.URL}] | SIMPLE | 1h |
| Version | VMware service version. | vmware.version[{$VMWARE.URL}] | SIMPLE | 1h |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$VMWARE.HV.SENSOR.DISCOVERY} | false |
| {$VMWARE.HV.SENSOR.DISCOVERY.NAME.MATCHES} | .* |
| {$VMWARE.HV.SENSOR.DISCOVERY.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$VMWARE.PASSWORD} | no value |
| {$VMWARE.URL} | no value |
| {$VMWARE.USERNAME} | no value |


<a name="discoveries" />

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Discover VMware clusters | vmware.cluster.discovery[{$VMWARE.URL}] | Discovery of clusters | SIMPLE | no lifetime | 1h |
| Discover VMware datastores | vmware.datastore.discovery[{$VMWARE.URL}] | no description | SIMPLE | no lifetime | 1h |
| Discover VMware hypervisors | vmware.hv.discovery[{$VMWARE.URL}] | Discovery of hypervisors. | SIMPLE | no lifetime | 1h |
| Discover VMware VMs FQDN | vmware.vm.discovery[{$VMWARE.URL}] | Discovery of guest virtual machines. | SIMPLE | no lifetime | 1h |


<a name="discovery_discover_vmware_clusters" />

## Discovery Discover VMware clusters

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Status of "{#CLUSTER.NAME}" cluster | VMware cluster status. | vmware.cluster.status[{$VMWARE.URL},{#CLUSTER.NAME}] | SIMPLE |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| The {#CLUSTER.NAME} status is Red | HIGH | A cluster enabled for DRS becomes invalid (red) when the tree is no longer internally consistent, that is, resource constraints are not observed. See also: https://docs.vmware.com/en/VMware-vSphere/8.0/vsphere-resource-management/GUID-C7417CAA-BD38-41D0-9529-9E7A5898BB12.html | last(/VMware FQDN/vmware.cluster.status[{$VMWARE.URL},{#CLUSTER.NAME}])=3 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| The {#CLUSTER.NAME} status is Yellow | AVERAGE | A cluster becomes overcommitted (yellow) when the tree of resource pools and virtual machines is internally consistent but the cluster does not have the capacity to support all resources reserved by the child resource pools. See also: https://docs.vmware.com/en/VMware-vSphere/8.0/vsphere-resource-management/GUID-ED8240A0-FB54-4A31-BD3D-F23FE740F10C.html | last(/VMware FQDN/vmware.cluster.status[{$VMWARE.URL},{#CLUSTER.NAME}])=2 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_discover_vmware_datastores" />

## Discovery Discover VMware datastores

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Average read latency of the datastore {#DATASTORE} | Amount of time for a read operation from the datastore (milliseconds). | vmware.datastore.read[{$VMWARE.URL},{#DATASTORE},latency] | SIMPLE |
| Free space on datastore {#DATASTORE} (percentage) | VMware datastore space in percentage from total. | vmware.datastore.size[{$VMWARE.URL},{#DATASTORE},pfree] | SIMPLE |
| Total size of datastore {#DATASTORE} | VMware datastore space in bytes. | vmware.datastore.size[{$VMWARE.URL},{#DATASTORE}] | SIMPLE |
| Average write latency of the datastore {#DATASTORE} | Amount of time for a write operation to the datastore (milliseconds). | vmware.datastore.write[{$VMWARE.URL},{#DATASTORE},latency] | SIMPLE |


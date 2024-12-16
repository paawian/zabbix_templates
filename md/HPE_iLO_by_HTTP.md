# HPE iLO by HTTP template description

This template is designed for the effortless deployment of HPE iLO monitoring by Zabbix via iLO RESTful API and doesn't require any external scripts.

Setup:

1. Create the iLO user for monitoring (for example, `zbx_monitor`). The user will only need to have the `Login` privilege, which can be assigned manually or by assigning the `ReadOnly` role to the user.
2. Set the iLO API endpoint URL in the `{$ILO.URL}` macro in the format `<scheme>://<host>[:port]/` (port is optional).
3. Set the name of the user that you created in step 1 in the `{$ILO.USER}` macro.
4. Set the password of the user that you created in step 1 in the `{$ILO.PASSWORD}` macro.

For more details about HPE Redfish services, refer to the official documentation:
https://servermanagementportal.ext.hpe.com/docs/redfishservices/

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery HPE iLO: Computer systems discovery ](#discovery_hpe_ilo:_computer_systems_discovery)
  * [Discovery HPE iLO: Controllers discovery ](#discovery_hpe_ilo:_controllers_discovery)
  * [Discovery HPE iLO: Drives discovery ](#discovery_hpe_ilo:_drives_discovery)
  * [Discovery HPE iLO: Fans discovery ](#discovery_hpe_ilo:_fans_discovery)
  * [Discovery HPE iLO: Managers discovery ](#discovery_hpe_ilo:_managers_discovery)
  * [Discovery HPE iLO: PSU discovery ](#discovery_hpe_ilo:_psu_discovery)
  * [Discovery HPE iLO: Temperature sensors discovery ](#discovery_hpe_ilo:_temperature_sensors_discovery)
  * [Discovery HPE iLO: Storages discovery ](#discovery_hpe_ilo:_storages_discovery)
  * [Discovery HPE iLO: Volumes discovery ](#discovery_hpe_ilo:_volumes_discovery)

<a name="items"></a>

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Get data | The JSON with the result of API requests. | hpe.ilo.get_data | SCRIPT | {$ILO.INTERVAL} |
| Get data check | The data collection check. | hpe.ilo.get_data.check | DEPENDENT | 0 |


<a name="macros"></a>

## Macros
| macro | value |
| ------------- |------------- |
| {$ILO.COMPUTER_SYSTEM.DISCOVERY.HOSTNAME.MATCHES} | .+ |
| {$ILO.COMPUTER_SYSTEM.DISCOVERY.HOSTNAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$ILO.COMPUTER_SYSTEM.DISCOVERY.TYPE.MATCHES} | .+ |
| {$ILO.COMPUTER_SYSTEM.DISCOVERY.TYPE.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$ILO.HTTP_PROXY} | no value |
| {$ILO.INTERVAL} | 1m |
| {$ILO.PASSWORD} | no value |
| {$ILO.SENSOR.DISCOVERY.CONTEXT.MATCHES} | .+ |
| {$ILO.SENSOR.DISCOVERY.CONTEXT.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$ILO.SENSOR.DISCOVERY.NAME.MATCHES} | .+ |
| {$ILO.SENSOR.DISCOVERY.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$ILO.TIMEOUT} | 15s |
| {$ILO.URL} | no value |
| {$ILO.USER} | no value |


<a name="triggers"></a>

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Failed to get data from API | HIGH | Failed to get data from API. Check the debug log for more information. | length(last(/HPE iLO by HTTP/hpe.ilo.get_data.check))>0 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discoveries"></a>

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| HPE iLO: Computer systems discovery | hpe.ilo.computer_systems.discovery | Discovers computer systems. | DEPENDENT | no lifetime | 0 |
| HPE iLO: Controllers discovery | hpe.ilo.controllers.discovery | Discovers storage controllers. | DEPENDENT | no lifetime | 0 |
| HPE iLO: Drives discovery | hpe.ilo.drives.discovery | Discovers storage drives. | DEPENDENT | no lifetime | 0 |
| HPE iLO: Fans discovery | hpe.ilo.fans.discovery | Discovers chassis fans. | DEPENDENT | no lifetime | 0 |
| HPE iLO: Managers discovery | hpe.ilo.managers.discovery | Discovers managers. | DEPENDENT | no lifetime | 0 |
| HPE iLO: PSU discovery | hpe.ilo.psu.discovery | Discovers chassis power supply units (PSU). | DEPENDENT | no lifetime | 0 |
| HPE iLO: Temperature sensors discovery | hpe.ilo.sensors.discovery | Discovers chassis temperature sensors. | DEPENDENT | no lifetime | 0 |
| HPE iLO: Storages discovery | hpe.ilo.storages.discovery | Discovers computer system storages. | DEPENDENT | no lifetime | 0 |
| HPE iLO: Volumes discovery | hpe.ilo.volumes.discovery | Discovers storage volumes. | DEPENDENT | no lifetime | 0 |


<a name="discovery_hpe_ilo:_computer_systems_discovery" />

## Discovery HPE iLO: Computer systems discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Computer system [{#SYSTEM_HOSTNAME}]: BIOS current version | The current BIOS version of the computer system. | hpe.ilo.computer_system.bios.current_version[{#SYSTEM_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Get data | Get data about the computer system. | hpe.ilo.computer_system.get_data[{#SYSTEM_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Model | The model name of the computer system. | hpe.ilo.computer_system.model[{#SYSTEM_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Serial number | The serial number of the computer system. | hpe.ilo.computer_system.serial_number[{#SYSTEM_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Status | The overall health state from the view of this computer system. Possible values:<br><br>0 - "OK", the computer system is in normal condition;<br>1 - "Warning", the computer system is in condition that requires attention;<br>2 - "Critical", the computer system is in critical condition that requires immediate attention;<br>10 - "Unknown", the computer system is in unknown condition. | hpe.ilo.computer_system.status[{#SYSTEM_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: System type | The type of the computer system. Possible values:<br><br>0 - "Physical", a computer system;<br>1 - "Virtual", a virtual machine instance running on this system;<br>2 - "OS", an operating system instance;<br>3 - "PhysicallyPartitioned", a hardware-based partition of a computer system;<br>4 - "VirtuallyPartitioned", a virtual or software-based partition of a computer system;<br>5 - "DPU", a virtual or software-based partition of a computer system;<br>10 - "Unknown", the computer system type is unknown. | hpe.ilo.computer_system.type[{#SYSTEM_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: CPU utilization, in % | Current CPU utilization of the computer system in percentage. | hpe.ilo.computer_system.usage.cpu_util[{#SYSTEM_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: I/O bus utilization, in % | Current I/O bus utilization of the computer system in percentage. | hpe.ilo.computer_system.usage.io_bus_util[{#SYSTEM_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Memory bus utilization, in % | Current memory bus utilization of the computer system in percentage. | hpe.ilo.computer_system.usage.memory_bus_util[{#SYSTEM_ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Computer system [{#SYSTEM_HOSTNAME}]: BIOS version has changed | INFO | The current version of BIOS has changed. Acknowledge to close the problem manually. | change(/HPE iLO by HTTP/hpe.ilo.computer_system.bios.current_version[{#SYSTEM_ID}])=1 and length(last(/HPE iLO by HTTP/hpe.ilo.computer_system.bios.current_version[{#SYSTEM_ID}]))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Computer system [{#SYSTEM_HOSTNAME}]: Computer system has been replaced | INFO | The computer system serial number has changed. Acknowledge to close the problem manually. | change(/HPE iLO by HTTP/hpe.ilo.computer_system.serial_number[{#SYSTEM_ID}])=1 and length(last(/HPE iLO by HTTP/hpe.ilo.computer_system.serial_number[{#SYSTEM_ID}]))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Computer system [{#SYSTEM_HOSTNAME}]: Computer system is in critical state | HIGH | The computer system is in critical condition that requires immediate attention. | last(/HPE iLO by HTTP/hpe.ilo.computer_system.status[{#SYSTEM_ID}])=2 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Computer system [{#SYSTEM_HOSTNAME}]: Computer system is in warning state | WARNING | The computer system is in condition that requires attention. | last(/HPE iLO by HTTP/hpe.ilo.computer_system.status[{#SYSTEM_ID}])=1 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_hpe_ilo:_controllers_discovery" />

## Discovery HPE iLO: Controllers discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Controller [{#CONTROLLER_ID}]: Get data | Get data about the controller. | hpe.ilo.controller.get_data[{#SYSTEM_ID}, {#STORAGE_ID}, {#CONTROLLER_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Controller [{#CONTROLLER_ID}]: Model | The model name of the controller. | hpe.ilo.controller.model[{#SYSTEM_ID}, {#STORAGE_ID}, {#CONTROLLER_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Controller [{#CONTROLLER_ID}]: Serial number | The serial number of the controller. | hpe.ilo.controller.serial_number[{#SYSTEM_ID}, {#STORAGE_ID}, {#CONTROLLER_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Controller [{#CONTROLLER_ID}]: Status | The health state of the controller. Possible values:<br><br>0 - "OK", the controller is in normal condition;<br>1 - "Warning", the controller is in condition that requires attention;<br>2 - "Critical", the controller is in critical condition that requires immediate attention;<br>10 - "Unknown", the controller is in unknown condition. | hpe.ilo.controller.status[{#SYSTEM_ID}, {#STORAGE_ID}, {#CONTROLLER_ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Controller [{#CONTROLLER_ID}]: Controller has been replaced | INFO | The controller serial number has changed. Acknowledge to close the problem manually. | change(/HPE iLO by HTTP/hpe.ilo.controller.serial_number[{#SYSTEM_ID}, {#STORAGE_ID}, {#CONTROLLER_ID}])=1 and length(last(/HPE iLO by HTTP/hpe.ilo.controller.serial_number[{#SYSTEM_ID}, {#STORAGE_ID}, {#CONTROLLER_ID}]))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Controller [{#CONTROLLER_ID}]: Controller is in critical state | HIGH | The controller is in critical condition that requires immediate attention. | last(/HPE iLO by HTTP/hpe.ilo.controller.status[{#SYSTEM_ID}, {#STORAGE_ID}, {#CONTROLLER_ID}])=2 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Controller [{#CONTROLLER_ID}]: Controller is in warning state | WARNING | The controller is in condition that requires attention. | last(/HPE iLO by HTTP/hpe.ilo.controller.status[{#SYSTEM_ID}, {#STORAGE_ID}, {#CONTROLLER_ID}])=1 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_hpe_ilo:_drives_discovery" />

## Discovery HPE iLO: Drives discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Drive [{#DRIVE_ID}]: Capacity | The capacity of the drive. | hpe.ilo.drive.capacity[{#SYSTEM_ID}, {#STORAGE_ID}, {#DRIVE_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Drive [{#DRIVE_ID}]: Get data | Get data about the drive. | hpe.ilo.drive.get_data[{#SYSTEM_ID}, {#STORAGE_ID}, {#DRIVE_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Drive [{#DRIVE_ID}]: Media type | The media type of the drive. | hpe.ilo.drive.media_type[{#SYSTEM_ID}, {#STORAGE_ID}, {#DRIVE_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Drive [{#DRIVE_ID}]: Model | The model name of the drive. | hpe.ilo.drive.model[{#SYSTEM_ID}, {#STORAGE_ID}, {#DRIVE_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Drive [{#DRIVE_ID}]: Predicted media life left, in % | The percentage of reads and writes that are predicted to still be available for the drive. | hpe.ilo.drive.predicted_life_left[{#SYSTEM_ID}, {#STORAGE_ID}, {#DRIVE_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Drive [{#DRIVE_ID}]: Serial number | The serial number of the drive. | hpe.ilo.drive.serial_number[{#SYSTEM_ID}, {#STORAGE_ID}, {#DRIVE_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Drive [{#DRIVE_ID}]: Status indicator | Status of drive. Possible values:<br><br>0 - "OK", the drive is ok;<br>1 - "Fail", the drive has failed;<br>2 - "Rebuild", the drive is being rebuilt;<br>3 - "PredictiveFailureAnalysis", the drive is still working but predicted to fail soon;<br>4 - "Hotspare", the drive is marked to be automatically rebuilt and used as a replacement for a failed drive;<br>5 - "InACriticalArray", the array that this drive is a part of is degraded;<br>6 - "InAFailedArray	", the array that this drive is a part of is failed;<br>10 - "Unknown", the drive status is unknown. | hpe.ilo.drive.status_indicator[{#SYSTEM_ID}, {#STORAGE_ID}, {#DRIVE_ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Drive [{#DRIVE_ID}]: Drive has been replaced | INFO | The drive serial number has changed. Acknowledge to close the problem manually. | change(/HPE iLO by HTTP/hpe.ilo.drive.serial_number[{#SYSTEM_ID}, {#STORAGE_ID}, {#DRIVE_ID}])=1 and length(last(/HPE iLO by HTTP/hpe.ilo.drive.serial_number[{#SYSTEM_ID}, {#STORAGE_ID}, {#DRIVE_ID}]))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Drive [{#DRIVE_ID}]: Drive has failed | HIGH | The drive has failed. | last(/HPE iLO by HTTP/hpe.ilo.drive.status_indicator[{#SYSTEM_ID}, {#STORAGE_ID}, {#DRIVE_ID}])=1 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Drive [{#DRIVE_ID}]: Drive is predicted to fail soon | HIGH | The drive is still working but predicted to fail soon. | last(/HPE iLO by HTTP/hpe.ilo.drive.status_indicator[{#SYSTEM_ID}, {#STORAGE_ID}, {#DRIVE_ID}])=3 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_hpe_ilo:_fans_discovery" />

## Discovery HPE iLO: Fans discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Chassis [{#CHASSIS_ID}]: Fan [{#FAN_NAME}]: Get data | Get data about the fan. | hpe.ilo.fan.get_data[{#CHASSIS_ID}, {#FAN_ID}] | DEPENDENT |
| Chassis [{#CHASSIS_ID}]: Fan [{#FAN_NAME}]: Speed, in % | The current speed of the fan. | hpe.ilo.fan.speed[{#CHASSIS_ID}, {#FAN_ID}] | DEPENDENT |
| Chassis [{#CHASSIS_ID}]: Fan [{#FAN_NAME}]: Status | The health state of the fan. Possible values:<br><br>0 - "OK", the fan is in normal condition;<br>1 - "Warning", the fan is in condition that requires attention;<br>2 - "Critical", the fan is in critical condition that requires immediate attention;<br>10 - "Unknown", the fan is in unknown condition. | hpe.ilo.fan.status[{#CHASSIS_ID}, {#FAN_ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Chassis [{#CHASSIS_ID}]: Fan [{#FAN_NAME}]: Fan is in critical state | HIGH | The fan is in critical condition that requires immediate attention. | last(/HPE iLO by HTTP/hpe.ilo.fan.status[{#CHASSIS_ID}, {#FAN_ID}])=2 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Chassis [{#CHASSIS_ID}]: Fan [{#FAN_NAME}]: Fan is in warning state | WARNING | The fan is in condition that requires attention. | last(/HPE iLO by HTTP/hpe.ilo.fan.status[{#CHASSIS_ID}, {#FAN_ID}])=1 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_hpe_ilo:_managers_discovery" />

## Discovery HPE iLO: Managers discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Manager [{#MANAGER_ID}]: Current firmware version | The current firmware version of the manager. | hpe.ilo.manager.firmware.current_version[{#MANAGER_ID}] | DEPENDENT |
| Manager [{#MANAGER_ID}]: Get data | Get data about the manager. | hpe.ilo.manager.get_data[{#MANAGER_ID}] | DEPENDENT |
| Manager [{#MANAGER_ID}]: Model | The model name of the manager. | hpe.ilo.manager.model[{#MANAGER_ID}] | DEPENDENT |
| Manager [{#MANAGER_ID}]: Status | The health state of the manager. Possible values:<br><br>0 - "OK", the manager is in normal condition;<br>1 - "Warning", the manager is in condition that requires attention;<br>2 - "Critical", the manager is in critical condition that requires immediate attention;<br>10 - "Unknown", the manager is in unknown condition. | hpe.ilo.manager.status[{#MANAGER_ID}] | DEPENDENT |
| Manager [{#MANAGER_ID}]: Manager type | The manager type. Possible values:<br><br>0 - "ManagementController", a controller used primarily to monitor or manage the operation of a device or system;<br>1 - "EnclosureManager", a controller which provides management functions for a chassis or group of devices or systems;<br>2 - "BMC", a controller which provides management functions for a single computer system;<br>10 - "Unknown", the manager type is unknown. | hpe.ilo.manager.type[{#MANAGER_ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Manager [{#MANAGER_ID}]: Firmware version has changed | INFO | The current firmware version of the manager has changed. Acknowledge to close the problem manually. | change(/HPE iLO by HTTP/hpe.ilo.manager.firmware.current_version[{#MANAGER_ID}])=1 and length(last(/HPE iLO by HTTP/hpe.ilo.manager.firmware.current_version[{#MANAGER_ID}]))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Manager [{#MANAGER_ID}]: Manager is in critical state | HIGH | The manager is in critical condition that requires immediate attention. | last(/HPE iLO by HTTP/hpe.ilo.manager.status[{#MANAGER_ID}])=2 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Manager [{#MANAGER_ID}]: Manager is in warning state | WARNING | The manager is in condition that requires attention. | last(/HPE iLO by HTTP/hpe.ilo.manager.status[{#MANAGER_ID}])=1 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_hpe_ilo:_psu_discovery" />

## Discovery HPE iLO: PSU discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Chassis [{#CHASSIS_ID}]: PSU [{#PSU_ID}]: Get data | Get data about the PSU. | hpe.ilo.psu.get_data[{#CHASSIS_ID}, {#PSU_ID}] | DEPENDENT |
| Chassis [{#CHASSIS_ID}]: PSU [{#PSU_ID}]: Last power output | The average power output of the PSU. | hpe.ilo.psu.last_power_output[{#CHASSIS_ID}, {#PSU_ID}] | DEPENDENT |
| Chassis [{#CHASSIS_ID}]: PSU [{#PSU_ID}]: Line input voltage | The line input voltage at which the PSU is operating. | hpe.ilo.psu.line_input_voltage[{#CHASSIS_ID}, {#PSU_ID}] | DEPENDENT |
| Chassis [{#CHASSIS_ID}]: PSU [{#PSU_ID}]: Model | The model name of the PSU. | hpe.ilo.psu.model[{#CHASSIS_ID}, {#PSU_ID}] | DEPENDENT |
| Chassis [{#CHASSIS_ID}]: PSU [{#PSU_ID}]: Serial number | The serial number of the PSU. | hpe.ilo.psu.serial_number[{#CHASSIS_ID}, {#PSU_ID}] | DEPENDENT |
| Chassis [{#CHASSIS_ID}]: PSU [{#PSU_ID}]: Status | The health state of the PSU. Possible values:<br><br>0 - "OK", the PSU is in normal condition;<br>1 - "Warning", the PSU is in condition that requires attention;<br>2 - "Critical", the PSU is in critical condition that requires immediate attention;<br>10 - "Unknown", the PSU is in unknown condition. | hpe.ilo.psu.status[{#CHASSIS_ID}, {#PSU_ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Chassis [{#CHASSIS_ID}]: PSU [{#PSU_ID}]: PSU has been replaced | INFO | The PSU serial number has changed. Acknowledge to close the problem manually. | change(/HPE iLO by HTTP/hpe.ilo.psu.serial_number[{#CHASSIS_ID}, {#PSU_ID}])=1 and length(last(/HPE iLO by HTTP/hpe.ilo.psu.serial_number[{#CHASSIS_ID}, {#PSU_ID}]))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Chassis [{#CHASSIS_ID}]: PSU [{#PSU_ID}]: PSU is in critical state | HIGH | The PSU is in critical condition that requires immediate attention. | last(/HPE iLO by HTTP/hpe.ilo.psu.status[{#CHASSIS_ID}, {#PSU_ID}])=2 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Chassis [{#CHASSIS_ID}]: PSU [{#PSU_ID}]: PSU is in warning state | WARNING | The PSU is in condition that requires attention. | last(/HPE iLO by HTTP/hpe.ilo.psu.status[{#CHASSIS_ID}, {#PSU_ID}])=1 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_hpe_ilo:_temperature_sensors_discovery" />

## Discovery HPE iLO: Temperature sensors discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Chassis [{#CHASSIS_ID}]: Sensor [{#SENSOR_NAME}]: Get data | Get data about the sensor. | hpe.ilo.sensor.get_data[{#CHASSIS_ID}, {#SENSOR_ID}] | DEPENDENT |
| Chassis [{#CHASSIS_ID}]: Sensor [{#SENSOR_NAME}]: Status | The health state of the sensor. Possible values:<br><br>0 - "OK", the sensor is in normal condition;<br>1 - "Warning", the sensor is in condition that requires attention;<br>2 - "Critical", the sensor is in critical condition that requires immediate attention;<br>10 - "Unknown", the sensor is in unknown condition. | hpe.ilo.sensor.status[{#CHASSIS_ID}, {#SENSOR_ID}] | DEPENDENT |
| Chassis [{#CHASSIS_ID}]: Sensor [{#SENSOR_NAME}]: Temperature | The current temperature reading in Celsius degrees for the sensor. | hpe.ilo.sensor.temperature[{#CHASSIS_ID}, {#SENSOR_ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Chassis [{#CHASSIS_ID}]: Sensor [{#SENSOR_NAME}]: Sensor is in critical state | HIGH | The sensor is in critical condition that requires immediate attention. | last(/HPE iLO by HTTP/hpe.ilo.sensor.status[{#CHASSIS_ID}, {#SENSOR_ID}])=2 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Chassis [{#CHASSIS_ID}]: Sensor [{#SENSOR_NAME}]: Sensor is in warning state | WARNING | The sensor is in condition that requires attention. | last(/HPE iLO by HTTP/hpe.ilo.sensor.status[{#CHASSIS_ID}, {#SENSOR_ID}])=1 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_hpe_ilo:_storages_discovery" />

## Discovery HPE iLO: Storages discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Get data | Get data about the storage. | hpe.ilo.storage.get_data[{#SYSTEM_ID}, {#STORAGE_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Status | The overall health state from the view of this storage. Possible values:<br><br>0 - "OK", the storage is in normal condition;<br>1 - "Warning", the storage is in condition that requires attention;<br>2 - "Critical", the storage is in critical condition that requires immediate attention;<br>10 - "Unknown", the storage is in unknown condition. | hpe.ilo.storage.status[{#SYSTEM_ID}, {#STORAGE_ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Storage is in critical state | HIGH | The computer system is in critical condition that requires immediate attention. | last(/HPE iLO by HTTP/hpe.ilo.storage.status[{#SYSTEM_ID}, {#STORAGE_ID}])=2 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Storage is in warning state | WARNING | The computer system is in condition that requires attention. | last(/HPE iLO by HTTP/hpe.ilo.storage.status[{#SYSTEM_ID}, {#STORAGE_ID}])=1 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_hpe_ilo:_volumes_discovery" />

## Discovery HPE iLO: Volumes discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Volume [{#VOLUME_ID}]: Capacity | The capacity of the volume. | hpe.ilo.volume.capacity[{#SYSTEM_ID}, {#STORAGE_ID}, {#VOLUME_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Volume [{#VOLUME_ID}]: Get data | Get data about the volume. | hpe.ilo.volume.get_data[{#SYSTEM_ID}, {#STORAGE_ID}, {#VOLUME_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Volume [{#VOLUME_ID}]: RAID level | The RAID level of the volume. | hpe.ilo.volume.raid_level[{#SYSTEM_ID}, {#STORAGE_ID}, {#VOLUME_ID}] | DEPENDENT |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Volume [{#VOLUME_ID}]: Status | The health state of the volume. Possible values:<br><br>0 - "OK", the volume is in normal condition;<br>1 - "Warning", the volume is in condition that requires attention;<br>2 - "Critical", the volume is in critical condition that requires immediate attention;<br>10 - "Unknown", the volume is in unknown condition. | hpe.ilo.volume.status[{#SYSTEM_ID}, {#STORAGE_ID}, {#VOLUME_ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Volume [{#VOLUME_ID}]: Volume is in critical state | HIGH | The volume is in critical condition that requires immediate attention. | last(/HPE iLO by HTTP/hpe.ilo.volume.status[{#SYSTEM_ID}, {#STORAGE_ID}, {#VOLUME_ID}])=2 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Computer system [{#SYSTEM_HOSTNAME}]: Storage [{#STORAGE_ID}]: Volume [{#VOLUME_ID}]: Volume is in warning state | WARNING | The volume is in condition that requires attention. | last(/HPE iLO by HTTP/hpe.ilo.volume.status[{#SYSTEM_ID}, {#STORAGE_ID}, {#VOLUME_ID}])=1 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |

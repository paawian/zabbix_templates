# Template: OpenBSD by Zabbix agent

## Overview
This is an Official OpenBSD template. It requires Zabbix agent 7.0 or newer.

Notes on filesystem (FS) discovery:
  - The ext4/3/2 FS reserves space for privileged usage, typically set at 5% by default.
  - BTRFS allocates a default of 10% of the volume for its own needs.
  - To mitigate potential disasters, FS usage triggers are based on the maximum available space.
    - Utilization formula: 'pused = 100 - 100 * (available / total - free + available)'
  - The FS utilization chart, derived from graph prototypes, reflects FS reserved space as the difference between used and available space from the total volume.

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/

Generated by official Zabbix template tool "Templator"

## Macros

No macros defined.

## Template Links

No linked templates.

## Items

| Name | Description | Data Type | Key | Tags |
|------|-------------|-----------|-----|------|
| Maximum number of opened files | May be increased by using the `sysctl` utility or modifying the file `/etc/sysctl.conf`. | Unknown | kernel.maxfiles | component:os |
| Maximum number of processes | May be increased by using the `sysctl` utility or modifying the file `/etc/sysctl.conf`. | Unknown | kernel.maxproc | component:processes |
| Number of running processes | The number of processes in a running state. | Unknown | proc.num[,,run] | component:processes |
| Number of processes | The total number of processes in any state. | Unknown | proc.num[] | component:processes |
| Host boot time |  | Unknown | system.boottime | component:os |
| Interrupts per second | Number of interrupts processed. | Unknown | system.cpu.intr | component:cpu |
| Processor load (15 min average per core) | Calculated as the system CPU load divided by the number of CPU cores. | Unknown | system.cpu.load[percpu,avg15] | component:cpu |
| Processor load (1 min average per core) | Calculated as the system CPU load divided by the number of CPU cores. | Unknown | system.cpu.load[percpu,avg1] | component:cpu |
| Processor load (5 min average per core) | Calculated as the system CPU load divided by the number of CPU cores. | Unknown | system.cpu.load[percpu,avg5] | component:cpu |
| Context switches per second | The combined rate at which all processors on the computer are switched from one thread to another. | Unknown | system.cpu.switches | component:cpu |
| CPU idle time | Time the CPU has spent doing nothing. | Unknown | system.cpu.util[,idle] | component:cpu |
| CPU interrupt time | Time the CPU has spent servicing hardware interrupts. | Unknown | system.cpu.util[,interrupt] | component:cpu |
| CPU nice time | Time the CPU has spent running users' processes that have been niced. | Unknown | system.cpu.util[,nice] | component:cpu |
| CPU system time | Time the CPU has spent running the kernel and its processes. | Unknown | system.cpu.util[,system] | component:cpu |
| CPU user time | Time the CPU has spent running users' processes that are not niced. | Unknown | system.cpu.util[,user] | component:cpu |
| Host name | The host name of the system. | Unknown | system.hostname | component:os |
| Host local time | The local system time of the host. | Unknown | system.localtime | component:os |
| Free swap space | The free space of the swap volume/file expressed in bytes. | Unknown | system.swap.size[,free] | component:memory |
| Free swap space in % | The free space of the swap volume/file expressed in %. | Unknown | system.swap.size[,pfree] | component:memory |
| Total swap space | Total space of the swap volume/file expressed in bytes. | Unknown | system.swap.size[,total] | component:memory |
| System information | Information as normally returned by `uname -a`. | Unknown | system.uname | component:os |
| System uptime |  | Unknown | system.uptime | component:os |
| Number of logged in users | The number of users who are currently logged in. | Unknown | system.users.num | component:os, component:security |
| Checksum of /etc/passwd |  | Unknown | vfs.file.cksum[/etc/passwd,sha256] | component:security |
| Available memory | Defined as free + cached + buffers. | Unknown | vm.memory.size[available] | component:memory |
| Total memory | Total memory expressed in bytes. | Unknown | vm.memory.size[total] | component:memory |
| Host name of Zabbix agent running |  | Unknown | agent.hostname | component:system |
| Zabbix agent ping | The agent always returns "1" for this item. May be used in combination with `nodata()` for the availability check. | Unknown | agent.ping | component:system |
| Version of Zabbix agent running |  | Unknown | agent.version | component:application |
| Zabbix agent availability | Used for monitoring the availability status of the agent. | Unknown | zabbix[host,agent,available] | component:system |
| Get filesystems | The `vfs.fs.get` key acquires raw information set about the filesystems. Later to be extracted by preprocessing in dependent items. | Unknown | vfs.fs.get | component:raw |
## Triggers

| Name | Description | Expression | Severity | Dependencies | Tags |
|------|-------------|------------|----------|--------------|------|
| Too many processes running on {HOST.NAME} | Too many processes running on {HOST.NAME} | {13089}>30 | Warning |  | scope:performance |
| Too many processes on {HOST.NAME} | Too many processes on {HOST.NAME} | {13088}>300 | Warning |  | scope:performance |
| Processor load is too high on {HOST.NAME} | Processor load is too high on {HOST.NAME} | {13087}>5 | Warning |  | scope:performance |
| Hostname was changed on {HOST.NAME} | Hostname was changed on {HOST.NAME} | {23374}<>{23375} | Information |  | scope:notice |
| Host information was changed on {HOST.NAME} | Host information was changed on {HOST.NAME} | {23376}<>{23377} | Information |  | scope:notice |
| {HOST.NAME} has just been restarted | {HOST.NAME} has just been restarted | {12726}<0 | Information |  | scope:notice |
| /etc/passwd has been changed on {HOST.NAME} | /etc/passwd has been changed on {HOST.NAME} | {23378}<>{23379} | Warning |  | scope:security |
| Configured max number of opened files is too low on {HOST.NAME} | Configured max number of opened files is too low on {HOST.NAME} | {20145}<1024 | Information |  | scope:notice, scope:performance |
| Configured max number of processes is too low on {HOST.NAME} | Configured max number of processes is too low on {HOST.NAME} | {20146}<256 | Information |  | scope:notice, scope:performance |
| Lack of available memory on server {HOST.NAME} | Lack of available memory on server {HOST.NAME} | {20147}<20M | Average |  | scope:capacity, scope:performance |
| Lack of free swap space on {HOST.NAME} | Lack of free swap space on {HOST.NAME} | {20148}<50 | Warning |  | scope:capacity, scope:performance |
| Zabbix agent is not available | Zabbix agent is not available | {30769}=0 | Average |  | scope:availability |
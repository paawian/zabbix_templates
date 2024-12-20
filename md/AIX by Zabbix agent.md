# AIX by Zabbix agent template description

This is an official AIX template. It requires Zabbix agent 7.0 or newer.

Notes on filesystem (FS) discovery:
  - The ext4/3/2 FS reserves space for privileged usage, typically set at 5% by default.
  - BTRFS allocates a default of 10% of the volume for its own needs.
  - To mitigate potential disasters, FS usage triggers are based on the maximum available space.
    - Utilization formula: 'pused = 100 - 100 * (available / total - free + available)'
  - The FS utilization chart, derived from graph prototypes, reflects FS reserved space as the difference between used and available space from the total volume.

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Network interface discovery ](#discovery_network_interface_discovery)
  * [Discovery Mounted filesystem discovery ](#discovery_mounted_filesystem_discovery)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Host name of Zabbix agent running | no description | agent.hostname | no type | 1h |
| Zabbix agent ping | The agent always returns "1" for this item. May be used in combination with `nodata()` for the availability check. | agent.ping | no type | no delay |
| Version of Zabbix agent running | no description | agent.version | no type | 1h |
| Number of running processes | Number of processes in a running state. | proc.num[,,run] | no type | no delay |
| Number of processes | Total number of processes in any state. | proc.num[] | no type | no delay |
| Interrupts per second | Number of interrupts processed. | system.cpu.intr | no type | no delay |
| Processor load (1 min average per core) | Calculated as the system CPU load divided by the number of CPU cores. | system.cpu.load[percpu,avg1] | no type | no delay |
| Processor load (5 min average per core) | Calculated as the system CPU load divided by the number of CPU cores. | system.cpu.load[percpu,avg5] | no type | no delay |
| Processor load (15 min average per core) | Calculated as the system CPU load divided by the number of CPU cores. | system.cpu.load[percpu,avg15] | no type | no delay |
| Context switches per second | The combined rate at which all processors on the computer are switched from one thread to another. | system.cpu.switches | no type | no delay |
| Host name | The host name of the system. | system.hostname | no type | 1h |
| Host local time | The local system time of the host. | system.localtime | no type | no delay |
| CPU available physical processors in the shared pool | no description | system.stat[cpu,app] | no type | no delay |
| CPU entitled capacity consumed | no description | system.stat[cpu,ec] | no type | no delay |
| CPU idle time | no description | system.stat[cpu,id] | no type | no delay |
| CPU logical processor utilization | no description | system.stat[cpu,lbusy] | no type | no delay |
| CPU number of physical processors consumed | no description | system.stat[cpu,pc] | no type | no delay |
| CPU system time | no description | system.stat[cpu,sy] | no type | no delay |
| CPU user time | no description | system.stat[cpu,us] | no type | no delay |
| CPU iowait time | no description | system.stat[cpu,wa] | no type | no delay |
| Amount of data transferred | no description | system.stat[disk,bps] | no type | no delay |
| Number of transfers | no description | system.stat[disk,tps] | no type | no delay |
| Processor units is entitled to receive | no description | system.stat[ent] | no type | 1h |
| Kernel thread context switches | no description | system.stat[faults,cs] | no type | no delay |
| Device interrupts | no description | system.stat[faults,in] | no type | no delay |
| System calls | no description | system.stat[faults,sy] | no type | no delay |
| Length of the swap queue | no description | system.stat[kthr,b] | no type | no delay |
| Length of the run queue | no description | system.stat[kthr,r] | no type | no delay |
| Active virtual pages | no description | system.stat[memory,avm] | no type | no delay |
| Free real memory | no description | system.stat[memory,fre] | no type | no delay |
| File page-ins per second | no description | system.stat[page,fi] | no type | no delay |
| File page-outs per second | no description | system.stat[page,fo] | no type | no delay |
| Pages freed (page replacement) | no description | system.stat[page,fr] | no type | no delay |
| Pages paged in from paging space | no description | system.stat[page,pi] | no type | no delay |
| Pages paged out to paging space | no description | system.stat[page,po] | no type | no delay |
| Pages scanned by page-replacement algorithm | no description | system.stat[page,sr] | no type | no delay |
| System information | Information as normally returned by `uname -a`. | system.uname | no type | 1h |
| System uptime | no description | system.uptime | no type | 10m |
| Number of logged in users | The number of users who are currently logged in. | system.users.num | no type | no delay |
| Checksum of /etc/passwd | no description | vfs.file.cksum[/etc/passwd,sha256] | no type | 15m |
| Get filesystems | The `vfs.fs.get` key acquires raw information set about the filesystems. Later to be extracted by preprocessing in dependent items. | vfs.fs.get | no type | no delay |
| Available memory | Defined as free + cached + buffers. | vm.memory.size[available] | no type | no delay |
| Total memory | Total memory expressed in bytes. | vm.memory.size[total] | no type | 1h |
| Zabbix agent availability | Used for monitoring the availability status of the agent. | zabbix[host,agent,available] | INTERNAL | no delay |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$AGENT.TIMEOUT} | 3m |
| {$VFS.FS.FSNAME.MATCHES} | .+ |
| {$VFS.FS.FSNAME.NOT_MATCHES} | ^(/dev\|/sys\|/run\|/proc\|.+/shm$) |
| {$VFS.FS.FSTYPE.MATCHES} | ^(btrfs\|ext2\|ext3\|ext4\|reiser\|xfs\|ffs\|ufs\|jfs\|jfs2\|vxfs\|hfs\|apfs\|refs\|ntfs\|fat32\|zfs)$ |
| {$VFS.FS.FSTYPE.NOT_MATCHES} | ^\s$ |
| {$VFS.FS.INODE.PFREE.MIN.CRIT} | 10 |
| {$VFS.FS.INODE.PFREE.MIN.WARN} | 20 |
| {$VFS.FS.PUSED.MAX.CRIT} | 90 |
| {$VFS.FS.PUSED.MAX.WARN} | 80 |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Too many processes running | WARNING | no description | avg(/AIX by Zabbix agent/proc.num[,,run],5m)>30 | [{"tag": "scope", "value": "performance"}] | no url |
| Too many processes | WARNING | no description | avg(/AIX by Zabbix agent/proc.num[],5m)>300 | [{"tag": "scope", "value": "performance"}] | no url |
| Processor load is too high | WARNING | no description | avg(/AIX by Zabbix agent/system.cpu.load[percpu,avg1],5m)>5 | [{"tag": "scope", "value": "performance"}] | no url |
| Hostname was changed | INFO | no description | last(/AIX by Zabbix agent/system.hostname,#1)<>last(/AIX by Zabbix agent/system.hostname,#2) | [{"tag": "scope", "value": "notice"}] | no url |
| Disk I/O is overloaded | WARNING | Extended OS wait times for I/O operations may signal potential performance issues with the storage system. | avg(/AIX by Zabbix agent/system.stat[cpu,wa],5m)>20 | [{"tag": "scope", "value": "performance"}] | no url |
| Host information was changed | INFO | no description | last(/AIX by Zabbix agent/system.uname,#1)<>last(/AIX by Zabbix agent/system.uname,#2) | [{"tag": "scope", "value": "notice"}] | no url |
| Server has just been restarted | INFO | no description | change(/AIX by Zabbix agent/system.uptime)<0 | [{"tag": "scope", "value": "notice"}] | no url |
| /etc/passwd has been changed | WARNING | no description | last(/AIX by Zabbix agent/vfs.file.cksum[/etc/passwd,sha256],#1)<>last(/AIX by Zabbix agent/vfs.file.cksum[/etc/passwd,sha256],#2) | [{"tag": "scope", "value": "security"}] | no url |
| Lack of available memory on server | AVERAGE | no description | last(/AIX by Zabbix agent/vm.memory.size[available])<20M | [{"tag": "scope", "value": "capacity"}, {"tag": "scope", "value": "performance"}] | no url |
| Zabbix agent is not available | AVERAGE | For passive checks only. The availability of the agent(s) and a host is used with `{$AGENT.TIMEOUT}` as the time threshold. | max(/AIX by Zabbix agent/zabbix[host,agent,available],{$AGENT.TIMEOUT})=0 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discoveries" />

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Network interface discovery | net.if.discovery | Used for the discovery of network interfaces. | no type | no lifetime | 1h |
| Mounted filesystem discovery | vfs.fs.dependent.discovery | The discovery of mounted filesystems with different types. | DEPENDENT | no lifetime | 0 |


<a name="discovery_network_interface_discovery" />

## Discovery Network interface discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Interface {#IFNAME}: Incoming network traffic | no description | net.if.in[{#IFNAME}] | no type |
| Interface {#IFNAME}: Outgoing network traffic | no description | net.if.out[{#IFNAME}] | no type |


<a name="discovery_mounted_filesystem_discovery" />

## Discovery Mounted filesystem discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| FS [{#FSNAME}]: Inodes: Free, in % | Free metadata space expressed in %. | vfs.fs.dependent.inode[{#FSNAME},pfree] | DEPENDENT |
| FS [{#FSNAME}]: Space: Available | Available storage space expressed in bytes. | vfs.fs.dependent.size[{#FSNAME},free] | DEPENDENT |
| FS [{#FSNAME}]: Space: Available, in % | Deprecated metric.<br>Space availability expressed as a percentage, calculated using the current and maximum available spaces. | vfs.fs.dependent.size[{#FSNAME},pfree] | DEPENDENT |
| FS [{#FSNAME}]: Space: Used, in % | Calculated as the percentage of currently used space compared to the maximum available space. | vfs.fs.dependent.size[{#FSNAME},pused] | DEPENDENT |
| FS [{#FSNAME}]: Space: Total | Total space expressed in bytes. | vfs.fs.dependent.size[{#FSNAME},total] | DEPENDENT |
| FS [{#FSNAME}]: Space: Used | Used storage expressed in bytes. | vfs.fs.dependent.size[{#FSNAME},used] | DEPENDENT |
| FS [{#FSNAME}]: Get data | Intermediate data of `{#FSNAME}` filesystem. | vfs.fs.dependent[{#FSNAME},data] | DEPENDENT |
| FS [{#FSNAME}]: Option: Read-only | The filesystem is mounted as read-only. It is available only for Zabbix agents 6.4 and higher. | vfs.fs.dependent[{#FSNAME},readonly] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| FS [{#FSNAME}]: Running out of free inodes | AVERAGE | Disk writing may fail if index nodes are exhausted, leading to error messages like "No space left on device" or "Disk is full", despite available free space. | min(/AIX by Zabbix agent/vfs.fs.dependent.inode[{#FSNAME},pfree],5m)<{$VFS.FS.INODE.PFREE.MIN.CRIT:"{#FSNAME}"} | [{"tag": "scope", "value": "capacity"}, {"tag": "scope", "value": "performance"}] | no url |
| FS [{#FSNAME}]: Running out of free inodes | WARNING | Disk writing may fail if index nodes are exhausted, leading to error messages like "No space left on device" or "Disk is full", despite available free space. | min(/AIX by Zabbix agent/vfs.fs.dependent.inode[{#FSNAME},pfree],5m)<{$VFS.FS.INODE.PFREE.MIN.WARN:"{#FSNAME}"} | [{"tag": "scope", "value": "capacity"}, {"tag": "scope", "value": "performance"}] | no url |
| FS [{#FSNAME}]: Space is critically low | AVERAGE | The volume's space usage exceeds the `{$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"}%` limit.<br>The trigger expression is based on the current used and maximum available spaces.<br>Event name represents the total volume space, which can differ from the maximum available space, depending on the filesystem type. | min(/AIX by Zabbix agent/vfs.fs.dependent.size[{#FSNAME},pused],5m)>{$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "capacity"}] | no url |
| FS [{#FSNAME}]: Space is low | WARNING | The volume's space usage exceeds the `{$VFS.FS.PUSED.MAX.WARN:"{#FSNAME}"}%` limit.<br>The trigger expression is based on the current used and maximum available spaces.<br>Event name represents the total volume space, which can differ from the maximum available space, depending on the filesystem type. | min(/AIX by Zabbix agent/vfs.fs.dependent.size[{#FSNAME},pused],5m)>{$VFS.FS.PUSED.MAX.WARN:"{#FSNAME}"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "capacity"}] | no url |
| FS [{#FSNAME}]: Filesystem has become read-only | AVERAGE | The filesystem has become read-only, possibly due to an I/O error. Available only for Zabbix agents 6.4 and higher. | last(/AIX by Zabbix agent/vfs.fs.dependent[{#FSNAME},readonly],#2)=0 and last(/AIX by Zabbix agent/vfs.fs.dependent[{#FSNAME},readonly])=1 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


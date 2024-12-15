# macOS by Zabbix agent template description

This is an official macOS template. It requires Zabbix agent 7.0 or newer.

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
  * [Discovery Mounted filesystem discovery ](#discovery_mounted_filesystem_discovery)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Host name of Zabbix agent running | no description | agent.hostname | no type | 1h |
| Zabbix agent ping | The agent always returns "1" for this item. May be used in combination with `nodata()` for the availability check. | agent.ping | no type | no delay |
| Version of Zabbix agent running | no description | agent.version | no type | 1h |
| Maximum number of opened files | May be increased by using the `sysctl` utility or modifying the file `/etc/sysctl.conf`. | kernel.maxfiles | no type | 1h |
| Maximum number of processes | May be increased by using the `sysctl` utility or modifying the file `/etc/sysctl.conf`. | kernel.maxproc | no type | 1h |
| Incoming network traffic on en0 | no description | net.if.in[en0] | no type | no delay |
| Outgoing network traffic on en0 | no description | net.if.out[en0] | no type | no delay |
| Host boot time | no description | system.boottime | no type | 10m |
| Processor load (1 min average per core) | Calculated as the system CPU load divided by the number of CPU cores. | system.cpu.load[percpu,avg1] | no type | no delay |
| Processor load (5 min average per core) | Calculated as the system CPU load divided by the number of CPU cores. | system.cpu.load[percpu,avg5] | no type | no delay |
| Processor load (15 min average per core) | Calculated as the system CPU load divided by the number of CPU cores. | system.cpu.load[percpu,avg15] | no type | no delay |
| Host name | The host name of the system. | system.hostname | no type | 1h |
| Host local time | The local system time of the host. | system.localtime | no type | no delay |
| System information | Information as normally returned by `uname -a`. | system.uname | no type | 1h |
| System uptime | The system uptime expressed in the following format: "N days, hh:mm:ss". | system.uptime | no type | 10m |
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
| Configured max number of opened files is too low | INFO | no description | last(/macOS by Zabbix agent/kernel.maxfiles)<1024 | [{"tag": "scope", "value": "notice"}, {"tag": "scope", "value": "performance"}] | no url |
| Configured max number of processes is too low | INFO | no description | last(/macOS by Zabbix agent/kernel.maxproc)<256 | [{"tag": "scope", "value": "notice"}, {"tag": "scope", "value": "performance"}] | no url |
| Processor load is too high | WARNING | no description | avg(/macOS by Zabbix agent/system.cpu.load[percpu,avg1],5m)>5 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Hostname was changed | INFO | no description | last(/macOS by Zabbix agent/system.hostname,#1)<>last(/macOS by Zabbix agent/system.hostname,#2) | [{"tag": "scope", "value": "notice"}] | no url |
| Host information was changed | INFO | no description | last(/macOS by Zabbix agent/system.uname,#1)<>last(/macOS by Zabbix agent/system.uname,#2) | [{"tag": "scope", "value": "notice"}] | no url |
| Server has just been restarted | INFO | no description | change(/macOS by Zabbix agent/system.uptime)<0 | [{"tag": "scope", "value": "notice"}] | no url |
| /etc/passwd has been changed | WARNING | no description | last(/macOS by Zabbix agent/vfs.file.cksum[/etc/passwd,sha256],#1)<>last(/macOS by Zabbix agent/vfs.file.cksum[/etc/passwd,sha256],#2) | [{"tag": "scope", "value": "security"}] | no url |
| Lack of available memory on server | AVERAGE | no description | last(/macOS by Zabbix agent/vm.memory.size[available])<20M | [{"tag": "scope", "value": "capacity"}, {"tag": "scope", "value": "performance"}] | no url |
| Zabbix agent is not available | AVERAGE | For passive checks only; the availability of the agent(s) and a host is used with `{$AGENT.TIMEOUT}` as the time threshold. | max(/macOS by Zabbix agent/zabbix[host,agent,available],{$AGENT.TIMEOUT})=0 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discoveries" />

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Mounted filesystem discovery | vfs.fs.dependent.discovery | The discovery of mounted filesystems with different types. Note that the option to exclude dmg software images from discovery is available only with Zabbix agents 6.4 and higher. | DEPENDENT | no lifetime | 0 |


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


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| FS [{#FSNAME}]: Running out of free inodes | AVERAGE | Disk writing may fail if index nodes are exhausted, leading to error messages like "No space left on device" or "Disk is full", despite available free space. | min(/macOS by Zabbix agent/vfs.fs.dependent.inode[{#FSNAME},pfree],5m)<{$VFS.FS.INODE.PFREE.MIN.CRIT:"{#FSNAME}"} | [{"tag": "scope", "value": "capacity"}, {"tag": "scope", "value": "performance"}] | no url |
| FS [{#FSNAME}]: Running out of free inodes | WARNING | Disk writing may fail if index nodes are exhausted, leading to error messages like "No space left on device" or "Disk is full", despite available free space. | min(/macOS by Zabbix agent/vfs.fs.dependent.inode[{#FSNAME},pfree],5m)<{$VFS.FS.INODE.PFREE.MIN.WARN:"{#FSNAME}"} | [{"tag": "scope", "value": "capacity"}, {"tag": "scope", "value": "performance"}] | no url |
| FS [{#FSNAME}]: Space is critically low | AVERAGE | The volume's space usage exceeds the `{$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"}%` limit.<br>The trigger expression is based on the current used and maximum available spaces.<br>Event name represents the total volume space, which can differ from the maximum available space, depending on the filesystem type. | min(/macOS by Zabbix agent/vfs.fs.dependent.size[{#FSNAME},pused],5m)>{$VFS.FS.PUSED.MAX.CRIT:"{#FSNAME}"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "capacity"}] | no url |
| FS [{#FSNAME}]: Space is low | WARNING | The volume's space usage exceeds the `{$VFS.FS.PUSED.MAX.WARN:"{#FSNAME}"}%` limit.<br>The trigger expression is based on the current used and maximum available spaces.<br>Event name represents the total volume space, which can differ from the maximum available space, depending on the filesystem type. | min(/macOS by Zabbix agent/vfs.fs.dependent.size[{#FSNAME},pused],5m)>{$VFS.FS.PUSED.MAX.WARN:"{#FSNAME}"} | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "capacity"}] | no url |

# Oracle by ODBC template description

1. Create an Oracle user for monitoring.

2. Set the hostname or IP address of the Oracle DB instance, user name and password in host macros ({$ORACLE.HOST}, {$ORACLE.USER} and {$ORACLE.PASSWORD}).
  Do not forget to install the Microsoft ODBC driver on the Zabbix server or the Zabbix proxy.
  See Oracle documentation for instructions: https://www.oracle.com/database/technologies/releasenote-odbc-ic.html.

  Note! Credentials in the odbc.ini do not work for Oracle.
  Note! Be sure that ODBC connects to Oracle with session parameter NLS_NUMERIC_CHARACTERS= '.,' It is important for correct display float numbers in Zabbix.
The "Service's TCP port state" item uses {$ORACLE.HOST} and {$ORACLE.PORT} macros to check the availability of the listener.

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Archive log discovery ](#discovery_archive_log_discovery)
  * [Discovery ASM disk groups discovery ](#discovery_asm_disk_groups_discovery)
  * [Discovery Database discovery ](#discovery_database_discovery)
  * [Discovery PDB discovery ](#discovery_pdb_discovery)
  * [Discovery Tablespace discovery ](#discovery_tablespace_discovery)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Get archive log | Gets the destinations of the log archive. | db.odbc.get[get_archivelog,,"Driver={$ORACLE.DRIVER};DBQ=//{$ORACLE.HOST}:{$ORACLE.PORT}/{$ORACLE.SERVICE};"] | ODBC | 1h |
| Get ASM disk groups | Gets the ASM disk groups. | db.odbc.get[get_asm,,"Driver={$ORACLE.DRIVER};DBQ=//{$ORACLE.HOST}:{$ORACLE.PORT}/{$ORACLE.SERVICE};"] | ODBC | 1h |
| Get database | Gets the databases in the database management system (DBMS). | db.odbc.get[get_db,,"Driver={$ORACLE.DRIVER};DBQ=//{$ORACLE.HOST}:{$ORACLE.PORT}/{$ORACLE.SERVICE};"] | ODBC | 1h |
| Get instance state | Gets the state of the current instance. | db.odbc.get[get_instance_state,,"Driver={$ORACLE.DRIVER};DBQ=//{$ORACLE.HOST}:{$ORACLE.PORT}/{$ORACLE.SERVICE};"] | ODBC | no delay |
| Get PDB | Gets the pluggable database (PDB) in DBMS. | db.odbc.get[get_pdb,,"Driver={$ORACLE.DRIVER};DBQ=//{$ORACLE.HOST}:{$ORACLE.PORT}/{$ORACLE.SERVICE};"] | ODBC | 1h |
| Get system metrics | Gets the values of the system metrics. | db.odbc.get[get_system_metrics,,"Driver={$ORACLE.DRIVER};DBQ=//{$ORACLE.HOST}:{$ORACLE.PORT}/{$ORACLE.SERVICE};"] | ODBC | 0;m0-59 |
| Get tablespace | Gets tablespaces in DBMS. | db.odbc.get[get_tablespace,,"Driver={$ORACLE.DRIVER};DBQ=//{$ORACLE.HOST}:{$ORACLE.PORT}/{$ORACLE.SERVICE};"] | ODBC | 1h |
| Service's TCP port state | Checks the availability of Oracle on the TCP port. | net.tcp.service[tcp,{$ORACLE.HOST},{$ORACLE.PORT}] | no type | 30s |
| Active parallel sessions | The number of active parallel sessions. | oracle.active_parallel_sessions | DEPENDENT | 0 |
| Active serial sessions | The number of active serial sessions. | oracle.active_serial_sessions | DEPENDENT | 0 |
| Average active sessions | The average number of active sessions at a point in time that are either working or waiting. | oracle.active_sessions | DEPENDENT | 0 |
| Archiver state | The status of automatic archiving. | oracle.archiver_state | DEPENDENT | 0 |
| Buffer cache hit ratio | The ratio of buffer cache hits ((LogRead - PhyRead)/LogRead). | oracle.buffer_cache_hit_ratio | DEPENDENT | 0 |
| Global cache blocks corrupted | The number of blocks that encountered corruption or checksum failure during the interconnect. | oracle.cache_blocks_corrupt | DEPENDENT | 0 |
| Global cache blocks lost | The number of lost global cache blocks. | oracle.cache_blocks_lost | DEPENDENT | 0 |
| Cursor cache hit ratio | The ratio of cursor cache hits (CursorCacheHit/SoftParse). | oracle.cursor_cache_hit_ratio | DEPENDENT | 0 |
| Database CPU time ratio | The ratio calculated by dividing the total CPU (used by the database) by the Oracle time model statistic DB time. | oracle.database_cpu_time_ratio | DEPENDENT | 0 |
| Database wait time ratio | Wait time - the time that the server process spends waiting for available shared resources to be released by other server processes such as latches, locks, data buffers, etc. | oracle.database_wait_time_ratio | DEPENDENT | 0 |
| Datafiles count | The current number of datafiles. | oracle.db_files_count | DEPENDENT | 0 |
| Datafiles limit | The maximum allowable number of datafiles. | oracle.db_files_limit | DEPENDENT | 0 |
| Disk sort per second | The number of sorts going to disk per second. | oracle.disk_sorts | DEPENDENT | 0 |
| Enqueue timeouts per second | Enqueue timeouts per second. | oracle.enqueue_timeouts_rate | DEPENDENT | 0 |
| FRA, Number of files | The number of files in the FRA. | oracle.fra_number_of_files | DEPENDENT | 0 |
| FRA, Number of restore points | Number of restore points in the FRA. | oracle.fra_restore_point | DEPENDENT | 0 |
| FRA, Space limit | The maximum amount of disk space (in bytes) that the database can use for the Fast Recovery Area (FRA). | oracle.fra_space_limit | DEPENDENT | 0 |
| FRA, Space reclaimable | The total amount of disk space (in bytes) that can be created by deleting obsolete, redundant, and other low-priority files from the FRA. | oracle.fra_space_reclaimable | DEPENDENT | 0 |
| FRA, Used space | The amount of disk space (in bytes) used by FRA files created in the current and all the previous FRAs. | oracle.fra_space_used | DEPENDENT | 0 |
| FRA, Usable space in % | Percentage of space usable in the FRA. | oracle.fra_usable_pct | DEPENDENT | 0 |
| GC CR block received per second | The global cache (GC) and the consistent read (CR) block received per second. | oracle.gc_cr_block_received_rate | DEPENDENT | 0 |
| Instance role | Indicates whether the instance is an active instance or an inactive secondary instance. | oracle.instance.role | DEPENDENT | 0 |
| Instance hostname | The name of the host machine. | oracle.instance_hostname | DEPENDENT | 0 |
| Instance name | The name of the instance. | oracle.instance_name | DEPENDENT | 0 |
| Instance status | The status of the instance. | oracle.instance_status | DEPENDENT | 0 |
| Library cache hit ratio | The ratio of library cache hits (Hits/Pins). | oracle.library_cache_hit_ratio | DEPENDENT | 0 |
| Logons per second | The number of logon attempts. | oracle.logons_rate | DEPENDENT | 0 |
| Long table scans per second | The number of long table scans per second. A table is considered long if it is not cached and if its high water mark is greater than five blocks. | oracle.long_table_scans_rate | DEPENDENT | 0 |
| Memory sorts ratio | The percentage of sorts (from `ORDER BY` clauses or index building) that are done to disk vs. in-memory. | oracle.memory_sorts_ratio | DEPENDENT | 0 |
| PGA, Global memory bound | The maximum size of a work area executed in automatic mode. | oracle.pga_global_bound | DEPENDENT | 0 |
| PGA, Aggregate target parameter | The current value of the `PGA_AGGREGATE_TARGET` initialization parameter. If this parameter is not set, then its value is "0" and automatic management of the PGA memory is disabled. | oracle.pga_target | DEPENDENT | 0 |
| Physical reads per second | Reads per second. | oracle.physical_reads_rate | DEPENDENT | 0 |
| Physical reads bytes per second | Read bytes per second. | oracle.physical_read_bytes_rate | DEPENDENT | 0 |
| Physical writes per second | Writes per second. | oracle.physical_writes_rate | DEPENDENT | 0 |
| Physical writes bytes per second | Write bytes per second. | oracle.physical_write_bytes_rate | DEPENDENT | 0 |
| Number of processes | The current number of user processes. | oracle.processes_count | DEPENDENT | 0 |
| Processes limit | The maximum number of user processes. | oracle.processes_limit | DEPENDENT | 0 |
| Redo logs available to switch | The number of inactive/unused redo logs available for log switching. | oracle.redo_logs_available | DEPENDENT | 0 |
| Rows per sort | The average number of rows per sort for all types of sorts performed. | oracle.rows_per_sort | DEPENDENT | 0 |
| SQL service response time | The Structured Query Language (SQL) service response time expressed in seconds. | oracle.service_response_time | DEPENDENT | 0 |
| Active background sessions | The number of active background sessions. | oracle.session_active_background | DEPENDENT | 0 |
| Active user sessions | The number of active user sessions. | oracle.session_active_user | DEPENDENT | 0 |
| Sessions concurrency | The percentage of concurrency. Concurrency is a database behavior when different transactions request to change the same resource. In the case of modifying data transactions, it sequentially temporarily blocks the right to change the data, and the rest of the transactions wait for access. When the access to a resource is locked for a long time, the concurrency grows (like the transaction queue), often leaving an extremely negative impact on performance. A high contention value does not indicate the root cause of the problem, but is a signal to search for it. | oracle.session_concurrency_rate | DEPENDENT | 0 |
| Session count | The session count. | oracle.session_count | DEPENDENT | 0 |
| Inactive user sessions | The number of inactive user sessions. | oracle.session_inactive_user | DEPENDENT | 0 |
| Sessions limit | The user and system sessions. | oracle.session_limit | DEPENDENT | 0 |
| Sessions lock rate | The percentage of locked sessions. Locks are mechanisms that prevent destructive interaction between transactions accessing the same resource - either user objects, such as tables and rows or system objects not visible to users, such as shared data structures in memory and data dictionary rows. | oracle.session_lock_rate | DEPENDENT | 0 |
| Sessions locked over {$ORACLE.SESSION.LOCK.MAX.TIME}s | The count of the prolongedly locked sessions. (You can change the duration of the maximum session lock in seconds for a query using the `{$ORACLE.SESSION.LOCK.MAX.TIME}` macro. Default = 600 s). | oracle.session_long_time_locked | DEPENDENT | 0 |
| SGA, buffer cache | The size of standard block cache. | oracle.sga_buffer_cache | DEPENDENT | 0 |
| SGA, fixed | The fixed System Global Area (SGA) is an internal housekeeping area. | oracle.sga_fixed | DEPENDENT | 0 |
| SGA, java pool | The memory is allocated from the Java pool. | oracle.sga_java_pool | DEPENDENT | 0 |
| SGA, large pool | The memory is allocated from a large pool. | oracle.sga_large_pool | DEPENDENT | 0 |
| SGA, log buffer | The number of bytes allocated for the redo log buffer. | oracle.sga_log_buffer | DEPENDENT | 0 |
| SGA, shared pool | The memory is allocated from a shared pool. | oracle.sga_shared_pool | DEPENDENT | 0 |
| Shared pool free % | Free memory of a shared pool expressed in %. | oracle.shared_pool_free | DEPENDENT | 0 |
| Total sorts per user call | The total sorts per user call. | oracle.sorts_per_user_call | DEPENDENT | 0 |
| Temp space used | Used temporary space. | oracle.temp_space_used | DEPENDENT | 0 |
| PGA, Total allocated | The current amount of the PGA memory allocated by the instance. The Oracle Database attempts to keep this number below the value of the `PGA_AGGREGATE_TARGET` initialization parameter. However, it is possible for the PGA allocated to exceed that value by a small percentage and for a short period of time when the work area workload is increasing very rapidly or when `PGA_AGGREGATE_TARGET` is set to a small value. | oracle.total_pga_allocated | DEPENDENT | 0 |
| PGA, Total freeable | The number of bytes of the PGA memory in all processes that could be freed back to the OS. | oracle.total_pga_freeable | DEPENDENT | 0 |
| PGA, Total inuse | The amount of Program Global Area (PGA) memory currently consumed by work areas. This number can be used to determine how much memory is consumed by other consumers of the PGA memory (for example, PL/SQL or Java). | oracle.total_pga_used | DEPENDENT | 0 |
| Uptime | The Oracle instance uptime expressed in seconds. | oracle.uptime | DEPENDENT | 0 |
| User '{$ORACLE.USER}' expire password | The number of days before the Zabbix account password expires. | oracle.user_expire_password | DEPENDENT | 0 |
| User rollbacks per second | The number of times that users manually issued the `ROLLBACK` statement or an error occurred during the users' transactions. | oracle.user_rollbacks_rate | DEPENDENT | 0 |
| Version | The Oracle Server version. | oracle.version | DEPENDENT | 0 |
| Number of LISTENER processes | The number of running listener processes. | proc.num[,,,"tnslsnr LISTENER"] | no type | 30s |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$ORACLE.ASM.USED.PCT.MAX.HIGH} | 95 |
| {$ORACLE.ASM.USED.PCT.MAX.WARN} | 90 |
| {$ORACLE.CONCURRENCY.MAX.WARN} | 80 |
| {$ORACLE.DB.FILE.MAX.WARN} | 80 |
| {$ORACLE.DBNAME.MATCHES} | .* |
| {$ORACLE.DBNAME.NOT_MATCHES} | PDB\$SEED |
| {$ORACLE.DRIVER} | <Put path to oracle driver here> |
| {$ORACLE.EXPIRE.PASSWORD.MIN.WARN} | 7 |
| {$ORACLE.HOST} | <Put oracle host here> |
| {$ORACLE.PASSWORD} | <Put your password here> |
| {$ORACLE.PGA.USE.MAX.WARN} | 90 |
| {$ORACLE.PORT} | 1521 |
| {$ORACLE.PROCESSES.MAX.WARN} | 80 |
| {$ORACLE.REDO.MIN.WARN} | 3 |
| {$ORACLE.SERVICE} | <Put oracle service name here> |
| {$ORACLE.SESSION.LOCK.MAX.TIME} | 600 |
| {$ORACLE.SESSION.LONG.LOCK.MAX.WARN} | 3 |
| {$ORACLE.SESSIONS.LOCK.MAX.WARN} | 20 |
| {$ORACLE.SESSIONS.MAX.WARN} | 80 |
| {$ORACLE.SHARED.FREE.MIN.WARN} | 5 |
| {$ORACLE.TABLESPACE.CONTAINER.MATCHES} | .* |
| {$ORACLE.TABLESPACE.CONTAINER.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$ORACLE.TABLESPACE.NAME.MATCHES} | .* |
| {$ORACLE.TABLESPACE.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$ORACLE.TBS.USED.PCT.FROM.MAX.HIGH} | 95 |
| {$ORACLE.TBS.USED.PCT.FROM.MAX.WARN} | 90 |
| {$ORACLE.TBS.USED.PCT.MAX.HIGH} | 95 |
| {$ORACLE.TBS.USED.PCT.MAX.WARN} | 90 |
| {$ORACLE.TBS.UTIL.PCT.MAX.HIGH} | 90 |
| {$ORACLE.TBS.UTIL.PCT.MAX.WARN} | 80 |
| {$ORACLE.USER} | <Put your username here> |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Instance hostname has changed | INFO | An Oracle Database instance hostname has changed. Acknowledge to close the problem manually. | last(/Oracle by ODBC/oracle.instance_hostname,#1)<>last(/Oracle by ODBC/oracle.instance_hostname,#2) and length(last(/Oracle by ODBC/oracle.instance_hostname))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Instance name has changed | INFO | An Oracle Database instance name has changed. Acknowledge to close the problem manually. | last(/Oracle by ODBC/oracle.instance_name,#1)<>last(/Oracle by ODBC/oracle.instance_name,#2) and length(last(/Oracle by ODBC/oracle.instance_name))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Number of REDO logs available for switching is too low | WARNING | The number of inactive/unused redos available for log switching is low (risk of database downtime). | max(/Oracle by ODBC/oracle.redo_logs_available,5m) < {$ORACLE.REDO.MIN.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |
| Too high database concurrency | WARNING | The concurrency rate exceeds `{$ORACLE.CONCURRENCY.MAX.WARN}`%. A high contention value does not indicate the root cause of the problem, but is a signal to review resource consumption (determine the "heaviest" queries in the database, trace sessions, etc.) This will help find the root cause and possible optimization points both in database configuration and the logic of building queries. | min(/Oracle by ODBC/oracle.session_concurrency_rate,5m) > {$ORACLE.CONCURRENCY.MAX.WARN} | [{"tag": "scope", "value": "performance"}] | no url |
| Too many locked sessions | WARNING | The number of locked sessions exceeds `{$ORACLE.SESSIONS.LOCK.MAX.WARN}`% of the running sessions. | min(/Oracle by ODBC/oracle.session_lock_rate,5m) > {$ORACLE.SESSIONS.LOCK.MAX.WARN} | [{"tag": "scope", "value": "performance"}] | no url |
| Too many sessions locked | WARNING | The number of locked sessions exceeding `{$ORACLE.SESSION.LOCK.MAX.TIME}` seconds is too high. Long-term locks can negatively affect the database performance. Therefore, if they are detected, you should first find the most difficult queries from the database point of view and then analyze possible resource leaks. | min(/Oracle by ODBC/oracle.session_long_time_locked,5m) > {$ORACLE.SESSION.LONG.LOCK.MAX.WARN} | [{"tag": "scope", "value": "performance"}] | no url |
| Shared pool free is too low | WARNING | The free memory percent of the shared pool has been less than `{$ORACLE.SHARED.FREE.MIN.WARN}`% for the last 5 minutes. | max(/Oracle by ODBC/oracle.shared_pool_free,5m)<{$ORACLE.SHARED.FREE.MIN.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |
| Failed to fetch info data | WARNING | Zabbix has not received any data for the items for the last 5 minutes. The database might be unavailable for connecting. | nodata(/Oracle by ODBC/oracle.uptime,5m)=1 | [{"tag": "scope", "value": "availability"}] | no url |
| Host has been restarted | INFO | Uptime is less than 10 minutes. | last(/Oracle by ODBC/oracle.uptime)<10m | [{"tag": "scope", "value": "notice"}] | no url |
| Zabbix account will expire soon | WARNING | The password for the Zabbix user in the database expires soon. | last(/Oracle by ODBC/oracle.user_expire_password)  < {$ORACLE.EXPIRE.PASSWORD.MIN.WARN} | [{"tag": "scope", "value": "notice"}] | no url |
| Version has changed | INFO | The Oracle Database version has changed. Acknowledge to close the problem manually. | last(/Oracle by ODBC/oracle.version,#1)<>last(/Oracle by ODBC/oracle.version,#2) and length(last(/Oracle by ODBC/oracle.version))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| LISTENER process is not running | DISASTER | The Oracle listener process is not running. | max(/Oracle by ODBC/proc.num[,,,"tnslsnr LISTENER"],#3)=0 | [{"tag": "scope", "value": "availability"}] | no url |
| Port {$ORACLE.PORT} is unavailable | DISASTER | The TCP port of the Oracle Server service is currently unavailable. | max(/Oracle by ODBC/net.tcp.service[tcp,{$ORACLE.HOST},{$ORACLE.PORT}],#3)=0  and max(/Oracle by ODBC/proc.num[,,,"tnslsnr LISTENER"],#3)>0 | [{"tag": "scope", "value": "availability"}] | no url |
| Too many active processes | WARNING | Active processes are using more than `{$ORACLE.PROCESSES.MAX.WARN}`% of the available number of processes. | min(/Oracle by ODBC/oracle.processes_count,5m) * 100 / last(/Oracle by ODBC/oracle.processes_limit) > {$ORACLE.PROCESSES.MAX.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |
| Too many active sessions | WARNING | Active sessions are using more than `{$ORACLE.SESSIONS.MAX.WARN}`% of the available sessions. | min(/Oracle by ODBC/oracle.session_count,5m) * 100 / last(/Oracle by ODBC/oracle.session_limit) > {$ORACLE.SESSIONS.MAX.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |
| Too many database files | WARNING | The number of datafiles is higher than `{$ORACLE.DB.FILE.MAX.WARN}`% of the available datafile limit. | min(/Oracle by ODBC/oracle.db_files_count,5m) * 100 / last(/Oracle by ODBC/oracle.db_files_limit) > {$ORACLE.DB.FILE.MAX.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |
| Total PGA inuse is too high | WARNING | The total PGA currently consumed by work areas is more than `{$ORACLE.PGA.USE.MAX.WARN}`% of `PGA_AGGREGATE_TARGET`. | min(/Oracle by ODBC/oracle.total_pga_used,5m) * 100 / last(/Oracle by ODBC/oracle.pga_target) > {$ORACLE.PGA.USE.MAX.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |


<a name="discoveries" />

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Archive log discovery | oracle.archivelog.discovery | Used for the discovery of the log archive. | DEPENDENT | no lifetime | 0 |
| ASM disk groups discovery | oracle.asm.discovery | Used for discovering the ASM disk groups. | DEPENDENT | no lifetime | 0 |
| Database discovery | oracle.db.discovery | Used for database discovery. | DEPENDENT | no lifetime | 0 |
| PDB discovery | oracle.pdb.discovery | Used for the discovery of the pluggable database (PDB). | DEPENDENT | no lifetime | 0 |
| Tablespace discovery | oracle.tablespace.discovery | Used for the discovery of tablespaces in DBMS. | DEPENDENT | no lifetime | 0 |


<a name="discovery_archive_log_discovery" />

## Discovery Archive log discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Archivelog '{#DEST_NAME}': Get archive log info | Gets the archive log statistics. | db.odbc.get[get_archivelog_{#DEST_NAME}_stat,,"Driver={$ORACLE.DRIVER};DBQ=//{$ORACLE.HOST}:{$ORACLE.PORT}/{$ORACLE.SERVICE};"] | ODBC |
| Archivelog '{#DEST_NAME}': Error | Displays the error message. | oracle.archivelog_error["{#DEST_NAME}"] | DEPENDENT |
| Archivelog '{#DEST_NAME}': Last sequence | Identifies the sequence number of the last archived redo log to be archived. | oracle.archivelog_log_sequence["{#DEST_NAME}"] | DEPENDENT |
| Archivelog '{#DEST_NAME}': Status | Identifies the current status of the destination where:<br>1 - VALID;<br>2 - DEFERRED;<br>3 - ERROR;<br>0 - UNKNOWN. | oracle.archivelog_log_status["{#DEST_NAME}"] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Archivelog '{#DEST_NAME}': Log Archive is not valid | HIGH | The trigger will launch if the archive log destination is not in one of these states:<br>2 - DEFERRED;<br>3 - VALID. | last(/Oracle by ODBC/oracle.archivelog_log_status["{#DEST_NAME}"])<2 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discovery_asm_disk_groups_discovery" />

## Discovery ASM disk groups discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| ASM '{#DGNAME}': Get ASM stats | Gets the ASM disk group statistics. | db.odbc.get[get_asm_{#DGNAME}_stat,,"Driver={$ORACLE.DRIVER};DBQ=//{$ORACLE.HOST}:{$ORACLE.PORT}/{$ORACLE.SERVICE};"] | ODBC |
| ASM '{#DGNAME}': Free size | The free size of the ASM disk group. | oracle.asm_free_size["{#DGNAME}"] | DEPENDENT |
| ASM '{#DGNAME}': Total size | The total size of the ASM disk group. | oracle.asm_total_size["{#DGNAME}"] | DEPENDENT |
| ASM '{#DGNAME}': Used size, percent | Usage of the ASM disk group expressed in %. | oracle.asm_used_pct["{#DGNAME}"] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| ASM '{#DGNAME}': Disk group usage is too high | HIGH | The usage of the ASM disk group expressed in % exceeds `{$ORACLE.ASM.USED.PCT.MAX.WARN}`. | min(/Oracle by ODBC/oracle.asm_used_pct["{#DGNAME}"],5m)>{$ORACLE.ASM.USED.PCT.MAX.HIGH} | [{"tag": "scope", "value": "capacity"}] | no url |
| ASM '{#DGNAME}': Disk group usage is too high | WARNING | The usage of the ASM disk group expressed in % exceeds `{$ORACLE.ASM.USED.PCT.MAX.WARN}`. | min(/Oracle by ODBC/oracle.asm_used_pct["{#DGNAME}"],5m)>{$ORACLE.ASM.USED.PCT.MAX.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |


<a name="discovery_database_discovery" />

## Discovery Database discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Oracle Database '{#DBNAME}': Get CDB and No-CDB info | Gets the information about the CDB and non-CDB database on an instance. | db.odbc.get[get_cdb_{#DBNAME}_info,,"Driver={$ORACLE.DRIVER};DBQ=//{$ORACLE.HOST}:{$ORACLE.PORT}/{$ORACLE.SERVICE};"] | ODBC |
| Oracle Database '{#DBNAME}': Force logging | Indicates whether the database is under force logging mode (`YES`/`NO`). | oracle.db_force_logging["{#DBNAME}"] | DEPENDENT |
| Oracle Database '{#DBNAME}': Log mode | The archive log mode where:<br>0 - NOARCHIVELOG;<br>1 - ARCHIVELOG;<br>2 - MANUAL. | oracle.db_log_mode["{#DBNAME}"] | DEPENDENT |
| Oracle Database '{#DBNAME}': Open status | 1 - MOUNTED;<br>2 - READ WRITE;<br>3 - READ ONLY;<br>4 - READ ONLY WITH APPLY (a physical standby database is open in real-time query mode). | oracle.db_open_mode["{#DBNAME}"] | DEPENDENT |
| Oracle Database '{#DBNAME}': Role | The current role of the database where:<br>1 - SNAPSHOT STANDBY;<br>2 - LOGICAL STANDBY;<br>3 - PHYSICAL STANDBY;<br>4 - PRIMARY;<br>5 - FAR SYNC. | oracle.db_role["{#DBNAME}"] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Oracle Database '{#DBNAME}': Open status has changed | INFO | The Oracle Database open status has changed. Acknowledge to close the problem manually. | last(/Oracle by ODBC/oracle.db_open_mode["{#DBNAME}"],#1)<>last(/Oracle by ODBC/oracle.db_open_mode["{#DBNAME}"],#2) | [{"tag": "scope", "value": "notice"}] | no url |
| Oracle Database '{#DBNAME}': Open status in mount mode | WARNING | The Oracle Database is in a mounted state. | last(/Oracle by ODBC/oracle.db_open_mode["{#DBNAME}"])=1 | [{"tag": "scope", "value": "notice"}] | no url |
| Oracle Database '{#DBNAME}': Role has changed | INFO | The Oracle Database role has changed. Acknowledge to close the problem manually. | last(/Oracle by ODBC/oracle.db_role["{#DBNAME}"],#1)<>last(/Oracle by ODBC/oracle.db_role["{#DBNAME}"],#2) | [{"tag": "scope", "value": "notice"}] | no url |
| Oracle Database '{#DBNAME}': Force logging is deactivated for DB with active Archivelog | WARNING | Force logging mode is a very important metric for databases in `ARCHIVELOG`. This feature allows to forcibly write all the transactions to the redo log. | last(/Oracle by ODBC/oracle.db_force_logging["{#DBNAME}"]) = 0 and last(/Oracle by ODBC/oracle.db_log_mode["{#DBNAME}"]) = 1 | [{"tag": "scope", "value": "performance"}] | no url |


<a name="discovery_pdb_discovery" />

## Discovery PDB discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Oracle Database '{#DBNAME}': Get PDB info | Gets the information about the PDB database on an instance. | db.odbc.get[get_pdb_{#DBNAME}_info,,"Driver={$ORACLE.DRIVER};DBQ=//{$ORACLE.HOST}:{$ORACLE.PORT}/{$ORACLE.SERVICE};"] | ODBC |
| Oracle Database '{#DBNAME}': Open status | 1 - MOUNTED;<br>2 - READ WRITE;<br>3 - READ ONLY;<br>4 - READ ONLY WITH APPLY (a physical standby database is open in real-time query mode). | oracle.pdb_open_mode["{#DBNAME}"] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Oracle Database '{#DBNAME}': Open status has changed | INFO | The Oracle Database open status has changed. Acknowledge to close the problem manually. | last(/Oracle by ODBC/oracle.pdb_open_mode["{#DBNAME}"],#1)<>last(/Oracle by ODBC/oracle.pdb_open_mode["{#DBNAME}"],#2) | [{"tag": "scope", "value": "notice"}] | no url |
| Oracle Database '{#DBNAME}': Open status in mount mode | WARNING | The Oracle Database is in a mounted state. | last(/Oracle by ODBC/oracle.pdb_open_mode["{#DBNAME}"])=1 | [{"tag": "scope", "value": "notice"}] | no url |


<a name="discovery_tablespace_discovery" />

## Discovery Tablespace discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Get tablespaces stats | Gets the statistics of the tablespace. | db.odbc.get[get_{#CON_NAME}_tablespace_{#TABLESPACE}_stats,,"Driver={$ORACLE.DRIVER};DBQ=//{$ORACLE.HOST}:{$ORACLE.PORT}/{$ORACLE.SERVICE};"] | ODBC |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Tablespace allocated, bytes | Currently allocated bytes for the tablespace (sum of the current size of datafiles). | oracle.tbs_alloc_bytes["{#CON_NAME}","{#TABLESPACE}"] | DEPENDENT |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Tablespace free, bytes | Free bytes of the allocated space. | oracle.tbs_free_bytes["{#CON_NAME}","{#TABLESPACE}"] | DEPENDENT |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Tablespace MAX size, bytes | The maximum size of the tablespace. | oracle.tbs_max_bytes["{#CON_NAME}","{#TABLESPACE}"] | DEPENDENT |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Open status | The tablespace status where:<br>1 - ONLINE;<br>2 - OFFLINE;<br>3 - READ ONLY. | oracle.tbs_status["{#CON_NAME}","{#TABLESPACE}"] | DEPENDENT |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Tablespace used, bytes | Currently used bytes for the tablespace (current size of datafiles minus the free space). | oracle.tbs_used_bytes["{#CON_NAME}","{#TABLESPACE}"] | DEPENDENT |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Tablespace usage, percent | Used bytes/allocated bytes*100. | oracle.tbs_used_file_pct["{#CON_NAME}","{#TABLESPACE}"] | DEPENDENT |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Tablespace usage from MAX, percent | Used bytes/max bytes*100. | oracle.tbs_used_from_max_pct["{#CON_NAME}","{#TABLESPACE}"] | DEPENDENT |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Tablespace allocated, percent | Allocated bytes/max bytes*100. | oracle.tbs_used_pct["{#CON_NAME}","{#TABLESPACE}"] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Tablespace is OFFLINE | WARNING | The tablespace is in the offline state. | last(/Oracle by ODBC/oracle.tbs_status["{#CON_NAME}","{#TABLESPACE}"])=2 | [{"tag": "scope", "value": "availability"}] | no url |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Tablespace status has changed | INFO | Oracle tablespace status has changed. Acknowledge to close the problem manually. | last(/Oracle by ODBC/oracle.tbs_status["{#CON_NAME}","{#TABLESPACE}"],#1)<>last(/Oracle by ODBC/oracle.tbs_status["{#CON_NAME}","{#TABLESPACE}"],#2) | [{"tag": "scope", "value": "capacity"}] | no url |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Tablespace usage is too high | HIGH | The usage of the tablespace `{#TABLESPACE}` exceeds `{$ORACLE.TBS.USED.PCT.MAX.HIGH}`% | min(/Oracle by ODBC/oracle.tbs_used_file_pct["{#CON_NAME}","{#TABLESPACE}"],5m)>{$ORACLE.TBS.USED.PCT.MAX.HIGH} | [{"tag": "scope", "value": "capacity"}] | no url |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Tablespace usage is too high | WARNING | The usage of the tablespace `{#TABLESPACE}` exceeds `{$ORACLE.TBS.USED.PCT.MAX.WARN}`% | min(/Oracle by ODBC/oracle.tbs_used_file_pct["{#CON_NAME}","{#TABLESPACE}"],5m)>{$ORACLE.TBS.USED.PCT.MAX.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Tablespace usage from MAX is too high | HIGH | The usage of the tablespace `{#TABLESPACE}` from MAX exceeds `{$ORACLE.TBS.USED.PCT.FROM.MAX.HIGH}`% | min(/Oracle by ODBC/oracle.tbs_used_from_max_pct["{#CON_NAME}","{#TABLESPACE}"],5m)>{$ORACLE.TBS.USED.PCT.FROM.MAX.HIGH} | [{"tag": "scope", "value": "capacity"}] | no url |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Tablespace usage from MAX is too high | WARNING | The usage of the tablespace `{#TABLESPACE}` from MAX exceeds `{$ORACLE.TBS.USED.PCT.FROM.MAX.WARN}`% | min(/Oracle by ODBC/oracle.tbs_used_from_max_pct["{#CON_NAME}","{#TABLESPACE}"],5m)>{$ORACLE.TBS.USED.PCT.FROM.MAX.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Tablespace utilization is too high | HIGH | The utilization of the tablespace `{#TABLESPACE}` exceeds `{$ORACLE.TBS.UTIL.PCT.MAX.HIGH}`% | min(/Oracle by ODBC/oracle.tbs_used_pct["{#CON_NAME}","{#TABLESPACE}"],5m)>{$ORACLE.TBS.UTIL.PCT.MAX.HIGH} | [{"tag": "scope", "value": "capacity"}] | no url |
| Oracle '{#CON_NAME}' TBS '{#TABLESPACE}': Tablespace utilization is too high | WARNING | The utilization of the tablespace `{#TABLESPACE}` exceeds `{$ORACLE.TBS.UTIL.PCT.MAX.WARN}`% | min(/Oracle by ODBC/oracle.tbs_used_pct["{#CON_NAME}","{#TABLESPACE}"],5m)>{$ORACLE.TBS.UTIL.PCT.MAX.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |

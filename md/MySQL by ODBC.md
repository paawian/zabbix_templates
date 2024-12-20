# MySQL by ODBC template description

Requirements for template operation:
1. Create a MySQL user for monitoring. For example:
CREATE USER 'zbx_monitor'@'%' IDENTIFIED BY '<password>';
GRANT REPLICATION CLIENT,PROCESS,SHOW DATABASES,SHOW VIEW ON *.* TO 'zbx_monitor'@'%';
For more information read the MYSQL documentation https://dev.mysql.com/doc/refman/8.0/en/grant.html , please.
2. Set the user name and password in the host macros ({$MYSQL.USER} and {$MYSQL.PASSWORD}).

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/384189-discussion-thread-for-official-zabbix-template-db-mysql

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Database discovery ](#discovery_database_discovery)
  * [Discovery MariaDB discovery ](#discovery_mariadb_discovery)
  * [Discovery Replication discovery ](#discovery_replication_discovery)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Get database | Used for scanning databases in DBMS. | db.odbc.get[get_database,"{$MYSQL.DSN}"] | ODBC | 1h |
| Get replication | Gets replication status information. | db.odbc.get[get_replication,"{$MYSQL.DSN}"] | ODBC | no delay |
| Get status variables | Gets server global status information. | db.odbc.get[get_status_variables,"{$MYSQL.DSN}"] | ODBC | no delay |
| Status | MySQL server status. | db.odbc.select[ping,"{$MYSQL.DSN}"] | ODBC | no delay |
| Version | MySQL server version. | db.odbc.select[version,"{$MYSQL.DSN}"] | ODBC | 15m |
| Aborted clients per second | Number of connections that were aborted because the client died without closing the connection properly. | mysql.aborted_clients.rate | DEPENDENT | 0 |
| Aborted connections per second | Number of failed attempts to connect to the MySQL server. | mysql.aborted_connects.rate | DEPENDENT | 0 |
| Binlog cache disk use | Number of transactions that used a temporary disk cache because they could not fit in the regular binary log cache, being larger than `binlog_cache_size`. | mysql.binlog_cache_disk_use | DEPENDENT | 0 |
| Buffer pool efficiency | The item shows how effectively the buffer pool is serving reads. | mysql.buffer_pool_efficiency | CALCULATED | no delay |
| Buffer pool utilization | Ratio of used to total pages in the buffer pool. | mysql.buffer_pool_utilization | CALCULATED | no delay |
| Bytes received | Number of bytes received from all clients. | mysql.bytes_received.rate | DEPENDENT | 0 |
| Bytes sent | Number of bytes sent to all clients. | mysql.bytes_sent.rate | DEPENDENT | 0 |
| Command Delete per second | The `Com_delete` counter variable indicates the number of times the `DELETE` statement has been executed. | mysql.com_delete.rate | DEPENDENT | 0 |
| Command Insert per second | The `Com_insert` counter variable indicates the number of times the `INSERT` statement has been executed. | mysql.com_insert.rate | DEPENDENT | 0 |
| Command Select per second | The `Com_select` counter variable indicates the number of times the `SELECT` statement has been executed. | mysql.com_select.rate | DEPENDENT | 0 |
| Command Update per second | The `Com_update` counter variable indicates the number of times the `UPDATE` statement has been executed. | mysql.com_update.rate | DEPENDENT | 0 |
| Connections per second | Number of connection attempts (successful or not) to the MySQL server. | mysql.connections.rate | DEPENDENT | 0 |
| Connection errors accept per second | Number of errors that occurred during calls to `accept()` on the listening port. | mysql.connection_errors_accept.rate | DEPENDENT | 0 |
| Connection errors internal per second | Number of refused connections due to internal server errors, for example, out of memory errors, or failed thread starts. | mysql.connection_errors_internal.rate | DEPENDENT | 0 |
| Connection errors max connections per second | Number of refused connections due to the `max_connections` limit being reached. | mysql.connection_errors_max_connections.rate | DEPENDENT | 0 |
| Connection errors peer address per second | Number of errors while searching for the connecting client's IP address. | mysql.connection_errors_peer_address.rate | DEPENDENT | 0 |
| Connection errors select per second | Number of errors during calls to `select()` or `poll()` on the listening port. The client would not necessarily have been rejected in these cases. | mysql.connection_errors_select.rate | DEPENDENT | 0 |
| Connection errors tcpwrap per second | Number of connections the libwrap library has refused. | mysql.connection_errors_tcpwrap.rate | DEPENDENT | 0 |
| Created tmp tables on disk per second | Number of internal on-disk temporary tables created by the server while executing statements. | mysql.created_tmp_disk_tables.rate | DEPENDENT | 0 |
| Created tmp files on disk per second | How many temporary files `mysqld` has created. | mysql.created_tmp_files.rate | DEPENDENT | 0 |
| Created tmp tables on memory per second | Number of internal temporary tables created by the server while executing statements. | mysql.created_tmp_tables.rate | DEPENDENT | 0 |
| InnoDB buffer pool pages free | The total size of the InnoDB buffer pool, in pages. | mysql.innodb_buffer_pool_pages_free | DEPENDENT | 0 |
| InnoDB buffer pool pages total | The total size of the InnoDB buffer pool, in pages. | mysql.innodb_buffer_pool_pages_total | DEPENDENT | 0 |
| InnoDB buffer pool reads | Number of logical reads that InnoDB could not satisfy from the buffer pool and had to read directly from the disk. | mysql.innodb_buffer_pool_reads | DEPENDENT | 0 |
| InnoDB buffer pool reads per second | Number of logical reads per second that InnoDB could not satisfy from the buffer pool and had to read directly from the disk. | mysql.innodb_buffer_pool_reads.rate | DEPENDENT | 0 |
| InnoDB buffer pool read requests | Number of logical read requests. | mysql.innodb_buffer_pool_read_requests | DEPENDENT | 0 |
| InnoDB buffer pool read requests per second | Number of logical read requests per second. | mysql.innodb_buffer_pool_read_requests.rate | DEPENDENT | 0 |
| Innodb buffer pool wait free | Number of times InnoDB waited for a free page before reading or creating a page. Normally, writes to the InnoDB buffer pool happen in the background. When no clean pages are available, dirty pages are flushed first in order to free some up. This counts the numbers of wait for this operation to finish. If this value is not small, look at the increasing `innodb_buffer_pool_size`. | mysql.innodb_buffer_pool_wait_free | DEPENDENT | 0 |
| Calculated value of innodb_log_file_size | `Innodb_log_file_size` is calculated as: (`innodb_os_log_written`-`innodb_os_log_written`(time shift -1h))/`{$MYSQL.INNODB_LOG_FILES}`. `Innodb_log_file_size` is the size in bytes of the each InnoDB redo log file in the log group. The combined size can be no more than 512 GB. Larger values mean less disk I/O due to less flushing checkpoint activity, but also slower recovery from a crash. | mysql.innodb_log_file_size | CALCULATED | no delay |
| Innodb number open files | Number of open files held by InnoDB. InnoDB only. | mysql.innodb_num_open_files | DEPENDENT | 0 |
| Innodb log written | Number of bytes written to the InnoDB log. | mysql.innodb_os_log_written | DEPENDENT | 0 |
| InnoDB row lock time | The total time spent in acquiring row locks for InnoDB tables, in milliseconds. | mysql.innodb_row_lock_time | DEPENDENT | 0 |
| InnoDB row lock time max | The maximum time to acquire a row lock for InnoDB tables, in milliseconds. | mysql.innodb_row_lock_time_max | DEPENDENT | 0 |
| InnoDB row lock waits | Number of times operations on InnoDB tables had to wait for a row lock. | mysql.innodb_row_lock_waits | DEPENDENT | 0 |
| Max used connections | The maximum number of connections that have been in use simultaneously since the server start. | mysql.max_used_connections | DEPENDENT | 0 |
| Open tables | Number of tables that are open. | mysql.open_tables | DEPENDENT | 0 |
| Open table definitions | Number of cached table definitions. | mysql.open_table_definitions | DEPENDENT | 0 |
| Queries per second | Number of statements executed by the server. This variable includes statements executed within stored programs, unlike the `Questions` variable. | mysql.queries.rate | DEPENDENT | 0 |
| Questions per second | Number of statements executed by the server. This includes only statements sent to the server by clients and not statements executed within stored programs, unlike the `Queries` variable. | mysql.questions.rate | DEPENDENT | 0 |
| Slow queries per second | Number of queries that have taken more than `long_query_time` seconds. | mysql.slow_queries.rate | DEPENDENT | 0 |
| Threads cached | Number of threads in the thread cache. | mysql.threads_cached | DEPENDENT | 0 |
| Threads connected | Number of currently open connections. | mysql.threads_connected | DEPENDENT | 0 |
| Threads created per second | Number of threads created to handle connections. If the value of `Threads_created` is large, you may want to increase the `thread_cache_size` value. The cache miss rate can be calculated as `Threads_created`/`Connections`. | mysql.threads_created.rate | DEPENDENT | 0 |
| Threads running | Number of threads that are not sleeping. | mysql.threads_running | DEPENDENT | 0 |
| Uptime | Number of seconds that the server has been up. | mysql.uptime | DEPENDENT | 0 |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$MYSQL.ABORTED_CONN.MAX.WARN} | 3 |
| {$MYSQL.BUFF_UTIL.MIN.WARN} | 50 |
| {$MYSQL.CREATED_TMP_DISK_TABLES.MAX.WARN} | 10 |
| {$MYSQL.CREATED_TMP_FILES.MAX.WARN} | 10 |
| {$MYSQL.CREATED_TMP_TABLES.MAX.WARN} | 30 |
| {$MYSQL.DBNAME.MATCHES} | .+ |
| {$MYSQL.DBNAME.NOT_MATCHES} | information_schema |
| {$MYSQL.DSN} | <Put your DSN here> |
| {$MYSQL.INNODB_LOG_FILES} | 2 |
| {$MYSQL.PASSWORD} | <Put your password here> |
| {$MYSQL.REPL_LAG.MAX.WARN} | 30m |
| {$MYSQL.SLOW_QUERIES.MAX.WARN} | 3 |
| {$MYSQL.USER} | <Put your username here> |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Service is down | HIGH | MySQL is down. | last(/MySQL by ODBC/db.odbc.select[ping,"{$MYSQL.DSN}"])=0 | [{"tag": "scope", "value": "availability"}] | no url |
| Version has changed | INFO | The MySQL version has changed. Acknowledge to close the problem manually. | last(/MySQL by ODBC/db.odbc.select[version,"{$MYSQL.DSN}"],#1)<>last(/MySQL by ODBC/db.odbc.select[version,"{$MYSQL.DSN}"],#2) and length(last(/MySQL by ODBC/db.odbc.select[version,"{$MYSQL.DSN}"]))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Server has aborted connections | AVERAGE | The number of failed attempts to connect to the MySQL server is more than `{$MYSQL.ABORTED_CONN.MAX.WARN}` in the last 5 minutes. | min(/MySQL by ODBC/mysql.aborted_connects.rate,5m)>{$MYSQL.ABORTED_CONN.MAX.WARN} | [{"tag": "scope", "value": "availability"}] | no url |
| Buffer pool utilization is too low | WARNING | The buffer pool utilization is less than `{$MYSQL.BUFF_UTIL.MIN.WARN}`% in the last 5 minutes. This means that there is a lot of unused RAM allocated for the buffer pool, which you can easily reallocate at the moment. | max(/MySQL by ODBC/mysql.buffer_pool_utilization,5m)<{$MYSQL.BUFF_UTIL.MIN.WARN} | [{"tag": "scope", "value": "notice"}] | no url |
| Refused connections | AVERAGE | Number of refused connections due to the `max_connections` limit being reached. | last(/MySQL by ODBC/mysql.connection_errors_max_connections.rate)>0 | [{"tag": "scope", "value": "availability"}] | no url |
| Number of on-disk temporary tables created per second is high | WARNING | The application using the database may be in need of query optimization. | min(/MySQL by ODBC/mysql.created_tmp_disk_tables.rate,5m)>{$MYSQL.CREATED_TMP_DISK_TABLES.MAX.WARN} | [{"tag": "scope", "value": "performance"}] | no url |
| Number of temporary files created per second is high | WARNING | The application using the database may be in need of query optimization. | min(/MySQL by ODBC/mysql.created_tmp_files.rate,5m)>{$MYSQL.CREATED_TMP_FILES.MAX.WARN} | [{"tag": "scope", "value": "performance"}] | no url |
| Number of internal temporary tables created per second is high | WARNING | The application using the database may be in need of query optimization. | min(/MySQL by ODBC/mysql.created_tmp_tables.rate,5m)>{$MYSQL.CREATED_TMP_TABLES.MAX.WARN} | [{"tag": "scope", "value": "performance"}] | no url |
| Server has slow queries | WARNING | The number of slow queries is more than `{$MYSQL.SLOW_QUERIES.MAX.WARN}` in the last 5 minutes. | min(/MySQL by ODBC/mysql.slow_queries.rate,5m)>{$MYSQL.SLOW_QUERIES.MAX.WARN} | [{"tag": "scope", "value": "performance"}] | no url |
| Failed to fetch info data | INFO | Zabbix has not received any data for items for the last 30 minutes. | nodata(/MySQL by ODBC/mysql.uptime,30m)=1 | [{"tag": "scope", "value": "availability"}] | no url |
| Service has been restarted | INFO | MySQL uptime is less than 10 minutes. | last(/MySQL by ODBC/mysql.uptime)<10m | [{"tag": "scope", "value": "notice"}] | no url |


<a name="discoveries" />

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Database discovery | mysql.database.discovery | Used for the discovery of the databases. | DEPENDENT | no lifetime | 0 |
| MariaDB discovery | mysql.extra_metric.discovery | Used for additional metrics if MariaDB is used. | DEPENDENT | no lifetime | 0 |
| Replication discovery | mysql.replication.discovery | Discovery of the replication. | DEPENDENT | no lifetime | 0 |


<a name="discovery_database_discovery" />

## Discovery Database discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Size of database {#DATABASE} | Database size. | db.odbc.select[{#DATABASE}_size,"{$MYSQL.DSN}"] | ODBC |


<a name="discovery_mariadb_discovery" />

## Discovery MariaDB discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Binlog commits | Total number of transactions committed to the binary log. | mysql.binlog_commits[{#SINGLETON}] | DEPENDENT |
| Binlog group commits | Total number of group commits done to the binary log. | mysql.binlog_group_commits[{#SINGLETON}] | DEPENDENT |
| Master GTID wait count | The number of times `MASTER_GTID_WAIT` called. | mysql.master_gtid_wait_count[{#SINGLETON}] | DEPENDENT |
| Master GTID wait timeouts | Number of timeouts occurring in `MASTER_GTID_WAIT`. | mysql.master_gtid_wait_timeouts[{#SINGLETON}] | DEPENDENT |
| Master GTID wait time | Total number of time spent in `MASTER_GTID_WAIT`. | mysql.master_gtid_wait_time[{#SINGLETON}] | DEPENDENT |


<a name="discovery_replication_discovery" />

## Discovery Replication discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Replication Seconds Behind Master {#MASTER_HOST} | The number of seconds the slave SQL thread has been behind processing the master binary log. A high number (or an increasing one) can indicate that the slave is unable to handle events from the master in a timely fashion. | mysql.seconds_behind_master["{#MASTER_HOST}"] | DEPENDENT |
| Replication Slave IO Running {#MASTER_HOST} | Whether the I/O thread for reading the master's binary log is running. Normally, you want this to be `Yes` unless you have not yet started a replication or have explicitly stopped it with `STOP SLAVE`. | mysql.slave_io_running["{#MASTER_HOST}"] | DEPENDENT |
| Replication Slave SQL Running {#MASTER_HOST} | Whether the SQL thread for executing events in the relay log is running.<br>As with the I/O thread, this should normally be `Yes`. | mysql.slave_sql_running["{#MASTER_HOST}"] | DEPENDENT |
| Replication Slave SQL Running State {#MASTER_HOST} | Shows the state of the SQL driver threads. | mysql.slave_sql_running_state["{#MASTER_HOST}"] | DEPENDENT |
| Replication Slave status {#MASTER_HOST} | Gets status information on the essential parameters of the slave threads. | mysql.slave_status["{#MASTER_HOST}"] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Replication lag is too high | WARNING | Replication delay is too long. | min(/MySQL by ODBC/mysql.seconds_behind_master["{#MASTER_HOST}"],5m)>{$MYSQL.REPL_LAG.MAX.WARN} | [{"tag": "scope", "value": "notice"}] | no url |
| The slave I/O thread is not connected to a replication master | WARNING | Whether the slave I/O thread is connected to the master. | count(/MySQL by ODBC/mysql.slave_io_running["{#MASTER_HOST}"],#1,"ne","Yes")=1 | [{"tag": "scope", "value": "availability"}] | no url |
| The slave I/O thread is not running | AVERAGE | Whether the I/O thread for reading the master's binary log is running. | count(/MySQL by ODBC/mysql.slave_io_running["{#MASTER_HOST}"],#1,"eq","No")=1 | [{"tag": "scope", "value": "notice"}] | no url |
| The SQL thread is not running | WARNING | Whether the SQL thread for executing events in the relay log is running. | count(/MySQL by ODBC/mysql.slave_sql_running["{#MASTER_HOST}"],#1,"eq","No")=1 | [{"tag": "scope", "value": "notice"}] | no url |


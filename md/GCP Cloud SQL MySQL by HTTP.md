# GCP Cloud SQL MySQL by HTTP template description

Get GCP Cloud SQL MySQL instances monitoring with script item usage to perform HTTP requests to Google Cloud Platform Monitoring API.
This template will be automatically connected to discovered entities with all their required parameters pre-defined.

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback.


Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Reserved CPU cores | Number of cores reserved for the database. | gcp.cloudsql.mysql.cpu.reserved_cores | DEPENDENT | 0 |
| CPU usage time | Cumulative CPU usage time in seconds. | gcp.cloudsql.mysql.cpu.usage_time | DEPENDENT | 0 |
| CPU utilization | Current CPU utilization represented as a percentage of the reserved CPU that is currently in use. | gcp.cloudsql.mysql.cpu.utilization | DEPENDENT | 0 |
| DB engine state | GCP Cloud SQL MySQL DB Engine State. | gcp.cloudsql.mysql.db.state | HTTP_AGENT | no delay |
| Disk bytes used | Data utilization in bytes. | gcp.cloudsql.mysql.disk.bytes_used | DEPENDENT | 0 |
| Disk size | Maximum data disk size in bytes. | gcp.cloudsql.mysql.disk.quota | DEPENDENT | 0 |
| Disk read I/O | Delta count of data disk read I/O operations. | gcp.cloudsql.mysql.disk.read_ops_count | DEPENDENT | 0 |
| Disk utilization | The fraction of the disk quota that is currently in use. <br>Shown as percentage. | gcp.cloudsql.mysql.disk.utilization | DEPENDENT | 0 |
| Disk write I/O | Delta count of data disk write I/O operations. | gcp.cloudsql.mysql.disk.write_ops_count | DEPENDENT | 0 |
| InnoDB dirty pages | Number of unflushed pages in the InnoDB buffer pool. | gcp.cloudsql.mysql.innodb_buffer_pool_pages_dirty | DEPENDENT | 0 |
| InnoDB free pages | Number of unused pages in the InnoDB buffer pool. | gcp.cloudsql.mysql.innodb_buffer_pool_pages_free | DEPENDENT | 0 |
| InnoDB total pages | Total number of pages in the InnoDB buffer pool. | gcp.cloudsql.mysql.innodb_buffer_pool_pages_total | DEPENDENT | 0 |
| InnoDB fsync calls | Delta count of InnoDB fsync() calls. | gcp.cloudsql.mysql.innodb_data_fsyncs | DEPENDENT | 0 |
| InnoDB log fsync calls | Delta count of InnoDB fsync() calls to the log file. | gcp.cloudsql.mysql.innodb_os_log_fsyncs | DEPENDENT | 0 |
| InnoDB pages read | Delta count of InnoDB pages read. | gcp.cloudsql.mysql.innodb_pages_read | DEPENDENT | 0 |
| InnoDB pages written | Delta count of InnoDB pages written. | gcp.cloudsql.mysql.innodb_pages_written | DEPENDENT | 0 |
| Instance state | GCP Cloud SQL MySQL Current instance state. | gcp.cloudsql.mysql.inst.state | HTTP_AGENT | no delay |
| Memory size | Maximum RAM size in bytes. | gcp.cloudsql.mysql.memory.quota | DEPENDENT | 0 |
| Memory used by DB engine | Total RAM usage in bytes. <br>This metric reports the RAM usage of the database process, including the buffer/cache. | gcp.cloudsql.mysql.memory.total_usage | DEPENDENT | 0 |
| Memory usage | The RAM usage in bytes. <br>This metric reports the RAM usage of the server, excluding the buffer/cache. | gcp.cloudsql.mysql.memory.usage | DEPENDENT | 0 |
| Memory utilization | The fraction of the memory quota that is currently in use.<br>Shown as percentage. | gcp.cloudsql.mysql.memory.utilization | DEPENDENT | 0 |
| Metrics get | MySQL metrics in raw format. | gcp.cloudsql.mysql.metrics.get | SCRIPT | {$GCP.TIME.WINDOW} |
| Connections | Number of connections to the databases on the Cloud SQL instance. | gcp.cloudsql.mysql.network.connections | DEPENDENT | 0 |
| Network: Received bytes | Delta count of bytes received through the network. | gcp.cloudsql.mysql.network.received_bytes_count | DEPENDENT | 0 |
| Network: Sent bytes | Delta count of bytes sent through the network. | gcp.cloudsql.mysql.network.sent_bytes_count | DEPENDENT | 0 |
| Open tables | The number of tables that are currently open. | gcp.cloudsql.mysql.open_tables | DEPENDENT | 0 |
| Open table definitions | The number of table definitions that are currently cached. | gcp.cloudsql.mysql.open_table_definitions | DEPENDENT | 0 |
| Network: Bytes received by MySQL | Delta count of bytes received by MySQL process. | gcp.cloudsql.mysql_received_bytes_count | DEPENDENT | 0 |
| Network: Bytes sent by MySQL | Delta count of bytes sent by MySQL process. | gcp.cloudsql.mysql_sent_bytes_count | DEPENDENT | 0 |
| Queries | Delta of statements executed by the server. | gcp.cloudsql.queries | DEPENDENT | 0 |
| Questions | Delta of statements executed by the server sent by the client. | gcp.cloudsql.questions | DEPENDENT | 0 |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$CLOUD_SQL.MYSQL.CPU.UTIL.MAX} | 95 |
| {$CLOUD_SQL.MYSQL.DISK.UTIL.CRIT} | 90 |
| {$CLOUD_SQL.MYSQL.DISK.UTIL.WARN} | 80 |
| {$CLOUD_SQL.MYSQL.RAM.UTIL.MAX} | 90 |
| {$GCP.DATA.TIMEOUT} | 15s |
| {$GCP.PROXY} | no value |
| {$GCP.TIME.WINDOW} | 5m |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| High CPU utilization | AVERAGE | The CPU utilization is too high. The system might be slow to respond. | min(/GCP Cloud SQL MySQL by HTTP/gcp.cloudsql.mysql.cpu.utilization,5m) >= {$CLOUD_SQL.MYSQL.CPU.UTIL.MAX} | [{"tag": "scope", "value": "performance"}] | no url |
| Database engine is down | AVERAGE | Database engine is down.<br>If an instance experiences unplanned (non-maintenance) downtime, the instance state will still be RUNNING, but the database engine state metric will report 0. | last(/GCP Cloud SQL MySQL by HTTP/gcp.cloudsql.mysql.db.state)=0 | [{"tag": "scope", "value": "availability"}] | no url |
| Disk space is critically low | AVERAGE | Critical utilization of the disk space. | last(/GCP Cloud SQL MySQL by HTTP/gcp.cloudsql.mysql.disk.utilization) >= {$CLOUD_SQL.MYSQL.DISK.UTIL.CRIT} | [{"tag": "scope", "value": "capacity"}] | no url |
| Disk space is low | WARNING | High utilization of the storage space. | last(/GCP Cloud SQL MySQL by HTTP/gcp.cloudsql.mysql.disk.utilization) >= {$CLOUD_SQL.MYSQL.DISK.UTIL.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |
| Failed to get the instance state | AVERAGE | Failed to get the instance state. <br>Check access permissions to GCP API or service account. | last(/GCP Cloud SQL MySQL by HTTP/gcp.cloudsql.mysql.inst.state) = 10 | [{"tag": "scope", "value": "availability"}] | no url |
| Instance is in failed state | AVERAGE | The instance creation failed, or an operation left the instance in an own bad state. | last(/GCP Cloud SQL MySQL by HTTP/gcp.cloudsql.mysql.inst.state) = 5 | [{"tag": "scope", "value": "availability"}] | no url |
| Instance is in maintenance | INFO | The instance is down for maintenance. | last(/GCP Cloud SQL MySQL by HTTP/gcp.cloudsql.mysql.inst.state) = 4 | [{"tag": "scope", "value": "availability"}] | no url |
| Instance is in suspended state | WARNING | The instance is in suspended state. <br>It is not available, for example, due to problems with billing. | last(/GCP Cloud SQL MySQL by HTTP/gcp.cloudsql.mysql.inst.state) = 1 | [{"tag": "scope", "value": "availability"}] | no url |
| Instance is in unknown state | AVERAGE | The state of the instance is unknown. | last(/GCP Cloud SQL MySQL by HTTP/gcp.cloudsql.mysql.inst.state) = 6 | [{"tag": "scope", "value": "availability"}] | no url |
| Instance is stopped by the owner | INFO | The instance has been stopped by the owner. <br>It is not currently running, but it's ready to be restarted. | last(/GCP Cloud SQL MySQL by HTTP/gcp.cloudsql.mysql.inst.state) = 2 | [{"tag": "scope", "value": "availability"}] | no url |
| High memory utilization | HIGH | RAM utilization is too high. The system might be slow to respond. | min(/GCP Cloud SQL MySQL by HTTP/gcp.cloudsql.mysql.memory.utilization,5m) >= {$CLOUD_SQL.MYSQL.RAM.UTIL.MAX} | [{"tag": "scope", "value": "performance"}] | no url |


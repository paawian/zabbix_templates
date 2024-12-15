# MongoDB node by Zabbix agent 2 template description

Get MongoDB metrics from plugin for the zabbix-agent2.
  1. Setup and configure zabbix-agent2 compiled with the MongoDB monitoring plugin.
  2. Set the {$MONGODB.CONNSTRING} such as <protocol(host:port)> or named session.
  3. Set the user name and password in host macros ({$MONGODB.USER}, {$MONGODB.PASSWORD}) if you want to override parameters from the Zabbix agent configuration file.

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/420659-discussion-thread-for-official-zabbix-template-db-mongodb

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Collection discovery ](#discovery_collection_discovery)
  * [Discovery Database discovery ](#discovery_database_discovery)
  * [Discovery Replication discovery ](#discovery_replication_discovery)
  * [Discovery WiredTiger metrics ](#discovery_wiredtiger_metrics)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Document: deleted, rate | Number of documents deleted per second. | mongod.document.deleted.rate | DEPENDENT | 0 |
| Document: inserted, rate | Number of documents inserted per second. | mongod.document.inserted.rate | DEPENDENT | 0 |
| Document: returned, rate | Number of documents returned by queries per second. | mongod.document.returned.rate | DEPENDENT | 0 |
| Document: updated, rate | Number of documents updated per second. | mongod.document.updated.rate | DEPENDENT | 0 |
| Active clients: readers | The number of the active client connections performing read operations. | mongodb.active_clients.readers | DEPENDENT | 0 |
| Active clients: total | The total number of internal client connections to the database including system threads as well as queued readers and writers. | mongodb.active_clients.total | DEPENDENT | 0 |
| Active clients: writers | The number of active client connections performing write operations. | mongodb.active_clients.writers | DEPENDENT | 0 |
| Asserts: message, rate | The number of message assertions raised per second.<br>Check the log file for more information about these messages. | mongodb.asserts.msg.rate | DEPENDENT | 0 |
| Asserts: regular, rate | The number of regular assertions raised per second.<br>Check the log file for more information about these messages. | mongodb.asserts.regular.rate | DEPENDENT | 0 |
| Asserts: rollovers, rate | Number of times that the rollover counters roll over per second.<br>The counters rollover to zero every 2^30 assertions. | mongodb.asserts.rollovers.rate | DEPENDENT | 0 |
| Asserts: user, rate | The number of "user asserts" that have occurred per second.<br>These are errors that user may generate, such as out of disk space or duplicate key. | mongodb.asserts.user.rate | DEPENDENT | 0 |
| Asserts: warning, rate | The number of warnings raised per second. | mongodb.asserts.warning.rate | DEPENDENT | 0 |
| Get collections usage stats | Returns usage statistics for each collection. | mongodb.collections.usage["{$MONGODB.CONNSTRING}","{$MONGODB.USER}","{$MONGODB.PASSWORD}"] | no type | no delay |
| Connections, active | The number of active client connections to the server.<br>Active client connections refers to client connections that currently have operations in progress.<br>Available starting in  4.0.7, 0 for older versions. | mongodb.connections.active | DEPENDENT | 0 |
| Connections, available | The number of unused incoming connections available. | mongodb.connections.available | DEPENDENT | 0 |
| Connections, current | The number of incoming connections from clients to the database server.<br>This number includes the current shell session. | mongodb.connections.current | DEPENDENT | 0 |
| New connections, rate | Rate of all incoming connections created to the server. | mongodb.connections.rate | DEPENDENT | 0 |
| Current queue: readers | The number of operations that are currently queued and waiting for the read lock.<br>A consistently small read-queue, particularly of shorter operations, should cause no concern. | mongodb.current_queue.readers | DEPENDENT | 0 |
| Current queue: total | The total number of operations queued waiting for the lock. | mongodb.current_queue.total | DEPENDENT | 0 |
| Current queue: writers | The number of operations that are currently queued and waiting for the write lock.<br> A consistently small write-queue, particularly of shorter operations, is no cause for concern. | mongodb.current_queue.writers | DEPENDENT | 0 |
| Cursor: open pinned | Number of pinned open cursors. | mongodb.cursor.open.pinned | DEPENDENT | 0 |
| Cursor: open total | Number of cursors that MongoDB is maintaining for clients. | mongodb.cursor.open.total | DEPENDENT | 0 |
| Cursor: timed out, rate | Number of cursors that time out, per second. | mongodb.cursor.timed_out.rate | DEPENDENT | 0 |
| Architecture | A number, either 64 or 32, that indicates whether the MongoDB instance is compiled for 64-bit or 32-bit architecture. | mongodb.mem.bits | DEPENDENT | 0 |
| Memory: mapped | Amount of mapped memory by the database. | mongodb.mem.mapped | DEPENDENT | 0 |
| Memory: mapped with journal | The amount of mapped memory, including the memory used for journaling. | mongodb.mem.mapped_with_journal | DEPENDENT | 0 |
| Memory: resident | Amount of memory currently used by the database process. | mongodb.mem.resident | DEPENDENT | 0 |
| Memory: virtual | Amount of virtual memory used by the mongod process. | mongodb.mem.virtual | DEPENDENT | 0 |
| Cursor: open no timeout | Number of open cursors with the option DBQuery.Option.noTimeout set to prevent timeout after a period of inactivity. | mongodb.metrics.cursor.open.no_timeout | DEPENDENT | 0 |
| Bytes in, rate | The total number of bytes that the server has received over network connections initiated by clients or other mongod/mongos instances per second. | mongodb.network.bytes_in.rate | DEPENDENT | 0 |
| Bytes out, rate | The total number of bytes that the server has sent over network connections initiated by clients or other mongod/mongos instances per second. | mongodb.network.bytes_out.rate | DEPENDENT | 0 |
| Requests, rate | Number of distinct requests that the server has received per second | mongodb.network.numRequests.rate | DEPENDENT | 0 |
| Operations: command, rate | The number of commands issued to the database the mongod instance per second.<br>Counts all commands except the write commands: insert, update, and delete. | mongodb.opcounters.command.rate | DEPENDENT | 0 |
| Operations: delete, rate | The number of delete operations the mongod instance per second. | mongodb.opcounters.delete.rate | DEPENDENT | 0 |
| Operations: getmore, rate | The number of "getmore" operations since the mongod instance per second. This counter can be high even if the query count is low.<br>Secondary nodes send getMore operations as part of the replication process. | mongodb.opcounters.getmore.rate | DEPENDENT | 0 |
| Operations: insert, rate | The number of insert operations received since the mongod instance per second. | mongodb.opcounters.insert.rate | DEPENDENT | 0 |
| Operations: query, rate | The number of queries received the mongod instance per second. | mongodb.opcounters.query.rate | DEPENDENT | 0 |
| Operations: update, rate | The number of update operations the mongod instance per second. | mongodb.opcounters.update.rate | DEPENDENT | 0 |
| Get oplog stats | Returns status of the replica set, using data polled from the oplog. | mongodb.oplog.stats["{$MONGODB.CONNSTRING}","{$MONGODB.USER}","{$MONGODB.PASSWORD}"] | no type | no delay |
| Ping | Test if a connection is alive or not. | mongodb.ping["{$MONGODB.CONNSTRING}","{$MONGODB.USER}","{$MONGODB.PASSWORD}"] | no type | 30s |
| Get Replica Set status | Returns the replica set status from the point of view of the member where the method is run. | mongodb.rs.status["{$MONGODB.CONNSTRING}","{$MONGODB.USER}","{$MONGODB.PASSWORD}"] | no type | no delay |
| Get server status | Returns a database's state. | mongodb.server.status["{$MONGODB.CONNSTRING}","{$MONGODB.USER}","{$MONGODB.PASSWORD}"] | no type | no delay |
| Uptime | Number of seconds that the mongod process has been active. | mongodb.uptime | DEPENDENT | 0 |
| MongoDB version | Version of the MongoDB server. | mongodb.version["{$MONGODB.CONNSTRING}","{$MONGODB.USER}","{$MONGODB.PASSWORD}"] | no type | 15m |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$MONGODB.CONNS.PCT.USED.MAX.WARN} | 80 |
| {$MONGODB.CONNSTRING} | tcp://localhost:27017 |
| {$MONGODB.CURSOR.OPEN.MAX.WARN} | 10000 |
| {$MONGODB.CURSOR.TIMEOUT.MAX.WARN} | 1 |
| {$MONGODB.LLD.FILTER.COLLECTION.MATCHES} | .* |
| {$MONGODB.LLD.FILTER.COLLECTION.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$MONGODB.LLD.FILTER.DB.MATCHES} | .* |
| {$MONGODB.LLD.FILTER.DB.NOT_MATCHES} | (admin\|config\|local) |
| {$MONGODB.PASSWORD} | no value |
| {$MONGODB.REPL.LAG.MAX.WARN} | 10s |
| {$MONGODB.USER} | no value |
| {$MONGODB.WIRED_TIGER.TICKETS.AVAILABLE.MIN.WARN} | 5 |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Too many cursors opened by MongoDB for clients | WARNING | no description | min(/MongoDB node by Zabbix agent 2/mongodb.cursor.open.total,5m)>{$MONGODB.CURSOR.OPEN.MAX.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |
| Too many cursors are timing out | WARNING | no description | min(/MongoDB node by Zabbix agent 2/mongodb.cursor.timed_out.rate,5m)>{$MONGODB.CURSOR.TIMEOUT.MAX.WARN} | [{"tag": "scope", "value": "performance"}] | no url |
| Connection to MongoDB is unavailable | HIGH | Connection to MongoDB instance is currently unavailable. | last(/MongoDB node by Zabbix agent 2/mongodb.ping["{$MONGODB.CONNSTRING}","{$MONGODB.USER}","{$MONGODB.PASSWORD}"])=0 | [{"tag": "scope", "value": "availability"}] | no url |
| Failed to fetch info data | WARNING | Zabbix has not received data for items for the last 10 minutes | nodata(/MongoDB node by Zabbix agent 2/mongodb.uptime,10m)=1 | [{"tag": "scope", "value": "availability"}] | no url |
| mongod process has been restarted | INFO | Uptime is less than 10 minutes. | last(/MongoDB node by Zabbix agent 2/mongodb.uptime)<10m | [{"tag": "scope", "value": "notice"}] | no url |
| Version has changed | INFO | MongoDB version has changed. Acknowledge to close the problem manually. | last(/MongoDB node by Zabbix agent 2/mongodb.version["{$MONGODB.CONNSTRING}","{$MONGODB.USER}","{$MONGODB.PASSWORD}"],#1)<>last(/MongoDB node by Zabbix agent 2/mongodb.version["{$MONGODB.CONNSTRING}","{$MONGODB.USER}","{$MONGODB.PASSWORD}"],#2) and length(last(/MongoDB node by Zabbix agent 2/mongodb.version["{$MONGODB.CONNSTRING}","{$MONGODB.USER}","{$MONGODB.PASSWORD}"]))>0 | [{"tag": "scope", "value": "notice"}] | no url |
| Total number of open connections is too high | WARNING | Too few available connections.<br>If MongoDB runs low on connections, in may not be able to handle incoming requests in a timely manner. | min(/MongoDB node by Zabbix agent 2/mongodb.connections.current,5m)/(last(/MongoDB node by Zabbix agent 2/mongodb.connections.available)+last(/MongoDB node by Zabbix agent 2/mongodb.connections.current))*100>{$MONGODB.CONNS.PCT.USED.MAX.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |


<a name="discoveries" />

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Collection discovery | mongodb.collections.discovery["{$MONGODB.CONNSTRING}","{$MONGODB.USER}","{$MONGODB.PASSWORD}"] | Collect collections metrics.<br>Note, depending on the number of DBs and collections this discovery operation may be expensive. Use filters with macros {$MONGODB.LLD.FILTER.DB.MATCHES}, {$MONGODB.LLD.FILTER.DB.NOT_MATCHES}, {$MONGODB.LLD.FILTER.COLLECTION.MATCHES}, {$MONGODB.LLD.FILTER.COLLECTION.NOT_MATCHES}. | no type | no lifetime | 30m |
| Database discovery | mongodb.db.discovery["{$MONGODB.CONNSTRING}","{$MONGODB.USER}","{$MONGODB.PASSWORD}"] | Collect database metrics.<br>Note, depending on the number of DBs this discovery operation may be expensive. Use filters with macros {$MONGODB.LLD.FILTER.DB.MATCHES}, {$MONGODB.LLD.FILTER.DB.NOT_MATCHES}. | no type | no lifetime | 30m |
| Replication discovery | mongodb.rs.discovery | Collect metrics by Zabbix agent if it exists. | DEPENDENT | no lifetime | 0 |
| WiredTiger metrics | mongodb.wired_tiger.discovery | Collect metrics of WiredTiger Storage Engine if it exists. | DEPENDENT | no lifetime | 0 |


<a name="discovery_collection_discovery" />

## Discovery Collection discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| MongoDB {#DBNAME}.{#COLLECTION}: Objects, avg size | The size of the average object in the collection in bytes. | mongodb.collection.avg_obj_size["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Capped | Whether or not the collection is capped. | mongodb.collection.capped["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Objects, count | Total number of objects in the collection. | mongodb.collection.count["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Capped: max number | Maximum number of documents that may be present in a capped collection. | mongodb.collection.max_number["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Capped: max size | Maximum size of a capped collection in bytes. | mongodb.collection.max_size["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Indexes | Total number of indices on the collection. | mongodb.collection.nindexes["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Operations: commands, ms/s | Fraction of time (ms/s) the mongod has spent to operations. | mongodb.collection.ops.commands.ms["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Operations: commands, rate | The number of operations per second. | mongodb.collection.ops.commands.rate["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Operations: getmore, ms/s | Fraction of time (ms/s) the mongod has spent to operations. | mongodb.collection.ops.getmore.ms["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Operations: getmore, rate | The number of operations per second. | mongodb.collection.ops.getmore.rate["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Operations: insert, ms/s | Fraction of time (ms/s) the mongod has spent to operations. | mongodb.collection.ops.insert.ms["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Operations: insert, rate | The number of operations per second. | mongodb.collection.ops.insert.rate["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Operations: queries, ms/s | Fraction of time (ms/s) the mongod has spent to operations. | mongodb.collection.ops.queries.ms["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Operations: queries, rate | The number of operations per second. | mongodb.collection.ops.queries.rate["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Operations: remove, ms/s | Fraction of time (ms/s) the mongod has spent to operations. | mongodb.collection.ops.remove.ms["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Operations: remove, rate | The number of operations per second. | mongodb.collection.ops.remove.rate["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Operations: total, ms/s | Fraction of time (ms/s) the mongod has spent to operations. | mongodb.collection.ops.total.ms["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Operations: total, rate | The number of operations per second. | mongodb.collection.ops.total.rate["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Operations: update, ms/s | Fraction of time (ms/s) the mongod has spent to operations. | mongodb.collection.ops.update.ms["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Operations: update, rate | The number of operations per second. | mongodb.collection.ops.update.rate["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Read lock, ms/s | Fraction of time (ms/s) the mongod has spent to operations. | mongodb.collection.read_lock.ms["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Read lock, rate | The number of operations per second. | mongodb.collection.read_lock.rate["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Size | The total size in bytes of the data in the collection plus the size of every indexes on the mongodb.collection. | mongodb.collection.size["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Get collection stats {#DBNAME}.{#COLLECTION} | Returns a variety of storage statistics for a given collection. | mongodb.collection.stats["{$MONGODB.CONNSTRING}","{$MONGODB.USER}","{$MONGODB.PASSWORD}","{#DBNAME}","{#COLLECTION}"] | no type |
| MongoDB {#DBNAME}.{#COLLECTION}: Storage size | Total storage space allocated to this collection for document storage. | mongodb.collection.storage_size["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Write lock, ms/s | Fraction of time (ms/s) the mongod has spent to operations. | mongodb.collection.write_lock.ms["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |
| MongoDB {#DBNAME}.{#COLLECTION}: Write lock, rate | The number of operations per second. | mongodb.collection.write_lock.rate["{#DBNAME}","{#COLLECTION}"] | DEPENDENT |


<a name="discovery_database_discovery" />

## Discovery Database discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| MongoDB {#DBNAME}: Collections | Contains a count of the number of collections in that database. | mongodb.db.collections["{#DBNAME}"] | DEPENDENT |
| MongoDB {#DBNAME}: Size, data | Total size of the data held in this database including the padding factor. | mongodb.db.data_size["{#DBNAME}"] | DEPENDENT |
| MongoDB {#DBNAME}: Extents | Contains a count of the number of extents in the database across all collections. | mongodb.db.extents["{#DBNAME}"] | DEPENDENT |
| MongoDB {#DBNAME}: Size, file | Total size of the data held in this database including the padding factor (only available with the mmapv1 storage engine). | mongodb.db.file_size["{#DBNAME}"] | DEPENDENT |
| MongoDB {#DBNAME}: Size, index | Total size of all indexes created on this database. | mongodb.db.index_size["{#DBNAME}"] | DEPENDENT |
| MongoDB {#DBNAME}: Objects, count | Number of objects (documents) in the database across all collections. | mongodb.db.objects["{#DBNAME}"] | DEPENDENT |
| MongoDB {#DBNAME}: Objects, avg size | The average size of each document in bytes. | mongodb.db.size["{#DBNAME}"] | DEPENDENT |
| MongoDB {#DBNAME}: Get db stats {#DBNAME} | Returns statistics reflecting the database system's state. | mongodb.db.stats["{$MONGODB.CONNSTRING}","{$MONGODB.USER}","{$MONGODB.PASSWORD}","{#DBNAME}"] | no type |
| MongoDB {#DBNAME}: Size, storage | Total amount of space allocated to collections in this database for document storage. | mongodb.db.storage_size["{#DBNAME}"] | DEPENDENT |


<a name="discovery_replication_discovery" />

## Discovery Replication discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Apply batches, ms/s | Fraction of time (ms/s) the mongod has spent applying operations from the oplog. | mongodb.rs.apply.batches.ms.rate[{#RS_NAME}] | DEPENDENT |
| Apply batches, rate | Number of batches applied across all databases per second. | mongodb.rs.apply.batches.rate[{#RS_NAME}] | DEPENDENT |
| Apply ops, rate | Number of oplog operations applied per second. | mongodb.rs.apply.rate[{#RS_NAME}] | DEPENDENT |
| Buffer | Number of operations in the oplog buffer. | mongodb.rs.buffer.count[{#RS_NAME}] | DEPENDENT |
| Buffer, max size | Maximum size of the buffer. | mongodb.rs.buffer.max_size[{#RS_NAME}] | DEPENDENT |
| Buffer, size | Current size of the contents of the oplog buffer. | mongodb.rs.buffer.size[{#RS_NAME}] | DEPENDENT |
| Replication lag | Delay between a write operation on the primary and its copy to a secondary. | mongodb.rs.lag[{#RS_NAME}] | DEPENDENT |
| Network bytes, rate | Amount of data read from the replication sync source per second. | mongodb.rs.network.bytes.rate[{#RS_NAME}] | DEPENDENT |
| Network getmores, ms/s | Fraction of time (ms/s) required to collect data from getmore operations. | mongodb.rs.network.getmores.ms.rate[{#RS_NAME}] | DEPENDENT |
| Network getmores, rate | Number of getmore operations per second. | mongodb.rs.network.getmores.rate[{#RS_NAME}] | DEPENDENT |
| Network ops, rate | Number of operations read from the replication source per second. | mongodb.rs.network.ops.rate[{#RS_NAME}] | DEPENDENT |
| Network readers created, rate | Number of oplog query processes created per second. | mongodb.rs.network.readers.rate[{#RS_NAME}] | DEPENDENT |
| MongoDB {#RS_NAME}: Oplog time diff | Oplog window: difference between the first and last operation in the oplog. Only present if there are entries in the oplog. | mongodb.rs.oplog.timediff[{#RS_NAME}] | DEPENDENT |
| Preload docs, ms/s | Fraction of time (ms/s) spent loading documents as part of the pre-fetch stage of replication. | mongodb.rs.preload.docs.ms.rate[{#RS_NAME}] | DEPENDENT |
| Preload docs, rate | Number of documents loaded per second during the pre-fetch stage of replication. | mongodb.rs.preload.docs.rate[{#RS_NAME}] | DEPENDENT |
| Preload indexes, ms/s | Fraction of time (ms/s) spent loading documents as part of the pre-fetch stage of replication. | mongodb.rs.preload.indexes.ms.rate[{#RS_NAME}] | DEPENDENT |
| Preload indexes, rate | Number of index entries loaded by members before updating documents as part of the pre-fetch stage of replication. | mongodb.rs.preload.indexes.rate[{#RS_NAME}] | DEPENDENT |
| Node state | An integer between 0 and 10 that represents the replica state of the current member. | mongodb.rs.state[{#RS_NAME}] | DEPENDENT |
| Number of replicas | The number of replicated nodes in current ReplicaSet. | mongodb.rs.total_nodes[{#RS_NAME}] | DEPENDENT |
| Unhealthy replicas | The replicated nodes in current ReplicaSet with member health value  = 0. | mongodb.rs.unhealthy[{#RS_NAME}] | DEPENDENT |
| Number of unhealthy replicas | The number of replicated nodes with member health value  = 0. | mongodb.rs.unhealthy_count[{#RS_NAME}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Replication lag with primary is too high | WARNING | no description | min(/MongoDB node by Zabbix agent 2/mongodb.rs.lag[{#RS_NAME}],5m)>{$MONGODB.REPL.LAG.MAX.WARN} | [{"tag": "scope", "value": "performance"}] | no url |
| Node in ReplicaSet changed the state | WARNING | Node in ReplicaSet  changed the state. Acknowledge to close the problem manually. | last(/MongoDB node by Zabbix agent 2/mongodb.rs.state[{#RS_NAME}],#1)<>last(/MongoDB node by Zabbix agent 2/mongodb.rs.state[{#RS_NAME}],#2) | [{"tag": "scope", "value": "notice"}] | no url |
| There are unhealthy replicas in ReplicaSet | AVERAGE | no description | last(/MongoDB node by Zabbix agent 2/mongodb.rs.unhealthy_count[{#RS_NAME}])>0 and length(last(/MongoDB node by Zabbix agent 2/mongodb.rs.unhealthy[{#RS_NAME}]))>0 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discovery_wiredtiger_metrics" />

## Discovery WiredTiger metrics

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| WiredTiger cache: bytes | Size of the data currently in cache. | mongodb.wired_tiger.cache.bytes_in_cache[{#SINGLETON}] | DEPENDENT |
| WiredTiger cache: bytes, max | Maximum cache size. | mongodb.wired_tiger.cache.maximum_bytes_configured[{#SINGLETON}] | DEPENDENT |
| WiredTiger cache: max page size at eviction | Maximum page size at eviction. | mongodb.wired_tiger.cache.max_page_size_eviction[{#SINGLETON}] | DEPENDENT |
| WiredTiger cache: modified pages evicted | Number of pages, that have been modified, evicted from the cache. | mongodb.wired_tiger.cache.modified_pages_evicted[{#SINGLETON}] | DEPENDENT |
| WiredTiger cache: pages evicted by application threads, rate | Number of page evicted by application threads per second. | mongodb.wired_tiger.cache.pages_evicted_threads.rate[{#SINGLETON}] | DEPENDENT |
| WiredTiger cache: pages held in cache | Number of pages currently held in the cache. | mongodb.wired_tiger.cache.pages_in_cache[{#SINGLETON}] | DEPENDENT |
| WiredTiger cache: pages read into cache | Number of pages read into the cache. | mongodb.wired_tiger.cache.pages_read[{#SINGLETON}] | DEPENDENT |
| WiredTiger cache: pages written from cache | Number of pages written from the cache. | mongodb.wired_tiger.cache.pages_written[{#SINGLETON}] | DEPENDENT |
| WiredTiger cache: in-memory page splits | In-memory page splits. | mongodb.wired_tiger.cache.splits[{#SINGLETON}] | DEPENDENT |
| WiredTiger cache: tracked dirty bytes in the cache | Size of the dirty data in the cache. | mongodb.wired_tiger.cache.tracked_dirty_bytes[{#SINGLETON}] | DEPENDENT |
| WiredTiger cache: unmodified pages evicted | Number of pages, that were not modified, evicted from the cache. | mongodb.wired_tiger.cache.unmodified_pages_evicted[{#SINGLETON}] | DEPENDENT |
| WiredTiger concurrent transactions: read, available | Number of available read tickets (concurrent transactions) remaining. | mongodb.wired_tiger.concurrent_transactions.read.available[{#SINGLETON}] | DEPENDENT |
| WiredTiger concurrent transactions: read, out | Number of read tickets (concurrent transactions) in use. | mongodb.wired_tiger.concurrent_transactions.read.out[{#SINGLETON}] | DEPENDENT |
| WiredTiger concurrent transactions: read, total tickets | Total number of read tickets (concurrent transactions) available. | mongodb.wired_tiger.concurrent_transactions.read.totalTickets[{#SINGLETON}] | DEPENDENT |
| WiredTiger concurrent transactions: write, available | Number of available write tickets (concurrent transactions) remaining. | mongodb.wired_tiger.concurrent_transactions.write.available[{#SINGLETON}] | DEPENDENT |
| WiredTiger concurrent transactions: write, out | Number of write tickets (concurrent transactions) in use. | mongodb.wired_tiger.concurrent_transactions.write.out[{#SINGLETON}] | DEPENDENT |
| WiredTiger concurrent transactions: write, total tickets | Total number of write tickets (concurrent transactions) available. | mongodb.wired_tiger.concurrent_transactions.write.totalTickets[{#SINGLETON}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Available WiredTiger read tickets is low | WARNING | Too few available read tickets.<br>When the number of available read tickets remaining reaches zero, new read requests will be queued until a new read ticket is available. | max(/MongoDB node by Zabbix agent 2/mongodb.wired_tiger.concurrent_transactions.read.available[{#SINGLETON}],5m)<{$MONGODB.WIRED_TIGER.TICKETS.AVAILABLE.MIN.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |
| Available WiredTiger write tickets is low | WARNING | Too few available write tickets.<br>When the number of available write tickets remaining reaches zero, new write requests will be queued until a new write ticket is available. | max(/MongoDB node by Zabbix agent 2/mongodb.wired_tiger.concurrent_transactions.write.available[{#SINGLETON}],5m)<{$MONGODB.WIRED_TIGER.TICKETS.AVAILABLE.MIN.WARN} | [{"tag": "scope", "value": "capacity"}] | no url |

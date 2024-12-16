# AWS by HTTP template description

Get AWS EC2, RDS and S3 instances, AWS ECS clusters, AWS Elastic Load Balancing. Don't forget to read the README.md for the correct setup of the template.

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback

Generated by official Zabbix template tool "Templator"

## Summary
* [macros](#macros)
* [discoveries](#discoveries)

<a name="macros"></a>

## Macros
| macro | value |
| ------------- |------------- |
| {$AWS.ACCESS.KEY.ID} | no value |
| {$AWS.AUTH_TYPE} | access_key |
| {$AWS.DATA.TIMEOUT} | 60s |
| {$AWS.EC2.LLD.FILTER.NAME.MATCHES} | .* |
| {$AWS.EC2.LLD.FILTER.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$AWS.EC2.LLD.FILTER.REGION.MATCHES} | .* |
| {$AWS.EC2.LLD.FILTER.REGION.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$AWS.ECS.LLD.FILTER.NAME.MATCHES} | .* |
| {$AWS.ECS.LLD.FILTER.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$AWS.ECS.LLD.FILTER.REGION.MATCHES} | .* |
| {$AWS.ECS.LLD.FILTER.REGION.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$AWS.ECS.LLD.FILTER.STATUS.MATCHES} | ACTIVE |
| {$AWS.ECS.LLD.FILTER.STATUS.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$AWS.ELB.LLD.FILTER.NAME.MATCHES} | .* |
| {$AWS.ELB.LLD.FILTER.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$AWS.ELB.LLD.FILTER.REGION.MATCHES} | .* |
| {$AWS.ELB.LLD.FILTER.REGION.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$AWS.ELB.LLD.FILTER.STATE.MATCHES} | active |
| {$AWS.ELB.LLD.FILTER.STATE.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$AWS.PROXY} | no value |
| {$AWS.RDS.LLD.FILTER.NAME.MATCHES} | .* |
| {$AWS.RDS.LLD.FILTER.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$AWS.RDS.LLD.FILTER.REGION.MATCHES} | .* |
| {$AWS.RDS.LLD.FILTER.REGION.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$AWS.S3.LLD.FILTER.NAME.MATCHES} | .* |
| {$AWS.S3.LLD.FILTER.NAME.NOT_MATCHES} | CHANGE_IF_NEEDED |
| {$AWS.SECRET.ACCESS.KEY} | no value |


<a name="discoveries"></a>

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| EC2 instances discovery | aws.ec2.discovery | Get EC2 instances. | SCRIPT | no lifetime | 12h |
| ECS clusters discovery | aws.ecs.discovery | Get ECS clusters. | SCRIPT | no lifetime | 12h |
| ELB load balancers discovery | aws.elb.discovery | Get ELB load balancers. | SCRIPT | no lifetime | 12h |
| RDS instances discovery | aws.rds.discovery | Get RDS instances. | SCRIPT | no lifetime | 12h |
| S3 buckets discovery | aws.s3.discovery | Get S3 bucket instances. | SCRIPT | no lifetime | 12h |

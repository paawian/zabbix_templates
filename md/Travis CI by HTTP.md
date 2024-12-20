# Travis CI by HTTP template description

Template for monitoring Travis CI https://travis-ci.com
You must set {$TRAVIS.API.TOKEN} and {$TRAVIS.API.URL} macros.
  {$TRAVIS.API.TOKEN} is a Travis API authentication token located in User -> Settings -> API authentication.
  {$TRAVIS.API.URL} could be in 2 different variations:
   - for a private project : api.travis-ci.com
   - for an enterprise projects: api.example.com (where you replace example.com with the domain Travis CI is running on)

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback/

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Repos metrics discovery ](#discovery_repos_metrics_discovery)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Builds duration | Sum of all builds durations in all repos. | travis.builds.duration | DEPENDENT | 0 |
| Builds | Total count of builds in all repos. | travis.builds.total | DEPENDENT | 0 |
| Get builds | Getting builds using Travis API. | travis.get_builds | HTTP_AGENT | no delay |
| Get health | Getting home JSON using Travis API. | travis.get_health | HTTP_AGENT | no delay |
| Get jobs | Getting jobs using Travis API. | travis.get_jobs | HTTP_AGENT | no delay |
| Get repos | Getting repos using Travis API. | travis.get_repos | HTTP_AGENT | no delay |
| Jobs active | Active jobs in all repos. | travis.jobs.active | DEPENDENT | 0 |
| Jobs in queue | Jobs in queue in all repos. | travis.jobs.queue | DEPENDENT | 0 |
| Jobs passed | Total count of passed jobs in all repos. | travis.jobs.total | DEPENDENT | 0 |


<a name="macros" />

## Macros
| macro | value |
| ------------- |------------- |
| {$TRAVIS.API.TOKEN} | no value |
| {$TRAVIS.API.URL} | api.travis-ci.com |
| {$TRAVIS.BUILDS.SUCCESS.PERCENT} | 80 |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Failed to fetch home page | WARNING | Zabbix has not received any data for items for the last 30 minutes. | nodata(/Travis CI by HTTP/travis.get_health,30m)=1 | [{"tag": "scope", "value": "availability"}] | no url |
| Service is unavailable | HIGH | Travis API is unavailable. Please check if the correct macros are set. | last(/Travis CI by HTTP/travis.get_health)=0 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discoveries" />

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Repos metrics discovery | travis.repos.discovery | Metrics for Repos statistics. | DEPENDENT | no lifetime | 0 |


<a name="discovery_repos_metrics_discovery" />

## Discovery Repos metrics discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| Repo [{#SLUG}]: Builds failed | Count of all failed builds in {#SLUG} repo. | travis.repo.builds.failed[{#SLUG}] | DEPENDENT |
| Repo [{#SLUG}]: Builds passed, % | Percent of passed builds in {#SLUG} repo. | travis.repo.builds.passed.pct[{#SLUG}] | CALCULATED |
| Repo [{#SLUG}]: Builds passed | Count of all passed builds in {#SLUG} repo. | travis.repo.builds.passed[{#SLUG}] | DEPENDENT |
| Repo [{#SLUG}]: Builds total | Count of total builds in {#SLUG} repo. | travis.repo.builds.total[{#SLUG}] | DEPENDENT |
| Repo [{#SLUG}]: Cache files | Count of cache files in {#SLUG} repo. | travis.repo.caches.files[{#SLUG}] | DEPENDENT |
| Repo [{#SLUG}]: Cache size | Total size of cache files in {#SLUG} repo. | travis.repo.caches.size[{#SLUG}] | DEPENDENT |
| Repo [{#SLUG}]: Description | Description of Travis repo (git project description). | travis.repo.description[{#SLUG}] | DEPENDENT |
| Repo [{#SLUG}]: Get builds | Getting builds of {#SLUG} using Travis API. | travis.repo.get_builds[{#SLUG}] | HTTP_AGENT |
| Repo [{#SLUG}]: Get caches | Getting caches of {#SLUG} using Travis API. | travis.repo.get_caches[{#SLUG}] | HTTP_AGENT |
| Repo [{#SLUG}]: Last build duration | Last build duration in {#SLUG} repo. | travis.repo.last_build.duration[{#SLUG}] | DEPENDENT |
| Repo [{#SLUG}]: Last build id | Last build id in {#SLUG} repo. | travis.repo.last_build.id[{#SLUG}] | DEPENDENT |
| Repo [{#SLUG}]: Last build number | Last build number in {#SLUG} repo. | travis.repo.last_build.number[{#SLUG}] | DEPENDENT |
| Repo [{#SLUG}]: Last build state | Last build state in {#SLUG} repo. | travis.repo.last_build.state[{#SLUG}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Repo [{#SLUG}]: Percent of successful builds | WARNING | Low successful builds rate. | last(/Travis CI by HTTP/travis.repo.builds.passed.pct[{#SLUG}])<{$TRAVIS.BUILDS.SUCCESS.PERCENT} | [{"tag": "scope", "value": "performance"}] | no url |
| Repo [{#SLUG}]: Last build status is 'errored' | WARNING | Last build status is errored. | find(/Travis CI by HTTP/travis.repo.last_build.state[{#SLUG}],,"like","errored")=1 | [{"tag": "scope", "value": "performance"}] | no url |


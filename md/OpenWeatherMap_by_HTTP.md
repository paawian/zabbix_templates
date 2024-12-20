# OpenWeatherMap by HTTP template description

Get weather metrics from OpenWeatherMap current weather API by HTTP.
It works without any external scripts and uses the Script item.

Setup:
  1. Create a host.

  2. Link the template to the host.

  3. Customize the values of {$OPENWEATHERMAP.API.TOKEN} and {$LOCATION} macros.  
      OpenWeatherMap API Tokens are available in your OpenWeatherMap account https://home.openweathermap.org/api_keys.  
      Locations can be set by few ways:
        - by geo coordinates (for example: 56.95,24.0833)
        - by location name (for example: Riga)
        - by location ID. Link to the list of city ID: http://bulk.openweathermap.org/sample/city.list.json.gz
        - by zip/post code with a country code (for example: 94040,us)
      A few locations can be added to the macro at the same time by "|" delimiter. 
      For example: 43.81821,7.76115|Riga|2643743|94040,us.
      Please note that API requests by city name, zip-codes and city id will be deprecated soon.
      
      Language and units macros can be customized too if necessary.
      List of available languages: https://openweathermap.org/current#multi.
      Available units of measurement are: standard, metric and imperial https://openweathermap.org/current#data.

You can discuss this template or leave feedback on our forum https://www.zabbix.com/forum/zabbix-suggestions-and-feedback

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [macros](#macros)
* [triggers](#triggers)
* [discoveries](#discoveries)
  * [Discovery Locations discovery ](#discovery_locations_discovery)

<a name="items"></a>

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Get data | JSON array with result of OpenWeatherMap API requests. | openweathermap.get.data | SCRIPT | 10m |
| Get data collection errors | Errors from get data requests by script item. | openweathermap.get.errors | DEPENDENT | 0 |


<a name="macros"></a>

## Macros
| macro | value |
| ------------- |------------- |
| {$LANG} | en |
| {$LOCATION} | Riga |
| {$OPENWEATHERMAP.API.ENDPOINT} | api.openweathermap.org/data/2.5/weather? |
| {$OPENWEATHERMAP.API.TOKEN} | no value |
| {$TEMP.CRIT.HIGH} | 30 |
| {$TEMP.CRIT.LOW} | -20 |
| {$UNITS} | metric |


<a name="triggers"></a>

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| There are errors in requests to OpenWeatherMap API | AVERAGE | Zabbix has received errors in requests to OpenWeatherMap API. | length(last(/OpenWeatherMap by HTTP/openweathermap.get.errors))>0 | [{"tag": "scope", "value": "availability"}] | no url |


<a name="discoveries"></a>

## Discoveries
| name | key | description | type | lifetime | delay |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Locations discovery | openweathermap.locations.discovery | Weather metrics discovery by location. | DEPENDENT | 0d | 0 |


<a name="discovery_locations_discovery"></a>

## Discovery Locations discovery

### Items

| name | description | key | type |
| ------------- |------------- |------------- |------------- |
| [{#LOCATION}, {#COUNTRY}]: Cloudiness | Cloudiness in %. | openweathermap.clouds[{#ID}] | DEPENDENT |
| [{#LOCATION}, {#COUNTRY}]: Short weather status | Short weather status description. | openweathermap.description[{#ID}] | DEPENDENT |
| [{#LOCATION}, {#COUNTRY}]: Humidity | Humidity in %. | openweathermap.humidity[{#ID}] | DEPENDENT |
| [{#LOCATION}, {#COUNTRY}]: Data | JSON with result of OpenWeatherMap API request by location. | openweathermap.location.data[{#ID}] | DEPENDENT |
| [{#LOCATION}, {#COUNTRY}]: Atmospheric pressure | Atmospheric pressure in Pa. | openweathermap.pressure[{#ID}] | DEPENDENT |
| [{#LOCATION}, {#COUNTRY}]: Rain volume for the last one hour | Rain volume for the lat one hour in m. | openweathermap.rain[{#ID}] | DEPENDENT |
| [{#LOCATION}, {#COUNTRY}]: Snow volume for the last one hour | Snow volume for the lat one hour in m. | openweathermap.snow[{#ID}] | DEPENDENT |
| [{#LOCATION}, {#COUNTRY}]: Temperature | Atmospheric temperature value. | openweathermap.temp[{#ID}] | DEPENDENT |
| [{#LOCATION}, {#COUNTRY}]: Visibility | Visibility in m. | openweathermap.visibility[{#ID}] | DEPENDENT |
| [{#LOCATION}, {#COUNTRY}]: Wind direction | Wind direction in degrees. | openweathermap.wind.direction[{#ID}] | DEPENDENT |
| [{#LOCATION}, {#COUNTRY}]: Wind speed | Wind speed value. | openweathermap.wind.speed[{#ID}] | DEPENDENT |


### Triggers

| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| [{#LOCATION}, {#COUNTRY}]: Temperature is too high | AVERAGE | Temperature value is too high. | min(/OpenWeatherMap by HTTP/openweathermap.temp[{#ID}],#3)>{$TEMP.CRIT.HIGH} | [{"tag": "scope", "value": "notice"}] | no url |
| [{#LOCATION}, {#COUNTRY}]: Temperature is too low | AVERAGE | Temperature value is too low. | max(/OpenWeatherMap by HTTP/openweathermap.temp[{#ID}],#3)<{$TEMP.CRIT.LOW} | [{"tag": "scope", "value": "notice"}] | no url |


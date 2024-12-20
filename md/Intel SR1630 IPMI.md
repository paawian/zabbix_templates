# Intel SR1630 IPMI template description

Template for monitoring Intel SR1630 server system.

Generated by official Zabbix template tool "Templator"

## Summary
* [items](#items)
* [triggers](#triggers)

<a name="items" />

## Items
| name | description | key | type | delay |
| ------------- |------------- |------------- |------------- |------------- |
| Baseboard Temp | no description | baseboard_temp | IPMI | no delay |
| BB +1.05V PCH | no description | bb_1.05v_pch | IPMI | no delay |
| BB +1.1V P1 Vccp | no description | bb_1.1v_p1_vccp | IPMI | no delay |
| BB +1.5V P1 DDR3 | no description | bb_1.5v_p1_ddr3 | IPMI | no delay |
| BB +3.3V | no description | bb_3.3v | IPMI | no delay |
| BB +3.3V STBY | no description | bb_3.3v_stby | IPMI | no delay |
| BB +5.0V | no description | bb_5.0v | IPMI | no delay |
| Front Panel Temp | no description | front_panel_temp | IPMI | no delay |
| Power | no description | power | IPMI | no delay |
| System Fan 2 | no description | system_fan_2 | IPMI | no delay |
| System Fan 3 | no description | system_fan_3 | IPMI | no delay |


<a name="triggers" />

## Triggers
| name | priority | description | expression | tags | url |
| ------------- |------------- |------------- |------------- |------------- |------------- |
| Baseboard Temp Critical [{ITEM.VALUE}] | DISASTER | no description | last(/Intel SR1630 IPMI/baseboard_temp)<5 or last(/Intel SR1630 IPMI/baseboard_temp)>90 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Baseboard Temp Non-Critical [{ITEM.VALUE}] | HIGH | no description | last(/Intel SR1630 IPMI/baseboard_temp)<10 or last(/Intel SR1630 IPMI/baseboard_temp)>83 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| BB +1.05V PCH Critical [{ITEM.VALUE}] | DISASTER | no description | last(/Intel SR1630 IPMI/bb_1.05v_pch)<0.953 or last(/Intel SR1630 IPMI/bb_1.05v_pch)>1.149 | [{"tag": "scope", "value": "availability"}] | no url |
| BB +1.05V PCH Non-Critical [{ITEM.VALUE}] | HIGH | no description | last(/Intel SR1630 IPMI/bb_1.05v_pch)<0.985 or last(/Intel SR1630 IPMI/bb_1.05v_pch)>1.117 | [{"tag": "scope", "value": "availability"}] | no url |
| BB +1.1V P1 Vccp Critical [{ITEM.VALUE}] | DISASTER | no description | last(/Intel SR1630 IPMI/bb_1.1v_p1_vccp)<0.683 or last(/Intel SR1630 IPMI/bb_1.1v_p1_vccp)>1.543 | [{"tag": "scope", "value": "availability"}] | no url |
| BB +1.1V P1 Vccp Non-Critical [{ITEM.VALUE}] | HIGH | no description | last(/Intel SR1630 IPMI/bb_1.1v_p1_vccp)<0.708 or last(/Intel SR1630 IPMI/bb_1.1v_p1_vccp)>1.501 | [{"tag": "scope", "value": "availability"}] | no url |
| BB +1.5V P1 DDR3 Critical [{ITEM.VALUE}] | DISASTER | no description | last(/Intel SR1630 IPMI/bb_1.5v_p1_ddr3)<1.362 or last(/Intel SR1630 IPMI/bb_1.5v_p1_ddr3)>1.635 | [{"tag": "scope", "value": "availability"}] | no url |
| BB +1.5V P1 DDR3 Non-Critical [{ITEM.VALUE}] | HIGH | no description | last(/Intel SR1630 IPMI/bb_1.5v_p1_ddr3)<1.401 or last(/Intel SR1630 IPMI/bb_1.5v_p1_ddr3)>1.589 | [{"tag": "scope", "value": "availability"}] | no url |
| BB +3.3V Critical [{ITEM.VALUE}] | DISASTER | no description | last(/Intel SR1630 IPMI/bb_3.3v)<2.982 or last(/Intel SR1630 IPMI/bb_3.3v)>3.625 | [{"tag": "scope", "value": "availability"}] | no url |
| BB +3.3V Non-Critical [{ITEM.VALUE}] | HIGH | no description | last(/Intel SR1630 IPMI/bb_3.3v)<3.067 or last(/Intel SR1630 IPMI/bb_3.3v)>3.525 | [{"tag": "scope", "value": "availability"}] | no url |
| BB +3.3V STBY Critical [{ITEM.VALUE}] | DISASTER | no description | last(/Intel SR1630 IPMI/bb_3.3v_stby)<2.982 or last(/Intel SR1630 IPMI/bb_3.3v_stby)>3.625 | [{"tag": "scope", "value": "availability"}] | no url |
| BB +3.3V STBY Non-Critical [{ITEM.VALUE}] | HIGH | no description | last(/Intel SR1630 IPMI/bb_3.3v_stby)<3.067 or last(/Intel SR1630 IPMI/bb_3.3v_stby)>3.525 | [{"tag": "scope", "value": "availability"}] | no url |
| BB +5.0V Critical [{ITEM.VALUE}] | DISASTER | no description | last(/Intel SR1630 IPMI/bb_5.0v)<4.471 or last(/Intel SR1630 IPMI/bb_5.0v)>5.538 | [{"tag": "scope", "value": "availability"}] | no url |
| BB +5.0V Non-Critical [{ITEM.VALUE}] | HIGH | no description | last(/Intel SR1630 IPMI/bb_5.0v)<4.630 or last(/Intel SR1630 IPMI/bb_5.0v)>5.380 | [{"tag": "scope", "value": "availability"}] | no url |
| Front Panel Temp Critical [{ITEM.VALUE}] | DISASTER | no description | last(/Intel SR1630 IPMI/front_panel_temp)<0 or last(/Intel SR1630 IPMI/front_panel_temp)>48 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Front Panel Temp Non-Critical [{ITEM.VALUE}] | HIGH | no description | last(/Intel SR1630 IPMI/front_panel_temp)<5 or last(/Intel SR1630 IPMI/front_panel_temp)>44 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| Power | WARNING | no description | last(/Intel SR1630 IPMI/power)=0 | [{"tag": "scope", "value": "availability"}] | no url |
| System Fan 2 Critical [{ITEM.VALUE}] | DISASTER | no description | last(/Intel SR1630 IPMI/system_fan_2)<324 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| System Fan 2 Non-Critical [{ITEM.VALUE}] | HIGH | no description | last(/Intel SR1630 IPMI/system_fan_2)<378 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| System Fan 3 Critical [{ITEM.VALUE}] | DISASTER | no description | last(/Intel SR1630 IPMI/system_fan_3)<324 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |
| System Fan 3 Non-Critical [{ITEM.VALUE}] | HIGH | no description | last(/Intel SR1630 IPMI/system_fan_3)<378 | [{"tag": "scope", "value": "availability"}, {"tag": "scope", "value": "performance"}] | no url |


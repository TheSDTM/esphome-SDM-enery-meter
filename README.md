# Esphome SDM enery meter custom component

This is a fully-working example of reading data from SDM enetry meter using device with Esphome firmware.

In this implementation I am using HardwareSerial to read data from SDM, because it's more stable than SoftwareSerial.

You should use TTL to RS485 converter and connect RX port of converter to TX port of Esphome device and TX port of converter to RX port of Esphome device.

This component uses the SDM library from https://github.com/reaper7/SDM_Energy_Meter

## Example

### Configuration

``` YAML
# load the component
external_components:
  - source: github://depuits/esphome-SDM-enery-meter

# disable logging
logger:
  baud_rate: 0

# uart setup
uart:
  tx_pin: TX
  rx_pin: RX
  baud_rate: 9600
  stop_bits: 1

# sdm sensor component setup
sensor:
- platform: sdm

  # optional parameters with defaults
  baud_rate: 9600
  tx_pin: TX
  rx_pin: RX
  channel: 1
  dere_pin: 16 # -1 is disabled

  # sdm registers to read and report
  sdm_phase_1_voltage:
    name: "Voltage"
  sdm_phase_1_current:
    name: "Current"
  sdm_phase_1_power:
    name: "Power"
  sdm_import_active_energy:
    name: "Energy import"
```

### Schematic

![Schematic of ESP32 mini using MAX485](Schematic_ESP32_mini_MAX485.png)

## Register list for SDM devices


| Register config name                         | Register address | Unit        | SDM630  | SDM230  | SDM220  | SDM120CT| SDM120  | SDM72D  |
|----------------------------------------------|------------------|-------------|---------|---------|---------|---------|---------|---------|
| sdm_phase_1_voltage                          | 0x0000           | V           |    1    |    1    |    1    |    1    |    1    |         |
| sdm_phase_2_voltage                          | 0x0002           | V           |    1    |         |         |         |         |         |
| sdm_phase_3_voltage                          | 0x0004           | V           |    1    |         |         |         |         |         |
| sdm_phase_1_current                          | 0x0006           | A           |    1    |    1    |    1    |    1    |    1    |         |
| sdm_phase_2_current                          | 0x0008           | A           |    1    |         |         |         |         |         |
| sdm_phase_3_current                          | 0x000A           | A           |    1    |         |         |         |         |         |
| sdm_phase_1_power                            | 0x000C           | W           |    1    |    1    |    1    |    1    |    1    |         |
| sdm_phase_2_power                            | 0x000E           | W           |    1    |         |         |         |         |         |
| sdm_phase_3_power                            | 0x0010           | W           |    1    |         |         |         |         |         |
| sdm_phase_1_apparent_power                   | 0x0012           | VA          |    1    |    1    |    1    |    1    |    1    |         |
| sdm_phase_2_apparent_power                   | 0x0014           | VA          |    1    |         |         |         |         |         |
| sdm_phase_3_apparent_power                   | 0x0016           | VA          |    1    |         |         |         |         |         |
| sdm_phase_1_reactive_power                   | 0x0018           | VAr         |    1    |    1    |    1    |    1    |    1    |         |
| sdm_phase_2_reactive_power                   | 0x001A           | VAr         |    1    |         |         |         |         |         |
| sdm_phase_3_reactive_power                   | 0x001C           | VAr         |    1    |         |         |         |         |         |
| sdm_phase_1_power_factor                     | 0x001E           |             |    1    |    1    |    1    |    1    |    1    |         |
| sdm_phase_2_power_factor                     | 0x0020           |             |    1    |         |         |         |         |         |
| sdm_phase_3_power_factor                     | 0x0022           |             |    1    |         |         |         |         |         |
| sdm_phase_1_angle                            | 0x0024           | Degrees     |    1    |    1    |    1    |    1    |         |         |
| sdm_phase_2_angle                            | 0x0026           | Degrees     |    1    |         |         |         |         |         |
| sdm_phase_3_angle                            | 0x0028           | Degrees     |    1    |         |         |         |         |         |
| sdm_average_l_to_n_volts                     | 0x002A           | V           |    1    |         |         |         |         |         |
| sdm_average_line_current                     | 0x002E           | A           |    1    |         |         |         |         |         |
| sdm_sum_line_current                         | 0x0030           | A           |    1    |         |         |         |         |         |
| sdm_total_system_power                       | 0x0034           | W           |    1    |         |         |         |         |    1    |
| sdm_total_system_apparent_power              | 0x0038           | VA          |    1    |         |         |         |         |         |
| sdm_total_system_reactive_power              | 0x003C           | VAr         |    1    |         |         |         |         |         |
| sdm_total_system_power_factor                | 0x003E           |             |    1    |         |         |         |         |         |
| sdm_total_system_phase_angle                 | 0x0042           | Degrees     |    1    |         |         |         |         |         |
| sdm_frequency                                | 0x0046           | Hz          |    1    |    1    |    1    |    1    |    1    |         |
| sdm_import_active_energy                     | 0x0048           | kWh/MWh     |    1    |    1    |    1    |    1    |    1    |    1    |
| sdm_export_active_energy                     | 0x004A           | kWh/MWh     |    1    |    1    |    1    |    1    |    1    |    1    |
| sdm_import_reactive_energy                   | 0x004C           | kVArh/MVArh |    1    |    1    |    1    |    1    |    1    |         |
| sdm_export_reactive_energy                   | 0x004E           | kVArh/MVArh |    1    |    1    |    1    |    1    |    1    |         |
| sdm_vah_since_last_reset                     | 0x0050           | kVAh/MVAh   |    1    |         |         |         |         |         |
| sdm_ah_since_last_reset                      | 0x0052           | Ah/kAh      |    1    |         |         |         |         |         |
| sdm_total_system_power_demand                | 0x0054           | W           |    1    |    1    |         |         |         |         |
| sdm_maximum_total_system_power_demand        | 0x0056           | W           |    1    |    1    |         |         |         |         |
| sdm_current_system_positive_power_demand     | 0x0058           | W           |         |    1    |         |         |         |         |
| sdm_maximum_system_positive_power_demand     | 0x005A           | W           |         |    1    |         |         |         |         |
| sdm_current_system_reverse_power_demand      | 0x005C           | W           |         |    1    |         |         |         |         |
| sdm_maximum_system_reverse_power_demand      | 0x005E           | W           |         |    1    |         |         |         |         |
| sdm_total_system_va_demand                   | 0x0064           | VA          |    1    |         |         |         |         |         |
| sdm_maximum_total_system_va_demand           | 0x0066           | VA          |    1    |         |         |         |         |         |
| sdm_neutral_current_demand                   | 0x0068           | A           |    1    |         |         |         |         |         |
| sdm_maximum_neutral_current                  | 0x006A           | A           |    1    |         |         |         |         |         |
| sdm_line_1_to_line_2_volts                   | 0x00C8           | V           |    1    |         |         |         |         |         |
| sdm_line_2_to_line_3_volts                   | 0x00CA           | V           |    1    |         |         |         |         |         |
| sdm_line_3_to_line_1_volts                   | 0x00CC           | V           |    1    |         |         |         |         |         |
| sdm_average_line_to_line_volts               | 0x00CE           | V           |    1    |         |         |         |         |         |
| sdm_neutral_current                          | 0x00E0           | A           |    1    |         |         |         |         |         |
| sdm_phase_1_ln_volts_thd                     | 0x00EA           | %           |    1    |         |         |         |         |         |
| sdm_phase_2_ln_volts_thd                     | 0x00EC           | %           |    1    |         |         |         |         |         |
| sdm_phase_3_ln_volts_thd                     | 0x00EE           | %           |    1    |         |         |         |         |         |
| sdm_phase_1_current_thd                      | 0x00F0           | %           |    1    |         |         |         |         |         |
| sdm_phase_2_current_thd                      | 0x00F2           | %           |    1    |         |         |         |         |         |
| sdm_phase_3_current_thd                      | 0x00F4           | %           |    1    |         |         |         |         |         |
| sdm_average_line_to_neutral_volts_thd        | 0x00F8           | %           |    1    |         |         |         |         |         |
| sdm_average_line_current_thd                 | 0x00FA           | %           |    1    |         |         |         |         |         |
| sdm_total_system_power_factor_inv            | 0x00FE           |             |    1    |         |         |         |         |         |
| sdm_phase_1_current_demand                   | 0x0102           | A           |    1    |    1    |         |         |         |         |
| sdm_phase_2_current_demand                   | 0x0104           | A           |    1    |         |         |         |         |         |
| sdm_phase_3_current_demand                   | 0x0106           | A           |    1    |         |         |         |         |         |
| sdm_maximum_phase_1_current_demand           | 0x0108           | A           |    1    |    1    |         |         |         |         |
| sdm_maximum_phase_2_current_demand           | 0x010A           | A           |    1    |         |         |         |         |         |
| sdm_maximum_phase_3_current_demand           | 0x010C           | A           |    1    |         |         |         |         |         |
| sdm_line_1_to_line_2_volts_thd               | 0x014E           | %           |    1    |         |         |         |         |         |
| sdm_line_2_to_line_3_volts_thd               | 0x0150           | %           |    1    |         |         |         |         |         |
| sdm_line_3_to_line_1_volts_thd               | 0x0152           | %           |    1    |         |         |         |         |         |
| sdm_average_line_to_line_volts_thd           | 0x0154           | %           |    1    |         |         |         |         |         |
| sdm_total_active_energy                      | 0x0156           | kWh         |    1    |    1    |    1    |    1    |    1    |    1    |
| sdm_total_reactive_energy                    | 0x0158           | kVArh       |    1    |    1    |    1    |    1    |    1    |         |
| sdm_l1_import_active_energy                  | 0x015A           | kWh         |    1    |         |         |         |         |         |
| sdm_l2_import_active_energy                  | 0x015C           | kWh         |    1    |         |         |         |         |         |
| sdm_l3_import_active_energy                  | 0x015E           | kWh         |    1    |         |         |         |         |         |
| sdm_l1_export_active_energy                  | 0x0160           | kWh         |    1    |         |         |         |         |         |
| sdm_l2_export_active_energy                  | 0x0162           | kWh         |    1    |         |         |         |         |         |
| sdm_l3_export_active_energy                  | 0x0164           | kWh         |    1    |         |         |         |         |         |
| sdm_l1_total_active_energy                   | 0x0166           | kWh         |    1    |         |         |         |         |         |
| sdm_l2_total_active_energy                   | 0x0168           | kWh         |    1    |         |         |         |         |         |
| sdm_l3_total_active_energy                   | 0x016a           | kWh         |    1    |         |         |         |         |         |
| sdm_l1_import_reactive_energy                | 0x016C           | kVArh       |    1    |         |         |         |         |         |
| sdm_l2_import_reactive_energy                | 0x016E           | kVArh       |    1    |         |         |         |         |         |
| sdm_l3_import_reactive_energy                | 0x0170           | kVArh       |    1    |         |         |         |         |         |
| sdm_l1_export_reactive_energy                | 0x0172           | kVArh       |    1    |         |         |         |         |         |
| sdm_l2_export_reactive_energy                | 0x0174           | kVArh       |    1    |         |         |         |         |         |
| sdm_l3_export_reactive_energy                | 0x0176           | kVArh       |    1    |         |         |         |         |         |
| sdm_l1_total_reactive_energy                 | 0x0178           | kVArh       |    1    |         |         |         |         |         |
| sdm_l2_total_reactive_energy                 | 0x017A           | kVArh       |    1    |         |         |         |         |         |
| sdm_l3_total_reactive_energy                 | 0x017C           | kVArh       |    1    |         |         |         |         |         |
| sdm_current_resettable_total_active_energy   | 0x0180           | kWh         |         |    1    |         |         |         |    1    |
| sdm_current_resettable_total_reactive_energy | 0x0182           | kVArh       |         |    1    |         |         |         |         |
| sdm_current_resettable_import_energy         | 0x0184           | kWh         |         |         |         |         |         |    1    |
| sdm_current_resettable_export_energy         | 0x0186           | kWh         |         |         |         |         |         |    1    |
| sdm_import_power                             | 0x0500           | W           |         |         |         |         |         |    1    |
| sdm_export_power                             | 0x0502           | W           |         |         |         |         |         |    1    |


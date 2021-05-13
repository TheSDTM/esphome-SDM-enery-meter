# Esphome SDM enery meter custom component

This is a fully-working example of reading data from SDM enetry meter (I used SDM630) using device with Esphome firmware (I used Sonoff TH16).

In this implementation I am using HardwareSerial to read data from SDM, because it's more stable than SoftwareSerial.

You should use TTL to RS485 converter and connect RX port of converter to TX port of Esphome device and TX port of converter to RX port of Esphome device. I used converter like this https://aliexpress.ru/item/32833209309.html

It was developed for SDM630. You may need to change reading registers that suits your device. You can find all reggisters in sdm/SDM.h file.

Also here you can find Esphome guide to add new sensors to this code (read "Bonus: Sensors With Multiple Output Values" section): https://esphome.io/components/sensor/custom.html

```
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
  dere_pin: -1 # -1 is disabled

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

This component uses the SDM library from https://github.com/reaper7/SDM_Energy_Meter

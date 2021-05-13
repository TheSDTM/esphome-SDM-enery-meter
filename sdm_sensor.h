#pragma once

#include "esphome/core/component.h"
#include "esphome/components/sensor/sensor.h"

class SDM;

#define INODE_SET_METHOD(type, name, default) \
  type name##_{default}; \
  void set_##name(type name) { name##_ = name; }

#define INODE_READ_PUBLISH(name, reg) \
  do { if (name##_) { \
    float value = readVal(reg); \
    name##_->publish_state(value); \
  } } while(0)

namespace esphome {
namespace sdm_sensor {
  class SDMSensor : public esphome::PollingComponent {
  public:
    void setup() override;
    void update() override;
    void dump_config() override;
    float get_setup_priority() const override { return esphome::setup_priority::DATA; }

    float readVal(uint16_t reg);

    SDM *sdm;
    INODE_SET_METHOD(long, baud, 9600);
    INODE_SET_METHOD(int, dere_pin, NOT_A_PIN);
    INODE_SET_METHOD(int8_t, rx_pin, 3);
    INODE_SET_METHOD(int8_t, tx_pin, 1);

    INODE_SET_METHOD(int8_t, channel, 1);

    //TODO change sensors and variables to match
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_1_voltage, 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_1_current, 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_1_power, 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_import_active_energy, 0);
  };
} //namespace sdm_sensor
} //namespace esphome

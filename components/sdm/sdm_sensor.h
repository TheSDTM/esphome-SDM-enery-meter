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

    // List of all registers
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_1_voltage                         , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_2_voltage                         , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_3_voltage                         , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_1_current                         , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_2_current                         , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_3_current                         , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_1_power                           , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_2_power                           , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_3_power                           , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_1_apparent_power                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_2_apparent_power                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_3_apparent_power                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_1_reactive_power                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_2_reactive_power                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_3_reactive_power                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_1_power_factor                    , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_2_power_factor                    , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_3_power_factor                    , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_1_angle                           , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_2_angle                           , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_3_angle                           , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_average_l_to_n_volts                    , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_average_line_current                    , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_sum_line_current                        , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_total_system_power                      , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_total_system_apparent_power             , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_total_system_reactive_power             , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_total_system_power_factor               , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_total_system_phase_angle                , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_frequency                               , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_import_active_energy                    , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_export_active_energy                    , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_import_reactive_energy                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_export_reactive_energy                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_vah_since_last_reset                    , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_ah_since_last_reset                     , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_total_system_power_demand               , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_maximum_total_system_power_demand       , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_current_system_positive_power_demand    , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_maximum_system_positive_power_demand    , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_current_system_reverse_power_demand     , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_maximum_system_reverse_power_demand     , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_total_system_va_demand                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_maximum_total_system_va_demand          , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_neutral_current_demand                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_maximum_neutral_current                 , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_line_1_to_line_2_volts                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_line_2_to_line_3_volts                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_line_3_to_line_1_volts                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_average_line_to_line_volts              , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_neutral_current                         , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_1_ln_volts_thd                    , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_2_ln_volts_thd                    , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_3_ln_volts_thd                    , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_1_current_thd                     , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_2_current_thd                     , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_3_current_thd                     , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_average_line_to_neutral_volts_thd       , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_average_line_current_thd                , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_total_system_power_factor_inv           , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_1_current_demand                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_2_current_demand                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_phase_3_current_demand                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_maximum_phase_1_current_demand          , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_maximum_phase_2_current_demand          , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_maximum_phase_3_current_demand          , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_line_1_to_line_2_volts_thd              , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_line_2_to_line_3_volts_thd              , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_line_3_to_line_1_volts_thd              , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_average_line_to_line_volts_thd          , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_total_active_energy                     , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_total_reactive_energy                   , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l1_import_active_energy                 , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l2_import_active_energy                 , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l3_import_active_energy                 , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l1_export_active_energy                 , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l2_export_active_energy                 , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l3_export_active_energy                 , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l1_total_active_energy                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l2_total_active_energy                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l3_total_active_energy                  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l1_import_reactive_energy               , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l2_import_reactive_energy               , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l3_import_reactive_energy               , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l1_export_reactive_energy               , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l2_export_reactive_energy               , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l3_export_reactive_energy               , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l1_total_reactive_energy                , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l2_total_reactive_energy                , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_l3_total_reactive_energy                , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_current_resettable_total_active_energy  , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_current_resettable_total_reactive_energy, 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_current_resettable_import_energy        , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_current_resettable_export_energy        , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_import_power                            , 0);
    INODE_SET_METHOD(esphome::sensor::Sensor *, sdm_export_power                            , 0);

  };
} //namespace sdm_sensor
} //namespace esphome

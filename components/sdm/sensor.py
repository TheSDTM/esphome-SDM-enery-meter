import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID, \
    CONF_BAUD_RATE, CONF_RX_PIN, CONF_TX_PIN, CONF_CHANNEL, \
    UNIT_EMPTY, UNIT_AMPERE, UNIT_HERTZ, UNIT_VOLT, \
    UNIT_VOLT_AMPS, UNIT_VOLT_AMPS_REACTIVE, \
    UNIT_WATT, UNIT_WATT_HOURS, UNIT_PERCENT, UNIT_DEGREES, \
    ICON_EMPTY, ICON_PULSE, ICON_POWER, ICON_CURRENT_AC, ICON_FLASH, \
    ESP_PLATFORM_ESP32

UNIT_KWH = 'kW/h'
UNIT_KVAH = 'kVAh'
UNIT_KVARH = 'kVArh'
UNIT_AMPERE_HOURS = 'Ah'
CONF_DERE_PIN = 'dere_pin'

CONF_SDM_PHASE_1_VOLTAGE                          = 'sdm_phase_1_voltage'
CONF_SDM_PHASE_2_VOLTAGE                          = 'sdm_phase_2_voltage'
CONF_SDM_PHASE_3_VOLTAGE                          = 'sdm_phase_3_voltage'
CONF_SDM_PHASE_1_CURRENT                          = 'sdm_phase_1_current'
CONF_SDM_PHASE_2_CURRENT                          = 'sdm_phase_2_current'
CONF_SDM_PHASE_3_CURRENT                          = 'sdm_phase_3_current'
CONF_SDM_PHASE_1_POWER                            = 'sdm_phase_1_power'
CONF_SDM_PHASE_2_POWER                            = 'sdm_phase_2_power'
CONF_SDM_PHASE_3_POWER                            = 'sdm_phase_3_power'
CONF_SDM_PHASE_1_APPARENT_POWER                   = 'sdm_phase_1_apparent_power'
CONF_SDM_PHASE_2_APPARENT_POWER                   = 'sdm_phase_2_apparent_power'
CONF_SDM_PHASE_3_APPARENT_POWER                   = 'sdm_phase_3_apparent_power'
CONF_SDM_PHASE_1_REACTIVE_POWER                   = 'sdm_phase_1_reactive_power'
CONF_SDM_PHASE_2_REACTIVE_POWER                   = 'sdm_phase_2_reactive_power'
CONF_SDM_PHASE_3_REACTIVE_POWER                   = 'sdm_phase_3_reactive_power'
CONF_SDM_PHASE_1_POWER_FACTOR                     = 'sdm_phase_1_power_factor'
CONF_SDM_PHASE_2_POWER_FACTOR                     = 'sdm_phase_2_power_factor'
CONF_SDM_PHASE_3_POWER_FACTOR                     = 'sdm_phase_3_power_factor'
CONF_SDM_PHASE_1_ANGLE                            = 'sdm_phase_1_angle'
CONF_SDM_PHASE_2_ANGLE                            = 'sdm_phase_2_angle'
CONF_SDM_PHASE_3_ANGLE                            = 'sdm_phase_3_angle'
CONF_SDM_AVERAGE_L_TO_N_VOLTS                     = 'sdm_average_l_to_n_volts'
CONF_SDM_AVERAGE_LINE_CURRENT                     = 'sdm_average_line_current'
CONF_SDM_SUM_LINE_CURRENT                         = 'sdm_sum_line_current'
CONF_SDM_TOTAL_SYSTEM_POWER                       = 'sdm_total_system_power'
CONF_SDM_TOTAL_SYSTEM_APPARENT_POWER              = 'sdm_total_system_apparent_power'
CONF_SDM_TOTAL_SYSTEM_REACTIVE_POWER              = 'sdm_total_system_reactive_power'
CONF_SDM_TOTAL_SYSTEM_POWER_FACTOR                = 'sdm_total_system_power_factor'
CONF_SDM_TOTAL_SYSTEM_PHASE_ANGLE                 = 'sdm_total_system_phase_angle'
CONF_SDM_FREQUENCY                                = 'sdm_frequency'
CONF_SDM_IMPORT_ACTIVE_ENERGY                     = 'sdm_import_active_energy'
CONF_SDM_EXPORT_ACTIVE_ENERGY                     = 'sdm_export_active_energy'
CONF_SDM_IMPORT_REACTIVE_ENERGY                   = 'sdm_import_reactive_energy'
CONF_SDM_EXPORT_REACTIVE_ENERGY                   = 'sdm_export_reactive_energy'
CONF_SDM_VAH_SINCE_LAST_RESET                     = 'sdm_vah_since_last_reset'
CONF_SDM_AH_SINCE_LAST_RESET                      = 'sdm_ah_since_last_reset'
CONF_SDM_TOTAL_SYSTEM_POWER_DEMAND                = 'sdm_total_system_power_demand'
CONF_SDM_MAXIMUM_TOTAL_SYSTEM_POWER_DEMAND        = 'sdm_maximum_total_system_power_demand'
CONF_SDM_CURRENT_SYSTEM_POSITIVE_POWER_DEMAND     = 'sdm_current_system_positive_power_demand'
CONF_SDM_MAXIMUM_SYSTEM_POSITIVE_POWER_DEMAND     = 'sdm_maximum_system_positive_power_demand'
CONF_SDM_CURRENT_SYSTEM_REVERSE_POWER_DEMAND      = 'sdm_current_system_reverse_power_demand'
CONF_SDM_MAXIMUM_SYSTEM_REVERSE_POWER_DEMAND      = 'sdm_maximum_system_reverse_power_demand'
CONF_SDM_TOTAL_SYSTEM_VA_DEMAND                   = 'sdm_total_system_va_demand'
CONF_SDM_MAXIMUM_TOTAL_SYSTEM_VA_DEMAND           = 'sdm_maximum_total_system_va_demand'
CONF_SDM_NEUTRAL_CURRENT_DEMAND                   = 'sdm_neutral_current_demand'
CONF_SDM_MAXIMUM_NEUTRAL_CURRENT                  = 'sdm_maximum_neutral_current'
CONF_SDM_LINE_1_TO_LINE_2_VOLTS                   = 'sdm_line_1_to_line_2_volts'
CONF_SDM_LINE_2_TO_LINE_3_VOLTS                   = 'sdm_line_2_to_line_3_volts'
CONF_SDM_LINE_3_TO_LINE_1_VOLTS                   = 'sdm_line_3_to_line_1_volts'
CONF_SDM_AVERAGE_LINE_TO_LINE_VOLTS               = 'sdm_average_line_to_line_volts'
CONF_SDM_NEUTRAL_CURRENT                          = 'sdm_neutral_current'
CONF_SDM_PHASE_1_LN_VOLTS_THD                     = 'sdm_phase_1_ln_volts_thd'
CONF_SDM_PHASE_2_LN_VOLTS_THD                     = 'sdm_phase_2_ln_volts_thd'
CONF_SDM_PHASE_3_LN_VOLTS_THD                     = 'sdm_phase_3_ln_volts_thd'
CONF_SDM_PHASE_1_CURRENT_THD                      = 'sdm_phase_1_current_thd'
CONF_SDM_PHASE_2_CURRENT_THD                      = 'sdm_phase_2_current_thd'
CONF_SDM_PHASE_3_CURRENT_THD                      = 'sdm_phase_3_current_thd'
CONF_SDM_AVERAGE_LINE_TO_NEUTRAL_VOLTS_THD        = 'sdm_average_line_to_neutral_volts_thd'
CONF_SDM_AVERAGE_LINE_CURRENT_THD                 = 'sdm_average_line_current_thd'
CONF_SDM_TOTAL_SYSTEM_POWER_FACTOR_INV            = 'sdm_total_system_power_factor_inv'
CONF_SDM_PHASE_1_CURRENT_DEMAND                   = 'sdm_phase_1_current_demand'
CONF_SDM_PHASE_2_CURRENT_DEMAND                   = 'sdm_phase_2_current_demand'
CONF_SDM_PHASE_3_CURRENT_DEMAND                   = 'sdm_phase_3_current_demand'
CONF_SDM_MAXIMUM_PHASE_1_CURRENT_DEMAND           = 'sdm_maximum_phase_1_current_demand'
CONF_SDM_MAXIMUM_PHASE_2_CURRENT_DEMAND           = 'sdm_maximum_phase_2_current_demand'
CONF_SDM_MAXIMUM_PHASE_3_CURRENT_DEMAND           = 'sdm_maximum_phase_3_current_demand'
CONF_SDM_LINE_1_TO_LINE_2_VOLTS_THD               = 'sdm_line_1_to_line_2_volts_thd'
CONF_SDM_LINE_2_TO_LINE_3_VOLTS_THD               = 'sdm_line_2_to_line_3_volts_thd'
CONF_SDM_LINE_3_TO_LINE_1_VOLTS_THD               = 'sdm_line_3_to_line_1_volts_thd'
CONF_SDM_AVERAGE_LINE_TO_LINE_VOLTS_THD           = 'sdm_average_line_to_line_volts_thd'
CONF_SDM_TOTAL_ACTIVE_ENERGY                      = 'sdm_total_active_energy'
CONF_SDM_TOTAL_REACTIVE_ENERGY                    = 'sdm_total_reactive_energy'
CONF_SDM_L1_IMPORT_ACTIVE_ENERGY                  = 'sdm_l1_import_active_energy'
CONF_SDM_L2_IMPORT_ACTIVE_ENERGY                  = 'sdm_l2_import_active_energy'
CONF_SDM_L3_IMPORT_ACTIVE_ENERGY                  = 'sdm_l3_import_active_energy'
CONF_SDM_L1_EXPORT_ACTIVE_ENERGY                  = 'sdm_l1_export_active_energy'
CONF_SDM_L2_EXPORT_ACTIVE_ENERGY                  = 'sdm_l2_export_active_energy'
CONF_SDM_L3_EXPORT_ACTIVE_ENERGY                  = 'sdm_l3_export_active_energy'
CONF_SDM_L1_TOTAL_ACTIVE_ENERGY                   = 'sdm_l1_total_active_energy'
CONF_SDM_L2_TOTAL_ACTIVE_ENERGY                   = 'sdm_l2_total_active_energy'
CONF_SDM_L3_TOTAL_ACTIVE_ENERGY                   = 'sdm_l3_total_active_energy'
CONF_SDM_L1_IMPORT_REACTIVE_ENERGY                = 'sdm_l1_import_reactive_energy'
CONF_SDM_L2_IMPORT_REACTIVE_ENERGY                = 'sdm_l2_import_reactive_energy'
CONF_SDM_L3_IMPORT_REACTIVE_ENERGY                = 'sdm_l3_import_reactive_energy'
CONF_SDM_L1_EXPORT_REACTIVE_ENERGY                = 'sdm_l1_export_reactive_energy'
CONF_SDM_L2_EXPORT_REACTIVE_ENERGY                = 'sdm_l2_export_reactive_energy'
CONF_SDM_L3_EXPORT_REACTIVE_ENERGY                = 'sdm_l3_export_reactive_energy'
CONF_SDM_L1_TOTAL_REACTIVE_ENERGY                 = 'sdm_l1_total_reactive_energy'
CONF_SDM_L2_TOTAL_REACTIVE_ENERGY                 = 'sdm_l2_total_reactive_energy'
CONF_SDM_L3_TOTAL_REACTIVE_ENERGY                 = 'sdm_l3_total_reactive_energy'
CONF_SDM_CURRENT_RESETTABLE_TOTAL_ACTIVE_ENERGY   = 'sdm_current_resettable_total_active_energy'
CONF_SDM_CURRENT_RESETTABLE_TOTAL_REACTIVE_ENERGY = 'sdm_current_resettable_total_reactive_energy'
CONF_SDM_CURRENT_RESETTABLE_IMPORT_ENERGY         = 'sdm_current_resettable_import_energy'
CONF_SDM_CURRENT_RESETTABLE_EXPORT_ENERGY         = 'sdm_current_resettable_export_energy'
CONF_SDM_IMPORT_POWER                             = 'sdm_import_power'
CONF_SDM_EXPORT_POWER                             = 'sdm_export_power'


ESP_PLATFORMS = [ESP_PLATFORM_ESP32]

sdm_sensor_ns = cg.esphome_ns.namespace('sdm_sensor')
SDMSensor = sdm_sensor_ns.class_('SDMSensor', cg.PollingComponent)


CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(SDMSensor),

    cv.Optional(CONF_BAUD_RATE, default=9600): cv.positive_not_null_int,
    cv.Optional(CONF_DERE_PIN, default=-1): cv.int_range(),
    cv.Optional(CONF_RX_PIN, default=3): cv.positive_int,
    cv.Optional(CONF_TX_PIN, default=1): cv.positive_int,
    cv.Optional(CONF_CHANNEL, default=1): cv.positive_not_null_int,

    cv.Optional(CONF_SDM_PHASE_1_VOLTAGE                          ): sensor.sensor_schema(UNIT_VOLT              , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_2_VOLTAGE                          ): sensor.sensor_schema(UNIT_VOLT              , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_3_VOLTAGE                          ): sensor.sensor_schema(UNIT_VOLT              , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_1_CURRENT                          ): sensor.sensor_schema(UNIT_AMPERE            , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_2_CURRENT                          ): sensor.sensor_schema(UNIT_AMPERE            , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_3_CURRENT                          ): sensor.sensor_schema(UNIT_AMPERE            , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_1_POWER                            ): sensor.sensor_schema(UNIT_WATT              , ICON_POWER, 1),
    cv.Optional(CONF_SDM_PHASE_2_POWER                            ): sensor.sensor_schema(UNIT_WATT              , ICON_POWER, 1),
    cv.Optional(CONF_SDM_PHASE_3_POWER                            ): sensor.sensor_schema(UNIT_WATT              , ICON_POWER, 1),
    cv.Optional(CONF_SDM_PHASE_1_APPARENT_POWER                   ): sensor.sensor_schema(UNIT_VOLT_AMPS         , ICON_POWER, 1),
    cv.Optional(CONF_SDM_PHASE_2_APPARENT_POWER                   ): sensor.sensor_schema(UNIT_VOLT_AMPS         , ICON_POWER, 1),
    cv.Optional(CONF_SDM_PHASE_3_APPARENT_POWER                   ): sensor.sensor_schema(UNIT_VOLT_AMPS         , ICON_POWER, 1),
    cv.Optional(CONF_SDM_PHASE_1_REACTIVE_POWER                   ): sensor.sensor_schema(UNIT_VOLT_AMPS_REACTIVE, ICON_POWER, 1),
    cv.Optional(CONF_SDM_PHASE_2_REACTIVE_POWER                   ): sensor.sensor_schema(UNIT_VOLT_AMPS_REACTIVE, ICON_POWER, 1),
    cv.Optional(CONF_SDM_PHASE_3_REACTIVE_POWER                   ): sensor.sensor_schema(UNIT_VOLT_AMPS_REACTIVE, ICON_POWER, 1),
    cv.Optional(CONF_SDM_PHASE_1_POWER_FACTOR                     ): sensor.sensor_schema(UNIT_EMPTY             , ICON_POWER, 1),
    cv.Optional(CONF_SDM_PHASE_2_POWER_FACTOR                     ): sensor.sensor_schema(UNIT_EMPTY             , ICON_POWER, 1),
    cv.Optional(CONF_SDM_PHASE_3_POWER_FACTOR                     ): sensor.sensor_schema(UNIT_EMPTY             , ICON_POWER, 1),
    cv.Optional(CONF_SDM_PHASE_1_ANGLE                            ): sensor.sensor_schema(UNIT_DEGREES           , ICON_PULSE, 1),
    cv.Optional(CONF_SDM_PHASE_2_ANGLE                            ): sensor.sensor_schema(UNIT_DEGREES           , ICON_PULSE, 1),
    cv.Optional(CONF_SDM_PHASE_3_ANGLE                            ): sensor.sensor_schema(UNIT_DEGREES           , ICON_PULSE, 1),
    cv.Optional(CONF_SDM_AVERAGE_L_TO_N_VOLTS                     ): sensor.sensor_schema(UNIT_VOLT              , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_AVERAGE_LINE_CURRENT                     ): sensor.sensor_schema(UNIT_AMPERE            , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_SUM_LINE_CURRENT                         ): sensor.sensor_schema(UNIT_AMPERE            , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_TOTAL_SYSTEM_POWER                       ): sensor.sensor_schema(UNIT_WATT              , ICON_POWER, 1),
    cv.Optional(CONF_SDM_TOTAL_SYSTEM_APPARENT_POWER              ): sensor.sensor_schema(UNIT_VOLT_AMPS         , ICON_POWER, 1),
    cv.Optional(CONF_SDM_TOTAL_SYSTEM_REACTIVE_POWER              ): sensor.sensor_schema(UNIT_VOLT_AMPS_REACTIVE, ICON_POWER, 1),
    cv.Optional(CONF_SDM_TOTAL_SYSTEM_POWER_FACTOR                ): sensor.sensor_schema(UNIT_EMPTY             , ICON_POWER, 1),
    cv.Optional(CONF_SDM_TOTAL_SYSTEM_PHASE_ANGLE                 ): sensor.sensor_schema(UNIT_DEGREES           , ICON_PULSE, 1),
    cv.Optional(CONF_SDM_FREQUENCY                                ): sensor.sensor_schema(UNIT_HERTZ             , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_IMPORT_ACTIVE_ENERGY                     ): sensor.sensor_schema(UNIT_KWH               , ICON_FLASH, 1),
    cv.Optional(CONF_SDM_EXPORT_ACTIVE_ENERGY                     ): sensor.sensor_schema(UNIT_KWH               , ICON_FLASH, 1),
    cv.Optional(CONF_SDM_IMPORT_REACTIVE_ENERGY                   ): sensor.sensor_schema(UNIT_KVARH             , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_EXPORT_REACTIVE_ENERGY                   ): sensor.sensor_schema(UNIT_KVARH             , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_VAH_SINCE_LAST_RESET                     ): sensor.sensor_schema(UNIT_KVAH              , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_AH_SINCE_LAST_RESET                      ): sensor.sensor_schema(UNIT_AMPERE_HOURS      , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_TOTAL_SYSTEM_POWER_DEMAND                ): sensor.sensor_schema(UNIT_WATT              , ICON_POWER, 1),
    cv.Optional(CONF_SDM_MAXIMUM_TOTAL_SYSTEM_POWER_DEMAND        ): sensor.sensor_schema(UNIT_WATT              , ICON_POWER, 1),
    cv.Optional(CONF_SDM_CURRENT_SYSTEM_POSITIVE_POWER_DEMAND     ): sensor.sensor_schema(UNIT_WATT              , ICON_POWER, 1),
    cv.Optional(CONF_SDM_MAXIMUM_SYSTEM_POSITIVE_POWER_DEMAND     ): sensor.sensor_schema(UNIT_WATT              , ICON_POWER, 1),
    cv.Optional(CONF_SDM_CURRENT_SYSTEM_REVERSE_POWER_DEMAND      ): sensor.sensor_schema(UNIT_WATT              , ICON_POWER, 1),
    cv.Optional(CONF_SDM_MAXIMUM_SYSTEM_REVERSE_POWER_DEMAND      ): sensor.sensor_schema(UNIT_WATT              , ICON_POWER, 1),
    cv.Optional(CONF_SDM_TOTAL_SYSTEM_VA_DEMAND                   ): sensor.sensor_schema(UNIT_VOLT_AMPS         , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_MAXIMUM_TOTAL_SYSTEM_VA_DEMAND           ): sensor.sensor_schema(UNIT_VOLT_AMPS         , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_NEUTRAL_CURRENT_DEMAND                   ): sensor.sensor_schema(UNIT_AMPERE            , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_MAXIMUM_NEUTRAL_CURRENT                  ): sensor.sensor_schema(UNIT_AMPERE            , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_LINE_1_TO_LINE_2_VOLTS                   ): sensor.sensor_schema(UNIT_VOLT              , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_LINE_2_TO_LINE_3_VOLTS                   ): sensor.sensor_schema(UNIT_VOLT              , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_LINE_3_TO_LINE_1_VOLTS                   ): sensor.sensor_schema(UNIT_VOLT              , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_AVERAGE_LINE_TO_LINE_VOLTS               ): sensor.sensor_schema(UNIT_VOLT              , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_NEUTRAL_CURRENT                          ): sensor.sensor_schema(UNIT_AMPERE            , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_1_LN_VOLTS_THD                     ): sensor.sensor_schema(UNIT_PERCENT           , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_2_LN_VOLTS_THD                     ): sensor.sensor_schema(UNIT_PERCENT           , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_3_LN_VOLTS_THD                     ): sensor.sensor_schema(UNIT_PERCENT           , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_1_CURRENT_THD                      ): sensor.sensor_schema(UNIT_PERCENT           , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_2_CURRENT_THD                      ): sensor.sensor_schema(UNIT_PERCENT           , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_3_CURRENT_THD                      ): sensor.sensor_schema(UNIT_PERCENT           , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_AVERAGE_LINE_TO_NEUTRAL_VOLTS_THD        ): sensor.sensor_schema(UNIT_PERCENT           , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_AVERAGE_LINE_CURRENT_THD                 ): sensor.sensor_schema(UNIT_PERCENT           , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_TOTAL_SYSTEM_POWER_FACTOR_INV            ): sensor.sensor_schema(UNIT_EMPTY             , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_1_CURRENT_DEMAND                   ): sensor.sensor_schema(UNIT_AMPERE            , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_2_CURRENT_DEMAND                   ): sensor.sensor_schema(UNIT_AMPERE            , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_3_CURRENT_DEMAND                   ): sensor.sensor_schema(UNIT_AMPERE            , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_MAXIMUM_PHASE_1_CURRENT_DEMAND           ): sensor.sensor_schema(UNIT_AMPERE            , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_MAXIMUM_PHASE_2_CURRENT_DEMAND           ): sensor.sensor_schema(UNIT_AMPERE            , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_MAXIMUM_PHASE_3_CURRENT_DEMAND           ): sensor.sensor_schema(UNIT_AMPERE            , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_LINE_1_TO_LINE_2_VOLTS_THD               ): sensor.sensor_schema(UNIT_PERCENT           , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_LINE_2_TO_LINE_3_VOLTS_THD               ): sensor.sensor_schema(UNIT_PERCENT           , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_LINE_3_TO_LINE_1_VOLTS_THD               ): sensor.sensor_schema(UNIT_PERCENT           , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_AVERAGE_LINE_TO_LINE_VOLTS_THD           ): sensor.sensor_schema(UNIT_PERCENT           , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_TOTAL_ACTIVE_ENERGY                      ): sensor.sensor_schema(UNIT_KWH               , ICON_FLASH, 1),
    cv.Optional(CONF_SDM_TOTAL_REACTIVE_ENERGY                    ): sensor.sensor_schema(UNIT_KVARH             , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_L1_IMPORT_ACTIVE_ENERGY                  ): sensor.sensor_schema(UNIT_KWH               , ICON_FLASH, 1),
    cv.Optional(CONF_SDM_L2_IMPORT_ACTIVE_ENERGY                  ): sensor.sensor_schema(UNIT_KWH               , ICON_FLASH, 1),
    cv.Optional(CONF_SDM_L3_IMPORT_ACTIVE_ENERGY                  ): sensor.sensor_schema(UNIT_KWH               , ICON_FLASH, 1),
    cv.Optional(CONF_SDM_L1_EXPORT_ACTIVE_ENERGY                  ): sensor.sensor_schema(UNIT_KWH               , ICON_FLASH, 1),
    cv.Optional(CONF_SDM_L2_EXPORT_ACTIVE_ENERGY                  ): sensor.sensor_schema(UNIT_KWH               , ICON_FLASH, 1),
    cv.Optional(CONF_SDM_L3_EXPORT_ACTIVE_ENERGY                  ): sensor.sensor_schema(UNIT_KWH               , ICON_FLASH, 1),
    cv.Optional(CONF_SDM_L1_TOTAL_ACTIVE_ENERGY                   ): sensor.sensor_schema(UNIT_KWH               , ICON_FLASH, 1),
    cv.Optional(CONF_SDM_L2_TOTAL_ACTIVE_ENERGY                   ): sensor.sensor_schema(UNIT_KWH               , ICON_FLASH, 1),
    cv.Optional(CONF_SDM_L3_TOTAL_ACTIVE_ENERGY                   ): sensor.sensor_schema(UNIT_KWH               , ICON_FLASH, 1),
    cv.Optional(CONF_SDM_L1_IMPORT_REACTIVE_ENERGY                ): sensor.sensor_schema(UNIT_KVARH             , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_L2_IMPORT_REACTIVE_ENERGY                ): sensor.sensor_schema(UNIT_KVARH             , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_L3_IMPORT_REACTIVE_ENERGY                ): sensor.sensor_schema(UNIT_KVARH             , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_L1_EXPORT_REACTIVE_ENERGY                ): sensor.sensor_schema(UNIT_KVARH             , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_L2_EXPORT_REACTIVE_ENERGY                ): sensor.sensor_schema(UNIT_KVARH             , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_L3_EXPORT_REACTIVE_ENERGY                ): sensor.sensor_schema(UNIT_KVARH             , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_L1_TOTAL_REACTIVE_ENERGY                 ): sensor.sensor_schema(UNIT_KVARH             , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_L2_TOTAL_REACTIVE_ENERGY                 ): sensor.sensor_schema(UNIT_KVARH             , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_L3_TOTAL_REACTIVE_ENERGY                 ): sensor.sensor_schema(UNIT_KVARH             , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_CURRENT_RESETTABLE_TOTAL_ACTIVE_ENERGY   ): sensor.sensor_schema(UNIT_KWH               , ICON_FLASH, 1),
    cv.Optional(CONF_SDM_CURRENT_RESETTABLE_TOTAL_REACTIVE_ENERGY ): sensor.sensor_schema(UNIT_KVARH             , ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_CURRENT_RESETTABLE_IMPORT_ENERGY         ): sensor.sensor_schema(UNIT_KWH               , ICON_FLASH, 1),
    cv.Optional(CONF_SDM_CURRENT_RESETTABLE_EXPORT_ENERGY         ): sensor.sensor_schema(UNIT_KWH               , ICON_FLASH, 1),
    cv.Optional(CONF_SDM_IMPORT_POWER                             ): sensor.sensor_schema(UNIT_WATT              , ICON_POWER, 1),
    cv.Optional(CONF_SDM_EXPORT_POWER                             ): sensor.sensor_schema(UNIT_WATT              , ICON_POWER, 1),

}).extend(cv.polling_component_schema('10s'))

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)

    cg.add(var.set_baud(config[CONF_BAUD_RATE]))
    cg.add(var.set_dere_pin(config[CONF_DERE_PIN]))
    cg.add(var.set_rx_pin(config[CONF_RX_PIN]))
    cg.add(var.set_tx_pin(config[CONF_TX_PIN]))
    cg.add(var.set_channel(config[CONF_CHANNEL]))

    if CONF_SDM_PHASE_1_VOLTAGE in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_1_VOLTAGE])
        cg.add(var.set_sdm_phase_1_voltage(sens))
    if CONF_SDM_PHASE_2_VOLTAGE in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_2_VOLTAGE])
        cg.add(var.set_sdm_phase_2_voltage(sens))
    if CONF_SDM_PHASE_3_VOLTAGE in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_3_VOLTAGE])
        cg.add(var.set_sdm_phase_3_voltage(sens))
    if CONF_SDM_PHASE_1_CURRENT in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_1_CURRENT])
        cg.add(var.set_sdm_phase_1_current(sens))
    if CONF_SDM_PHASE_2_CURRENT in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_2_CURRENT])
        cg.add(var.set_sdm_phase_2_current(sens))
    if CONF_SDM_PHASE_3_CURRENT in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_3_CURRENT])
        cg.add(var.set_sdm_phase_3_current(sens))
    if CONF_SDM_PHASE_1_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_1_POWER])
        cg.add(var.set_sdm_phase_1_power(sens))
    if CONF_SDM_PHASE_2_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_2_POWER])
        cg.add(var.set_sdm_phase_2_power(sens))
    if CONF_SDM_PHASE_3_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_3_POWER])
        cg.add(var.set_sdm_phase_3_power(sens))
    if CONF_SDM_PHASE_1_APPARENT_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_1_APPARENT_POWER])
        cg.add(var.set_sdm_phase_1_apparent_power(sens))
    if CONF_SDM_PHASE_2_APPARENT_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_2_APPARENT_POWER])
        cg.add(var.set_sdm_phase_2_apparent_power(sens))
    if CONF_SDM_PHASE_3_APPARENT_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_3_APPARENT_POWER])
        cg.add(var.set_sdm_phase_3_apparent_power(sens))
    if CONF_SDM_PHASE_1_REACTIVE_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_1_REACTIVE_POWER])
        cg.add(var.set_sdm_phase_1_reactive_power(sens))
    if CONF_SDM_PHASE_2_REACTIVE_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_2_REACTIVE_POWER])
        cg.add(var.set_sdm_phase_2_reactive_power(sens))
    if CONF_SDM_PHASE_3_REACTIVE_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_3_REACTIVE_POWER])
        cg.add(var.set_sdm_phase_3_reactive_power(sens))
    if CONF_SDM_PHASE_1_POWER_FACTOR in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_1_POWER_FACTOR])
        cg.add(var.set_sdm_phase_1_power_factor(sens))
    if CONF_SDM_PHASE_2_POWER_FACTOR in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_2_POWER_FACTOR])
        cg.add(var.set_sdm_phase_2_power_factor(sens))
    if CONF_SDM_PHASE_3_POWER_FACTOR in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_3_POWER_FACTOR])
        cg.add(var.set_sdm_phase_3_power_factor(sens))
    if CONF_SDM_PHASE_1_ANGLE in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_1_ANGLE])
        cg.add(var.set_sdm_phase_1_angle(sens))
    if CONF_SDM_PHASE_2_ANGLE in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_2_ANGLE])
        cg.add(var.set_sdm_phase_2_angle(sens))
    if CONF_SDM_PHASE_3_ANGLE in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_3_ANGLE])
        cg.add(var.set_sdm_phase_3_angle(sens))
    if CONF_SDM_AVERAGE_L_TO_N_VOLTS in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_AVERAGE_L_TO_N_VOLTS])
        cg.add(var.set_sdm_average_l_to_n_volts(sens))
    if CONF_SDM_AVERAGE_LINE_CURRENT in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_AVERAGE_LINE_CURRENT])
        cg.add(var.set_sdm_average_line_current(sens))
    if CONF_SDM_SUM_LINE_CURRENT in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_SUM_LINE_CURRENT])
        cg.add(var.set_sdm_sum_line_current(sens))
    if CONF_SDM_TOTAL_SYSTEM_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_TOTAL_SYSTEM_POWER])
        cg.add(var.set_sdm_total_system_power(sens))
    if CONF_SDM_TOTAL_SYSTEM_APPARENT_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_TOTAL_SYSTEM_APPARENT_POWER])
        cg.add(var.set_sdm_total_system_apparent_power(sens))
    if CONF_SDM_TOTAL_SYSTEM_REACTIVE_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_TOTAL_SYSTEM_REACTIVE_POWER])
        cg.add(var.set_sdm_total_system_reactive_power(sens))
    if CONF_SDM_TOTAL_SYSTEM_POWER_FACTOR in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_TOTAL_SYSTEM_POWER_FACTOR])
        cg.add(var.set_sdm_total_system_power_factor(sens))
    if CONF_SDM_TOTAL_SYSTEM_PHASE_ANGLE in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_TOTAL_SYSTEM_PHASE_ANGLE])
        cg.add(var.set_sdm_total_system_phase_angle(sens))
    if CONF_SDM_FREQUENCY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_FREQUENCY])
        cg.add(var.set_sdm_frequency(sens))
    if CONF_SDM_IMPORT_ACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_IMPORT_ACTIVE_ENERGY])
        cg.add(var.set_sdm_import_active_energy(sens))
    if CONF_SDM_EXPORT_ACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_EXPORT_ACTIVE_ENERGY])
        cg.add(var.set_sdm_export_active_energy(sens))
    if CONF_SDM_IMPORT_REACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_IMPORT_REACTIVE_ENERGY])
        cg.add(var.set_sdm_import_reactive_energy(sens))
    if CONF_SDM_EXPORT_REACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_EXPORT_REACTIVE_ENERGY])
        cg.add(var.set_sdm_export_reactive_energy(sens))
    if CONF_SDM_VAH_SINCE_LAST_RESET in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_VAH_SINCE_LAST_RESET])
        cg.add(var.set_sdm_vah_since_last_reset(sens))
    if CONF_SDM_AH_SINCE_LAST_RESET in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_AH_SINCE_LAST_RESET])
        cg.add(var.set_sdm_ah_since_last_reset(sens))
    if CONF_SDM_TOTAL_SYSTEM_POWER_DEMAND in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_TOTAL_SYSTEM_POWER_DEMAND])
        cg.add(var.set_sdm_total_system_power_demand(sens))
    if CONF_SDM_MAXIMUM_TOTAL_SYSTEM_POWER_DEMAND in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_MAXIMUM_TOTAL_SYSTEM_POWER_DEMAND])
        cg.add(var.set_sdm_maximum_total_system_power_demand(sens))
    if CONF_SDM_CURRENT_SYSTEM_POSITIVE_POWER_DEMAND in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_CURRENT_SYSTEM_POSITIVE_POWER_DEMAND])
        cg.add(var.set_sdm_current_system_positive_power_demand(sens))
    if CONF_SDM_MAXIMUM_SYSTEM_POSITIVE_POWER_DEMAND in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_MAXIMUM_SYSTEM_POSITIVE_POWER_DEMAND])
        cg.add(var.set_sdm_maximum_system_positive_power_demand(sens))
    if CONF_SDM_CURRENT_SYSTEM_REVERSE_POWER_DEMAND in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_CURRENT_SYSTEM_REVERSE_POWER_DEMAND])
        cg.add(var.set_sdm_current_system_reverse_power_demand(sens))
    if CONF_SDM_MAXIMUM_SYSTEM_REVERSE_POWER_DEMAND in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_MAXIMUM_SYSTEM_REVERSE_POWER_DEMAND])
        cg.add(var.set_sdm_maximum_system_reverse_power_demand(sens))
    if CONF_SDM_TOTAL_SYSTEM_VA_DEMAND in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_TOTAL_SYSTEM_VA_DEMAND])
        cg.add(var.set_sdm_total_system_va_demand(sens))
    if CONF_SDM_MAXIMUM_TOTAL_SYSTEM_VA_DEMAND in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_MAXIMUM_TOTAL_SYSTEM_VA_DEMAND])
        cg.add(var.set_sdm_maximum_total_system_va_demand(sens))
    if CONF_SDM_NEUTRAL_CURRENT_DEMAND in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_NEUTRAL_CURRENT_DEMAND])
        cg.add(var.set_sdm_neutral_current_demand(sens))
    if CONF_SDM_MAXIMUM_NEUTRAL_CURRENT in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_MAXIMUM_NEUTRAL_CURRENT])
        cg.add(var.set_sdm_maximum_neutral_current(sens))
    if CONF_SDM_LINE_1_TO_LINE_2_VOLTS in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_LINE_1_TO_LINE_2_VOLTS])
        cg.add(var.set_sdm_line_1_to_line_2_volts(sens))
    if CONF_SDM_LINE_2_TO_LINE_3_VOLTS in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_LINE_2_TO_LINE_3_VOLTS])
        cg.add(var.set_sdm_line_2_to_line_3_volts(sens))
    if CONF_SDM_LINE_3_TO_LINE_1_VOLTS in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_LINE_3_TO_LINE_1_VOLTS])
        cg.add(var.set_sdm_line_3_to_line_1_volts(sens))
    if CONF_SDM_AVERAGE_LINE_TO_LINE_VOLTS in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_AVERAGE_LINE_TO_LINE_VOLTS])
        cg.add(var.set_sdm_average_line_to_line_volts(sens))
    if CONF_SDM_NEUTRAL_CURRENT in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_NEUTRAL_CURRENT])
        cg.add(var.set_sdm_neutral_current(sens))
    if CONF_SDM_PHASE_1_LN_VOLTS_THD in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_1_LN_VOLTS_THD])
        cg.add(var.set_sdm_phase_1_ln_volts_thd(sens))
    if CONF_SDM_PHASE_2_LN_VOLTS_THD in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_2_LN_VOLTS_THD])
        cg.add(var.set_sdm_phase_2_ln_volts_thd(sens))
    if CONF_SDM_PHASE_3_LN_VOLTS_THD in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_3_LN_VOLTS_THD])
        cg.add(var.set_sdm_phase_3_ln_volts_thd(sens))
    if CONF_SDM_PHASE_1_CURRENT_THD in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_1_CURRENT_THD])
        cg.add(var.set_sdm_phase_1_current_thd(sens))
    if CONF_SDM_PHASE_2_CURRENT_THD in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_2_CURRENT_THD])
        cg.add(var.set_sdm_phase_2_current_thd(sens))
    if CONF_SDM_PHASE_3_CURRENT_THD in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_3_CURRENT_THD])
        cg.add(var.set_sdm_phase_3_current_thd(sens))
    if CONF_SDM_AVERAGE_LINE_TO_NEUTRAL_VOLTS_THD in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_AVERAGE_LINE_TO_NEUTRAL_VOLTS_THD])
        cg.add(var.set_sdm_average_line_to_neutral_volts_thd(sens))
    if CONF_SDM_AVERAGE_LINE_CURRENT_THD in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_AVERAGE_LINE_CURRENT_THD])
        cg.add(var.set_sdm_average_line_current_thd(sens))
    if CONF_SDM_TOTAL_SYSTEM_POWER_FACTOR_INV in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_TOTAL_SYSTEM_POWER_FACTOR_INV])
        cg.add(var.set_sdm_total_system_power_factor_inv(sens))
    if CONF_SDM_PHASE_1_CURRENT_DEMAND in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_1_CURRENT_DEMAND])
        cg.add(var.set_sdm_phase_1_current_demand(sens))
    if CONF_SDM_PHASE_2_CURRENT_DEMAND in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_2_CURRENT_DEMAND])
        cg.add(var.set_sdm_phase_2_current_demand(sens))
    if CONF_SDM_PHASE_3_CURRENT_DEMAND in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_3_CURRENT_DEMAND])
        cg.add(var.set_sdm_phase_3_current_demand(sens))
    if CONF_SDM_MAXIMUM_PHASE_1_CURRENT_DEMAND in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_MAXIMUM_PHASE_1_CURRENT_DEMAND])
        cg.add(var.set_sdm_maximum_phase_1_current_demand(sens))
    if CONF_SDM_MAXIMUM_PHASE_2_CURRENT_DEMAND in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_MAXIMUM_PHASE_2_CURRENT_DEMAND])
        cg.add(var.set_sdm_maximum_phase_2_current_demand(sens))
    if CONF_SDM_MAXIMUM_PHASE_3_CURRENT_DEMAND in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_MAXIMUM_PHASE_3_CURRENT_DEMAND])
        cg.add(var.set_sdm_maximum_phase_3_current_demand(sens))
    if CONF_SDM_LINE_1_TO_LINE_2_VOLTS_THD in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_LINE_1_TO_LINE_2_VOLTS_THD])
        cg.add(var.set_sdm_line_1_to_line_2_volts_thd(sens))
    if CONF_SDM_LINE_2_TO_LINE_3_VOLTS_THD in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_LINE_2_TO_LINE_3_VOLTS_THD])
        cg.add(var.set_sdm_line_2_to_line_3_volts_thd(sens))
    if CONF_SDM_LINE_3_TO_LINE_1_VOLTS_THD in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_LINE_3_TO_LINE_1_VOLTS_THD])
        cg.add(var.set_sdm_line_3_to_line_1_volts_thd(sens))
    if CONF_SDM_AVERAGE_LINE_TO_LINE_VOLTS_THD in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_AVERAGE_LINE_TO_LINE_VOLTS_THD])
        cg.add(var.set_sdm_average_line_to_line_volts_thd(sens))
    if CONF_SDM_TOTAL_ACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_TOTAL_ACTIVE_ENERGY])
        cg.add(var.set_sdm_total_active_energy(sens))
    if CONF_SDM_TOTAL_REACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_TOTAL_REACTIVE_ENERGY])
        cg.add(var.set_sdm_total_reactive_energy(sens))
    if CONF_SDM_L1_IMPORT_ACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L1_IMPORT_ACTIVE_ENERGY])
        cg.add(var.set_sdm_l1_import_active_energy(sens))
    if CONF_SDM_L2_IMPORT_ACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L2_IMPORT_ACTIVE_ENERGY])
        cg.add(var.set_sdm_l2_import_active_energy(sens))
    if CONF_SDM_L3_IMPORT_ACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L3_IMPORT_ACTIVE_ENERGY])
        cg.add(var.set_sdm_l3_import_active_energy(sens))
    if CONF_SDM_L1_EXPORT_ACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L1_EXPORT_ACTIVE_ENERGY])
        cg.add(var.set_sdm_l1_export_active_energy(sens))
    if CONF_SDM_L2_EXPORT_ACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L2_EXPORT_ACTIVE_ENERGY])
        cg.add(var.set_sdm_l2_export_active_energy(sens))
    if CONF_SDM_L3_EXPORT_ACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L3_EXPORT_ACTIVE_ENERGY])
        cg.add(var.set_sdm_l3_export_active_energy(sens))
    if CONF_SDM_L1_TOTAL_ACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L1_TOTAL_ACTIVE_ENERGY])
        cg.add(var.set_sdm_l1_total_active_energy(sens))
    if CONF_SDM_L2_TOTAL_ACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L2_TOTAL_ACTIVE_ENERGY])
        cg.add(var.set_sdm_l2_total_active_energy(sens))
    if CONF_SDM_L3_TOTAL_ACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L3_TOTAL_ACTIVE_ENERGY])
        cg.add(var.set_sdm_l3_total_active_energy(sens))
    if CONF_SDM_L1_IMPORT_REACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L1_IMPORT_REACTIVE_ENERGY])
        cg.add(var.set_sdm_l1_import_reactive_energy(sens))
    if CONF_SDM_L2_IMPORT_REACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L2_IMPORT_REACTIVE_ENERGY])
        cg.add(var.set_sdm_l2_import_reactive_energy(sens))
    if CONF_SDM_L3_IMPORT_REACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L3_IMPORT_REACTIVE_ENERGY])
        cg.add(var.set_sdm_l3_import_reactive_energy(sens))
    if CONF_SDM_L1_EXPORT_REACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L1_EXPORT_REACTIVE_ENERGY])
        cg.add(var.set_sdm_l1_export_reactive_energy(sens))
    if CONF_SDM_L2_EXPORT_REACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L2_EXPORT_REACTIVE_ENERGY])
        cg.add(var.set_sdm_l2_export_reactive_energy(sens))
    if CONF_SDM_L3_EXPORT_REACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L3_EXPORT_REACTIVE_ENERGY])
        cg.add(var.set_sdm_l3_export_reactive_energy(sens))
    if CONF_SDM_L1_TOTAL_REACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L1_TOTAL_REACTIVE_ENERGY])
        cg.add(var.set_sdm_l1_total_reactive_energy(sens))
    if CONF_SDM_L2_TOTAL_REACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L2_TOTAL_REACTIVE_ENERGY])
        cg.add(var.set_sdm_l2_total_reactive_energy(sens))
    if CONF_SDM_L3_TOTAL_REACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_L3_TOTAL_REACTIVE_ENERGY])
        cg.add(var.set_sdm_l3_total_reactive_energy(sens))
    if CONF_SDM_CURRENT_RESETTABLE_TOTAL_ACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_CURRENT_RESETTABLE_TOTAL_ACTIVE_ENERGY])
        cg.add(var.set_sdm_current_resettable_total_active_energy(sens))
    if CONF_SDM_CURRENT_RESETTABLE_TOTAL_REACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_CURRENT_RESETTABLE_TOTAL_REACTIVE_ENERGY])
        cg.add(var.set_sdm_current_resettable_total_reactive_energy(sens))
    if CONF_SDM_CURRENT_RESETTABLE_IMPORT_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_CURRENT_RESETTABLE_IMPORT_ENERGY])
        cg.add(var.set_sdm_current_resettable_import_energy(sens))
    if CONF_SDM_CURRENT_RESETTABLE_EXPORT_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_CURRENT_RESETTABLE_EXPORT_ENERGY])
        cg.add(var.set_sdm_current_resettable_export_energy(sens))
    if CONF_SDM_IMPORT_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_IMPORT_POWER])
        cg.add(var.set_sdm_import_power(sens))
    if CONF_SDM_EXPORT_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_EXPORT_POWER])
        cg.add(var.set_sdm_export_power(sens))

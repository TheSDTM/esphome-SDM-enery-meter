import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ID, \
    CONF_BAUD_RATE, CONF_RX_PIN, CONF_TX_PIN, CONF_CHANNEL, \
    UNIT_EMPTY, UNIT_AMPERE, UNIT_HERTZ, UNIT_VOLT, \
    UNIT_VOLT_AMPS, UNIT_VOLT_AMPS_REACTIVE, \
    UNIT_WATT, UNIT_WATT_HOURS, UNIT_PERCENT, \
    ICON_EMPTY, ICON_PULSE, ICON_POWER, ICON_CURRENT_AC, ICON_FLASH, \
    ESP_PLATFORM_ESP32

UNIT_KWH = 'kW/h'
CONF_DERE_PIN = 'dere_pin'

CONF_SDM_PHASE_1_VOLTAGE = 'sdm_phase_1_voltage'
CONF_SDM_PHASE_1_CURRENT = 'sdm_phase_1_current'
CONF_SDM_PHASE_1_POWER = 'sdm_phase_1_power'
CONF_SDM_IMPORT_ACTIVE_ENERGY = 'sdm_import_active_energy'

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

    cv.Optional(CONF_SDM_PHASE_1_VOLTAGE): sensor.sensor_schema(UNIT_VOLT, ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_1_CURRENT): sensor.sensor_schema(UNIT_AMPERE, ICON_CURRENT_AC, 1),
    cv.Optional(CONF_SDM_PHASE_1_POWER): sensor.sensor_schema(UNIT_WATT, ICON_POWER, 1),
    cv.Optional(CONF_SDM_IMPORT_ACTIVE_ENERGY): sensor.sensor_schema(UNIT_KWH, ICON_FLASH, 1),

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

    if CONF_SDM_PHASE_1_CURRENT in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_1_CURRENT])
        cg.add(var.set_sdm_phase_1_current(sens))

    if CONF_SDM_PHASE_1_POWER in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_PHASE_1_POWER])
        cg.add(var.set_sdm_phase_1_power(sens))
        
    if CONF_SDM_IMPORT_ACTIVE_ENERGY in config:
        sens = yield sensor.new_sensor(config[CONF_SDM_IMPORT_ACTIVE_ENERGY])
        cg.add(var.set_import_active_energy(sens))


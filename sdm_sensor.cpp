#include "sdm_sensor.h"
#include "esphome/core/log.h"
#include "SDM.h"

namespace esphome {
namespace sdm_sensor {

static const char *TAG = "sdm_sensor.SDMSensor";

float SDMSensor::readVal(uint16_t reg) {
	float val = sdm->readVal(reg, channel_);

	uint16_t err = sdm->getErrCode(true);
	if (err != 0) {
		ESP_LOGE(TAG, "Error %i", err);
	}

	return val;
}
void SDMSensor::setup() {
	sdm = new SDM(Serial, baud_, dere_pin_, SERIAL_8N1, rx_pin_, tx_pin_);
	ESP_LOGD(TAG, "Setup completed");
}

void SDMSensor::update() {
	ESP_LOGD(TAG, "Start reading");

	INODE_READ_PUBLISH(this->sdm_phase_1_voltage, 		SDM_PHASE_1_VOLTAGE);
	INODE_READ_PUBLISH(this->sdm_phase_1_current, 		SDM_PHASE_1_CURRENT);
	INODE_READ_PUBLISH(this->sdm_phase_1_power, 		SDM_PHASE_1_POWER);
	INODE_READ_PUBLISH(this->sdm_import_active_energy, 	SDM_IMPORT_ACTIVE_ENERGY);

	ESP_LOGD(TAG, "End reading");
}

void SDMSensor::dump_config() {
	ESP_LOGCONFIG(TAG, "SDM sensor");

	ESP_LOGD(TAG, "Baud rate: %ld", baud_);
	ESP_LOGD(TAG, "DeRe pin: %i", dere_pin_);
	ESP_LOGD(TAG, "RX pin: %i", rx_pin_);
	ESP_LOGD(TAG, "TX pin: %i", tx_pin_);

	LOG_SENSOR("  ", "sdm_phase_1_voltage", this->sdm_phase_1_voltage_);
	LOG_SENSOR("  ", "sdm_phase_1_current", this->sdm_phase_1_current_);
	LOG_SENSOR("  ", "sdm_phase_1_power", this->sdm_phase_1_power_);
	LOG_SENSOR("  ", "sdm_import_active_energy", this->sdm_import_active_energy_);
}

} //namespace sdm_sensor
} //namespace esphome

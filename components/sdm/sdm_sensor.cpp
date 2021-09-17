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

	delay(10); // https://github.com/reaper7/SDM_Energy_Meter/issues/7#issuecomment-272080139
	return val;
}
void SDMSensor::setup() {
	sdm = new SDM(Serial, baud_, dere_pin_, SERIAL_8N1, rx_pin_, tx_pin_);
	sdm->begin();
	ESP_LOGD(TAG, "Setup completed");
}

void SDMSensor::update() {
	ESP_LOGD(TAG, "Start reading");

	INODE_READ_PUBLISH(this->sdm_phase_1_voltage                         , SDM_PHASE_1_VOLTAGE                         );
	INODE_READ_PUBLISH(this->sdm_phase_2_voltage                         , SDM_PHASE_2_VOLTAGE                         );
	INODE_READ_PUBLISH(this->sdm_phase_3_voltage                         , SDM_PHASE_3_VOLTAGE                         );
	INODE_READ_PUBLISH(this->sdm_phase_1_current                         , SDM_PHASE_1_CURRENT                         );
	INODE_READ_PUBLISH(this->sdm_phase_2_current                         , SDM_PHASE_2_CURRENT                         );
	INODE_READ_PUBLISH(this->sdm_phase_3_current                         , SDM_PHASE_3_CURRENT                         );
	INODE_READ_PUBLISH(this->sdm_phase_1_power                           , SDM_PHASE_1_POWER                           );
	INODE_READ_PUBLISH(this->sdm_phase_2_power                           , SDM_PHASE_2_POWER                           );
	INODE_READ_PUBLISH(this->sdm_phase_3_power                           , SDM_PHASE_3_POWER                           );
	INODE_READ_PUBLISH(this->sdm_phase_1_apparent_power                  , SDM_PHASE_1_APPARENT_POWER                  );
	INODE_READ_PUBLISH(this->sdm_phase_2_apparent_power                  , SDM_PHASE_2_APPARENT_POWER                  );
	INODE_READ_PUBLISH(this->sdm_phase_3_apparent_power                  , SDM_PHASE_3_APPARENT_POWER                  );
	INODE_READ_PUBLISH(this->sdm_phase_1_reactive_power                  , SDM_PHASE_1_REACTIVE_POWER                  );
	INODE_READ_PUBLISH(this->sdm_phase_2_reactive_power                  , SDM_PHASE_2_REACTIVE_POWER                  );
	INODE_READ_PUBLISH(this->sdm_phase_3_reactive_power                  , SDM_PHASE_3_REACTIVE_POWER                  );
	INODE_READ_PUBLISH(this->sdm_phase_1_power_factor                    , SDM_PHASE_1_POWER_FACTOR                    );
	INODE_READ_PUBLISH(this->sdm_phase_2_power_factor                    , SDM_PHASE_2_POWER_FACTOR                    );
	INODE_READ_PUBLISH(this->sdm_phase_3_power_factor                    , SDM_PHASE_3_POWER_FACTOR                    );
	INODE_READ_PUBLISH(this->sdm_phase_1_angle                           , SDM_PHASE_1_ANGLE                           );
	INODE_READ_PUBLISH(this->sdm_phase_2_angle                           , SDM_PHASE_2_ANGLE                           );
	INODE_READ_PUBLISH(this->sdm_phase_3_angle                           , SDM_PHASE_3_ANGLE                           );
	INODE_READ_PUBLISH(this->sdm_average_l_to_n_volts                    , SDM_AVERAGE_L_TO_N_VOLTS                    );
	INODE_READ_PUBLISH(this->sdm_average_line_current                    , SDM_AVERAGE_LINE_CURRENT                    );
	INODE_READ_PUBLISH(this->sdm_sum_line_current                        , SDM_SUM_LINE_CURRENT                        );
	INODE_READ_PUBLISH(this->sdm_total_system_power                      , SDM_TOTAL_SYSTEM_POWER                      );
	INODE_READ_PUBLISH(this->sdm_total_system_apparent_power             , SDM_TOTAL_SYSTEM_APPARENT_POWER             );
	INODE_READ_PUBLISH(this->sdm_total_system_reactive_power             , SDM_TOTAL_SYSTEM_REACTIVE_POWER             );
	INODE_READ_PUBLISH(this->sdm_total_system_power_factor               , SDM_TOTAL_SYSTEM_POWER_FACTOR               );
	INODE_READ_PUBLISH(this->sdm_total_system_phase_angle                , SDM_TOTAL_SYSTEM_PHASE_ANGLE                );
	INODE_READ_PUBLISH(this->sdm_frequency                               , SDM_FREQUENCY                               );
	INODE_READ_PUBLISH(this->sdm_import_active_energy                    , SDM_IMPORT_ACTIVE_ENERGY                    );
	INODE_READ_PUBLISH(this->sdm_export_active_energy                    , SDM_EXPORT_ACTIVE_ENERGY                    );
	INODE_READ_PUBLISH(this->sdm_import_reactive_energy                  , SDM_IMPORT_REACTIVE_ENERGY                  );
	INODE_READ_PUBLISH(this->sdm_export_reactive_energy                  , SDM_EXPORT_REACTIVE_ENERGY                  );
	INODE_READ_PUBLISH(this->sdm_vah_since_last_reset                    , SDM_VAH_SINCE_LAST_RESET                    );
	INODE_READ_PUBLISH(this->sdm_ah_since_last_reset                     , SDM_AH_SINCE_LAST_RESET                     );
	INODE_READ_PUBLISH(this->sdm_total_system_power_demand               , SDM_TOTAL_SYSTEM_POWER_DEMAND               );
	INODE_READ_PUBLISH(this->sdm_maximum_total_system_power_demand       , SDM_MAXIMUM_TOTAL_SYSTEM_POWER_DEMAND       );
	INODE_READ_PUBLISH(this->sdm_current_system_positive_power_demand    , SDM_CURRENT_SYSTEM_POSITIVE_POWER_DEMAND    );
	INODE_READ_PUBLISH(this->sdm_maximum_system_positive_power_demand    , SDM_MAXIMUM_SYSTEM_POSITIVE_POWER_DEMAND    );
	INODE_READ_PUBLISH(this->sdm_current_system_reverse_power_demand     , SDM_CURRENT_SYSTEM_REVERSE_POWER_DEMAND     );
	INODE_READ_PUBLISH(this->sdm_maximum_system_reverse_power_demand     , SDM_MAXIMUM_SYSTEM_REVERSE_POWER_DEMAND     );
	INODE_READ_PUBLISH(this->sdm_total_system_va_demand                  , SDM_TOTAL_SYSTEM_VA_DEMAND                  );
	INODE_READ_PUBLISH(this->sdm_maximum_total_system_va_demand          , SDM_MAXIMUM_TOTAL_SYSTEM_VA_DEMAND          );
	INODE_READ_PUBLISH(this->sdm_neutral_current_demand                  , SDM_NEUTRAL_CURRENT_DEMAND                  );
	INODE_READ_PUBLISH(this->sdm_maximum_neutral_current                 , SDM_MAXIMUM_NEUTRAL_CURRENT                 );
	INODE_READ_PUBLISH(this->sdm_line_1_to_line_2_volts                  , SDM_LINE_1_TO_LINE_2_VOLTS                  );
	INODE_READ_PUBLISH(this->sdm_line_2_to_line_3_volts                  , SDM_LINE_2_TO_LINE_3_VOLTS                  );
	INODE_READ_PUBLISH(this->sdm_line_3_to_line_1_volts                  , SDM_LINE_3_TO_LINE_1_VOLTS                  );
	INODE_READ_PUBLISH(this->sdm_average_line_to_line_volts              , SDM_AVERAGE_LINE_TO_LINE_VOLTS              );
	INODE_READ_PUBLISH(this->sdm_neutral_current                         , SDM_NEUTRAL_CURRENT                         );
	INODE_READ_PUBLISH(this->sdm_phase_1_ln_volts_thd                    , SDM_PHASE_1_LN_VOLTS_THD                    );
	INODE_READ_PUBLISH(this->sdm_phase_2_ln_volts_thd                    , SDM_PHASE_2_LN_VOLTS_THD                    );
	INODE_READ_PUBLISH(this->sdm_phase_3_ln_volts_thd                    , SDM_PHASE_3_LN_VOLTS_THD                    );
	INODE_READ_PUBLISH(this->sdm_phase_1_current_thd                     , SDM_PHASE_1_CURRENT_THD                     );
	INODE_READ_PUBLISH(this->sdm_phase_2_current_thd                     , SDM_PHASE_2_CURRENT_THD                     );
	INODE_READ_PUBLISH(this->sdm_phase_3_current_thd                     , SDM_PHASE_3_CURRENT_THD                     );
	INODE_READ_PUBLISH(this->sdm_average_line_to_neutral_volts_thd       , SDM_AVERAGE_LINE_TO_NEUTRAL_VOLTS_THD       );
	INODE_READ_PUBLISH(this->sdm_average_line_current_thd                , SDM_AVERAGE_LINE_CURRENT_THD                );
	INODE_READ_PUBLISH(this->sdm_total_system_power_factor_inv           , SDM_TOTAL_SYSTEM_POWER_FACTOR_INV           );
	INODE_READ_PUBLISH(this->sdm_phase_1_current_demand                  , SDM_PHASE_1_CURRENT_DEMAND                  );
	INODE_READ_PUBLISH(this->sdm_phase_2_current_demand                  , SDM_PHASE_2_CURRENT_DEMAND                  );
	INODE_READ_PUBLISH(this->sdm_phase_3_current_demand                  , SDM_PHASE_3_CURRENT_DEMAND                  );
	INODE_READ_PUBLISH(this->sdm_maximum_phase_1_current_demand          , SDM_MAXIMUM_PHASE_1_CURRENT_DEMAND          );
	INODE_READ_PUBLISH(this->sdm_maximum_phase_2_current_demand          , SDM_MAXIMUM_PHASE_2_CURRENT_DEMAND          );
	INODE_READ_PUBLISH(this->sdm_maximum_phase_3_current_demand          , SDM_MAXIMUM_PHASE_3_CURRENT_DEMAND          );
	INODE_READ_PUBLISH(this->sdm_line_1_to_line_2_volts_thd              , SDM_LINE_1_TO_LINE_2_VOLTS_THD              );
	INODE_READ_PUBLISH(this->sdm_line_2_to_line_3_volts_thd              , SDM_LINE_2_TO_LINE_3_VOLTS_THD              );
	INODE_READ_PUBLISH(this->sdm_line_3_to_line_1_volts_thd              , SDM_LINE_3_TO_LINE_1_VOLTS_THD              );
	INODE_READ_PUBLISH(this->sdm_average_line_to_line_volts_thd          , SDM_AVERAGE_LINE_TO_LINE_VOLTS_THD          );
	INODE_READ_PUBLISH(this->sdm_total_active_energy                     , SDM_TOTAL_ACTIVE_ENERGY                     );
	INODE_READ_PUBLISH(this->sdm_total_reactive_energy                   , SDM_TOTAL_REACTIVE_ENERGY                   );
	INODE_READ_PUBLISH(this->sdm_l1_import_active_energy                 , SDM_L1_IMPORT_ACTIVE_ENERGY                 );
	INODE_READ_PUBLISH(this->sdm_l2_import_active_energy                 , SDM_L2_IMPORT_ACTIVE_ENERGY                 );
	INODE_READ_PUBLISH(this->sdm_l3_import_active_energy                 , SDM_L3_IMPORT_ACTIVE_ENERGY                 );
	INODE_READ_PUBLISH(this->sdm_l1_export_active_energy                 , SDM_L1_EXPORT_ACTIVE_ENERGY                 );
	INODE_READ_PUBLISH(this->sdm_l2_export_active_energy                 , SDM_L2_EXPORT_ACTIVE_ENERGY                 );
	INODE_READ_PUBLISH(this->sdm_l3_export_active_energy                 , SDM_L3_EXPORT_ACTIVE_ENERGY                 );
	INODE_READ_PUBLISH(this->sdm_l1_total_active_energy                  , SDM_L1_TOTAL_ACTIVE_ENERGY                  );
	INODE_READ_PUBLISH(this->sdm_l2_total_active_energy                  , SDM_L2_TOTAL_ACTIVE_ENERGY                  );
	INODE_READ_PUBLISH(this->sdm_l3_total_active_energy                  , SDM_L3_TOTAL_ACTIVE_ENERGY                  );
	INODE_READ_PUBLISH(this->sdm_l1_import_reactive_energy               , SDM_L1_IMPORT_REACTIVE_ENERGY               );
	INODE_READ_PUBLISH(this->sdm_l2_import_reactive_energy               , SDM_L2_IMPORT_REACTIVE_ENERGY               );
	INODE_READ_PUBLISH(this->sdm_l3_import_reactive_energy               , SDM_L3_IMPORT_REACTIVE_ENERGY               );
	INODE_READ_PUBLISH(this->sdm_l1_export_reactive_energy               , SDM_L1_EXPORT_REACTIVE_ENERGY               );
	INODE_READ_PUBLISH(this->sdm_l2_export_reactive_energy               , SDM_L2_EXPORT_REACTIVE_ENERGY               );
	INODE_READ_PUBLISH(this->sdm_l3_export_reactive_energy               , SDM_L3_EXPORT_REACTIVE_ENERGY               );
	INODE_READ_PUBLISH(this->sdm_l1_total_reactive_energy                , SDM_L1_TOTAL_REACTIVE_ENERGY                );
	INODE_READ_PUBLISH(this->sdm_l2_total_reactive_energy                , SDM_L2_TOTAL_REACTIVE_ENERGY                );
	INODE_READ_PUBLISH(this->sdm_l3_total_reactive_energy                , SDM_L3_TOTAL_REACTIVE_ENERGY                );
	INODE_READ_PUBLISH(this->sdm_current_resettable_total_active_energy  , SDM_CURRENT_RESETTABLE_TOTAL_ACTIVE_ENERGY  );
	INODE_READ_PUBLISH(this->sdm_current_resettable_total_reactive_energy, SDM_CURRENT_RESETTABLE_TOTAL_REACTIVE_ENERGY);
	INODE_READ_PUBLISH(this->sdm_current_resettable_import_energy        , SDM_CURRENT_RESETTABLE_IMPORT_ENERGY        );
	INODE_READ_PUBLISH(this->sdm_current_resettable_export_energy        , SDM_CURRENT_RESETTABLE_EXPORT_ENERGY        );
	INODE_READ_PUBLISH(this->sdm_import_power                            , SDM_IMPORT_POWER                            );
	INODE_READ_PUBLISH(this->sdm_export_power                            , SDM_EXPORT_POWER                            );

	ESP_LOGD(TAG, "End reading");
}

void SDMSensor::dump_config() {
	ESP_LOGCONFIG(TAG, "SDM sensor");

	ESP_LOGD(TAG, "Baud rate: %ld", baud_);
	ESP_LOGD(TAG, "DeRe pin: %i", dere_pin_);
	ESP_LOGD(TAG, "RX pin: %i", rx_pin_);
	ESP_LOGD(TAG, "TX pin: %i", tx_pin_);
	ESP_LOGD(TAG, "Channel: %i", channel_);

	LOG_SENSOR("  ", "sdm_phase_1_voltage", this->sdm_phase_1_voltage_);
	LOG_SENSOR("  ", "sdm_phase_1_current", this->sdm_phase_1_current_);
	LOG_SENSOR("  ", "sdm_phase_1_power", this->sdm_phase_1_power_);
	LOG_SENSOR("  ", "sdm_import_active_energy", this->sdm_import_active_energy_);

	LOG_SENSOR("  ", "sdm_phase_1_voltage                         ", this->sdm_phase_1_voltage_                         );
	LOG_SENSOR("  ", "sdm_phase_2_voltage                         ", this->sdm_phase_2_voltage_                         );
	LOG_SENSOR("  ", "sdm_phase_3_voltage                         ", this->sdm_phase_3_voltage_                         );
	LOG_SENSOR("  ", "sdm_phase_1_current                         ", this->sdm_phase_1_current_                         );
	LOG_SENSOR("  ", "sdm_phase_2_current                         ", this->sdm_phase_2_current_                         );
	LOG_SENSOR("  ", "sdm_phase_3_current                         ", this->sdm_phase_3_current_                         );
	LOG_SENSOR("  ", "sdm_phase_1_power                           ", this->sdm_phase_1_power_                           );
	LOG_SENSOR("  ", "sdm_phase_2_power                           ", this->sdm_phase_2_power_                           );
	LOG_SENSOR("  ", "sdm_phase_3_power                           ", this->sdm_phase_3_power_                           );
	LOG_SENSOR("  ", "sdm_phase_1_apparent_power                  ", this->sdm_phase_1_apparent_power_                  );
	LOG_SENSOR("  ", "sdm_phase_2_apparent_power                  ", this->sdm_phase_2_apparent_power_                  );
	LOG_SENSOR("  ", "sdm_phase_3_apparent_power                  ", this->sdm_phase_3_apparent_power_                  );
	LOG_SENSOR("  ", "sdm_phase_1_reactive_power                  ", this->sdm_phase_1_reactive_power_                  );
	LOG_SENSOR("  ", "sdm_phase_2_reactive_power                  ", this->sdm_phase_2_reactive_power_                  );
	LOG_SENSOR("  ", "sdm_phase_3_reactive_power                  ", this->sdm_phase_3_reactive_power_                  );
	LOG_SENSOR("  ", "sdm_phase_1_power_factor                    ", this->sdm_phase_1_power_factor_                    );
	LOG_SENSOR("  ", "sdm_phase_2_power_factor                    ", this->sdm_phase_2_power_factor_                    );
	LOG_SENSOR("  ", "sdm_phase_3_power_factor                    ", this->sdm_phase_3_power_factor_                    );
	LOG_SENSOR("  ", "sdm_phase_1_angle                           ", this->sdm_phase_1_angle_                           );
	LOG_SENSOR("  ", "sdm_phase_2_angle                           ", this->sdm_phase_2_angle_                           );
	LOG_SENSOR("  ", "sdm_phase_3_angle                           ", this->sdm_phase_3_angle_                           );
	LOG_SENSOR("  ", "sdm_average_l_to_n_volts                    ", this->sdm_average_l_to_n_volts_                    );
	LOG_SENSOR("  ", "sdm_average_line_current                    ", this->sdm_average_line_current_                    );
	LOG_SENSOR("  ", "sdm_sum_line_current                        ", this->sdm_sum_line_current_                        );
	LOG_SENSOR("  ", "sdm_total_system_power                      ", this->sdm_total_system_power_                      );
	LOG_SENSOR("  ", "sdm_total_system_apparent_power             ", this->sdm_total_system_apparent_power_             );
	LOG_SENSOR("  ", "sdm_total_system_reactive_power             ", this->sdm_total_system_reactive_power_             );
	LOG_SENSOR("  ", "sdm_total_system_power_factor               ", this->sdm_total_system_power_factor_               );
	LOG_SENSOR("  ", "sdm_total_system_phase_angle                ", this->sdm_total_system_phase_angle_                );
	LOG_SENSOR("  ", "sdm_frequency                               ", this->sdm_frequency_                               );
	LOG_SENSOR("  ", "sdm_import_active_energy                    ", this->sdm_import_active_energy_                    );
	LOG_SENSOR("  ", "sdm_export_active_energy                    ", this->sdm_export_active_energy_                    );
	LOG_SENSOR("  ", "sdm_import_reactive_energy                  ", this->sdm_import_reactive_energy_                  );
	LOG_SENSOR("  ", "sdm_export_reactive_energy                  ", this->sdm_export_reactive_energy_                  );
	LOG_SENSOR("  ", "sdm_vah_since_last_reset                    ", this->sdm_vah_since_last_reset_                    );
	LOG_SENSOR("  ", "sdm_ah_since_last_reset                     ", this->sdm_ah_since_last_reset_                     );
	LOG_SENSOR("  ", "sdm_total_system_power_demand               ", this->sdm_total_system_power_demand_               );
	LOG_SENSOR("  ", "sdm_maximum_total_system_power_demand       ", this->sdm_maximum_total_system_power_demand_       );
	LOG_SENSOR("  ", "sdm_current_system_positive_power_demand    ", this->sdm_current_system_positive_power_demand_    );
	LOG_SENSOR("  ", "sdm_maximum_system_positive_power_demand    ", this->sdm_maximum_system_positive_power_demand_    );
	LOG_SENSOR("  ", "sdm_current_system_reverse_power_demand     ", this->sdm_current_system_reverse_power_demand_     );
	LOG_SENSOR("  ", "sdm_maximum_system_reverse_power_demand     ", this->sdm_maximum_system_reverse_power_demand_     );
	LOG_SENSOR("  ", "sdm_total_system_va_demand                  ", this->sdm_total_system_va_demand_                  );
	LOG_SENSOR("  ", "sdm_maximum_total_system_va_demand          ", this->sdm_maximum_total_system_va_demand_          );
	LOG_SENSOR("  ", "sdm_neutral_current_demand                  ", this->sdm_neutral_current_demand_                  );
	LOG_SENSOR("  ", "sdm_maximum_neutral_current                 ", this->sdm_maximum_neutral_current_                 );
	LOG_SENSOR("  ", "sdm_line_1_to_line_2_volts                  ", this->sdm_line_1_to_line_2_volts_                  );
	LOG_SENSOR("  ", "sdm_line_2_to_line_3_volts                  ", this->sdm_line_2_to_line_3_volts_                  );
	LOG_SENSOR("  ", "sdm_line_3_to_line_1_volts                  ", this->sdm_line_3_to_line_1_volts_                  );
	LOG_SENSOR("  ", "sdm_average_line_to_line_volts              ", this->sdm_average_line_to_line_volts_              );
	LOG_SENSOR("  ", "sdm_neutral_current                         ", this->sdm_neutral_current_                         );
	LOG_SENSOR("  ", "sdm_phase_1_ln_volts_thd                    ", this->sdm_phase_1_ln_volts_thd_                    );
	LOG_SENSOR("  ", "sdm_phase_2_ln_volts_thd                    ", this->sdm_phase_2_ln_volts_thd_                    );
	LOG_SENSOR("  ", "sdm_phase_3_ln_volts_thd                    ", this->sdm_phase_3_ln_volts_thd_                    );
	LOG_SENSOR("  ", "sdm_phase_1_current_thd                     ", this->sdm_phase_1_current_thd_                     );
	LOG_SENSOR("  ", "sdm_phase_2_current_thd                     ", this->sdm_phase_2_current_thd_                     );
	LOG_SENSOR("  ", "sdm_phase_3_current_thd                     ", this->sdm_phase_3_current_thd_                     );
	LOG_SENSOR("  ", "sdm_average_line_to_neutral_volts_thd       ", this->sdm_average_line_to_neutral_volts_thd_       );
	LOG_SENSOR("  ", "sdm_average_line_current_thd                ", this->sdm_average_line_current_thd_                );
	LOG_SENSOR("  ", "sdm_total_system_power_factor_inv           ", this->sdm_total_system_power_factor_inv_           );
	LOG_SENSOR("  ", "sdm_phase_1_current_demand                  ", this->sdm_phase_1_current_demand_                  );
	LOG_SENSOR("  ", "sdm_phase_2_current_demand                  ", this->sdm_phase_2_current_demand_                  );
	LOG_SENSOR("  ", "sdm_phase_3_current_demand                  ", this->sdm_phase_3_current_demand_                  );
	LOG_SENSOR("  ", "sdm_maximum_phase_1_current_demand          ", this->sdm_maximum_phase_1_current_demand_          );
	LOG_SENSOR("  ", "sdm_maximum_phase_2_current_demand          ", this->sdm_maximum_phase_2_current_demand_          );
	LOG_SENSOR("  ", "sdm_maximum_phase_3_current_demand          ", this->sdm_maximum_phase_3_current_demand_          );
	LOG_SENSOR("  ", "sdm_line_1_to_line_2_volts_thd              ", this->sdm_line_1_to_line_2_volts_thd_              );
	LOG_SENSOR("  ", "sdm_line_2_to_line_3_volts_thd              ", this->sdm_line_2_to_line_3_volts_thd_              );
	LOG_SENSOR("  ", "sdm_line_3_to_line_1_volts_thd              ", this->sdm_line_3_to_line_1_volts_thd_              );
	LOG_SENSOR("  ", "sdm_average_line_to_line_volts_thd          ", this->sdm_average_line_to_line_volts_thd_          );
	LOG_SENSOR("  ", "sdm_total_active_energy                     ", this->sdm_total_active_energy_                     );
	LOG_SENSOR("  ", "sdm_total_reactive_energy                   ", this->sdm_total_reactive_energy_                   );
	LOG_SENSOR("  ", "sdm_l1_import_active_energy                 ", this->sdm_l1_import_active_energy_                 );
	LOG_SENSOR("  ", "sdm_l2_import_active_energy                 ", this->sdm_l2_import_active_energy_                 );
	LOG_SENSOR("  ", "sdm_l3_import_active_energy                 ", this->sdm_l3_import_active_energy_                 );
	LOG_SENSOR("  ", "sdm_l1_export_active_energy                 ", this->sdm_l1_export_active_energy_                 );
	LOG_SENSOR("  ", "sdm_l2_export_active_energy                 ", this->sdm_l2_export_active_energy_                 );
	LOG_SENSOR("  ", "sdm_l3_export_active_energy                 ", this->sdm_l3_export_active_energy_                 );
	LOG_SENSOR("  ", "sdm_l1_total_active_energy                  ", this->sdm_l1_total_active_energy_                  );
	LOG_SENSOR("  ", "sdm_l2_total_active_energy                  ", this->sdm_l2_total_active_energy_                  );
	LOG_SENSOR("  ", "sdm_l3_total_active_energy                  ", this->sdm_l3_total_active_energy_                  );
	LOG_SENSOR("  ", "sdm_l1_import_reactive_energy               ", this->sdm_l1_import_reactive_energy_               );
	LOG_SENSOR("  ", "sdm_l2_import_reactive_energy               ", this->sdm_l2_import_reactive_energy_               );
	LOG_SENSOR("  ", "sdm_l3_import_reactive_energy               ", this->sdm_l3_import_reactive_energy_               );
	LOG_SENSOR("  ", "sdm_l1_export_reactive_energy               ", this->sdm_l1_export_reactive_energy_               );
	LOG_SENSOR("  ", "sdm_l2_export_reactive_energy               ", this->sdm_l2_export_reactive_energy_               );
	LOG_SENSOR("  ", "sdm_l3_export_reactive_energy               ", this->sdm_l3_export_reactive_energy_               );
	LOG_SENSOR("  ", "sdm_l1_total_reactive_energy                ", this->sdm_l1_total_reactive_energy_                );
	LOG_SENSOR("  ", "sdm_l2_total_reactive_energy                ", this->sdm_l2_total_reactive_energy_                );
	LOG_SENSOR("  ", "sdm_l3_total_reactive_energy                ", this->sdm_l3_total_reactive_energy_                );
	LOG_SENSOR("  ", "sdm_current_resettable_total_active_energy  ", this->sdm_current_resettable_total_active_energy_  );
	LOG_SENSOR("  ", "sdm_current_resettable_total_reactive_energy", this->sdm_current_resettable_total_reactive_energy_);
	LOG_SENSOR("  ", "sdm_current_resettable_import_energy        ", this->sdm_current_resettable_import_energy_        );
	LOG_SENSOR("  ", "sdm_current_resettable_export_energy        ", this->sdm_current_resettable_export_energy_        );
	LOG_SENSOR("  ", "sdm_import_power                            ", this->sdm_import_power_                            );
	LOG_SENSOR("  ", "sdm_export_power                            ", this->sdm_export_power_                            );
}

} //namespace sdm_sensor
} //namespace esphome

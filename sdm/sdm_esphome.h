#include "esphome.h"

class SDMComponent : public PollingComponent {
public:
  SDM sdm = SDM(Serial, 9600, NOT_A_PIN, SERIAL_8N1, false);

  Sensor *voltage_sensor = new Sensor();
  Sensor *current_sensor = new Sensor();
  Sensor *power_sensor = new Sensor();
  Sensor *energy_import_sensor = new Sensor();

  SDMComponent() : PollingComponent(15000) {}

  void setup() override {
    ESP_LOGD("SDM", "Setup completed");
  }

  void update() override {
    ESP_LOGD("SDM", "Start reading");
    float voltage1 = sdm.readVal(SDM630_VOLTAGE1);
    float voltage2 = sdm.readVal(SDM630_VOLTAGE2);
    float voltage3 = sdm.readVal(SDM630_VOLTAGE3);
    ESP_LOGD("SDM", "Voltages %f %f %f", voltage1, voltage2, voltage3);
    voltage_sensor->publish_state((voltage1 + voltage2 + voltage3)/3);

    float current = sdm.readVal(SDM630_CURRENTSUM);
    current_sensor->publish_state(current);

    float power = sdm.readVal(SDM630_POWERTOTAL);
    power_sensor->publish_state(power);

    float import1 = sdm.readVal(SDM630_IMPORT1);
    float import2 = sdm.readVal(SDM630_IMPORT2);
    float import3 = sdm.readVal(SDM630_IMPORT3);
    ESP_LOGD("SDM", "Imports %f %f %f", import1, import2, import3);
    energy_import_sensor->publish_state(import1 + import2 + import3);

    ESP_LOGD("SDM", "End reading");
  }
};
#include <ArduinoJson.h>
#include <SPIFFS.h>

#ifdef __cplusplus
extern "C" {
#endif
uint8_t temprature_sens_read();
#ifdef __cplusplus
}
#endif
uint8_t temprature_sens_read();

void setup() {
  Serial.begin(115200);

  if (!SPIFFS.begin(true)) {
    Serial.println("SPIFFS initialization failed!");
    return;
  }
}

void loop() {
  // Read sensor data
  int measurement = hallRead();
  int temp = (temprature_sens_read() - 32) / random(0, 20);

  // Create JSON object
  DynamicJsonDocument doc(128); // Adjust the size based on your JSON structure
  doc["hall_sensor_measurement"] = measurement;
  doc["temperature_C"] = temp;

  // Serialize JSON to string
  String output;
  serializeJson(doc, output);

  // Write JSON to file
  File file = SPIFFS.open("/data.json", FILE_WRITE);
  if (!file) {
    Serial.println("Failed to open file for writing");
  } else {
    if (file.print(output)) {
      Serial.println("File written successfully");
    } else {
      Serial.println("Write failed");
    }
    file.close();
  }

  // Wait for a few seconds
  delay(2000);
}



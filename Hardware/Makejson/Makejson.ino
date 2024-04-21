#include <ArduinoJson.h>
#include <SPI.h>
#include <SD.h>

#ifdef __cplusplus
extern "C" {
#endif
#include <esp32-hal-adc.h> // Include ESP32 ADC library
#ifdef __cplusplus
}
#endif

#ifdef __cplusplus
extern "C" {
#endif
uint8_t temprature_sens_read();
#ifdef __cplusplus
}
#endif
uint8_t temprature_sens_read();


#define HALL_SENSOR_PIN 34 // Example pin for Hall sensor on ESP32
#define JSON_FILENAME "Sensors.json"

void setup() {
  Serial.begin(115200);
  if (!SD.begin()) {
    Serial.println("SD card initialization failed.");
    return;
  }
}

void loop() {
  int measurement = hallRead();
  float temp = (temprature_sens_read() - 32) / random(0, 20); // Calculate temperature

  // Create JSON object
  StaticJsonDocument<64> doc;
  doc["Hall"] = measurement;
  doc["Temperature"] = temp;

  // Open JSON file
  File file = SD.open(JSON_FILENAME, FILE_WRITE);
  if (!file) {
    Serial.println("Failed to open file for writing");
    return;
  }

  // Serialize JSON to file
  if (serializeJson(doc, file) == 0) {
    Serial.println("Failed to write to file");
  } else {
    Serial.println("JSON file updated successfully");
  }

  // Close file
  file.close();

  // Print sensor readings to serial monitor
  Serial.print("Hall sensor measurement: ");
  Serial.println(measurement);
  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.println(" C");

  delay(2000);
}


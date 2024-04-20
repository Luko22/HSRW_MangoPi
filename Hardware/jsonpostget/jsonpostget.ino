#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "LukoSpot";
const char* password = "Duisbu5.";
const char* serverUrl = "https://luko22.github.io/";


//sensor parameters
int pin1 = A0;
int pin2 = A3;
int pin3 = A0;

float sensorData = 0.0;

void setup() {
  Serial.begin(9600);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
}

void loop() {
  // Read sensor data
  float sensorData = hallRead();

  delay(500); // Wait for 5 seconds before sending next data

  Serial.println(hallRead());
}

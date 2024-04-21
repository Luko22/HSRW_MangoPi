#ifdef __cplusplus
extern "C" {
#endif
uint8_t temperature_sens_read(); 
#ifdef __cplusplus
}
#endif

void setup() {
  Serial.begin(115200);  // Initialize serial communication at 115200 bits per second
}

void loop() {
  // Read the value from the Hall sensor
  int measurement = hallRead();  
  Serial.print("Hall sensor measurement: ");
  Serial.println(measurement);

  // Read and display the temperature from the onboard sensor
  Serial.print("Temperature: ");
  float temperature = (temperature_sens_read() - 32) / 1.8;  // Assuming the reading is in Fahrenheit
  Serial.print(temperature);
  Serial.println(" C");

  delay(500);  // Wait for half a second before the next read
}

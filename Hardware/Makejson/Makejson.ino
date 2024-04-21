#include <SD.h> // Include the SD library
#include <ArduinoJson.h> // Include the ArduinoJson library

const int chipSelect = 14; // Set the chip select pin for the SD card

void setup() {
  Serial.begin(9600);

  // Initialize the SD card
  if (!SD.begin(chipSelect)) {
    Serial.println("SD card initialization failed.");
    return;
  }
  Serial.println("SD card initialized.");

  // Create and write to the JSON file
  writeFile("/data.json");
}

void loop() {
  // Your main code here
}

void writeFile(const char *filename) {
  // Create or open the JSON file for writing
  File file = SD.open(filename, FILE_WRITE);

  // Check if the file opened successfully
  if (!file) {
    Serial.println("Error opening file.");
    return;
  }

  // Create a JSON object
  StaticJsonDocument<200> doc;

  // Add data to the JSON object
  doc["temperatures"] = "25";
  doc["Speed"] = "30";

  // Serialize the JSON object to a string
  String output;
  serializeJson(doc, output);

  // Write the JSON data to the file
  file.println(output);

  // Close the file
  file.close();

  Serial.println("JSON data written to file.");
}

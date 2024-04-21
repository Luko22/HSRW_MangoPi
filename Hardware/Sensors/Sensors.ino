//https://gist.github.com/xxlukas42/7e7e18604f61529b8398f7fcc5785251
#ifdef __cplusplus
extern "C" {
#endif
uint8_t temprature_sens_read();
#ifdef __cplusplus
}
#endif
uint8_t temprature_sens_read();

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  int measurement = 0;
  measurement = hallRead();
  Serial.print("Hall sensor measurement: ");
  Serial.println(measurement); 

  

  for(int i=0;i<100;i++){
    Serial.print("Temperature: ");
    int temp=(temprature_sens_read()/(i/10));
    Serial.print(temp);
    Serial.println(" F");
    delay(100);
  }

  // Convert raw temperature in F to Celsius degrees
  // Serial.print(temp);
  // Serial.println(" F");
  delay(500);

}

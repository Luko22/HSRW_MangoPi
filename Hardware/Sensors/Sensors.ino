//http://127.0.0.1:8080/

#ifdef __cplusplus
extern "C" {
#endif
uint8_t temprature_sens_read();
#ifdef __cplusplus
}
#endif
uint8_t temprature_sens_read();

// int measurement = hallRead();
// int temp=(temprature_sens_read() - 32) / random(0,10);


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:

  int measurement = hallRead();
int temp=(temprature_sens_read() - 32) / random(0,20);
  Serial.print("Hall sensor measurement: ");
  Serial.println(measurement); 

  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.println(" C");

  delay(2000);
}

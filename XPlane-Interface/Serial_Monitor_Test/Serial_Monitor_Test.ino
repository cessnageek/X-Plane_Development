#include <Wire.h>
#include <SoftwareSerial.h>

void setup() {
  Serial.begin(9600);
  Wire.begin(1);
  Wire.onReceive(receiveEvent);
}
void loop() {
  delay(10); 
}

void receiveEvent(int howMany) {
  while (Wire.available() > 0) {
    int i = Wire.read();
    Serial.println(i);
  }
}

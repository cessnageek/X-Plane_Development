#include <SoftwareSerial.h>
#include <SPI.h>
byte dataIn;
void setup() {
  Serial.begin(9600);
  SPI.begin();
}
void loop() {
  while(digitalRead(0) == LOW) {
    dataIn = SPI.transfer(0);
  }
}
  


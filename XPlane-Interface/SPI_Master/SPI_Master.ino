#include <SoftwareSerial.h>
#include <SPI.h>
#define pinSS 0
byte dataOut;
byte dataIn;

void setup() {
  Serial.begin(9600);
  pinMode(pinSS, OUTPUT);
  digitalWrite(pinSS, HIGH);
  SPI.begin();  
}
  
void loop() {
  while(Serial.available() > 0) {
    dataOut = Serial.read();
    digitalWrite(pinSS, LOW);
    delay(1);
    dataIn = SPI.transfer(dataOut);
    digitalWrite(pinSS, HIGH);
  }
    
}


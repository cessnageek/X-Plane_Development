#include "variables.h"
#include <Wire.h>
#include <FloatMap.h>
#include <Servo.h> 
void setup()
{
  // Attach each Servo object to a digital pin
  //servo1.attach(PIN_SERVO1, minPulse, maxPulse);
  //servo2.attach(PIN_SERVO2, minPulse, maxPulse);
 
  // Open the serial connection, 9600 baud
  Serial.begin(2400);
  for(int i = 3; i<14; i++)
  {
    pinMode(i, INPUT);
  }
  
 
  sStartl = 0;
  sMagr = 0;
  sMagl = 0;
  sStartr = 0;
  
  Wire.begin();
} 
 
void loop()
{
  collectAndPresentData();
  delay(10);
  sendData();
  //getData();
  //WaitForSerial();
  //Switches();
}

void sendData() {
  byte x = 257;
  Wire.beginTransmission(1);
  Wire.write(input);
  Wire.endTransmission();
}
  
void getData() {
  while(Serial.available() > 0) {
    input = Serial.read();
    //Serial.print(input);
  }
  //return input;
}
    








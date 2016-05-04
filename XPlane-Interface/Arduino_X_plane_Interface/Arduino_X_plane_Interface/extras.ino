/*
pinMode(5, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(6, INPUT);
  pinMode(7, INPUT);
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
  pinMode(12, INPUT);
  pinMode(13, INPUT);
  
void WaitForSerial()
{
  // Wait for serial input (min 3 bytes in buffer)
  if (Serial.available() > 2) {
    // Read the first byte
    startByte = Serial.read();
    // If it's really the startByte (255) ...
    if (startByte == 255) {
      // ... then get the next two bytes
      for (i = 0; i < 2; i++) {
        userInput[i] = Serial.read();
      }
      // First byte = servo to move?
      servo = userInput[0];
      // Second byte = which position?
      pos = userInput[1];
      // Packet error checking and recovery
      if (pos == 255) { servo = 255; }
      // Assign new position to appropriate servo
      switch (servo) {
        case 1:
          servo1.write(pos);    // move servo1 to 'pos'
          break;
        case 2:
          servo2.write(pos);
          break;
        case 3:
          digitalWrite(6, HIGH);
          digitalWrite(4, HIGH);
          digitalWrite(2, HIGH);
          break;
        case 4:
          digitalWrite(6, LOW);
          digitalWrite(4, LOW);
          digitalWrite(2, LOW);
          break;
      }
    }
  }
}

void Switches()
{
  battSend = 1;
  LaltSend = 3;
  Serial.print(battSend); 
  Serial.print(",");
  Serial.print(LaltSend);
  delay(450);
  battSend = 2;
  LaltSend = 4;
  Serial.print(battSend);
  Serial.print(",");  
  Serial.print(LaltSend);
  delay(450);
}

float floatMap(float x, float in_min, float in_max, float out_min, float out_max)
{
  return(x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
*/

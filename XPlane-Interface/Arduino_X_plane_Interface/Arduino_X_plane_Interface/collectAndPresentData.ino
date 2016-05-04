void collectAndPresentData() {
  int lAlt = digitalRead(3);
  int rAlt = digitalRead(4);
  int lMag1 = digitalRead(5);
  int lMag2 = digitalRead(6);
  int lStart = digitalRead(7);
  int rMag1 = digitalRead(8);
  int rMag2 = digitalRead(9);
  int rStart = digitalRead(10);
  int mastAvionics = digitalRead(11);
  int propSync = digitalRead(12);
  int lPitotHeat = digitalRead(13);
  int rPitotHeat = 0;
  int key = 8;
  Serial.print(lAlt);
  Serial.print(',');
  Serial.print(rAlt);
  Serial.print(',');
  Serial.print(sMagl);
  Serial.print(',');
  Serial.print(sMagr);
  Serial.print(',');
  Serial.print(mastAvionics);
  Serial.print(',');
  Serial.print(propSync);
  Serial.print(',');
  Serial.print(lPitotHeat);
  Serial.print(',');
  Serial.print(rPitotHeat);
  Serial.print(',');
  Serial.print(key);
  Serial.print('\n');
  Serial.flush();
  
     //sMagl
  if((lMag1 == HIGH) && (lMag2 == HIGH))
  {
    sMagl = 3;
  }
  if((lMag1 == LOW) && (lMag2 == HIGH))
  {
    sMagl = 1;
  }
  if((lMag1 == HIGH) && (lMag2 == LOW))
  {
    sMagl = 2;
  }
  if((lMag1 == LOW) && (lMag2 == LOW))
  {
    sMagl = 0;
  }  
  if(sMagr != 0)
  {
  if(lStart == LOW)
  {
    sMagl = 4;
  }
  }
  
  //sMagr
  if((rMag1 == HIGH) && (rMag2 == HIGH))
  {
    sMagr = 3;
  }
  if((rMag1 == LOW) && (rMag2 == HIGH))
  {
    sMagr = 1;
  }
  if((rMag1 == HIGH) && (rMag2 == LOW))
  {
    sMagr = 2;
  }
  if((rMag1 == LOW) && (rMag2 == LOW))
  {
    sMagr = 0;
  }  
  if(sMagr != 0)
  {
  if(rStart == LOW)
  {
    sMagr = 4;
  }
  }
}

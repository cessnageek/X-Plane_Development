#include "Arduino.h"
#define PIN_SERVO1 11
#define PIN_SERVO2 12


// Create a Servo object for each servo
/*Servo servo1;
Servo servo2;*/
 
// Common servo setup values
int minPulse = 600;   // minimum servo position, us (microseconds)
int maxPulse = 2400;  // maximum servo position, us

int throttle1Pin = 0; 
// User input for servo and position
int userInput[3];    // raw input from serial buffer, 3 bytes
int startByte;       // start byte, begin reading input
int servo;           // which servo to pulse?
int pos;             // servo angle 0-180
int i;   
int sMagl;
int sMagr;
int sStartr;
int sStartl;
int bytes[3];
byte input;

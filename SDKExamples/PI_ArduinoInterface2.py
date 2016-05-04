"""
PI_XArduino for Servos
 
Copyright (c) 2012 by Chris Strosser
"""
 
from XPLMDefs import *
from XPLMProcessing import *
from XPLMDataAccess import *
from XPLMUtilities import *
from XPLMPlugin import *
import serial
import sys
import time

class PythonInterface:
    def XPluginStart(self):
        
            self.Name = "XArduino for Servos2"
            self.Sig =  "Hindman.Python.ArduinoInterface2"
            self.Desc = "Interfaces Arduino with X-Plane"

            try:
                self.s = serial.Serial('/dev/tty.usbmodem14221', 9600)
                print "Arduino Found!!"
                self.run = True;
                self.datarefs = {}
                #Here is where I am finding all the datarefs:
                self.fuelRightDataref = self.getDataref("sim/flightmodel/weight/m_fuel2")
                self.fuelLeftDataref = self.getDataref("sim/flightmodel/weight/m_fuel1")
                self.PilotAltDataref = self.getDataref("sim/cockpit2/gauges/indicators/altitude_ft_pilot")
                self.BatteryOnDR = XPLMFindDataRef("sim/cockpit/electrical/battery_on")
                self.isBatteryOnDR = self.getDataref("sim/cockpit/electrical/battery_on")
                self.aileronDataref = self.getDataref("sim/joystick/yoke_roll_ratio")
                self.elevatorDataref = self.getDataref("sim/joystick/yoke_pitch_ratio")
                self.rudderDataref = self.getDataref("sim/joystick/yoke_heading_ratio")
                self.engineOverride = self.getDataref("sim/operation/override/override_joystick")
                self.throttleDataref = self.getDataref("sim/cockpit2/engine/actuators/throttle_ratio")
                self.Alt = self.getDataref("sim/cockpit2/electrical/generator_on")
                self.airspeed = self.getDataref("sim/cockpit2/gauges/indicators/airspeed_kts_pilot")
                self.interval = -1
                self.FlightLoopCB = self.FlightLoopCallback
                XPLMRegisterFlightLoopCallback(self, self.FlightLoopCB, self.interval, 0)
            except serial.SerialException:
                print "Could not load Arduino"
                print "Arduino not Found!!!!!"
                
                self.run = False;
 
            return self.Name, self.Sig, self.Desc
 
    def getDataref(self, datarefString):
        if (self.datarefs.get(datarefString) == None):
            self.datarefs[datarefString] = XPLMFindDataRef(datarefString)
        return self.datarefs.get(datarefString)
 
    def move(self, servo, angle):
    	if(0 < angle < 180):
            self.s.write(chr(255))
            self.s.write(chr(servo))
            self.s.write(chr(angle))
            

    def XPluginStop(self):
        if self.run:
            # Unregister the callback
            XPLMUnregisterFlightLoopCallback(self, self.FlightLoopCB, 0)
            self.s.close();
        pass
 
    def XPluginEnable(self):
        return 1
    
    def XPluginDisable(self):
        pass
 
    def XPluginReceiveMessage(self, inFromWho, inMessage, inParam):
        pass
    
    def FlightLoopCallback(self, elapsedMe, elapsedSim, counter, refcon):
        if (True != self.run):
            print "Arduino not running";
            return 1;
 
        try:
            
            fuelRight = XPLMGetDataf(self.fuelRightDataref)
            rightAngle = (170  - fuelRight/1.6) + 13
            self.move(2, int(rightAngle))

            fuelLeft = XPLMGetDataf(self.fuelLeftDataref)
            leftAngle = (170 - fuelLeft/1.6) + 13
            self.move(1, int(leftAngle))
            
            altimiter = XPLMGetDataf(self.PilotAltDataref)
            self.move(3, int(altimiter))
            
            Airspeed = XPLMGetDataf(self.airspeed)
            self.move(4, int(Airspeed))
            
            
            aInput = self.s.readline()
            print aInput
            arduino = aInput.strip('\n')
            alts1 = arduino.split(',')
            lalt = int(alts1[0])
            ralt = int(alts1[1])
            lInig = int(alts1[2])
            rInig = int(alts1[3])
            Skey = int(alts1[4])
            Lthrot = float(alts1[5])
            Rthrot = float(alts1[6])
            self.s.flushInput()
            altList = [lalt, ralt, 0, 0, 0, 0, 0, 0]
            Alt = XPLMFindDataRef("sim/cockpit2/electrical/generator_on")
            ignitionList = [lInig, rInig, 0, 0, 0, 0, 0, 0]
            Ignition = XPLMFindDataRef("sim/cockpit2/engine/actuators/ignition_key")
            throtList = [Lthrot, Rthrot]
            Throttle = XPLMFindDataRef("sim/flightmodel/engine/ENGN_thro")
            if (Skey == 8):
            	XPLMSetDatavi(Alt, altList, 0, 2)			
            	XPLMSetDatavi(Ignition, ignitionList, 0, 2)
            	XPLMSetDatavf(Throttle, throtList, 0, 2)
            elif (Skey != 8):
            	pass
            	                                        
        except serial.SerialException:
            print "Exception: No connection found"
            return 2;
        except serial.SerialTimeoutException:
            print "Exception: Connection timed out"
        except:
            print "Unexpected error: %s" % sys.exc_info()[1]
 
        return self.interval;

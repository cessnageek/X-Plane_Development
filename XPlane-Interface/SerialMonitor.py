import serial
import sys
i = 1
s = serial.Serial('/dev/tty.usbserial-AM01VB8E') #idk if it is zero or O
while i == 1:
	s.flushInput()
	s.flushOutput()
	input = s.readline()
	print input


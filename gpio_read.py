#!/usr/local/bin/python  
# GPIO   : RPi.GPIO v3.1.0a  
# http://www.rpiblog.com/2012/11/reading-analog-values-from-digital-pins.html


import time, sys
try:
  import RPi.GPIO as GPIO
except ImportError:
  print "Can't import RPi.GPIO. Exiting with sys(0)"
  sys.exit(0)
GPIO.setmode(GPIO.BCM)  
  
# Define function to measure charge time  
def RC_Analog (Pin):  
  counter = 0  
  # Discharge capacitor  
  GPIO.setup(Pin, GPIO.OUT)  
  GPIO.output(Pin, GPIO.LOW)  
  time.sleep(0.1)  
  GPIO.setup(Pin, GPIO.IN)  
  # Count loops until voltage across capacitor reads high on GPIO  
  while(GPIO.input(Pin)==GPIO.LOW):  
        counter =counter+1  
  return counter  
  
# Main program loop  
  
while True:  
  print RC_Analog(4) # Measure timing using GPIO4 

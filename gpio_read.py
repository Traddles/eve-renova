#!/usr/local/bin/python  
# GPIO   : RPi.GPIO v3.1.0a  
# http://www.rpiblog.com/2012/11/reading-analog-values-from-digital-pins.html

# calc std: http://stackoverflow.com/questions/1174984/how-to-efficiently-calculate-a-running-standard-deviation

# pi: pi@169.254.182.11
import time, sys
import math

N_SAMPL = 10

try:
  import RPi.GPIO as GPIO
except ImportError:
  print "Can't import RPi.GPIO. Exiting with sys(0)"
  sys.exit(0)
GPIO.setmode(GPIO.BCM)  
  
# Define function to measure charge time  
def rcAnalog (Pin=4):  
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

def calcAverageFloat(samples):
  if len(samples) == 0:
    raise Exception('Ask for more than a zero sample average!')
  return (float(sum(samples))/len(samples))

def calcAverageStdDevFloat(samples):
  if len(samples) == 0:
    raise Exception('Ask for more than a zero sample average!')
  sum_x1 = float(sum(samples))
  sum_x2 = float(sum(map(lambda x: x ** 2, samples)))
  n = len(samples)
  avg = sum_x1/n
  sd = math.sqrt(((n * sum_x2) - (sum_x1 * sum_x1)) / (n * (n - 1)))
  return (avg,sd)

def calcAverageCheepStdDevFloat(samples):
  maxv, minv = max(samples), min(samples)
  return (calcAverageFloat(samples), maxv - minv)

def readNTimesThenAverage(nSamples=N_SAMPL): # use a reasonable value for N
  samples = []
  for n in range(0,nSamples):
    # Measure timing using GPIO4 
    samples.append(rcAnalog())
  # Calc average of samples
  return calcAverageCheepStdDevFloat(samples)

def convertToCentigrades(avgTValue):
  # Do some calculation based on measured values or anything
  return avgTValue

# Main program loop  
#if __main__ == "__main__":
while True:  
  #print rcAnalog(4) # Measure timing using GPIO4 
  print readNTimesThenAverage()

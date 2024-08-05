import time
from machine import Pin, ADC
time.sleep (0.1)# Wait for USB to be

print ("Hello, Pi Pico!")

while 1==1:
  print (ADC(27).read_u16())
  time.sleep(.1)

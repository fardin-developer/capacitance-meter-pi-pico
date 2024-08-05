from machine import ADC
import machine
from time import sleep
adc = ADC(26)
charge_pin = machine.Pin(16, machine.Pin.OUT)
charge_pin.value(1) 
while True:
    value = adc.read_u16()
    print("Analog value is: ")
    print(value)
    sleep(0.25)
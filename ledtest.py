import machine
import utime

# Define the pin connected to the LED
led_pin = machine.Pin(25, machine.Pin.OUT)

# Blink the LED in a loop
while True:
    led_pin.value(1)  # Turn the LED on
    utime.sleep(1)    # Wait for 1 second
    led_pin.value(0)  # Turn the LED off
    utime.sleep(1)    # Wait for 1 second

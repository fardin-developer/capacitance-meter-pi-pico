import machine
import utime
from machine import Pin, ADC

# Define the GPIO and ADC pins
charge_pin = Pin(16, Pin.OUT)
adc = ADC(Pin(27))  # GPIO27

# Known resistor value in ohms
resistor_value = 10000  # 10k ohms

# Function to read the voltage from the ADC
def read_voltage(adc):
    raw = adc.read_u16()  # Read the raw ADC value
    voltage = (raw / 65535) * 3.3  # Convert to voltage assuming 3.3V reference
    return voltage

# Charge the capacitor
charge_pin.value(1)  # Set GPIO pin to HIGH
start_time = utime.ticks_us()
threshold_voltage = 0.63 * 3.3  # 63% of 3.3V

# Monitor the voltage until it reaches the threshold
while True:
    voltage = read_voltage(adc)
    print("Voltage across the capacitor: {:.2f} V".format(voltage))
    if voltage >= threshold_voltage:
        break

# Time when the capacitor reaches 63% charge
charge_time = utime.ticks_diff(utime.ticks_us(), start_time)
print("Time to reach 63% charge: {} microseconds".format(charge_time))

# Discharge the capacitor
charge_pin.value(0)  # Set GPIO pin to LOW
utime.sleep(1)  # Wait for the capacitor to discharge

# Read the voltage across the capacitor after discharging
voltage = read_voltage(adc)
print("Voltage across the capacitor after discharging: {:.2f} V".format(voltage))

# Calculate the capacitance
capacitance = charge_time / (resistor_value * 1e6)  # Capacitance in farads
capacitance_nF = capacitance * 1e6  # Convert to microfarads
print("Measured Capacitance: {:.2f}uF".format(capacitance_nF))

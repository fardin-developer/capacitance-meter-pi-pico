import machine
import utime
from machine import Pin, ADC
import json

charge_pin = Pin(16, Pin.OUT)
adc = ADC(Pin(27))  

# Known resistor value in ohms
resistor_value = 10000  # 10k ohms
actual_capacitance_value = float(input("Enter the actual capacitance of the capacitor (in microfarads) to calculate the error: "))  # in microfarads

# Function to read the voltage from the ADC
def read_voltage(adc):
    raw = adc.read_u16()  
    voltage = (raw / 65535) * 3.3  
    return voltage


data = []

start_time = utime.time()

while True:
    # Charge the capacitor
    charge_pin.value(1)  
    start_charge_time = utime.ticks_us()
    threshold_voltage = 0.63 * 3.3  

    # Monitor the voltage until it reaches the threshold
    while True:
        voltage = read_voltage(adc)
        if voltage >= threshold_voltage:
            break

    charge_time = utime.ticks_diff(utime.ticks_us(), start_charge_time)

    # Discharge the capacitor
    charge_pin.value(0)  
    utime.sleep(1) 

    voltage = read_voltage(adc)

    # Calculate the capacitance
    capacitance = charge_time / (resistor_value * 1e6)  
    capacitance_uF = capacitance * 1e6  
    time_constant = charge_time
    error_percentage = ((capacitance_uF - actual_capacitance_value) / actual_capacitance_value) * 100


    # Append the data to the list as a dictionary
    data.append({
        "Time Constant (us)": time_constant,
        "Capacitance (uF)": capacitance_uF,
        "Actual Capacitance (uF)": actual_capacitance_value,
        "Error (%)": error_percentage
    })

    # Print the data as JSON
    print(json.dumps(data))

    utime.sleep(5)  







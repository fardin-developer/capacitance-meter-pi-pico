import machine
import utime

# Define pins
charge_pin = machine.Pin(16, machine.Pin.OUT)
adc = machine.ADC(27)

# Known resistor value in ohms
R = 1000  # 1k ohm resistor

def discharge_capacitor():
    # Discharge the capacitor
    charge_pin.value(0)
    utime.sleep(1)

def measure_capacitance():
    # Discharge the capacitor first
    discharge_capacitor()

    # Start charging the capacitor
    charge_pin.value(1)
    start_time = utime.ticks_us()

    # Measure the time taken for the voltage to reach a threshold (e.g., 63% of Vcc)
    threshold = int(0.63 * 1024)  # 63% of 3.3V in ADC value (16-bit)

    while adc.read_u16() < threshold:
        pass

    end_time = utime.ticks_us()
    charge_pin.off()

    # Calculate elapsed time in seconds
    elapsed_time = utime.ticks_diff(end_time, start_time)

    # Calculate capacitance using the formula T = RC, C = T / R
    capacitance = elapsed_time / R

    return capacitance

# Main loop
try:
    while True:
        capacitance = measure_capacitance()
        print("Capacitance: {:.6f} F".format(capacitance))
        utime.sleep(2)
except KeyboardInterrupt:
    print("Measurement stopped by user")
    charge_pin.off()
    discharge_capacitor() 

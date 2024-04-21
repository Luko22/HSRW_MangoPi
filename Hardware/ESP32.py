# Flash MicroPython Firmware
# 1.download MicroPython
# 2.Install esptool: pip install esptool
# 3. Put ESP32 in Flash Mode:usually  holding down  buttons while resetting the board
# 4.Erase Flash Memory: esptool.py --chip esp32 --port COM14 erase_flash
# 5.Flash MicroPython Firmware: esptool.py --chip esp32 --port COM14 write_flash -z 0x1000 C:\Users\laudo\Downloads\micropython-1.22.2
# 6.Reset the Board
# 7.Access the MicroPython REPL



#ampy --port COM14 run ESP32.py

from machine import Pin, ADC
import time
import random

# Define pin numbers
hall_pin = 34  # Example pin number, replace with the appropriate GPIO pin
temp_sensor_pin = 35  # Example pin number, replace with the appropriate GPIO pin

# Setup ADC for temperature sensor
temp_sensor = ADC(Pin(temp_sensor_pin))
temp_sensor.atten(ADC.ATTN_11DB)  # Set attenuation for full range of 0-3.3V

# Setup Hall sensor
hall_sensor = Pin(hall_pin, Pin.IN)

def temprature_sens_read():
    # Replace with your temperature sensor reading logic
    # This is just a placeholder
    return random.randint(0, 1023)  # Simulating temperature sensor reading

def setup():
    # Initialize serial communication
    import machine
    uart = machine.UART(0, baudrate=115200)
    print("UART Initialized")
    time.sleep(2)  # Wait for serial to initialize

def loop():
    while True:
        # Read hall sensor
        measurement = hall_sensor.value()

        # Read temperature sensor
        temp_raw = temp_sensor.read()
        temp = ((temp_raw * 3.3 / 4095) - 0.5) * 100  # Convert raw ADC value to voltage and then to Celsius
        temp = (temp - 32) / random.randint(0, 20)  # Convert to Celsius and apply random scaling (just for example)

        # Print measurements
        print("Hall sensor measurement:", measurement)
        print("Temperature:", temp, "C")

        time.sleep(2)  # Delay before next reading

if __name__ == "__main__":
    setup()
    loop()

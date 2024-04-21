# Flash MicroPython Firmware
# 1.download MicroPython
# 2.Install esptool: pip install esptool
# 3. Put ESP32 in Flash Mode:usually  holding down  buttons while resetting the board
# 4.Erase Flash Memory: esptool.py --chip esp32 --port COM14 erase_flash
# 5.Flash MicroPython Firmware: esptool.py --chip esp32 --port COM14 write_flash -z 0x1000 <path_to_firmware>
# 6.Reset the Board
# 7.Access the MicroPython REPL



#ampy --port COM14 run ESP32.py



import machine 
machine.freq()          # get the current frequency of the CPU
machine.freq(240000000) # set the CPU frequency to 240 MHz

import esp
esp.osdebug(None)       # turn off vendor O/S debugging messages
esp.osdebug(0) 

# low level methods to interact with flash storage
esp.flash_size()
esp.flash_user_start()
esp.flash_erase(sector_no)
esp.flash_write(byte_offset, buffer)
esp.flash_read(byte_offset, buffer)

import esp32

Sensor= esp32.hall_sensor()     # read the internal hall sensor
Temperature= esp32.raw_temperature() # read the internal temperature of the MCU, in Farenheit
esp32.ULP()             # access to the Ultra-Low-Power Co-processor



# import urequests



# def http_get_request(url):
#     try:
#         response = urequests.get(url)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             print("Failed to fetch data. Status code:", response.status_code)
#             return None
#     except Exception as e:
#         print("Exception occurred:", e)
#         return None

# def main():
#     server_ip = "127.0.0.42"
#     port = 8080
#     endpoint = "/Sample.json"
#     url = "http://{}:{}{}".format(server_ip, port, endpoint)

#     data = http_get_request(url)
#     if data:
#         print("Fruit:", data["fruit"])
#         print("Size:", data["size"])
#         print("Color:", data["color"])

# if __name__ == "__main__":
#     main()

print(Sensor)
print(Temperature)
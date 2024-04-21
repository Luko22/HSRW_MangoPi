# Flash MicroPython Firmware
# 1.download MicroPython
# 2.Install esptool: pip install esptool
# 3. Put ESP32 in Flash Mode:usually  holding down  buttons while resetting the board
# 4.Erase Flash Memory: esptool.py --chip esp32 --port COM14 erase_flash
# 5.Flash MicroPython Firmware: esptool.py --chip esp32 --port COM14 write_flash -z 0x1000 <path_to_firmware>
# 6.Reset the Board
# 7.Access the MicroPython REPL



#ampy --port COM14 run ESP32.py


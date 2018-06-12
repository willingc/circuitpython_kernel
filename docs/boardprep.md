
# Board Preparation


## Adafruit Express Boards, SAMD

### Boards Supported:

 - [Circuit Playground Express](https://www.adafruit.com/product/3333)
 - [Feather M0 Express](https://www.adafruit.com/product/3403)
 - [Trinket M0](https://www.adafruit.com/product/3500)
 - [Metro M0 Express](https://www.adafruit.com/product/3505)
 - [Gemma M0](https://www.adafruit.com/product/3501)

### Add CircuitPython firmware

- Download the [CircuitPython Firmware (.uf2 file) from the CircuitPython Repo](https://github.com/adafruit/circuitpython/releases)
- Plug in board and double click the **reset** button to enter bootloader mode.
- Drag and drop the \*.uf2 CircuitPython file to the USB drive.
- If you see the `CIRCUITPY` as the new name of the USB drive, you're ready to go.


## Adafruit Feather Huzzah ESP8266

### Add CircuitPython firmware

- python3 -m pip install esptool
- - Download the [CircuitPython Firmware (.bin file) from the CircuitPython Repo](https://github.com/adafruit/circuitpython/releases)
- Install the [SiLabs CP210x driver](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)
- Erase flash `python3 esptool.py --port /path/to/ESP8266 erase_flash`
- Load firmware: `esptool.py --port /path/to/ESP8266 --baud 460800 write_flash --flash_size=detect 0 firmware.bin`
- Press reset or unplug/plug the board.

### Access the REPL

Use `screen` program:

    screen <device> 115200


## ampy

- Install ampy `python3 -m pip install adafruit-ampy`
- To get options for listing files and moving files: `ampy --help`

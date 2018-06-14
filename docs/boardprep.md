
# Board Preparation

Before you start using the CircuitPython_Kernel, you'll need a board running CircuitPython. If you're not sure if
the board plugged into your computer is running CircuitPython, check your file explorer for a drive named `CIRCUITPY`

## Designed for CircuitPython (SAMD21 and SAMD51)

### Boards Supported:

 - [Circuit Playground Express](https://www.adafruit.com/product/3333)
 - [Feather M0](https://www.adafruit.com/product/3403)
 - [Trinket M0](https://www.adafruit.com/product/3500)
 - [Metro M0 Express](https://www.adafruit.com/product/3505)
 - [Gemma M0](https://www.adafruit.com/product/3501)
 - [ItsyBitsy M0](https://www.adafruit.com/product/3727)

 - [Metro M4 ]( https://www.adafruit.com/product/3382)
 - [ItsyBitsy M4](https://www.adafruit.com/product/3727)


### Installing CircuitPython Firmware

- Download the [CircuitPython Firmware (.uf2 file) from the CircuitPython Repo](https://github.com/adafruit/circuitpython/releases)
- Plug in board and double click the **reset** button to enter bootloader mode.
- Drag and drop the \*.uf2 CircuitPython file to the USB drive.
- If you see the `CIRCUITPY` as the new name of the USB drive, you're ready to go.


## Adafruit Feather Huzzah ESP8266

While they do work with CircuitPython_Kernel, ESP8266-based boards require a different type of installation and configuration
from the boards designed for circuitpython.

### Installing CircuitPython Firmware

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

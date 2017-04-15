# Board Preparation


## Adafruit Feather M0 Express

### Add CircuitPython firmware

- Download CircuitPython firmware.
- Plug in board and double click the **reset** button.
- Drag and drop the \*.uf2 CircuitPython file to the USB drive
- You should see the `CIRCUITPY` as the new name of the USB drive

## Adafruit Feather M0 SAMD21

### Add CircuitPython firmware

- Download CircuitPython firmware.
- Go to the BOSSA GitHub releases page and download the latest release.
- Plug in board and double click the **reset** button.
- Copy firmware into the same directory as BOSSA tool.
- Enter `bossac -e -w -v -R -p PORT_NAME firmware.bin`

### Access the REPL

Use `screen` program:

    screen /dev/cu.usb1421 115200


## Adafruit Feather Huzzah ESP8266

### Add CircuitPython firmware

- python2 -m pip install esptool
- Download CircuitPython firmware
- Install the [SiLabs CP210x driver](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)
- Erase flash `python2 esptool.py --port /path/to/ESP8266 erase_flash`
- Load firmware: `esptool.py --port /path/to/ESP8266 --baud 460800 write_flash --flash_size=detect 0 firmware.bin`
- Press reset or unplug/plug the board.

### Access the REPL

Use `screen` program:

    screen <device> 115200


## ampy

- Install ampy `python3 -m pip install adafruit-ampy`
- To get options for listing files and moving files: `ampy --help`

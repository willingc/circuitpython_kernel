# -*- coding: utf-8 -*-
"""Serial Connection to a Board"""
import time
from serial import Serial
from serial.tools.list_ports import comports

# Vendor ID for SAMD Adafruit
ADAFRUIT_VID = 0x239A


# Vendor ID for Feather Huzzah ESP8266
ESP8266_VID = 0x10C4

BAUDRATE = 115200
IS_ESP = False

def find_adafruit_board():
    """Find serial port where Adafruit board is connected"""
    # pylint: disable-msg=W0603
    global IS_ESP
    port = None
    for port in comports():
        print('vid: ', port.vid)
        if port.vid == ADAFRUIT_VID:
            IS_ESP = False
        elif port.vid == ESP8266_VID:
            IS_ESP = True
    return port.device

def connect():
    """Connect to a pySerial Serial object.

    If you do not see the REPL hit `enter` a few times. Control-A or Home
    sends you to beginning of line. Control-E or End to the end of the line.

    SAMD21 REPL prompt is `>>>`
       - Press any key will enter REPL
       - Ctrl-D does a soft reset.

    ESP8266 REPL prompt is `>>>`

    There are four other control commands:

    Ctrl-A on a blank line will enter raw REPL mode. This is like a permanent
    paste mode, except that characters are not echoed back.

    Ctrl-B on a blank like goes to normal REPL mode.

    Ctrl-C cancels any input, or interrupts the currently running code.

    Ctrl-D on a blank line will do a soft reset.

    Note that Ctrl-A and Ctrl-D do not work with WebREPL.

    Returns
    -------
    obj
        Serial object connected to the microcontroller board

    """
    cpy_board = Serial(find_adafruit_board(), 115200, parity='N')
    time.sleep(0.5)
    if not cpy_board.is_open:
        cpy_board.open()
    if not IS_ESP:
        cpy_board.write(b'\x03\x03\x01')  # ctrl+c (2x), ctrl+a
        cpy_board.read_until(b'raw REPL')
        cpy_board.read_until(b'\r\n>')  # Wait for prompt
    else:
        cpy_board.write(b'\r\x03\x03')
        cpy_board.write(b'\r\x01') # ctrl-A: enter raw REPL
        cpy_board.read_until(b'raw REPL; CTRL-B to exit\r\n>')
    return cpy_board

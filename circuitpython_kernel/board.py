# -*- coding: utf-8 -*-
"""Serial Connection to a Board"""

from serial import Serial
from serial.tools.list_ports import comports

# Boards USB
FEATHER_MO_BASIC_VID = '239A'
FEATHER_MO_BASIC_PID = '8015'

BAUDRATE = 115200
PARITY = 'N'


def find_board():
    """Find port where first board is connected."""
    for port in comports():
        if port.vid == FEATHER_MO_BASIC_VID and port.pid == FEATHER_MO_BASIC_PID:
            return port.device


def connect():
    """Connect to a pySerial Serial object.

    If you do not see the REPL hit `enter` a few times. Control-A or Home
    sends you to beginning of line. Control-E or End to the end of the line.

    ESP8266 REPL prompt is `>>>`

    SAMD21 REPL prompt is `>>>`

    There are four other control commands:

    Ctrl-A on a blank line will enter raw REPL mode. This is like a permanent
    paste mode, except that characters are not echoed back.

    Ctrl-B on a blank like goes to normal REPL mode.

    Ctrl-C cancels any input, or interrupts the currently running code.

    Ctrl-D on a blank line will do a soft reset.

    Note that ctrl-A and ctrl-D do not work with WebREPL.

    """
    s = Serial(find_board(), BAUDRATE, parity=PARITY)
    if not s.is_open:
        s.open()
    s.write(b'\x03\x01')  # Ctrl-C: interrupt, Ctrl-A: switch to raw REPL
    s.read_until(b'raw REPL')
    s.read_until(b'\r\n>')  # Wait for prompt
    return s

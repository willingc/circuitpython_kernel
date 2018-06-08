# -*- coding: utf-8 -*-
"""Serial Connection to a Board"""

from serial import Serial
from serial.tools.list_ports import comports


# Atmel SAMD Boards USB
FEATHER_MO_BASIC = {'VID': 0x239A, 'PID': 0x8015}
FEATHER_MO_EXPRESS = {'VID': 0x239A, 'PID': 0x8023}
FEATHER_MO_WIFI = {'VID': 0x239A, 'PID': 0x801b}
TRINKET_MO = {'VID': 0x239A, 'PID': 0x801F}
METRO_M0 = {'VID': 0x239A, 'PID': 0x8014}
METRO_M4 = {'VID': 0x239A, 'PID': 0x8021}
CPX_M0 = {'VID': 0x239A, 'PID': 0x8018}

# ESP Boards USB (SLAB_USBtoUART)
HUZZAH_8266 = {'VID': 0x10C4, 'PID': 0xEA60}

BAUDRATE = 115200
PARITY = 'N'


def find_board():
    """Find connected board port

    Returns
    -------
    port.device
        Serial object connected to the microcontroller board
    is_samd
        bool: samd or non-samd (ESP-based) board type
    """
    is_samd = True
    for port in comports():
        # check if SAMD-based
        if (
            (
                port.vid == FEATHER_MO_BASIC['VID']
                and port.pid == FEATHER_MO_BASIC['PID']
            )
            or (
                port.vid == FEATHER_MO_EXPRESS['VID']
                and port.pid == FEATHER_MO_EXPRESS['PID']
            )
            or (
                port.vid == TRINKET_MO['VID']
                and port.pid == TRINKET_MO['PID']
            )
            or (
                port.vid == METRO_M4['VID']
                and port.pid == METRO_M4['PID']
            )
            or (
                port.vid == CPX_M0['VID']
                and port.pid == CPX_M0['PID']
            )
            or (
                port.vid == FEATHER_MO_WIFI['VID']
                and port.pid == FEATHER_MO_WIFI['PID']
            )
        ):
            #return port.device
            is_samd = True
        # check if ESP-based
        elif (
                (
                    port.vid == HUZZAH_8266['VID']
                    and port.pid == HUZZAH_8266['PID']
                )
        ):
            is_samd = False
        return is_samd
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
    try:
        s = Serial(find_board(), 115200, parity=PARITY)
    except:
        print("Board not found")
    if not s.is_open:
        s.open()
    s.write(b'\x03\x01')  # Ctrl-C: interrupt, Ctrl-A: switch to raw REPL
    s.read_until(b'raw REPL')
    s.read_until(b'\r\n>')  # Wait for prompt
    print (s)
    return s

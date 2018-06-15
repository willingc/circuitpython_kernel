# -*- coding: utf-8 -*-
"""Serial Connection to a Board"""
from serial import Serial
from serial.tools.list_ports import comports

# Vendor ID for SAMD Adafruit
ADAFRUIT_VID = 0x239A
# Vendor ID for Feather Huzzah ESP8266
ESP8266_VID = 0x10C4

# repl commands
CHAR_CTRL_A = b'\x01'
CHAR_CTRL_B = b'\x02'
CHAR_CTRL_C = b'\x03'
CHAR_CTRL_D = b'\x04'
# repl messages
MSG_NEWLINE = b"\r\n"
MSG_RAWREPL = b"raw REPL; CTRL-B to exit"
MSG_RAWREPL_PROMPT = b"\r\n>"

class CPboardError(BaseException):
    """ Reporter for CircuitPython Board Errors. """
    pass


def find_adafruit_board():
    """Find serial port where Adafruit board is connected"""
    for port in comports():
        if port.vid == ADAFRUIT_VID or port.vid == ESP8266_VID:
            return port.device

def connect():
    """Connects to a pySerial Serial object.

    Returns
    -------
    obj
        Serial object connected to the microcontroller board

    """
    try:
        cpy_board = Serial(find_adafruit_board(), 115200, parity='N')
    except:
        raise CPboardError('failed to access ' + cpy_board)
    if not cpy_board.is_open:
        cpy_board.open()
    # open the REPL
    cpy_board.write(CHAR_CTRL_C)
    cpy_board.write(CHAR_CTRL_A)
    # wait for prompt
    cpy_board.read_until(MSG_RAWREPL)
    cpy_board.read_until(MSG_RAWREPL_PROMPT)
    return cpy_board

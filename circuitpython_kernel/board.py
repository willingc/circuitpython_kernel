# -*- coding: utf-8 -*-
"""Serial Connection to a Board"""

from serial import Serial
from serial.tools.list_ports import comports

CPSAMD_PID = 516
CPSAMD_VID = 3368
BAUDRATE = 115200
PARITY = 'N'


def find_board():
    """Find the port for the first board found connected to the kernel."""
    for port in comports():
        if port.vid == CPSAMD_VID and port.pid == CPSAMD_PID:
            return port.device


def connect():
    """Connect using a pySerial Serial object to talk to the boards"""
    #s = Serial(find_circuitpython_board(), BAUDRATE, parity=PARITY)
    # Hardcoded current device
    s = Serial('/dev/tty.usbmodem1421', BAUDRATE, parity=PARITY)
    s.write(b'\x03\x01')  # Ctrl-C: interrupt, Ctrl-A: switch to raw REPL
    s.read_until(b'raw REPL')
    s.read_until(b'\r\n>')  # Wait for prompt
    return s

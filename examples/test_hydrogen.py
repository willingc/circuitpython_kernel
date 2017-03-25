import serial

ser = serial.Serial('/dev/cu.usbmodem1421')

print(ser.name)
print(ser.baudrate)
print(ser.fileno)

import serial
import time

ser = serial.Serial(port='/dev/ttyUSB0',baudrate=115200,timeout=1)
time.sleep(1)

print(ser.name) 
while True:
    ser.write(b'1')
    time.sleep(2)
ser.close()


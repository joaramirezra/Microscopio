import serial
import time

ser = serial.Serial(port='/dev/ttyUSB1',baudrate=9600,timeout=0.5)

ser.close()
ser.open()

print(ser.name) 

while True :
    ser.write(b'1\n')
    time.sleep(1)
ser.close()



import serial
import time

ser = serial.Serial(port='/dev/ttyUSB1',baudrate=9600,timeout=0)

ser.close()
ser.open()

print(ser.name) 

while True :
    ser.write('1 \n'.encode())
    time.sleep(1)
    r = ser.readline()
    print(r)
ser.close()



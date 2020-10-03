import serial
import time
ser = serial.Serial(
    port='/dev/ttyUSB0',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)
count=1
while True:
    for line in ser.read():

        print(str(count) + str(': ') + chr(line) )
        count = count+1
    ser.write(b'1')
    time.sleep(4)
    ser.write(b'2')
    time.sleep(4)
ser.close()

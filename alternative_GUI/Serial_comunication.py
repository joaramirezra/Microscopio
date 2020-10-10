import serial
import time

#-------------------------------------------------------------------------------
def create_port(port):
    port = str('/dev/')+port
    try:
        ser = serial.Serial(port=port,baudrate=9600,timeout=1)
        time.sleep(2)
        return ser
    except:
        print('Open port failded')
        return False

#-------------------------------------------------------------------------------
def open_port(ser):
    if(ser.isOpen()):
        return True
    else: 
        try:
            ser.open()
            return True
        except:
            print("error opening")
            return False

#-------------------------------------------------------------------------------
def close_port(ser):
    ser.close()

#-------------------------------------------------------------------------------
def send_value(value,ser):
	string = "".join([str(value),' \n'])
	ser.write(string.encode())


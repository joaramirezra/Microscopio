import serial
import time

#-------------------------------------------------------------------------------
def create_port(port):
    port = str('/dev/')+port
    try:
        ser = serial.Serial(port=port,baudrate=9600,timeout=1)
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


# import time
# def prueba_cuadrado():
#     port = create_port('ttyUSB0')
#     send_value("5,10,60",port)
#     time_1 = 4
#     while True:
#         send_value("1",port)
#         time.sleep(time_1)
#         send_value("4",port)
#         time.sleep(time_1)
#         send_value("2",port)
#         time.sleep(time_1)
#         send_value("3",port)
#         time.sleep(time_1)

# prueba_cuadrado()
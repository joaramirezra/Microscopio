import serial
import time
from Files_management import get_mov_parameters,change_mov_parameters

#-------------------------------------------------------------------------------
def create_port():
    port = get_mov_parameters()[1]
    try:
        ser = serial.Serial(port=port,baudrate=9600,timeout=1)
        return ser
    except:
        print('Open port failded')
        change_mov_parameters('0',port,'0','0')
        return False

#-------------------------------------------------------------------------------
def port_status(ser):
    if(ser.isOpen()):
        if(get_mov_parameters()[0] == "1" or get_mov_parameters()[0] == "True"):
            return True
    else: 
        try:
            create_port()
            return True
        except:
            print("error opening")
            change_mov_parameters('0',get_mov_parameters()[1],'0','0')
            return False

#-------------------------------------------------------------------------------
def close_port(ser):
    ser.close()

#-------------------------------------------------------------------------------
def send_value(value):
    port = create_port()
    status = get_mov_parameters()[0]
    if(port_status(port)):
        if(status == '1' or status == 'True'):
            string = "".join([str(value),' \n'])
            port.write(string.encode())
            print('True')
    else :
        print('False')
    

from file_flow import *
from Serial_comunication import create_port,open_port,send_value
import time


#-------------------------------------------------------------------------------
def move_right(port):
	send_value("1",port)

#-------------------------------------------------------------------------------	
def move_left(port):
	send_value("2",port)

#-------------------------------------------------------------------------------
def move_up(port):
	send_value("3",port)

#-------------------------------------------------------------------------------
def move_down(port):
	send_value("4",port)

#-------------------------------------------------------------------------------
def cal_next_point(coor_x,coor_y,port):
	if (coor_x < 40 and coor_y%2 == 0):
		move_right(port)
	elif (coor_x < 40 and coor_y%2 == 1):
		move_left(port)
	elif (coor_x == 40):
		move_up(port)

#-------------------------------------------------------------------------------        

port = create_port('ttyUSB0')

if(open_port(port)):
    for prueba in range(10):
        x = int(input())
        y = int(input())
        cal_next_point(x,y,port)






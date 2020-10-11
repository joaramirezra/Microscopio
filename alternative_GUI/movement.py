from Serial_comunication import send_value
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
	try:
		coor_x = int(coor_x)
		coor_y = int(coor_y)
		if (coor_x < 40 and coor_y%2 == 0):
			move_right(port)
		elif (coor_x < 40 and coor_y%2 == 1):
			move_left(port)
		elif (coor_x == 40):
			move_up(port)
	except:
		print('bad coord')
#-------------------------------------------------------------------------------
def back_to_last(coor_x,coor_y,port):
	if (coor_x < 40 and coor_y%2 == 0):
		move_left(port)
	elif (coor_x < 40 and coor_y%2 == 1):
		move_right(port)
	elif (coor_x == 40):
		move_down(port)
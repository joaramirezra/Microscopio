from file_flow import * 
from Serial_comunication import send_value,create_port

def init_port():
    port = create_port('ttyUSB0')
    return port
#-------------------------------------------------------------------------------
def read_param():
    cont,step,x,y  = 0,0,0,0
    if(is_empty()):
        clean_file()
        create_title()
        print('Send to home')
        cont,step,x,y  = 0,1,0,0
    else:
        line = Read_last_line()
        cont,step,x,y = line[0],line[1],line[2],line[3]
    return cont,int(step),int(x),int(y)

#-------------------------------------------------------------------------------
def cal_movement(direction): # 1:forward, -1:backward 
    x_limit,y_limit = 44,24
    cont,step,x,y = read_param()

    dir = (1 if (y%2==0) else -1)*direction

    if((x+dir*step) in range(x_limit)):
        mov = (1 if (dir > 0) else 2)
    elif ((y+dir*step) in range(y_limit)):
        mov = (3 if (dir > 0) else 4)
    else :
        mov = -1
    return mov,cont,step,x,y

#-------------------------------------------------------------------------------
def save_new_point(dir,port):
    mov,cont,step,x,y = cal_movement(int(dir))
    cont = number_components()
   
    send_value(str(mov),port)
    if( mov == 1 or mov == 2):
        difx = (1 if (y%2==0) else -1)*dir*step
        add_point_to_file(cont,step,x+difx,y,1,1)
    elif(mov == 3 or mov == 4):
        dify = dir*step
        add_point_to_file(cont,step,x,y+dify,1,1)   
    else :
        pass

port = init_port()
while True:
    save_new_point(int(input("dir : ")),port)

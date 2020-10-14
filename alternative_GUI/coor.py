#point calculations

# if file is empty is necesary send to home
# if is not, read the last line and calculate the coordinates
# or save in a file the position 

from file_flow import *   

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
    x_limit,y_limit = 5,10
    _,step,x,y = read_param()

    dir = (1 if (y%2==0) else -1)*direction
    
    print(x,dir,step,(x+dir*step) in range(x_limit))
    if((x+dir*step) in range(x_limit)):
        return (1 if (dir > 0) else 2)
    elif ((y+dir*step) in range(y_limit)):
        return (3 if (dir > 0) else 4)
    else :
        return -1

#-------------------------------------------------------------------------------
def save_new_point(dir):
    cont,step,x,y = read_param()
    cont = number_components()
    mov = cal_movement(int(dir))
    print(mov)
    if( mov == 1 or mov == 2):
        add_point_to_file(cont,step,x+step,y,1,1)   
    elif(mov == 3 or mov == 4):
        add_point_to_file(cont,step,x,y+step,1,1)   
    else :
        pass

while True: 
    save_new_point(int(input("dir : ")))

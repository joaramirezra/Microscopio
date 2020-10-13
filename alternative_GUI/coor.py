#point calculations

# if file is empty is necesary send to home
# if is not, read the last line and calculate the coordinates
# or save in a file the position 

from file_flow import is_empty, Read_last_line

def read_coor(coor_x,coor_y,step):
    if(is_empty()):
       print('Send to home')
       return 0,0
    else:
        line = Read_last_line()
        print(line)
        return line[1],line[2]


print(read_coor(1,1,1))
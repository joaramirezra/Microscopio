from file_flow import clean_file,create_title,add_point_to_file,is_empty,number_components
from movement import cal_next_point
from Serial_comunication import create_port,open_port

#-------------------------------------------------------------------------------
def init_port():
    port = create_port('ttyUSB0')
    return port

#-------------------------------------------------------------------------------
def next_point(coor_x,coor_y,element,size):
    port = init_port()

    if (is_empty()):
        clean_file()
        create_title()
        cont = 1
        add_point_to_file(cont,1, coor_x , coor_y, element, size)

    else:
        cont = number_components()
        add_point_to_file(cont,1, coor_x , coor_y, element, size)
        cal_next_point(coor_x,coor_y,port)




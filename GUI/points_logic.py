# control crud points
from Files_management import create_file,there_is_component,add_size,get_info
from Files_management import add_components_count,get_count_parameters
from Files_management import set_count_parameters_off,cal_movement_direction
from Files_management import cal_new_coordinates,set_count_parameters_on
from Files_management import add_components,get_size,reduce_key_and_size_count
from Files_management import get_last_component_size,delete_last_lines_component_list
from setup_logic import get_mov_parameters

#-------------------------------------------------------------------------------        
def reset_all():
    [create_file(i) for i in range(6) ]
    
#-------------------------------------------------------------------------------        
def add_point(key,size):
    status,_,step,_ = get_mov_parameters()
    max_counter,counter = map(int,get_count_parameters()[:2])
        
    if(status == '0' or status == 'False'):
        if(max_counter>counter and there_is_component(key)):    
            add_size(size)
            add_components_count(key)
            counter += 1
            set_count_parameters_off(counter)
            component,_ = get_info(key)
            size =get_size(size)
            add_components(counter,'0','0',component,size)
            return True
        else:
            return False
    
    elif(status == 'True' or status == '1' ):
        if(max_counter>counter and there_is_component(key)):
            mov = cal_movement_direction(1)
            if(mov in range(1,5)):
                add_size(size)
                add_components_count(key)
                counter += 1
                x,y = cal_new_coordinates(int(step),mov)
                set_count_parameters_on(counter,x,y)
                component,_ = get_info(key)
                size =get_size(size)
                add_components(counter,x,y,component,size)
                return True
            else:
                return False
    
#-------------------------------------------------------------------------------        
def erase_last():
    status,_,step,_ = get_mov_parameters()
    max_counter,counter = map(int,get_count_parameters()[:2])
        
    if(counter>0):
        if(status == '0' or status == 'False'):
            key, size = get_last_component_size()
            reduce_key_and_size_count(key, size) 
            counter -= 1
            set_count_parameters_off(counter)
            delete_last_lines_component_list()	       
            print('erased')
    
        elif(status == 'True' or status == '1' ):
            key, size = get_last_component_size()
            reduce_key_and_size_count(key, size) 
            counter -= 1
            
            mov = cal_movement_direction(-1)
            x,y = cal_new_coordinates(int(step),mov)
            
            set_count_parameters_on(counter,x,y)
            delete_last_lines_component_list()	       
            print('erased')
    
#-----------------------------test--------------------------------------------
# reset_all()
# # from Components_logic import fill_to_test
# # fill_to_test()
# import time
# for k in range(10):
#     erase_last()
#     time.sleep(1)
# # for k in range (10):
# #     add_point('f',k)
# #     add_point('a',k)
# #     add_point('q',k)
# #     add_point('w',k)
    

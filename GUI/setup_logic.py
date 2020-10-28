#setup_logic
from Files_management import change_mov_parameters,get_mov_parameters


def setup(new_step, new_speed):
    status,portname,_,_ = get_mov_parameters()
    if(status == '0' or status == 'False'): # No connect
        print('value no send')
    else :
        print('send(5, new_speed,new_step)')
    change_mov_parameters(status,portname,new_step,new_speed)

def send_home():
    status,_,_,_ = get_mov_parameters()
    if(status == '1' or status == 'True'): # No connect
        print('send(0)')
        print('also change coordinates')
    else:
        print('no conected')

# this file helps to manage some files

#-------------------------------------------------------------------------------        
def create_file(reference):
	files = ["mov_parameters.csv","count_parameters.csv","components.csv",
			 "size-count.csv","compenents-count.csv","pair_compenents_key.csv"]

	file = open(files[reference],"w") 
	
	if (reference == 0):
		parameters = ["connection_status","port_name","step","speed"]
		[file.write(":".join([param,"0"]) + '\n' ) for param in parameters]

	elif (reference == 1):
		parameters = ["max_count","counter","coor_x","coor_y","x_limit","y_limit"]
		change_count_parameters(300,0,0,0,40,20)

	elif (reference == 2):
		tittle = ";".join(["count" ,"coor x" , "coor y","Component", "Size"])
		file.write((tittle+' \n'))

	elif (reference == 3):
		sizes = ["<1e-3","2e-3","5e-3","0.01","0.02","0.05","0.1","0.25","0.2",
			   "0.5","1","2","3","5","10","20",">20"]
		[file.write(":".join([size,"0"]) + '\n' ) for size in sizes]

	file.close() 

#-------------------------------------------------------------------------------        
def change_mov_parameters(status,portname,step,speed):
	file = open("mov_parameters.csv","w")
	
	status = True if (status=="1") else False
	parameters = ["connection_status","port_name","step","speed"]
	values = [str(status),str(portname),str(step),str(speed)] 
	
	[file.write(":".join([parameters[i],values[i]]) + '\n' ) for i in range(4)]
	file.close()

#-------------------------------------------------------------------------------        
def get_mov_parameters():
	file = open("mov_parameters.csv","r")
	lines = file.readlines()
	file.close()
	return [line.split(':')[1].replace('\n','') for line in lines]	

#-------------------------------------------------------------------------------        
def get_count_parameters():
	file = open("count_parameters.csv","r")
	lines =file.readlines()
	return [line.split(':')[1].replace('\n','') for line in lines]
		
#-------------------------------------------------------------------------------        
def change_count_parameters(max_count,counter,coor_x,coor_y,x_limit,y_limit):
	file = open("count_parameters.csv","w")
	
	parameters = ["max_count","counter","coor_x","coor_y",'x_limit','y_limit']
	values = [str(max_count),str(counter),str(coor_x),str(coor_y)
		      ,str(x_limit),str(y_limit)] 
	
	[file.write(":".join([parameters[i],values[i]]) + '\n' ) for i in range(6)]
	file.close()

#-------------------------------------------------------------------------------        
def set_count_parameters_off(counter):
	parameters = ["max_count","counter","coor_x","coor_y",'x_limit','y_limit']
	param = get_count_parameters()
	param[1] = str(counter)
	file = open("count_parameters.csv","w")
	for paramet,value in zip(parameters, param):
		file.write(":".join([paramet,value])+str('\n'))

#-------------------------------------------------------------------------------        
def add_components(count ,coor_x ,coor_y,Component, Size):
	file = open("components.csv","a")
	
	values = [str(count),str(coor_x),str(coor_y),str(Component),str(Size)] 
	
	[file.write((",".join([value for value in values])+ str('\n')))]
	file.close()

#-------------------------------------------------------------------------------        
def add_size(Size):
	file = open("size-count.csv","r+")
	lines = file.readlines()

	value,count = lines[Size].split(":")
	count = int(count)+1
	
	file.close()
	file = open("size-count.csv","w")

	lines[Size] = ":".join([value,str(count)])+str('\n')
	
	[file.write(line) for line in lines]
	file.close()	

#-------------------------------------------------------------------------------        
def get_size(Size):
	file = open("size-count.csv","r+")
	lines = file.readlines()
	file.close()
	return lines[Size].split(':')[0]
	
#-------------------------------------------------------------------------------        
def add_components_count(new_key):
	_,index=get_info(new_key)
	
	file = open("compenents-count.csv","r+")
	
	lines = file.readlines()
	component,count = lines[index].split(':')
	line = ":".join([component,str(int(count)+1)])+str('\n')
	lines[index] = line
	file.close()
	file = open("compenents-count.csv","w")
	[file.write(line) for line in lines]
	file.close()
	return True	

#-------------------------------------------------------------------------------        
def add_pair_key_component(new_key,new_component):
	if(there_is_component(new_key)):
		return False
	else: 
		file = open("pair_compenents_key.csv","a")
		string = ":".join([new_key,new_component])+str('\n')
		file.write(string)
		file.close()
	return True

#-------------------------------------------------------------------------------        
def new_component_count(new_component):
	file = open("compenents-count.csv","a")
	file.write(":".join([new_component,'0'])+str('\n'))
	file.close()
	return True

#-------------------------------------------------------------------------------        
def there_is_component(key_to_check):
	file = open("pair_compenents_key.csv","r")
	keys = [line.replace('\n','').split(':')[0] for line in file.readlines()]
	file.close()
	return ( True if(key_to_check in keys) else False)
	
#-------------------------------------------------------------------------------        
def replace_pair_key_component(new_key,new_component):
	file = open("pair_compenents_key.csv","r")
	lines = file.readlines()
	keys =[line.replace('\n','').split(':')[0] for line in lines]
	file.close()

	index = keys.index(str(new_key)) 
	lines[index]= str(new_key)+str(":")+str(new_component)+str('\n')
	
	file = open("pair_compenents_key.csv","w")
	[file.write(line) for line in lines]
	file.close()

	return True

#-------------------------------------------------------------------------------        
def get_info(key_to_find):
	components=[]
	keys=[]
	try:
		file = open("pair_compenents_key.csv","r+")
	except:
		file = open("pair_compenents_key.csv","w+")

	lines = file.readlines()
	if(len(lines)>0):
		for line in lines : 
			key ,component= line.split(':')
			keys.append(key)
			components.append(component)

	index = keys.index(str(key_to_find))
	key_to_find = components[index].replace('\n','')
	file.close()

	return key_to_find,index

#-------------------------------------------------------------------------------        
def replace_component_count(new_key,new_component):
	file = open("compenents-count.csv","r")
	
	lines = file.readlines()
	_,index = get_info(new_key)
	count = lines[index].replace('\n','').split(':')[1]
	new_line = str(new_component)+str(":")+str(count) + str('\n')

	lines[index] = new_line

	file.close()
	file = file = open("compenents-count.csv","w")
	[file.write(line) for line in lines]
	file.close()
	return True
	
#-------------------------------------------------------------------------------
def get_param_counter():
	file = open("count_parameters.csv","r")
	parameters = [int(line.split(':')[1]) for line in file.readlines()]	
	file.close()
	return parameters

#-------------------------------------------------------------------------------
def cal_movement_direction(direction): # 1:forward, -1:backward 
	x,y,limit_x,limit_y = get_count_parameters()[2:]
	x,y,limit_x,limit_y = map(int,[x,y,limit_x,limit_y])
	step = int(get_mov_parameters()[2])

	dir = (1 if (y%2==0) else -1)*direction

	if((x+dir*step) in range(limit_x)):
		mov = (1 if (dir > 0) else 2)
	elif ((y+direction*step) in range(limit_y)):
		mov = (3 if (direction > 0) else 4)
	else :
		mov = -1
	return mov

#-------------------------------------------------------------------------------
def cal_new_coordinates(step,move_direction):
	x,y = map(int,get_count_parameters()[2:4]) 
	# step = int(get_mov_parameters()[2])	
	
	if(move_direction in [1,2]):
		x = x+(step*(1 if move_direction ==1 else -1))
	elif(move_direction in [3,4]):
		y = y+(step*(1 if move_direction == 3 else -1))
	else :
		pass

	return x,y
	
#-------------------------------------------------------------------------------
def set_count_parameters_on(counter,x,y):
	parameters = ["max_count","counter","coor_x","coor_y",'x_limit','y_limit']
	param = get_count_parameters()
	param[1],param[2],param[3] = map(str,[counter,x,y])
	file = open("count_parameters.csv","w")
	for paramet,value in zip(parameters, param):
		print (":".join([paramet,value]))
		file.write(":".join([paramet,value])+str('\n'))
	
#-------------------------------------------------------------------------------
def get_components():
	file = open("components.csv","r")
	lines = file.readlines()
	file.close()
	return (lines[len(lines)-1].replace('\n','').split(','))[-2:]

#-------------------------------------------------------------------------------
def get_key(component):
	file = open("pair_compenents_key.csv","r+")	
	pair  = [line.replace('\n','').split(':') for line in file.readlines()]
	file.close()

	list_value = [par[1] == component for par in pair]
	index = list_value.index(True)
	return pair[index][0]

#-------------------------------------------------------------------------------
def get_dimention(Size):
	file = open("size-count.csv","r+")
	lines = [line.replace('\n','').split(':') for line in file.readlines()]
	file.close()

	list_value = [par[0] == Size for par in lines]
	index = list_value.index(True)
	return index
	
#-------------------------------------------------------------------------------
def reduce_size(Size):
	file = open("size-count.csv","r+")
	lines = file.readlines()

	value,count = lines[Size].split(":")
	count = int(count)-1 
	count = (0 if (count<0) else count)
	file.close()
	file = open("size-count.csv","w")

	lines[Size] = ":".join([value,str(count)])+str('\n')
	
	[file.write(line) for line in lines]
	file.close()	

#-------------------------------------------------------------------------------
def reduce_components_count(new_key):
	_,index=get_info(new_key)
	
	file = open("compenents-count.csv","r+")
	
	lines = file.readlines()
	component,count = lines[index].split(':')
	count = (0 if (int(count)<1) else (int(count)-1))
	line = ":".join([component,str(count)])+str('\n')
	lines[index] = line
	file.close()
	file = open("compenents-count.csv","w")
	[file.write(line) for line in lines]
	file.close()
	return True	

#-------------------------------------------------------------------------------
def get_last_component_size():
	# component = ()
	component, size = get_components()
	key = get_key(component)
	size = get_dimention(size)
	return key, size

#-------------------------------------------------------------------------------
def reduce_key_and_size_count(key,size):
	reduce_components_count(key)
	reduce_size(size)

#-------------------------------------------------------------------------------
def delete_last_lines_component_list():
	file = open("components.csv","r")
	lines = file.readlines()
	file.close()

	file = open("components.csv","w")
	[file.write(line) for line in lines[:len(lines)-1]]	
	file.close()

# - Others

def split_input(input_string):
	key =[]
	for w in list(input_string):
		if(w.isalpha()):
			key.append(w)
		else :
			break
	key = "".join(key)
	if(len(key)<len(input_string)):
		size = input_string[len(key):]	
	else :
		size = "-1"

	if(size.isdigit()):
		return key,size
	else:
		return key,-1

def get_components_to_print():
	file = open("compenents-count.csv","r+")
	pairs = [line.replace('\n','').split(':') for line in file.readlines()]
	file.close()
	components = [pair[0] for pair in pairs]
	counts = [pair[1] for pair in pairs]
	return components,counts

def get_size_to_print():
	file = open("size-count.csv","r+")
	pairs = [line.replace('\n','').split(':') for line in file.readlines()]
	file.close()
	components = [pair[0] for pair in pairs]
	counts = [pair[1] for pair in pairs]
	return components,counts

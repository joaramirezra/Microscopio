# file managment functions 

#-------------------------------------------------------------------------------        
def clean_file():
	file = open("compuestos.csv","w") 
	file.close() 

#-------------------------------------------------------------------------------        
def create_title():
	file = open("compuestos.csv","w") 
	str_to_append = ";".join(["Point","Step" ,"Coor x" , "Coor y", 
							  "Component", "Size"])
	file.write((str_to_append+' \n'))
	file.close() 

#-------------------------------------------------------------------------------
def is_empty():
	try:
		file = open("compuestos.csv","r") 
	except:
		create_title()
		file = open("compuestos.csv","r")
	lines = file.readlines()
	return bool((len(lines)) <=1 )

#-------------------------------------------------------------------------------
def number_components():
	file = open("compuestos.csv","r") 
	lines = file.readlines()
	return (len(lines))

#-------------------------------------------------------------------------------
def add_point_to_file(point, step,coor_x , coor_y, element, size):
	str_to_append = ";".join([str(point),str(step), str(coor_x) , str(coor_y), 
							  str(element), str(size)])
	file = open("compuestos.csv","a")
	file.write(str_to_append+'\n')

#-------------------------------------------------------------------------------
def Read_last_line():
	file = open("compuestos.csv","r")
	lines = file.readlines()
	
	if(len(lines)<2):
		print("Empty file error")	
		return False
	else :
		last = lines[len(lines)-1].split(";")

	if(len(last) == 6):
		if(last[3].isnumeric() and last[1].isnumeric() and last[2].isnumeric()):
			return last
		else: 
			print("format error")
			return False
	else:
		print("size error")
		return False

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
#---------------------movement parameters file flow-----------------------------
def create_movement_parameters_file():
	file = open("hardware_parameters.csv","w") 
	str_to_append = ";".join(["speed","Step" ,"port_name" , "conection_status"])
	file.write((str_to_append+' \n'))
	str_to_append = ";".join(["0","0" ,"ttyUSB0" , "False"])
	file.write((str_to_append+' \n'))
	file.close() 

#-------------------------------------------------------------------------------        
def change_movement_parameters_file(speed,step,port,status):
	file = open("hardware_parameters.csv","w") 
	str_to_append = ";".join(["speed","Step" ,"port_name" , "conection_status"])
	file.write((str_to_append+' \n'))
	str_to_append = ";".join([str(speed),str(step),str(port),str(status)])
	file.write((str_to_append+' \n'))
	file.close() 

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++        
#--------------------------components file flow---------------------------------

def create_component_key_list():
	file = open("component-key-list.csv","w") 
	str_to_append = ";".join(["component","key"])
	file.write((str_to_append+' \n'))
	file.close() 

#-------------------------------------------------------------------------------        
def add_component_to_list(Component,key):
	file = open("component-key-list.csv","a") 
	str_to_append = ";".join([str(Component),str(key)])
	file.write((str_to_append+' \n'))
	file.close() 


add_component_to_list('hola','key')
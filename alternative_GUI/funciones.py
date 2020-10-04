from SerialArduino import *

elements_list = {}
points_list = {}

dim_reference = {"<1e-3  ":0,"2e-3":0,"5e-3":0,"0.01":0,"0.02":0,"0.05":0,
				 "0.1":0,"0.25":0,"0.2":0,"0.5":0,"1":0,"2":0,"3":0,"5":0,
				 "10":0,">10":0}


## from here are the funcion to add elements to the dict
# elements will have this structure 
# {key : component , count}
# where key is the keyboard combination of tree keys
# component is the material asociated to this combinations
# and count is the times user see in a sample

# The parameters to define a new element are :
# it must a have maximum 3 key asociated (XYZ)
# the key can be repeated 
# two components can't have the same key combinatios

#-------------------------------------------------------------------------------        
def init_size_dict():
	dim_reference = {"<1e-3  ":0,"2e-3":0,"5e-3":0,"0.01":0,"0.02":0,"0.05":0,
				 "0.1":0,"0.25":0,"0.2":0,"0.5":0,"1":0,"2":0,"3":0,"5":0,
				 "10":0,">10":0}
	return dim_reference
	
#-------------------------------------------------------------------------------        
def count_element():
	elements=[]
	size_count = []

	for x in elements_list:
		elements.append(elements_list[x]['component'])
		size_count.append(elements_list[x]['count'])
	return elements,size_count

#-------------------------------------------------------------------------------        
def count_sizes():
	siezes = [*dim_reference]
	size_count = [dim_reference[key] for key in siezes]
	
	return siezes,size_count

#-------------------------------------------------------------------------------        
def add_component(keys_combination, component):
	elements_list[keys_combination] = { 'component': component,
										'count':0}
	return True

#-------------------------------------------------------------------------------        
def add_component_list(keys_combination):
	elements_list[keys_combination]['count'] +=1

#-------------------------------------------------------------------------------        
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

#-------------------------------------------------------------------------------        
def find_key(keys_combination):
	if (keys_combination in elements_list):
		elements_list[keys_combination]['count'] +=1
		return True
	else :
		return False
#-------------------------------------------------------------------------------        

def add_size_mesuare(size):
	if(size in dim_reference):
		dim_reference[size]+=1
	return True


#-------------------------------------------------------------------------------        
def get_component(keys_combination):
	return elements_list[keys_combination].get('component')

#-------------------------------------------------------------------------------        
def size_translation(dimention_value):
	index = int(dimention_value)
	dim_reference_1 = list(dim_reference.keys())
	return dim_reference_1[index]

#-------------------------------------------------------------------------------        
def get_info(key,dimention_value):
	component = get_component(key)
	size = size_translation(dimention_value)
	return component,size

#-------------------------------------------------------------------------------        
def new_element_validation(element_string):
	pass

#-------------------------------------------------------------------------------        
def move_setup(speed,step):
    print(speed,step)

#-------------------------------------------------------------------------------        
def turn_on():
	print('Encendio')

#-------------------------------------------------------------------------------        
def turn_off():
	print('apagado')


#-------------------------------------------------------------------------------        
def find_component():
	return True

#-------------------------------------------------------------------------------        
def replace_element():
	print('reemplazar')

#-------------------------------------------------------------------------------        
def reference_size():
	print('reference')

#-------------------------------------------------------------------------------        
def next_point():
	print('next point')

#-------------------------------------------------------------------------------        
def home():
	home_serial()

#-------------------------------------------------------------------------------        
def reset():
	elements_list.clear()
	dim_reference_1 = list(dim_reference.keys())
	for value in dim_reference_1:
			dim_reference[value] = 0 

#-------------------------------------------------------------------------------        
def erase():
	send_2()
	print('reset')


#-------------------------------------------------------------------------------        
def add_to_list(value):
    print(value)

#-------------------------------------------------------------------------------        
def write_file(component,size):
	file = open("compuestos.txt","a") 
	Line_to_write = "".join([";".join([component,size]),"\n"])
	file.write(Line_to_write) 
	file.close() 

def clean_file():
	file = open("compuestos.csv","w") 
	file.close() 

def leer_ultimo():
	pass
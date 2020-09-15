
elements_list = {}
# points_dictonary = {}

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

def count_element():
	elements=[]
	size_count = []

	for x in elements_list:
		elements.append(elements_list[x]['component'])
		size_count.append(elements_list[x]['count'])
	return elements,size_count

def add_component(keys_combination, component):
	elements_list[keys_combination] = { 'component': component,
										'count':0}
	print(elements_list)
	return True

def add_component_list(keys_combination):
	elements_list[keys_combination]['count'] +=1

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

	if(size.isdigit):
		return key,size
	else:
		return key,-1


def find_key(keys_combination):
	if (keys_combination in elements_list):
		elements_list[keys_combination]['count'] +=1
		return True
	else :
		return False

def get_component(keys_combination):
	return elements_list[keys_combination].get('component')

def size_translation(dimention_value):
	index = int(dimention_value)-1
	dim_reference = ["<0.001","0.002","0.005","0.01","0.02","0.05","0.1","0.25",
						"0.2","0.5","1","2","3","5","10",">20"]
	return dim_reference[index]


def get_info(key,dimention_value):
	component = get_component(key)
	size = size_translation(dimention_value)
	return component,size

## 

def new_element_validation(element_string):
	pass

def move_setup(speed,step):
    print(speed,step)

def turn_on():
	print('Encendio')

def turn_off():
	print('apagado')




def find_component():
	return True

def replace_element():
	print('reemplazar')

def reference_size():
	print('reference')

def next_point():
	print('next point')

def home():
	print('home')

def reset():
	print('reset')

def erase():
	print('erase last')


def add_to_list(value):
    print(value)


# funcntion to plot 


# from pyqtgraph import PlotWidget
# import numpy as np


    #     self.graphicsView.setBackground('#3c3f58')
    #     self.graphicsView_2.setBackground('#3c3f58')
    #     self.begin_button.clicked.connect(self.draw_size)
    
    # def draw_size(self):
    #     x = range(100)
    #     y = [w*3 +4  for w in x]
    #     y2 = [ w*w for w in x]
    #     self.graphicsView.plot(x,y)
    #     self.graphicsView_2.plot(x,y2)



# function to get logic 

# # funcion johan 
#         self.begin_button.clicked.connect(self.move_init)
#         self.home_button.clicked.connect(home)
#         self.Save_element_button.clicked.connect(self.add_element)
#         self.next_button.clicked.connect(self.save_element)
#         self.erase_last_button.clicked.connect(erase) 
#         self.restart_counting_button.clicked.connect(reset)
#         self.Size_reference_button.clicked.connect(self.reference_pop)      
#         # call when enter is presed
#         self.lineEdit.returnPressed.connect(self.save_element) 
            
#     def reference_pop(self):
#         print('pop up with a image of size')

#     def move_init(self):
    
#         step_setup = self.Step_spinbox.value()
#         speed_setup = self.speed_spinbox.value()
#         move_setup(speed_setup,step_setup)
    
#     def add_element(self):

#         keys_string = self.Key_input.text()
#         component_string = self.new_compnent_input.text()

#         if(len(keys_string) < 4  and keys_string.isalpha() ):
#             if( len(component_string) == 0 ) : 
#                 print('error no element ')
#             else : 
#                 if(add_component(list(keys_string),list(component_string))):
#                     self.Key_input.clear()
#                     self.new_compnent_input.clear()
#                 else: 
#                     print('error existing element or key')
#         else:
#             print ('error key with number or too long')

#     def save_element(self):
#         element_input = self.lineEdit.text() 
#         self.lineEdit.clear()
#         # here i have to have ecvaluete values
#         add_to_list(element_input)

# #end johna funcion


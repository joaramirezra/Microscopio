
elements_list = {}

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


def add_component(keys_combination, component):
	elements_list[keys_combination] = { 'component': component,
										'count':0}
	print(elements_list)
	return True


def find_key(keys_combination):
	if (keys_combination in elements_list):
		print('exits')
		elements_list[keys_combination]['count'] +=1
	else :
		print('No exists')
	return True



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


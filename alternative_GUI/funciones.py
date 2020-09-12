
elements_list = {}

def move_setup(speed,step):
    print(speed,step)


def turn_on():
	print('Encendio')

def turn_off():
	print('apagado')

def add_element(key , component ):
	elements_list[key] = component
	print(str(key)+str(component))
	# if(len(key)==3):
	# 	return True
	# else:
	# 	return False
	print(elements_list)

def find_key():
	return True

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
	print('erase')


# # action butons
# 	self.begin_button.clicked.connect(turn_on)
# 	self.home_button.clicked.connect(home)
# 	self.Save_element_button.clicked.connect(add_element)
# 	self.replace_element_button.clicked.connect(replace_element)
# 	self.Size_reference_button.clicked.connect(reference_size)
# 	self.restart_counting_button.clicked.connect(reset)
# 	self.erase_last_button.clicked.connect(erase)
# 	self.next_button.clicked.connect(next_point)



        
# # action butons ------------------------------------------------------------------------------
#         self.next_button.clicked.connect(self.save_element)
#         self.lineEdit.returnPressed.connect(self.save_element)
     
# #---------------------------------------------------------------------------------------------    
#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def save_element(self):
#         element_input = self.lineEdit.text() 
#         self.lineEdit.clear()
#         print(element_input)


    # def add_element(self):

    #     keys_string = self.Key_input.text()
    #     component_string = self.new_compnent_input.text()

    #     if(len(keys_string) < 4  and keys_string.isalpha() ):
    #         if( len(component_string) == 0 ) : 
    #             print('error no element ')
    #         else : 
    #             if(add_element(list(keys_string),list(component_string))):
    #                 self.Key_input.clear()
    #                 self.new_compnent_input.clear()
    #             else: 
    #                 print('error existing element or key')
    #     else:
    #         print ('error key with number or too long')

    # def edit_element(self):

    #     keys_string = self.Key_input.text()
    #     component_string = self.new_compnent_input.text()

    #     # if(find_key(keys_string)  or find_component(component_string) ):
    #     #     if( len(component_string) == 0 ) : 
    #     #         print('error no element ')
    #     #     else : 
    #     #         if(add_element(list(keys_string),list(component_string))):
    #     #             self.Key_input.clear()
    #     #             self.new_compnent_input.clear()
    #     #         else: 
    #     #             print('error existing element or key')
    #     # else:
    #     #     print ('error key with number or too long')


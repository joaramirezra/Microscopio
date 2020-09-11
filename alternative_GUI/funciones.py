def turn_on():
	print('Encendio')

def turn_off():
	print('apagado')

def add_element():
	print('Agregar')

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



        
# action butons ------------------------------------------------------------------------------
        self.next_button.clicked.connect(self.save_element)
        self.lineEdit.returnPressed.connect(self.save_element)
     
#---------------------------------------------------------------------------------------------    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def save_element(self):
        element_input = self.lineEdit.text() 
        self.lineEdit.clear()
        print(element_input)
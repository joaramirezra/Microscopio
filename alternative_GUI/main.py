from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import * 
elements_List = {}

def add_to_list(key_element,componet,count):
    elements_List[key_element] = {'component':componet,'count':count}
    print(elements_List)

def increase_counting(key_element):
    elements_List[key_element]['count'] +=1

def decrease_counting(key_element):
    if(elements_List[key_element]['count'] >0):
        elements_List[key_element]['count'] -=1
    else :
        elements_List[key_element]['count'] = 0

if __name__ == "__main__":
    import os
    os.system('clear')
    for x in range (3):
        add_to_list(str('adf'+str(x)),'masdfds',x)
    
    for x in range (10):
        increase_counting('adf2')
        print(elements_List['adf2'])
    
    for x in range (15):
        decrease_counting('adf2')
        print(elements_List['adf2'])        
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())}



    # Plot background color
        self.graphicsView.setBackground('#3c3f58')
        self.graphicsView_2.setBackground('#3c3f58')
        self.graphicsView.showGrid(x=True, y=True)
        self.graphicsView_2.showGrid(x=True, y=True)
        
# callbacks 
        self.begin_button.clicked.connect(self.move_init)
        self.home_button.clicked.connect(home)
        self.Save_element_button.clicked.connect(self.add_element)
        self.next_button.clicked.connect(self.save_point)
        self.erase_last_button.clicked.connect(erase) 
        self.restart_counting_button.clicked.connect(reset)
        self.Size_reference_button.clicked.connect(self.reference_pop)      
        # call when enter is presed
        self.elemnt_input.returnPressed.connect(self.save_point) 
        self.new_compnent_input.returnPressed.connect(self.add_element)

# Functions 
    def reference_pop(self):
        pass
       
    def move_init(self):
        step_setup = self.Step_spinbox.value()
        speed_setup = self.speed_spinbox.value()
        move_setup(speed_setup,step_setup)
    
    def add_element(self):

        keys_string = self.Key_input.text()
        component_string = self.new_compnent_input.text()

        if(len(keys_string) < 4  and keys_string.isalpha() ):
            if( len(component_string) == 0 ) : 
                print('error no element ')
            else : 
                if(add_component(keys_string,component_string)):
                    self.Key_input.clear()
                    self.new_compnent_input.clear()
                else: 
                    print('error existing element or key')
        else:
            print ('error key with number or too long')

    def update_table(self,new_element,new_size):
        # move a row elements   
        for x in reversed(range(1,7)):
            element_change = self.last_componet_table.item(x, 0)
            size = self.last_componet_table.item(x, 1)
            element_change.setText(self.last_componet_table.item(x-1, 0).text())
            size.setText(self.last_componet_table.item(x-1, 1).text())
        
        # then print the new last last element 
        self.last_componet_table.item(0, 0).setText(new_element)
        self.last_componet_table.item(0, 1).setText(new_size)
        
    def save_point(self):
        
        element_input = self.elemnt_input.text() 
        key,dimention_value = split_input(element_input)
       
        if( int(dimention_value) > 0 and int(dimention_value) < 17):
            if(find_key(key)):
                component,size = get_info(key,dimention_value)
                self.update_table(component,size)
                self.graphicsView.clear()
                self.draw_size()
            else :
                print("No exists")
        else:
            print("size out range")
            
        self.elemnt_input.clear()

    def draw_size(self):
        components_name ,components_count = count_element() 
        print(components_name ,components_count )
        xlabel = " - ".join(components_name)
        x = range(len(components_count))
        self.graphicsView.plot(x,components_count, symbol='+')
        self.graphicsView.setLabel('bottom',xlabel)
        self.graphicsView.setXRange(-0.2,len(components_name))
        self.graphicsView_2.BarGraphItem(1,2)
        # self.graphicsView_2.plot(x,y2)


#end Johan funcion
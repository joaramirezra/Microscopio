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
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())



    
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import Ui_MainWindow
from File_control import *
import os
import sys

if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
        print("please enter the file name")
        name = input()
        init_document(name)
        
        



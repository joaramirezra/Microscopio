# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from funciones import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(128, 22, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(710, 90, 235, 179))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 101, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(150, 20, 67, 21))
        self.label_5.setObjectName("label_5")
        self.next_button = QtWidgets.QPushButton(self.frame_2)
        self.next_button.setGeometry(QtCore.QRect(142, 52, 71, 31))
        self.next_button.setObjectName("next_button")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(70, 0, 121, 20))
        self.label_6.setObjectName("label_6")
        self.erase_last_button = QtWidgets.QPushButton(self.frame_2)
        self.erase_last_button.setGeometry(QtCore.QRect(22, 92, 191, 31))
        self.erase_last_button.setObjectName("erase_last_button")
        self.restart_counting_button = QtWidgets.QPushButton(self.frame_2)
        self.restart_counting_button.setGeometry(QtCore.QRect(22, 132, 191, 31))
        self.restart_counting_button.setObjectName("restart_counting_button")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 111, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(20, 90, 201, 179))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setGeometry(QtCore.QRect(10, 30, 67, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setGeometry(QtCore.QRect(10, 70, 67, 17))
        self.label_12.setObjectName("label_12")
        self.spinBox = QtWidgets.QSpinBox(self.frame_4)
        self.spinBox.setGeometry(QtCore.QRect(140, 20, 48, 31))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame_4)
        self.spinBox_2.setGeometry(QtCore.QRect(140, 60, 48, 31))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setGeometry(QtCore.QRect(10, 0, 151, 20))
        self.label_16.setObjectName("label_16")
        self.begin_button = QtWidgets.QPushButton(self.frame_4)
        self.begin_button.setGeometry(QtCore.QRect(10, 100, 181, 31))
        self.begin_button.setObjectName("begin_button")
        self.home_button = QtWidgets.QPushButton(self.frame_4)
        self.home_button.setGeometry(QtCore.QRect(10, 140, 181, 31))
        self.home_button.setObjectName("home_button")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(20, 280, 201, 171))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_14 = QtWidgets.QLabel(self.frame_5)
        self.label_14.setGeometry(QtCore.QRect(10, 30, 51, 17))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_5)
        self.label_15.setGeometry(QtCore.QRect(30, 0, 141, 21))
        self.label_15.setObjectName("label_15")
        self.Save_element_button = QtWidgets.QPushButton(self.frame_5)
        self.Save_element_button.setGeometry(QtCore.QRect(10, 90, 181, 31))
        self.Save_element_button.setObjectName("Save_element_button")
        self.replace_element_button = QtWidgets.QPushButton(self.frame_5)
        self.replace_element_button.setGeometry(QtCore.QRect(10, 130, 181, 31))
        self.replace_element_button.setObjectName("replace_element_button")
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        self.label_13.setGeometry(QtCore.QRect(90, 30, 67, 17))
        self.label_13.setObjectName("label_13")
        self.Key_input = QtWidgets.QLineEdit(self.frame_5)
        self.Key_input.setGeometry(QtCore.QRect(10, 50, 61, 25))
        self.Key_input.setObjectName("Key_input")
        self.new_compnent_input = QtWidgets.QLineEdit(self.frame_5)
        self.new_compnent_input.setGeometry(QtCore.QRect(90, 50, 91, 25))
        self.new_compnent_input.setObjectName("new_compnent_input")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(674, 22, 171, 21))
        self.label_10.setObjectName("label_10")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(674, 54, 271, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(880, 20, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(250, 90, 461, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(710, 280, 241, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(236, 290, 461, 191))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.Size_reference_button = QtWidgets.QPushButton(self.centralwidget)
        self.Size_reference_button.setGeometry(QtCore.QRect(20, 460, 201, 25))
        self.Size_reference_button.setObjectName("Size_reference_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 959, 22))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        self.menuEditar = QtWidgets.QMenu(self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        self.menuTama_o_muestra = QtWidgets.QMenu(self.menuEditar)
        self.menuTama_o_muestra.setObjectName("menuTama_o_muestra")
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNuevo = QtWidgets.QAction(MainWindow)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_Como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_Como.setObjectName("actionGuardar_Como")
        self.actionTutorial = QtWidgets.QAction(MainWindow)
        self.actionTutorial.setObjectName("actionTutorial")
        self.actionFAQ_s = QtWidgets.QAction(MainWindow)
        self.actionFAQ_s.setObjectName("actionFAQ_s")
        self.actionAcerca = QtWidgets.QAction(MainWindow)
        self.actionAcerca.setObjectName("actionAcerca")
        self.actionTeclado = QtWidgets.QAction(MainWindow)
        self.actionTeclado.setObjectName("actionTeclado")
        self.actionCalibrar = QtWidgets.QAction(MainWindow)
        self.actionCalibrar.setObjectName("actionCalibrar")
        self.actionInspeccionar = QtWidgets.QAction(MainWindow)
        self.actionInspeccionar.setObjectName("actionInspeccionar")
        self.actionDefecto_47x32 = QtWidgets.QAction(MainWindow)
        self.actionDefecto_47x32.setObjectName("actionDefecto_47x32")
        self.action3x3 = QtWidgets.QAction(MainWindow)
        self.action3x3.setObjectName("action3x3")
        self.action4x4 = QtWidgets.QAction(MainWindow)
        self.action4x4.setObjectName("action4x4")
        self.actionAgregar = QtWidgets.QAction(MainWindow)
        self.actionAgregar.setObjectName("actionAgregar")
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_Como)
        self.menuTama_o_muestra.addSeparator()
        self.menuTama_o_muestra.addSeparator()
        self.menuTama_o_muestra.addAction(self.actionDefecto_47x32)
        self.menuTama_o_muestra.addAction(self.action3x3)
        self.menuTama_o_muestra.addAction(self.action4x4)
        self.menuTama_o_muestra.addAction(self.actionAgregar)
        self.menuEditar.addAction(self.actionTeclado)
        self.menuEditar.addAction(self.menuTama_o_muestra.menuAction())
        self.menuEditar.addAction(self.actionCalibrar)
        self.menuEditar.addAction(self.actionInspeccionar)
        self.menuAyuda.addAction(self.actionTutorial)
        self.menuAyuda.addAction(self.actionFAQ_s)
        self.menuAyuda.addAction(self.actionAcerca)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.Save_element_button.clicked.connect(self.add_element)
    
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sistema de gestion para el conteo de puntos"))
        self.label_4.setText(_translate("MainWindow", "Coordenadas"))
        self.label_5.setText(_translate("MainWindow", "[0,0]"))
        self.next_button.setText(_translate("MainWindow", "siguiente"))
        self.label_6.setText(_translate("MainWindow", "Agregar punto"))
        self.erase_last_button.setText(_translate("MainWindow", "Borrar Anterior"))
        self.restart_counting_button.setText(_translate("MainWindow", "Reiniciar conteo"))
        self.label_11.setText(_translate("MainWindow", "Avance"))
        self.label_12.setText(_translate("MainWindow", "Velocidad"))
        self.label_16.setText(_translate("MainWindow", "Confi. de movimiento"))
        self.begin_button.setText(_translate("MainWindow", "Iniciar"))
        self.home_button.setText(_translate("MainWindow", "Home"))
        self.label_14.setText(_translate("MainWindow", "Letra(s)"))
        self.label_15.setText(_translate("MainWindow", "Agregar compuesto"))
        self.Save_element_button.setText(_translate("MainWindow", "Agregar"))
        self.replace_element_button.setText(_translate("MainWindow", "reemplazar"))
        self.label_13.setText(_translate("MainWindow", "Elemento"))
        self.label_10.setText(_translate("MainWindow", "Puntos  medidos"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "01"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "02"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "03"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "04"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "05"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "06"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "07"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Componente"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tamaño"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "moscovita_hialita"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "0.001"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "hialita"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "0.05"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "cuarzo"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "0.07"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "feldespato"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "0.01"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "oro"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "0.5"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "Gato"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("MainWindow", "0.98"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("MainWindow", "suesca"))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("MainWindow", "1.5"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.Size_reference_button.setText(_translate("MainWindow", "Tamaños de referencia"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuEditar.setTitle(_translate("MainWindow", "Editar"))
        self.menuTama_o_muestra.setTitle(_translate("MainWindow", "Tamaño muestra"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar_Como.setText(_translate("MainWindow", "Guardar Como"))
        self.actionTutorial.setText(_translate("MainWindow", "Tutorial"))
        self.actionFAQ_s.setText(_translate("MainWindow", "FAQ\'s"))
        self.actionAcerca.setText(_translate("MainWindow", "Acerca"))
        self.actionTeclado.setText(_translate("MainWindow", "Teclado"))
        self.actionCalibrar.setText(_translate("MainWindow", "Calibrar"))
        self.actionInspeccionar.setText(_translate("MainWindow", "Inspeccionar"))
        self.actionDefecto_47x32.setText(_translate("MainWindow", "Defecto(47x32)"))
        self.action3x3.setText(_translate("MainWindow", "3x3"))
        self.action4x4.setText(_translate("MainWindow", "4x4"))
        self.actionAgregar.setText(_translate("MainWindow", "Agregar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


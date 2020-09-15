from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import os.path

app = QtWidgets.QApplication([])
dlg = uic.loadUi("Lista_Materiales.ui")
materialesList = []

class Material ():
    def __init__ (self, nombre, letra, propied):
        self.nombre = nombre
        self.letra = letra
        self.propied = propied

materialesList.append(Material("oro","au","amarillo"))
materialesList.append(Material("plata","ag","plateado"))
materialesList.append(Material("cobre","cu","feo"))
materialesList.append(Material("mercurio","hg","mortal"))


def writeDoc(first, second, third):
    newMaterial = str(first) + "," + str(second) + "," + str(third)  
    print(newMaterial)
    materialesList.write(newMaterial)


def loadData():
    primer = dlg.lineEdit.text() 
    segung = dlg.lineEdit_2.text()
    tercer = dlg.lineEdit_3.text()
    if primer != "" or segung != "" or tercer != "" :
        materialesList.append( Material(primer,segung,tercer))
        show()
        # writeDoc(primer,segung,tercer)
        dlg.lineEdit.setText("")
        dlg.lineEdit_2.setText("")
        dlg.lineEdit_3.setText("")

def loadMaterials():
    if(os.path.isfile('./materiales.txt')):
        print("Archivo existente")
    else:
        print("Archivo creado")

def elementExist(elemento,clase):
    if clase == 1:
        for mat in materialesList:
            if elemento == str(mat.nombre):
                return True
        return False
    else:
        for mat in materialesList:
            if elemento == str(mat.letra):
                return True
        return False

def verifyElement():
    elemento = dlg.lineEdit_4.text() 
    if elementExist(elemento,1):
        dlg.label_6.setText(str(elemento)+" esta en la lista" )
    else:
        dlg.label_6.setText(str(elemento)+" no esta en la lista")


def letterExist():
    letra = dlg.lineEdit_5.text() 
    if elementExist(letra,2):
        dlg.label_6.setText(str(letra)+" esta en la lista" )
    else:
        dlg.label_6.setText(str(letra)+" no esta en la lista")
    dlg.lineEdit_5.setText("")
    

def deleteElement():
    elemento = dlg.lineEdit_4.text() 
    for mat in materialesList:
            if elemento == str(mat.nombre):
                materialesList.remove(mat)
    dlg.lineEdit_4.setText("")
    show()
    

def show():
    dlg.tableWidget.clearContents()
    dlg.tableWidget.setRowCount(0)
    for mat in materialesList:
        row = dlg.tableWidget.rowCount()
        dlg.tableWidget.insertRow(row)
        dlg.tableWidget.setItem(row,0,QTableWidgetItem(mat.nombre))     
        dlg.tableWidget.setItem(row,1,QTableWidgetItem(mat.letra))
        dlg.tableWidget.setItem(row,2,QTableWidgetItem(mat.propied))

dlg.pushButton.clicked.connect(loadData)
dlg.pushButton_2.clicked.connect(verifyElement)
dlg.pushButton_3.clicked.connect(letterExist)
dlg.pushButton_4.clicked.connect(deleteElement) 

show()

dlg.show()
app.exec()
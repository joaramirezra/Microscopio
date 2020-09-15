from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from time import sleep
import os.path
import RPi.GPIO as GPIO

app = QtWidgets.QApplication([])
dlg = uic.loadUi("prototipo_posicionador.ui")

stp_1 = 16
dir_1 = 20
enb_1 = 21
stp_2 = 13
dir_3 = 19
enb_4 = 26

GPIO.setmode(GPIO.BPM)
GPIO.setup(dir_1, GPIO.OUT)
GPIO.setup(dir_2, GPIO.OUT)
GPIO.setup(stp_1, GPIO.OUT)
GPIO.setup(stp_2, GPIO.OUT)

materialesList = []

class Motor():
    def __init__(self,step_pin,dir_pin):
        self.direccion = 0
        self.paso = 1.8
        self.npasos = 200
        self.STEP = step_pin
        self.DIR = dir_pin
        GPIO.setup(self.STEP, GPIO.OUT)
        GPIO.setup(self.DIR, GPIO.OUT)
        GPIO.output(self.DIR, self.direccion)

    def move(self, vueltas):
        for x in range(self.npasos*vueltas):
            GPIO.output(self.STEP, GPIO.HIGH)
            sleep(0.01)
            GPIO.output(self.STEP, GPIO.LOW)
            sleep(0.01)

    def setDirection(self, direccion):
        if direccion == 1:
            GPIO.output(self.DIR, 1)
        else:
            GPIO.output(self.DIR, 0)

motor_1 = Motor(19, 26)
motor_2 = Motor(20, 21)

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
    primer = dlg.lineEdit_2.text() 
    segung = dlg.lineEdit_3.text()
    tercer = dlg.lineEdit_4.text()
    if primer != "" or segung != "" or tercer != "" :
        materialesList.append( Material(primer,segung,tercer))
        show()
        # writeDoc(primer,segung,tercer)
        dlg.lineEdit_2.setText("")
        dlg.lineEdit_3.setText("")
        dlg.lineEdit_4.setText("")

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
    elemento = dlg.lineEdit.text() 
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
    elemento = dlg.lineEdit.text() 
    for mat in materialesList:
            if elemento == str(mat.nombre):
                materialesList.remove(mat)
    dlg.lineEdit.setText("")
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

def moveUp():
    print("up")
    motor_1.setDirection(1)
    motor_1.move(2)


def moveDown():
    print("up")
    motor_1.setDirection(0)
    motor_1.move(2)

def moveLeft():
    print("left")
    motor_2.setDirection(0)
    motor_2.move(2)

def moveRight():
    print("right")
    motor_2.setDirection(1)
    motor_2.move(2)


dlg.pushButton_7.clicked.connect(loadData)
dlg.pushButton_9.clicked.connect(verifyElement)
dlg.pushButton_10.clicked.connect(letterExist)
dlg.pushButton_8.clicked.connect(deleteElement) 

dlg.up.clicked.connect(moveUp)
dlg.down.clicked.connect(moveDown)
dlg.left.clicked.connect(moveLeft)
dlg.right.clicked.connect(moveRight) 

dlg.up.setShortcut("up")
dlg.down.setShortcut("down")
dlg.left.setShortcut("left")
dlg.right.setShortcut("right")

show()


dlg.show()
app.exec()
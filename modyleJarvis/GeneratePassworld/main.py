# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint
import sys


class Ui_GeneratPorol(object):
    generat_porol = ""
    poroli = ""

    def setupUi(self, GeneratPorol):
        GeneratPorol.setObjectName("GeneratPorol")
        GeneratPorol.resize(481, 471)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        GeneratPorol.setFont(font)
        GeneratPorol.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(GeneratPorol)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 491, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/1625718621_25-kartinkin-com-p-oboi-dzharvis-krasivie-29.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(149, 110, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(176, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(212, 85, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 180, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgba(0, 0, 0, 100);")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 340, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 310, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_4.setObjectName("label_4")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 220, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 250, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 280, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(10, 310, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(9, 340, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        GeneratPorol.setCentralWidget(self.centralwidget)

        self.retranslateUi(GeneratPorol)
        QtCore.QMetaObject.connectSlotsByName(GeneratPorol)

        self.correct_button()

    def correct_button(self):
        self.pushButton.clicked.connect(self.main)

    def generat_vse_clychui(self, dlina: int, colvo: int):
        slovar_ang_chisla_cpes_simvol = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*"
        for i in range(1, int(colvo)+1):
            for g in range(1, int(dlina)+1):
                indx = randint(0, len(slovar_ang_chisla_cpes_simvol)-1)
                self.generat_porol += slovar_ang_chisla_cpes_simvol[indx]
            
            yield self.generat_porol
            self.generat_porol = ""

    def generat_porol_spes_ang(self, dlina: int, colvo: int):
        slovar_ang_spec_simvoli =  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%&*"
        
        for i in range(1, int(colvo)+1):
            for g in range(1, int(dlina)+1):
                indx = randint(0, len(slovar_ang_spec_simvoli)-1)
                self.generat_porol += slovar_ang_spec_simvoli[indx]
            
            yield self.generat_porol
            self.generat_porol = ""  
    
    def generat_porol_ang(self, dlina: int, colvo: int):
        slovar_ang =  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        
        for i in range(1, int(colvo)+1):
            for g in range(1, int(dlina)+1):
                indx = randint(0, len(slovar_ang)-1)
                self.generat_porol += slovar_ang[indx]
            
            yield self.generat_porol
            self.generat_porol = ""  
    
    def generat_porol_ang_chisla(self, dlina: int, colvo: int):
        slovar_ang =  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        
        for i in range(1, int(colvo)+1):
            for g in range(1, int(dlina)+1):
                indx = randint(0, len(slovar_ang)-1)
                self.generat_porol += slovar_ang[indx]
            
            yield self.generat_porol
            self.generat_porol = ""  
    
    def generat_porol_chisla(self, dlina: int, colvo: int):
        slovar_ang =  "0123456789"
        
        for i in range(1, int(colvo)+1):
            for g in range(1, int(dlina)+1):
                indx = randint(0, len(slovar_ang)-1)
                self.generat_porol += slovar_ang[indx]
            
            yield self.generat_porol
            self.generat_porol = "" 
        
    def generat_porol_cpec(self, dlina: int, colvo: int):
        slovar_ang =  "!@#$%&*"
        
        for i in range(1, int(colvo)+1):
            for g in range(1, int(dlina)+1):
                indx = randint(0, len(slovar_ang)-1)
                self.generat_porol += slovar_ang[indx]
            
            yield self.generat_porol
            self.generat_porol = "" 
    
    def generat_porol_cpec_chisla(self, dlina: int, colvo: int):
        slovar_ang =  "0123456789!@#$%&*"
        
        for i in range(1, int(colvo)+1):
            for g in range(1, int(dlina)+1):
                indx = randint(0, len(slovar_ang)-1)
                self.generat_porol += slovar_ang[indx]
            
            yield self.generat_porol
            self.generat_porol = "" 


    def main(self):
        dlina_porola = self.lineEdit.text()
        colvo = self.spinBox.value()

        if self.checkBox.isChecked() == True:
            if self.checkBox_2.isChecked() == True:
                if self.checkBox_3.isChecked() == True:
                    for i in self.generat_vse_clychui(dlina=dlina_porola, colvo=colvo):
                        self.poroli += i + "\n"
                    
                    self.textEdit.setText(self.poroli)
                    self.poroli = ""
                else:
                    if self.checkBox_3.isChecked() == False:
                        for i in self.generat_porol_ang_chisla(dlina=dlina_porola, colvo=colvo):
                            self.poroli += i + "\n"
                    
                        self.textEdit.setText(self.poroli)
                        self.poroli = ""
                
            else:
                if self.checkBox_2.isChecked() == False:
                    if self.checkBox_3.isChecked() == True:
                        for i in self.generat_porol_spes_ang(dlina=dlina_porola, colvo=colvo):
                            self.poroli += i + "\n"
                    
                        self.textEdit.setText(self.poroli)
                        self.poroli = ""
                
                    else:
                        for i in self.generat_porol_ang(dlina=dlina_porola, colvo=colvo):
                            self.poroli += i + "\n"
                    
                        self.textEdit.setText(self.poroli)
                        self.poroli = ""
        else:
            if self.checkBox_2.isChecked() == True:
                if self.checkBox_3.isChecked() == False:
                    for i in self.generat_porol_chisla(dlina=dlina_porola, colvo=colvo):
                        self.poroli += i + "\n"
                    
                    self.textEdit.setText(self.poroli)
                    self.poroli = ""
                
                else:
                    for i in self.generat_porol_cpec_chisla(dlina=dlina_porola, colvo=colvo):
                        self.poroli += i + "\n"
                    
                    self.textEdit.setText(self.poroli)
                    self.poroli = ""
                    

            
            else:
                if self.checkBox_3.isChecked() == True:
                    for i in self.generat_porol_cpec(dlina=dlina_porola, colvo=colvo):
                        self.poroli += i + "\n"
                    
                    self.textEdit.setText(self.poroli)
                    self.poroli = ""
                    
        

    def retranslateUi(self, GeneratPorol):
        _translate = QtCore.QCoreApplication.translate
        GeneratPorol.setWindowTitle(_translate("GeneratPorol", "Jarvis - генератор поролей"))
        self.label_2.setText(_translate("GeneratPorol", "JARVIS"))
        self.label_3.setText(_translate("GeneratPorol", "Длина"))
        self.pushButton.setText(_translate("GeneratPorol", "Сгенирировать"))
        self.label_4.setText(_translate("GeneratPorol", "Разультат"))
        self.checkBox.setText(_translate("GeneratPorol", "(A-Z)"))
        self.checkBox_2.setText(_translate("GeneratPorol", "(1-9)"))
        self.checkBox_3.setText(_translate("GeneratPorol", "(@!#$)"))
        self.label_5.setText(_translate("GeneratPorol", "Каличество"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_GeneratPorol()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())     
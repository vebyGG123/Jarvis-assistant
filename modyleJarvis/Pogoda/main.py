# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from config import config 
from tkinter import messagebox
import requests
import sys


class JarvisPogoda(object):
    pogoda = {}
    wd = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(476, 298)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 521, 331))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/1625718621_25-kartinkin-com-p-oboi-dzharvis-krasivie-29.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 70, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(153, 180, 192, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.correct_button()

    def quit(self):
        sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jarvis - Погода"))
        self.pushButton.setText(_translate("MainWindow", "Покозать погоду"))
        self.label_2.setText(_translate("MainWindow", "JARVIS"))

    def correct_button(self):
        self.pushButton.clicked.connect(self.main)

    def get_pogoda(self, city, token=config.TOKEN_API):
        
        req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric")
        data = req.json()

        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }

        pod = data["weather"][0]["main"]
        if pod in code_to_smile:
            self.wd = code_to_smile[pod]
        

        self.pogoda = {
            "Город":data["name"],
            "Температура":data["main"]["temp"],
            "Влажность": data["main"]["humidity"],
            "Давление": data["main"]["pressure"],
            "Скорость ветра": data["wind"]["speed"],
            "Погода": self.wd
        }


    def main(self):
        sity = self.textEdit.toPlainText()
        self.get_pogoda(city=sity)

        get_info_pogoda = f"""
            Город: {self.pogoda["Город"]}
            Температура: {round(self.pogoda["Температура"])}
            Влажность: {self.pogoda["Влажность"]}
            Давление: {self.pogoda["Давление"]}
            Скорость ветра: {self.pogoda["Скорость ветра"]}
            Погода: {self.wd}
        """

        messagebox.showinfo("Погода", get_info_pogoda)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = JarvisPogoda()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skeleton1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

price = 0.5727
d1_con = 44
d2_con = 98
d3_con = 510
d4_con = 303
d5_con = 750
d6_con = 2200
d7_con = 2500
d8_con = 800
d9_con = 2600
d10_con = 1080
d11_con = 2200
d12_con = 2000



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bill_1236104.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.device1 = QtWidgets.QLabel(self.centralwidget)
        self.device1.setGeometry(QtCore.QRect(50, 40, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.device1.setFont(font)
        self.device1.setObjectName("device1")
        self.d1_box_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.d1_box_1.setGeometry(QtCore.QRect(260, 40, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d1_box_1.setFont(font)
        self.d1_box_1.setMaximum(24)
        self.d1_box_1.setObjectName("d1_box_1")
        self.d1_box_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.d1_box_2.setGeometry(QtCore.QRect(260, 80, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d1_box_2.setFont(font)
        self.d1_box_2.setMaximum(24)
        self.d1_box_2.setObjectName("d1_box_2")
        self.device2 = QtWidgets.QLabel(self.centralwidget)
        self.device2.setGeometry(QtCore.QRect(50, 80, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.device2.setFont(font)
        self.device2.setObjectName("device2")
        self.d1_box_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.d1_box_3.setGeometry(QtCore.QRect(260, 120, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d1_box_3.setFont(font)
        self.d1_box_3.setMaximum(24)
        self.d1_box_3.setObjectName("d1_box_3")
        self.device3 = QtWidgets.QLabel(self.centralwidget)
        self.device3.setGeometry(QtCore.QRect(50, 120, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.device3.setFont(font)
        self.device3.setObjectName("device3")
        self.d1_box_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.d1_box_4.setGeometry(QtCore.QRect(260, 160, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d1_box_4.setFont(font)
        self.d1_box_4.setMaximum(24)
        self.d1_box_4.setObjectName("d1_box_4")
        self.device4 = QtWidgets.QLabel(self.centralwidget)
        self.device4.setGeometry(QtCore.QRect(50, 160, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.device4.setFont(font)
        self.device4.setObjectName("device4")
        self.d1_box_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.d1_box_5.setGeometry(QtCore.QRect(260, 200, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d1_box_5.setFont(font)
        self.d1_box_5.setMaximum(24)
        self.d1_box_5.setObjectName("d1_box_5")
        self.device5 = QtWidgets.QLabel(self.centralwidget)
        self.device5.setGeometry(QtCore.QRect(50, 200, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.device5.setFont(font)
        self.device5.setObjectName("device5")
        self.d1_box_6 = QtWidgets.QSpinBox(self.centralwidget)
        self.d1_box_6.setGeometry(QtCore.QRect(260, 240, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d1_box_6.setFont(font)
        self.d1_box_6.setMaximum(240)
        self.d1_box_6.setObjectName("d1_box_6")
        self.device6 = QtWidgets.QLabel(self.centralwidget)
        self.device6.setGeometry(QtCore.QRect(50, 240, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.device6.setFont(font)
        self.device6.setObjectName("device6")
        self.device12 = QtWidgets.QLabel(self.centralwidget)
        self.device12.setGeometry(QtCore.QRect(350, 240, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.device12.setFont(font)
        self.device12.setObjectName("device12")
        self.device7 = QtWidgets.QLabel(self.centralwidget)
        self.device7.setGeometry(QtCore.QRect(350, 40, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.device7.setFont(font)
        self.device7.setObjectName("device7")
        self.d1_box_10 = QtWidgets.QSpinBox(self.centralwidget)
        self.d1_box_10.setGeometry(QtCore.QRect(560, 160, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d1_box_10.setFont(font)
        self.d1_box_10.setMaximum(24)
        self.d1_box_10.setObjectName("d1_box_10")
        self.device10 = QtWidgets.QLabel(self.centralwidget)
        self.device10.setGeometry(QtCore.QRect(350, 160, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.device10.setFont(font)
        self.device10.setObjectName("device10")
        self.device11 = QtWidgets.QLabel(self.centralwidget)
        self.device11.setGeometry(QtCore.QRect(350, 200, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.device11.setFont(font)
        self.device11.setObjectName("device11")
        self.d1_box_12 = QtWidgets.QSpinBox(self.centralwidget)
        self.d1_box_12.setGeometry(QtCore.QRect(560, 240, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d1_box_12.setFont(font)
        self.d1_box_12.setMaximum(240)
        self.d1_box_12.setObjectName("d1_box_12")
        self.d1_box_7 = QtWidgets.QSpinBox(self.centralwidget)
        self.d1_box_7.setGeometry(QtCore.QRect(560, 40, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d1_box_7.setFont(font)
        self.d1_box_7.setMaximum(24)
        self.d1_box_7.setObjectName("d1_box_7")
        self.d1_box_8 = QtWidgets.QSpinBox(self.centralwidget)
        self.d1_box_8.setGeometry(QtCore.QRect(560, 80, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d1_box_8.setFont(font)
        self.d1_box_8.setMaximum(240)
        self.d1_box_8.setObjectName("d1_box_8")
        self.d1_box_9 = QtWidgets.QSpinBox(self.centralwidget)
        self.d1_box_9.setGeometry(QtCore.QRect(560, 120, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d1_box_9.setFont(font)
        self.d1_box_9.setMaximum(24)
        self.d1_box_9.setObjectName("d1_box_9")
        self.device9 = QtWidgets.QLabel(self.centralwidget)
        self.device9.setGeometry(QtCore.QRect(350, 120, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.device9.setFont(font)
        self.device9.setObjectName("device9")
        self.d1_box_11 = QtWidgets.QSpinBox(self.centralwidget)
        self.d1_box_11.setGeometry(QtCore.QRect(560, 200, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.d1_box_11.setFont(font)
        self.d1_box_11.setMaximum(240)
        self.d1_box_11.setObjectName("d1_box_11")
        self.device8 = QtWidgets.QLabel(self.centralwidget)
        self.device8.setGeometry(QtCore.QRect(350, 80, 195, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.device8.setFont(font)
        self.device8.setObjectName("device8")
        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(160, 290, 101, 30))
        self.calculate_button.setObjectName("calculate_button")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(30, 290, 101, 30))
        self.clear_button.setObjectName("clear_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.calculate_button.clicked.connect(self.calculate_bill)
        self.clear_button.clicked.connect(self.undo_changes)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Electricity Bill Calculator"))
        self.device1.setText(_translate("MainWindow", "Refrigerator (hrs/day) "))
        self.device2.setText(_translate("MainWindow", "Television (hrs/day) "))
        self.device3.setText(_translate("MainWindow", "Dishwasher Machine (hrs/week) "))
        self.device4.setText(_translate("MainWindow", "Washing Machine (hrs/week) "))
        self.device5.setText(_translate("MainWindow", "Vacuum Cleaner (hrs/week) "))
        self.device6.setText(_translate("MainWindow", "Hair Dryer (min/day) "))  
        self.device7.setText(_translate("MainWindow", "Oven (hrs/week) "))
        self.device8.setText(_translate("MainWindow", "Micrawave Oven (min/day) "))
        self.device9.setText(_translate("MainWindow", "Iron (min/week) "))
        self.device10.setText(_translate("MainWindow", "Air Conditioner (hrs/day) "))
        self.device11.setText(_translate("MainWindow", "Kettle (min/day) "))
        self.device12.setText(_translate("MainWindow", "Toast Machine (min/day) "))
       
        self.calculate_button.setText(_translate("MainWindow", "Calculate"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        
        
    def undo_changes(self):
        self.d1_box_1.setProperty("value", 0)
        self.d1_box_2.setProperty("value", 0)
        self.d1_box_3.setProperty("value", 0)
        self.d1_box_4.setProperty("value", 0)
        self.d1_box_5.setProperty("value", 0)
        self.d1_box_6.setProperty("value", 0)
        self.d1_box_7.setProperty("value", 0)
        self.d1_box_8.setProperty("value", 0)
        self.d1_box_9.setProperty("value", 0)
        self.d1_box_10.setProperty("value", 0)
        self.d1_box_11.setProperty("value", 0)
        self.d1_box_12.setProperty("value", 0)
        
    def calculate_bill(self):
        con_ref = int(self.d1_box_1.value()) * d1_con * 30 / 1000 #kwh
        con_tel = int(self.d1_box_2.value()) * d2_con * 30 / 1000 #kwh
        con_dis = int(self.d1_box_3.value()) * d3_con * 30 / 1000 / 7 #kwh
        con_was = int(self.d1_box_4.value()) * d4_con * 30 / 1000 / 7 #kwh
        con_vac = int(self.d1_box_5.value()) * d5_con * 30 / 1000 / 7 #kwh
        con_hai = int(self.d1_box_6.value()) * d6_con * 30 / 1000 / 60 #kwh
        con_ove = int(self.d1_box_7.value()) * d7_con * 30 / 1000 / 7 #kwh
        con_mic = int(self.d1_box_8.value()) * d8_con * 30 / 1000 / 60 #kwh
        con_iro = int(self.d1_box_9.value()) * d9_con * 30 / 1000 / 420 #kwh
        con_air = int(self.d1_box_10.value()) * d10_con * 30 / 1000 #kwh
        con_ket = int(self.d1_box_11.value()) * d11_con * 30 / 1000 / 60 #kwh
        con_toa = int(self.d1_box_12.value()) * d12_con * 30 / 1000 / 60#kwh
        total_con = con_ref + con_tel + con_dis + con_was + con_vac + con_hai + con_ove + con_mic + con_iro + con_air + con_ket + con_toa
        total_con_price = total_con * price
        con_price = total_con_price * 0.64
        price_with_taxes = total_con_price + (con_price * 0.01 ) + (con_price * 0.02) + (con_price * 0.05) #Enerji fonu, TRT payı ve BTV'nin eklenmiş hali
        kdv = price_with_taxes * 0.18
        final_price = price_with_taxes + kdv
        final_price_string = "The total bill price with taxes is: {:.2f} TL".format(final_price)
        answer = QMessageBox()
        answer.setWindowTitle("Final Bill Price")
        answer.setText(final_price_string)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bill_1236104.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        answer.setWindowIcon(icon)
<<<<<<< HEAD
        answer.setDetailedText("KDV: {:.2f} TL".format(kdv)+"\nEnerji Fonu: {:.2f} TL".format(con_price * 0.01)+"\nBTV: {:.2f} TL".format(con_price * 0.02))
        
        #answer.setDetailedText("KDV:"+str(kdv)+"\n Enerji Fonu: "+str(con_price * 0.01)+"\nBTV: "+str(con_price * 0.02))
=======
        answer.setDetailedText(" KDV: {:.2f} TL".format(kdv)+"\n Enerji Fonu: {:.2f} TL".format(con_price*0.01)+"\n TRT Payı: {:.2f} TL".format(con_price*0.02)+"\n BTV: {:.2f} TL".format(con_price*0.05))
>>>>>>> f32c860925234f70cdd33acd03e05a34cda8b613
        answer.exec_()
    
         
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
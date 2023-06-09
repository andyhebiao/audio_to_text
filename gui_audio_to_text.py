# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\gui_audio_to_text.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(588, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ql_virtual_human = QtWidgets.QLabel(self.centralwidget)
        self.ql_virtual_human.setGeometry(QtCore.QRect(710, 10, 241, 371))
        self.ql_virtual_human.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ql_virtual_human.setStyleSheet("background-color:rgb(100,100,100);\n"
"color:rgb(255,255,255)")
        self.ql_virtual_human.setObjectName("ql_virtual_human")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 380, 91, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pb_ask = QtWidgets.QPushButton(self.centralwidget)
        self.pb_ask.setGeometry(QtCore.QRect(110, 280, 100, 100))
        self.pb_ask.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pb_ask.setStyleSheet("")
        self.pb_ask.setObjectName("pb_ask")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 381, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.le_ue_ip = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_ue_ip.setObjectName("le_ue_ip")
        self.gridLayout.addWidget(self.le_ue_ip, 0, 1, 1, 1)
        self.le_appid = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_appid.setObjectName("le_appid")
        self.gridLayout.addWidget(self.le_appid, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.le_apikey = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_apikey.setObjectName("le_apikey")
        self.gridLayout.addWidget(self.le_apikey, 3, 1, 1, 1)
        self.sb_ue_port = QtWidgets.QSpinBox(self.layoutWidget)
        self.sb_ue_port.setMaximum(100000)
        self.sb_ue_port.setObjectName("sb_ue_port")
        self.gridLayout.addWidget(self.sb_ue_port, 0, 3, 1, 1)
        self.le_apisecret = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_apisecret.setObjectName("le_apisecret")
        self.gridLayout.addWidget(self.le_apisecret, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.le_python_ip = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_python_ip.setReadOnly(True)
        self.le_python_ip.setObjectName("le_python_ip")
        self.gridLayout.addWidget(self.le_python_ip, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1)
        self.sb_python_port = QtWidgets.QSpinBox(self.layoutWidget)
        self.sb_python_port.setReadOnly(True)
        self.sb_python_port.setMaximum(100000)
        self.sb_python_port.setObjectName("sb_python_port")
        self.gridLayout.addWidget(self.sb_python_port, 1, 3, 1, 1)
        self.pb_ask_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pb_ask_2.setGeometry(QtCore.QRect(270, 310, 101, 51))
        self.pb_ask_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pb_ask_2.setStyleSheet("")
        self.pb_ask_2.setObjectName("pb_ask_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ql_virtual_human.setText(_translate("MainWindow", "Virtual Human"))
        self.pb_ask.setText(_translate("MainWindow", "提问"))
        self.label_7.setText(_translate("MainWindow", "APIKey"))
        self.label_5.setText(_translate("MainWindow", "UE Port"))
        self.label_8.setText(_translate("MainWindow", "APISecret"))
        self.label_6.setText(_translate("MainWindow", "APPID"))
        self.label_4.setText(_translate("MainWindow", "UE IP"))
        self.label_9.setText(_translate("MainWindow", "Python  IP"))
        self.label_10.setText(_translate("MainWindow", "Python Port"))
        self.pb_ask_2.setText(_translate("MainWindow", "清除记录（&C）"))

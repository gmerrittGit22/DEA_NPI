# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(500, 380))
        Dialog.setMaximumSize(QtCore.QSize(500, 380))
        font = QtGui.QFont()
        font.setFamily("Arial")
        Dialog.setFont(font)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Dialog.setStyleSheet("QDialog{\n"
"    background:#ffffff\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.le_email = QtWidgets.QLineEdit(Dialog)
        self.le_email.setGeometry(QtCore.QRect(170, 130, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.le_email.setFont(font)
        self.le_email.setObjectName("le_email")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 200, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.le_password = QtWidgets.QLineEdit(Dialog)
        self.le_password.setGeometry(QtCore.QRect(170, 200, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.le_password.setFont(font)
        self.le_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_password.setObjectName("le_password")
        self.btn_login = QtWidgets.QPushButton(Dialog)
        self.btn_login.setGeometry(QtCore.QRect(280, 305, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
        self.btn_close = QtWidgets.QPushButton(Dialog)
        self.btn_close.setGeometry(QtCore.QRect(100, 306, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_close.setFont(font)
        self.btn_close.setObjectName("btn_close")
        self.lb_logo = QtWidgets.QLabel(Dialog)
        self.lb_logo.setGeometry(QtCore.QRect(0, 0, 500, 71))
        self.lb_logo.setStyleSheet("background:#ffffff")
        self.lb_logo.setText("")
        self.lb_logo.setObjectName("lb_logo")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 70, 500, 10))
        self.label_3.setStyleSheet("background:#26a9e1")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.cb_agree = QtWidgets.QCheckBox(Dialog)
        self.cb_agree.setGeometry(QtCore.QRect(30, 250, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.cb_agree.setFont(font)
        self.cb_agree.setObjectName("cb_agree")
        self.btn_agree_link = QtWidgets.QPushButton(Dialog)
        self.btn_agree_link.setGeometry(QtCore.QRect(200, 254, 161, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btn_agree_link.setFont(font)
        self.btn_agree_link.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn_agree_link.setStyleSheet("QPushButton{\n"
"    background:rgba(0,0,0,0);\n"
"    color:#26a9e1;\n"
"    text-align:left;\n"
"}\n"
"QPushButton:hover{\n"
"    text-decoration:underline;\n"
"}")
        self.btn_agree_link.setObjectName("btn_agree_link")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.le_email, self.le_password)
        Dialog.setTabOrder(self.le_password, self.btn_login)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Deactivated Data Engine"))
        self.label.setText(_translate("Dialog", "Email:"))
        self.label_2.setText(_translate("Dialog", "Password:"))
        self.btn_login.setText(_translate("Dialog", "Log In"))
        self.btn_close.setText(_translate("Dialog", "Close"))
        self.cb_agree.setText(_translate("Dialog", "I agree to the"))
        self.btn_agree_link.setText(_translate("Dialog", "End User License Agreement"))

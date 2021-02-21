# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(800, 550))
        Dialog.setMaximumSize(QtCore.QSize(800, 550))
        Dialog.setStyleSheet("QDialog{\n"
"    background:#ffffff\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 70, 801, 10))
        self.label.setMaximumSize(QtCore.QSize(16777215, 10))
        self.label.setStyleSheet("background:#26a9e1")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lb_logo = QtWidgets.QLabel(Dialog)
        self.lb_logo.setGeometry(QtCore.QRect(0, 0, 801, 71))
        self.lb_logo.setStyleSheet("background:#ffffff")
        self.lb_logo.setText("")
        self.lb_logo.setObjectName("lb_logo")
        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setGeometry(QtCore.QRect(670, 506, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_ok.setFont(font)
        self.btn_ok.setObjectName("btn_ok")
        self.lb_main = QtWidgets.QLabel(Dialog)
        self.lb_main.setGeometry(QtCore.QRect(35, 100, 731, 391))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.lb_main.setFont(font)
        self.lb_main.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lb_main.setObjectName("lb_main")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Deactivated Data Engine"))
        self.btn_ok.setText(_translate("Dialog", "OK"))
        self.lb_main.setText(_translate("Dialog", "Deactivated Data Engine\n"
"Version [version]\n"
"© 2020 DEA Lookup.com, Inc. All rights reserved.\n"
"\n"
"Deactivated Data Engine software are protected by trademark and other pending or\n"
"existing intellectual property rights in the United States and other\n"
"countries/regions.\n"
"\n"
"\n"
"This product is licensed under the DEA Lookup End User License Agreement\n"
"to:\n"
"    [name]\n"
"    [email]\n"
"    [company name]"))

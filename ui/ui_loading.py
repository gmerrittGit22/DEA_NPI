# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loading.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(454, 52)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(1, 2, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setStyleSheet("background:#bbbbbb; border: 1px solid black;")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.lb_loading = QtWidgets.QLabel(self.frame)
        self.lb_loading.setGeometry(QtCore.QRect(171, 16, 181, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(62)
        self.lb_loading.setFont(font)
        self.lb_loading.setStyleSheet("border:none; color: white; font-weight:500;")
        self.lb_loading.setObjectName("lb_loading")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Deactivated Data Engine"))
        self.lb_loading.setText(_translate("Dialog", "Loading ..."))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'automate.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(700, 500))
        Dialog.setMaximumSize(QtCore.QSize(700, 500))
        Dialog.setStyleSheet("QDialog{\n"
"    background:#ffffff\n"
"}")
        self.btn_save = QtWidgets.QPushButton(Dialog)
        self.btn_save.setGeometry(QtCore.QRect(420, 441, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btn_save.setFont(font)
        self.btn_save.setObjectName("btn_save")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 70, 700, 10))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label.setFont(font)
        self.label.setStyleSheet("background:#26a9e1")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lb_logo = QtWidgets.QLabel(Dialog)
        self.lb_logo.setGeometry(QtCore.QRect(0, 0, 700, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lb_logo.setFont(font)
        self.lb_logo.setStyleSheet("background:#ffffff")
        self.lb_logo.setText("")
        self.lb_logo.setObjectName("lb_logo")
        self.btn_close = QtWidgets.QPushButton(Dialog)
        self.btn_close.setGeometry(QtCore.QRect(150, 441, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btn_close.setFont(font)
        self.btn_close.setObjectName("btn_close")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(0, 85, 701, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color:#8bc53f")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(-2, 140, 701, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(294, 232, 10, 25))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.lb_apm_back = QtWidgets.QLabel(Dialog)
        self.lb_apm_back.setGeometry(QtCore.QRect(413, 248, 90, 56))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lb_apm_back.setFont(font)
        self.lb_apm_back.setStyleSheet("QLabel{\n"
"    background : \"#d4d9e2\";\n"
"    border:none;\n"
"    border-radius:10px;\n"
"\n"
"}")
        self.lb_apm_back.setText("")
        self.lb_apm_back.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_apm_back.setObjectName("lb_apm_back")
        self.btn_am = QtWidgets.QPushButton(Dialog)
        self.btn_am.setGeometry(QtCore.QRect(421, 200, 75, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_am.setFont(font)
        self.btn_am.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background: #26a9e0;\n"
"\n"
"    border-radius:7px;\n"
"}\n"
"QPushButton:checked{\n"
"        border: 3px solid #0679e0;\n"
"}\n"
"QPushButton:!checked{\n"
"        border: none;\n"
"}")
        self.btn_am.setCheckable(True)
        self.btn_am.setChecked(False)
        self.btn_am.setObjectName("btn_am")
        self.btn_pm = QtWidgets.QPushButton(Dialog)
        self.btn_pm.setGeometry(QtCore.QRect(421, 256, 75, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_pm.setFont(font)
        self.btn_pm.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    background: #26a9e0;\n"
"     border: none;\n"
"    border-radius:7px;\n"
"}\n"
"")
        self.btn_pm.setCheckable(False)
        self.btn_pm.setChecked(False)
        self.btn_pm.setObjectName("btn_pm")
        self.btn_hplus = QtWidgets.QPushButton(Dialog)
        self.btn_hplus.setGeometry(QtCore.QRect(235, 192, 25, 20))
        self.btn_hplus.setAccessibleName("")
        self.btn_hplus.setStyleSheet("QPushButton{\n"
"    background:#00ffffff;\n"
"}\n"
"QPushButton:hover:!pressed{\n"
"    background:#eeeeee;\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:#cccccc;\n"
"\n"
"}")
        self.btn_hplus.setText("")
        self.btn_hplus.setObjectName("btn_hplus")
        self.btn_mplus = QtWidgets.QPushButton(Dialog)
        self.btn_mplus.setGeometry(QtCore.QRect(335, 192, 25, 20))
        self.btn_mplus.setStyleSheet("QPushButton{\n"
"    background:#00ffffff;\n"
"}\n"
"QPushButton:hover:!pressed{\n"
"    background:#eeeeee;\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:#cccccc;\n"
"\n"
"}")
        self.btn_mplus.setText("")
        self.btn_mplus.setObjectName("btn_mplus")
        self.btn_hminus = QtWidgets.QPushButton(Dialog)
        self.btn_hminus.setGeometry(QtCore.QRect(235, 282, 25, 20))
        self.btn_hminus.setStyleSheet("QPushButton{\n"
"    background:#00ffffff;\n"
"}\n"
"QPushButton:hover:!pressed{\n"
"    background:#eeeeee;\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:#cccccc;\n"
"\n"
"}")
        self.btn_hminus.setText("")
        self.btn_hminus.setObjectName("btn_hminus")
        self.btn_mminus = QtWidgets.QPushButton(Dialog)
        self.btn_mminus.setGeometry(QtCore.QRect(335, 282, 25, 20))
        self.btn_mminus.setStyleSheet("QPushButton{\n"
"    background:#00ffffff;\n"
"}\n"
"QPushButton:hover:!pressed{\n"
"    background:#eeeeee;\n"
"    border: none;\n"
"}\n"
"QPushButton:pressed{\n"
"    background:#cccccc;\n"
"\n"
"}")
        self.btn_mminus.setText("")
        self.btn_mminus.setObjectName("btn_mminus")
        self.btn_update_now = QtWidgets.QPushButton(Dialog)
        self.btn_update_now.setGeometry(QtCore.QRect(289, 370, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btn_update_now.setFont(font)
        self.btn_update_now.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.btn_update_now.setObjectName("btn_update_now")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(192, 320, 331, 3))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background:#cccccc")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.pb_update = QtWidgets.QProgressBar(Dialog)
        self.pb_update.setGeometry(QtCore.QRect(192, 323, 331, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_update.sizePolicy().hasHeightForWidth())
        self.pb_update.setSizePolicy(sizePolicy)
        self.pb_update.setMinimumSize(QtCore.QSize(0, 10))
        self.pb_update.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pb_update.setFont(font)
        self.pb_update.setStyleSheet("QProgressBar::chunk { color: black;  }")
        self.pb_update.setProperty("value", 0)
        self.pb_update.setAlignment(QtCore.Qt.AlignCenter)
        self.pb_update.setTextVisible(True)
        self.pb_update.setObjectName("pb_update")
        self.le_minute = QtWidgets.QLineEdit(Dialog)
        self.le_minute.setEnabled(True)
        self.le_minute.setGeometry(QtCore.QRect(310, 222, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.le_minute.setFont(font)
        self.le_minute.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.le_minute.setStyleSheet("QLineEdit{\n"
"    background : \"#f7f9ff\";\n"
"    border: 1px solid \"#c7c9ff\";\n"
"    border-radius:8px;\n"
"\n"
"}")
        self.le_minute.setInputMask("")
        self.le_minute.setMaxLength(2)
        self.le_minute.setCursorPosition(1)
        self.le_minute.setAlignment(QtCore.Qt.AlignCenter)
        self.le_minute.setClearButtonEnabled(False)
        self.le_minute.setObjectName("le_minute")
        self.le_hour = QtWidgets.QLineEdit(Dialog)
        self.le_hour.setGeometry(QtCore.QRect(211, 222, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.le_hour.setFont(font)
        self.le_hour.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.le_hour.setStyleSheet("QLineEdit{\n"
"    background : \"#f7f9ff\";\n"
"    border: 1px solid \"#c7c9ff\";\n"
"    border-radius:8px;\n"
"\n"
"}")
        self.le_hour.setInputMask("")
        self.le_hour.setMaxLength(2)
        self.le_hour.setAlignment(QtCore.Qt.AlignCenter)
        self.le_hour.setObjectName("le_hour")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.le_hour, self.le_minute)
        Dialog.setTabOrder(self.le_minute, self.btn_am)
        Dialog.setTabOrder(self.btn_am, self.btn_pm)
        Dialog.setTabOrder(self.btn_pm, self.btn_update_now)
        Dialog.setTabOrder(self.btn_update_now, self.btn_close)
        Dialog.setTabOrder(self.btn_close, self.btn_save)
        Dialog.setTabOrder(self.btn_save, self.btn_mminus)
        Dialog.setTabOrder(self.btn_mminus, self.btn_hminus)
        Dialog.setTabOrder(self.btn_hminus, self.btn_mplus)
        Dialog.setTabOrder(self.btn_mplus, self.btn_hplus)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Deactivated Data Engine"))
        self.btn_save.setText(_translate("Dialog", "Save Changes"))
        self.btn_close.setText(_translate("Dialog", "Close"))
        self.label_14.setText(_translate("Dialog", "Automate DEA Data"))
        self.label_2.setText(_translate("Dialog", "Daily Update Time:"))
        self.label_5.setText(_translate("Dialog", ":"))
        self.btn_am.setText(_translate("Dialog", "AM"))
        self.btn_pm.setText(_translate("Dialog", "PM"))
        self.btn_update_now.setText(_translate("Dialog", "Update Now"))
        self.pb_update.setFormat(_translate("Dialog", "Updating DEA data %p%"))
        self.le_minute.setText(_translate("Dialog", "00"))
        self.le_hour.setText(_translate("Dialog", "02"))

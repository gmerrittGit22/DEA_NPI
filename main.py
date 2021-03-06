# -------------------------------------------------------------------------------
# DEA-NPI Data Engine (DNDE)
#
# version   : 1
# summary   : The app downloads DEA data and NPI data, and then builds a cross \
#             reference output file between the two.
# -------------------------------------------------------------------------------

## Begin import packages

# buit-in packages
import sys
import os
import pathlib
from shutil import copyfile

import threading
import socket
import uuid     # to get mac address

import ctypes
from datetime import datetime

# web browser
import webbrowser

import tempfile
import sqlite3
import pyAesCrypt

from configparser import ConfigParser

# pakages related with PyQt
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtNetwork
from PyQt5 import QtWidgets
from PyQt5 import QtPrintSupport

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtNetwork import *
from PyQt5.QtPrintSupport import *


# UIs
from ui.ui_main import Ui_MainWindow
from ui.ui_loading import Ui_Dialog as Ui_Loading_Dialog
from ui.ui_login import Ui_Dialog as Ui_Login_Dialog
from ui.ui_about import Ui_Dialog as Ui_About_Dialog
from ui.ui_splash import Ui_Dialog as Ui_Splash_Dialog
from ui.ui_automate import Ui_Dialog as Ui_Automate_Dialog
from ui.ui_agree import Ui_Dialog as Ui_Agree_Dialog

# utils
import utils.util_log as log
import utils.util_crypt as crypt
import utils.util as util

# import golabal contents
import global_content as gl_content 

## End import packages

# parse config file
conf_parser = ConfigParser()
conf_parser.read('config.ini')

# initialize the global contents
gl_content.initialize()

## Begin Implement UIs

# Splash Dialog
class SplashDialog(QDialog, Ui_Splash_Dialog):
    """
    the class to implement the Splash Dialog
    """

    # class variables...
    check_result = -1
    checkResultSignal = pyqtSignal(int)
    thread = None
    pros = 0

    # Network Access Manager to manage requests
    networkAccessManager = QtNetwork.QNetworkAccessManager()

    check_timer = QTimer()
    login_timer = QTimer()

    # constructor
    def __init__(self,parent):
        super(SplashDialog, self).__init__(parent)
        self.setupUi(self)
        
        # frameless
        self.setWindowFlags(Qt.FramelessWindowHint)
        # icon
        self.setWindowIcon(QtGui.QIcon(util.resource_path(sys, 'icon'))) 
        # set logo
        lh = 200
        lw = 460
        self.lb_logo.setPixmap(QtGui.QPixmap(util.resource_path(sys, 'logo')).scaled(
            lw, lh, 
            QtCore.Qt.KeepAspectRatio, 
            QtCore.Qt.SmoothTransformation))
        
        # start check server thread
        self.thread = threading.Thread(target=self.checkServerThread)
        self.thread.setDaemon(True)
        self.thread.start()

        self.checkResultSignal.connect(self.onCheckResult)

        # start time out timer
        self.lb_msg.setText("Checking internet connection ...")
        self.check_timer.start(300)
        self.check_timer.timeout.connect(self.onCheckTimeOut)
        self.login_timer.timeout.connect(self.onLoginTimeOut)

        #connect signal
        self.networkAccessManager.finished.connect(self.handleResponse)

    def onCheckTimeOut(self):
        """
        the function to check the Internet connection         
        """

        self.pros += 1
        self.pb_load.setValue(self.pros * 5)
        
        # timeout error
        if(self.pros == 20):
            self.check_timer.stop()
            self.onCheckConnectionError()
        # connected to server
        if(self.pros > 5 and self.check_result == 0): 
            self.check_timer.stop()
            self.checkSession()

    def onLoginTimeOut(self):
        """
        the function to check the log in         
        """

        self.pros +=1
        self.pb_load.setValue(self.pros * 4)
        # login timeout error
        if(self.pros == 25):
            self.check_timer.stop()

    def onCheckConnectionError(self):
        """
        the function to show the connection error & interact with user
        """

        # show the error message
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle(conf_parser.get("APP", "name"))
        msgBox.setText("Internet connection not detected.")
        msgBox.setStandardButtons(QMessageBox.Retry | QMessageBox.Close)
        msgBox.setDefaultButton(QMessageBox.Close)
        ret = msgBox.exec()

        # interact user
        if(ret == QMessageBox.Close):
            # exit program
            sys.exit()
        if(ret == QMessageBox.Retry):
            # retry connection
            self.thread = threading.Thread(target=self.checkServerThread)
            self.thread.setDaemon(True)
            self.thread.start()
            self.pros = 0
            self.check_timer.start(100)

    def onCheckResult(self,result):
        print("result,", result)
        self.check_result = result
        #if(result == 0):#connected to server successfully
            #self.check_timer.stop()
            #self.checkSession()
            #self.check_result = result
        #else:#error while connection
            #self.onCheckConnectionError()

    def checkSession(self):
        """
        the function to check the session
        """

        app_settings = QSettings(conf_parser.get("APP", "name"))
        end_date_time = app_settings.value("EndDateTime", type=QDateTime)
        cur_date_time = QDateTime.currentDateTime()
        if(cur_date_time.secsTo(end_date_time) > 0):
            # get values from app_settings
            gl_content.auth_email = app_settings.value("Email")
            gl_content.auth_user_company = app_settings.value("UserCompany")
            gl_content.auth_first_name = app_settings.value("FirstName")
            gl_content.auth_last_name = app_settings.value("LastName")
            gl_content.auth_user_sys_id = app_settings.value("UserSysId")
            gl_content.auth_password = app_settings.value("Password")
            
            # decrypt password
            bytes_password = bytes(gl_content.auth_password)
            gl_content.auth_password = crypt.decrypt(bytes_password)

            # make login request
            # get mac address
            mac_addr = uuid.getnode()
            if(not mac_addr):
                self.accept()
                return
            
            # configure data
            data = QtCore.QByteArray()
            data.append("username={}&".format(gl_content.auth_email))
            data.append("appVersion={}&".format(conf_parser.get("APP", "version")))
            data.append("appID={}&".format(conf_parser.get("APP", "id")))
            data.append("machineID={}&".format(mac_addr))
            data.append("password={}".format(gl_content.auth_password))
            
            # send request
            request = QtNetwork.QNetworkRequest(QtCore.QUrl(conf_parser.get("URLs", "auth")))
            request.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader,'application/x-www-form-urlencoded')
            self.networkAccessManager.post(request, data)
            
            # start timer
            self.lb_msg.setText("Logging in to the server ...")
            self.login_timer.start(200)
            self.pros = 0
        else:
            self.accept()

    def handleResponse(self, reply):
        
        # read data
        data = reply.readAll().data().decode()
        print("reply data: ", data,"|")

        gl_content.auth_result = data[0:1]
        if(gl_content.auth_result == '1'):
            data_list = data.split("|")
            reLoginTime = data_list[6]  
            AllDaySession = data_list[7]
            end_date_time = QDateTime.currentDateTime()
            reLoginTime_num = 0
            try:
                reLoginTime_num = int(reLoginTime)
            except ValueError as ex:
                reLoginTime_num = 0
            end_date_time = end_date_time.addSecs( reLoginTime_num * 60 )

            print("AllDaySession:", AllDaySession)
            if(AllDaySession == "True"):
                end_date_time.setTime(QTime(23,59,59))
            print("End Date Time: ", end_date_time.toString())      
            #save first , last name, compnay, user_sys_id
            gl_content.auth_user_sys_id = data_list[8]
            gl_content.auth_first_name = data_list[10]
            gl_content.auth_last_name = data_list[11]
            gl_content.auth_user_company = data_list[12]

            email = gl_content.auth_email
            gl_content.auth_email = email
            app_settings = QSettings(conf_parser.get("APP", "name"))
            app_settings.setValue("EndDateTime", end_date_time)
            email_cookie = app_settings.value("EmailCookie")
            if not email_cookie:
                email_cookie = email
            else:
                cookies = email_cookie.split("\x0D") #switched from underscore
                if email not in cookies:
                    email_cookie = email_cookie + "\x0D" + email
            app_settings.setValue("EmailCookie", email_cookie)
            app_settings.setValue("Email", gl_content.auth_email)
            app_settings.setValue("UserSysId", gl_content.auth_user_sys_id)
            app_settings.setValue("FirstName", gl_content.auth_first_name)
            app_settings.setValue("LastName", gl_content.auth_last_name)
            app_settings.setValue("UserCompany", gl_content.auth_user_company)
            #crypt password and save it
            crypt_password = crypt.encrypt(gl_content.auth_password)
            crypt_password = QByteArray(crypt_password)
            app_settings.setValue("Password", crypt_password)
            del app_settings
        self.accept()

    def checkServerThread(self):
        """
        the function to check the server is live or not
        """

        # check if the server is alive
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        result = 1
        try:
            result = sock.connect_ex(("dealookup.com", 80))
        except:
            result = 1 

        # server is not live    
        if result != 0:
            result = 1

        self.checkResultSignal.emit(result)

# Login Dialog
class LoginDialog(QDialog, Ui_Login_Dialog):

    # class variables...
    networkAccessManager = None
    completer = None
    error_timer = QTimer()

    def __init__(self, parent):
        super(LoginDialog, self).__init__(parent)
        self.setupUi(self)

        # icon & logo
        self.setWindowIcon(QtGui.QIcon(util.resource_path(sys, 'icon')))
        lh = 180
        lw = 180
        self.lb_logo.setPixmap(QtGui.QPixmap(util.resource_path(sys, 'logo')).scaled(
            lw, lh, 
            QtCore.Qt.KeepAspectRatio, 
            QtCore.Qt.SmoothTransformation))

        # set window flag
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

        # connect to signals
        self.networkAccessManager = QtNetwork.QNetworkAccessManager()
        self.networkAccessManager.finished.connect(self.handleResponse)

        self.btn_login.setEnabled(False)
        self.btn_login.clicked.connect(self.onLogIn)
        
        self.btn_close.clicked.connect(self.close)
        self.btn_agree_link.clicked.connect(self.onAgreeSlot)

        try:
            scale_factor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
            print('factor',scale_factor)
        except:
            scale_factor = 1.0

        self.btn_agree_link.setGeometry(
            QtCore.QRect(int(361 - (1.5 - scale_factor) * 100), 254, 
            int(164 * scale_factor), 23))

        self.cb_agree.stateChanged.connect(self.onStateChange)

        # set auto complete
        app_settings = QSettings(conf_parser.get("APP", "name"))
        email_cookie = app_settings.value("EmailCookie")
        if(email_cookie != None):
            cookies = email_cookie.split("\x0D") # switched from underscore
            self.completer = QCompleter(cookies)
            self.completer.setCaseSensitivity(Qt.CaseInsensitive)
            self.le_email.setCompleter(self.completer)

            #install event filter for empty field completer
            self.le_email.installEventFilter(self)

        # check license agree state
        license_agree = app_settings.value("LicenseAgree")
        if(license_agree == "1"):
            self.cb_agree.setChecked(True)
        
        # align the agreement text to center
        cw = self.cb_agree.fontMetrics().boundingRect(self.cb_agree.text()).width()
        cw += int(cw/4) + 7 # rectangle and space
        lw = self.btn_agree_link.fontMetrics().boundingRect(self.btn_agree_link.text()).width()
        sx = int( (self.width() - cw - lw) / 2 )

        self.cb_agree.move(sx, 250)
        self.btn_agree_link.move(sx+cw, 254)
        
        # check if error occured in relogin process or not
        if(gl_content.auth_result != '1'): # if not success
            self.le_email.setText(gl_content.auth_email)
            self.le_password.setText(gl_content.auth_password)
            self.error_timer.setSingleShot(True)
            self.error_timer.start(200) 
            self.error_timer.timeout.connect(self.showErrorMsg)

    def showErrorMsg(self):
        # failed to login
        if(gl_content.auth_result == '0'):
            QtWidgets.QMessageBox.warning( self, conf_parser.get("APP", "name"), "Failed to login. \nPlease check email and password again.")
        
        # credential is in use on another machine
        if(gl_content.auth_result == '8'):
            QtWidgets.QMessageBox.warning( self, conf_parser.get("APP", "name"), "This login is currently in use on another machine.")
            util.smtpSendMessage('Login Error', "The login({}) is currently in use on another machine.".format(self.le_email.text()))

    def onStateChange(self, state):
        print('onstatechange', state)
        license_agree = "1"
        if state == Qt.Checked:
            self.btn_login.setEnabled(True)
        else:
            self.btn_login.setEnabled(False)
            license_agree = "0"


    def eventFilter(self, object, event):
        if(object == self.le_email and event.type() == QtCore.QEvent.MouseButtonRelease):
            print('click')
            self.completer.complete()
            return False
        return False

    def onAgreeSlot(self):
        webbrowser.open(conf_parser.get("URLs", "license"))

    def onLogIn(self):
        # check emtpy field
        if(self.le_email.text() == ""):
            QtWidgets.QMessageBox.warning( self, conf_parser.get("APP", "name"), "Please fill email field.")
            return
        if(self.le_password.text() == ""):
            QtWidgets.QMessageBox.warning( self, conf_parser.get("APP", "name"), "Please fill password field.")
            return
        
        # get mac address
        mac_addr = uuid.getnode()
        if(not mac_addr):
            QtWidgets.QMessageBox.warning(self, conf_parser.get("APP", "name"), "Unable to get machine id.")
            return

        # make request
        data = QtCore.QByteArray()
        data.append("username={}&".format(self.le_email.text()))
        data.append("appVersion={}&".format(conf_parser.get("APP", "version")))
        data.append("appID={}&".format(conf_parser.get("APP", "id")))
        data.append("machineID={}&".format(mac_addr))
        data.append("password={}".format(self.le_password.text()))

        print("data:", data.data())
        request = QtNetwork.QNetworkRequest(QtCore.QUrl(conf_parser.get("URLs", "auth")))
        request.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader, 'application/x-www-form-urlencoded')
        self.networkAccessManager.post(request, data)

    def handleResponse(self, reply):
        # show login dialog
        self.setVisible(True)

        # read data
        data = reply.readAll().data().decode()
        print("reply data: ", data, "|")
        gl_content.auth_result = data[0:1]

        #check simulation first
        if(gl_content.auth_result == '9' or gl_content.SIMULATE_LOGIN9):
            QMessageBox.warning(self, conf_parser.get("APP", "name"),
                               "Version {} is no longer active. <br>"
		                       "Visit <a  href='https:/dealookup.com' style='color:#26a9e1'>www.dealookup.com</a> \
                                and log in to download the latest version.".format(conf_parser.get("APP", "version"))
                              )
            return
        #check simulation : end
        if(gl_content.auth_result == '1'):
            data_list = data.split("|")
            reLoginTime = data_list[6]  
            AllDaySession = data_list[7]
            end_date_time = QDateTime.currentDateTime()
            reLoginTime_num = 0
            try:
                reLoginTime_num = int(reLoginTime)
            except ValueError as ex:
                reLoginTime_num = 0
            end_date_time = end_date_time.addSecs( reLoginTime_num * 60 )

            print("AllDaySession:", AllDaySession)
            if(AllDaySession == "True"):
                end_date_time.setTime(QTime(23,59,59))
            print("End Date Time: ", end_date_time.toString())      
            #save first , last name, compnay, user_sys_id
            gl_content.auth_user_sys_id = data_list[8]
            gl_content.auth_first_name = data_list[10]
            gl_content.auth_last_name = data_list[11]
            gl_content.auth_user_company = data_list[12]

            email = self.le_email.text()
            gl_content.auth_email = email
            app_settings = QSettings(conf_parser.get("APP", "name"))
            app_settings.setValue("EndDateTime", end_date_time)
            email_cookie = app_settings.value("EmailCookie")
            if not email_cookie:
                email_cookie = email
            else:
                cookies = email_cookie.split("\x0D")
                if email not in cookies:
                    email_cookie = email_cookie + "\x0D" + email
            app_settings.setValue("EmailCookie", email_cookie)
            app_settings.setValue("Email", gl_content.auth_email)
            app_settings.setValue("UserSysId", gl_content.auth_user_sys_id)
            app_settings.setValue("FirstName", gl_content.auth_first_name)
            app_settings.setValue("LastName", gl_content.auth_last_name)
            app_settings.setValue("UserCompany", gl_content.auth_user_company)

            app_settings.setValue("LicenseAgree", "1")

            #crypt password and save it
            gl_content.auth_password = self.le_password.text()
            crypt_password = crypt.encrypt(gl_content.auth_password)
            crypt_password = QByteArray(crypt_password)
            app_settings.setValue("Password", crypt_password)
            del app_settings
            '''
            1|valid|[details]|[superadmin 1 or 0]|[admin 1 or 0]|[Localhost Location]|[reLoginTime - in minutes]|[AllDaySession - true false]|
            [user_sys_id]|[last login date/time]|[user first name]|[user last name]|[user company]|
            '''
            self.accept()
        else:
            app_settings = QSettings(conf_parser.get("APP", "name"))
            app_settings.setValue("LicenseAgree", "0")
            self.showErrorMsg()

# About Dialog
class AboutDialog(QDialog, Ui_About_Dialog):
    def __init__(self, parent):
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)

        # set icon
        self.setWindowIcon(QtGui.QIcon(util.resource_path(sys, 'icon'))) 
        # set logo
        lh = 180
        lw = 180
        self.lb_logo.setPixmap(QtGui.QPixmap(util.resource_path(sys, 'logo')).scaled(
            lw, lh, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        
        # init field values
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

        # connect signals
        self.btn_ok.clicked.connect(self.close)

        # init values
        html = self.lb_main.text()
        html = html.replace("[name]", "{} {}".format(gl_content.auth_first_name, gl_content.auth_last_name))
        html = html.replace("[email]", gl_content.auth_email)
        html = html.replace("[company name]", gl_content.auth_user_company)
        html = html.replace("[version]", conf_parser.get("APP", "version"))
        self.lb_main.setText(html)

# Loading Dialog
class LoadingDialog(QDialog, Ui_Loading_Dialog):

    # class scope variables
    timer = None
    dot_count = 2

    def __init__(self, parent):
        super(LoadingDialog, self).__init__(parent)
        self.setupUi(self)

        #icon
        self.setWindowIcon(QtGui.QIcon(util.resource_path(sys, "icon")))

        #start timer
        self.timer = QTimer()
        self.timer.start(300)
        self.timer.timeout.connect(self.timeOutSlot)

    def timeOutSlot(self):
        self.dot_count += 1
        if(self.dot_count == 4):
            self.dot_count = 0
        loading_text = "Loading "
        for x in range(self.dot_count):
            loading_text += "."

        self.lb_loading.setText(loading_text)

# Main
class MainUI(QMainWindow, Ui_MainWindow):
    """
    the class to implement the Main UI
    """

    # define class variables
    thread = None
    buildProgressSignal = pyqtSignal(int)
    importProgressSignal = pyqtSignal(int)
    loadingFinishedSignal = pyqtSignal()

    # main database
    db_data = None
    cursor_data = None
    # config database
    db_config = None
    cursor_config = None

    # flags to show first time to popup
    b_first_popup = True
    # flag to show latest message when check updates
    check_update_show_latest = False

    # Compoments
    loading_dialog = None
    automate_dialog = None
    sb_progressbar  = None

    # Network Access Manager to manage requests
    networkAccessManager = QtNetwork.QNetworkAccessManager()

    # timers for build and update
    update_timer = QTimer()
    build_timer = QTimer()

    # constructor
    def __init__(self):
        super(MainUI, self).__init__()
        self.setupUi(self)

        #icon
        self.setWindowIcon(QtGui.QIcon(util.resource_path(sys, 'icon')) )
        # set logo
        lh = 180
        lw = 180
        self.lb_logo.setPixmap(QtGui.QPixmap(util.resource_path(sys, 'logo')).scaled(
            lw, lh, 
            QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            )

        # window size
        self.setFixedHeight(620)
        self.setFixedWidth(900)

        self.ckb_sil.setChecked(True)
        self.sb_mday.hide()
        self.cb_wday.hide()
        self.te_time.hide()

        #hide progress  bar
        self.pb_build.hide()

        # connect slots
        # self.buildProgressSignal.connect(self.buildProgressSlot)
        self.loadingFinishedSignal.connect(self.loadingFinishedSlot)
        self.importProgressSignal.connect(self.importProgressSlot)

        # self.btn_save.clicked.connect(self.clickedSaveSlot)
        # self.btn_view.clicked.connect(self.clickedViewSlot)
        # self.btn_build.clicked.connect(self.clickedBuildSlot)
        # self.rb_ads.clicked.connect(self.clickedAdsSlot)
        # self.rb_mds.clicked.connect(self.clickedMdsSlot)
        # self.rb_mrm.clicked.connect(self.clickedMrmSlot)
        # self.cb_frequency.currentIndexChanged.connect(self.frequencyChangedSlot)
        self.btn_brw.clicked.connect(self.clickedBrowseSlot)

        # menu actions
        self.act_import.triggered.connect(self.clickedImportSlot)
        self.act_backup.triggered.connect(self.clickedBackupSlot)    
        self.act_about.triggered.connect(self.clickedAboutSlot)
        self.act_help.triggered.connect(self.clickedHelpSlot)
        self.act_check_update.triggered.connect(self.clickedCheckUpdateSlot)
        # self.act_automate.triggered.connect(self.clickedAutomateSlot)
        self.act_exit.triggered.connect(self.close)

        # timers
        # self.update_timer.timeout.connect(self.updateSlot)
        # self.build_timer.timeout.connect(self.clickedBuildSlot)
        # self.update_timer.setSingleShot(True)
        # self.build_timer.setSingleShot(True)


        # loading dialog
        self.setEnabled(False)
        self.loading_dialog = LoadingDialog(self)
        self.loading_dialog.setWindowFlags(Qt.FramelessWindowHint)
        ww = (self.width() - self.loading_dialog.width()) / 2
        hh = (self.height() - self.loading_dialog.height()) / 2
        self.loading_dialog.move(int(ww), int(hh) - 100)

        # dialog
        # self.automate_dialog = AutomateDialog(self)

        # add status bar
        status_bar  = QStatusBar(self)
        self.setStatusBar(status_bar)
        self.sb_pbar = QProgressBar(self)
        self.sb_pbar.setFormat("Updating DEA data  %p%")
        self.sb_pbar.setAlignment(Qt.AlignCenter)
        self.sb_pbar.setValue(0)
        self.sb_pbar.hide()
        self.sb_pbar.setMaximumWidth(350)
        status_bar.addPermanentWidget(self.sb_pbar)

        #welcome message
        self.lb_welcome_msg.setText("Welcome {} {}".format(gl_content.auth_first_name, gl_content.auth_last_name))
        self.btn_preferences.clicked.connect(self.clickedPreferencesSlot)

        # check if db exists
        if(not util.check_db_files()):
            QtWidgets.QMessageBox.warning(self, conf_parser.get("APP", "name"), "DB file does not exists.")
            sys.exit()
        # check new verison : make request
        self.networkAccessManager.finished.connect(self.handleResponse)

        if(gl_content.auth_new_login):
            data = QtCore.QByteArray()
            data.append("username={}&".format(gl_content.auth_email))
            data.append("appVersion={}&".format(conf_parser.get("APP", "version")))
            data.append("appID={}&".format(conf_parser.get("APP", "id")))
            data.append("password={}".format(gl_content.auth_password))
            # send request
            request = QtNetwork.QNetworkRequest(QtCore.QUrl(conf_parser.get("URLs", "version")))
            request.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader, 'application/x-www-form-urlencoded')
            self.networkAccessManager.post(request, data)

        # loading thread
        self.thread = threading.Thread(target=self.firstLoadThread)
        self.thread.setDaemon(True)
        self.thread.start()

    # Begin Slots
    def clickedPreferencesSlot(self):
        url = "{}&username={}&password={}".format(
            conf_parser.get("URLs", "preference"), gl_content.auth_email, gl_content.auth_password)
        print('url', url)
        webbrowser.open(url)

    def clickedBackupSlot(self):
        # check already working
        # if(self.thread != None or self.automate_dialog.thread != None):#already working
        if(self.thread != None):
            QtWidgets.QMessageBox.warning( self, \
                conf_parser.get("APP", "name"), "The database is updating. Please wait.")
            return
        #choose file
        default_path = QDateTime.currentDateTime().toString("yyyy_MM_dd_H_mm_ss")
        default_path = "db(back)_" + default_path
        fileName = QFileDialog.getSaveFileName(self, 'License Lookup',default_path,"Db files (*.db)")
        if(fileName[0] == ''):
            return
        try:
            copyfile(gl_content.db_path, fileName[0])
        except IOError as e:
            print('backup failed')
            return
        QtWidgets.QMessageBox.information( self, \
            conf_parser.get("APP", "name"), "Succeeded to backup db as {}.".format(fileName[0]))

    def clickedCheckUpdateSlot(self, reply):
        # make the content
        data = QtCore.QByteArray()
        data.append("username={}&".format(gl_content.auth_email))
        data.append("appVersion={}&".format(conf_parser.get("APP", "version")))
        data.append("appID={}&".format(conf_parser.get("APP", "id")))
        data.append("password={}".format(gl_content.auth_password))
        
        # set flag
        self.check_update_show_latest = True
        
        # send request
        request = QtNetwork.QNetworkRequest(QtCore.QUrl(conf_parser.get("URLs", "version")))
        request.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader, 'application/x-www-form-urlencoded')
        self.networkAccessManager.post(request, data)

    def clickedHelpSlot(self):
        webbrowser.open(conf_parser.get("URLs", "help"))

    def clickedAboutSlot(self):
        about_dialog = AboutDialog(self)
        about_dialog.exec_()

    def clickedBrowseSlot(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.DirectoryOnly)
        dialog.setOption(QFileDialog.ShowDirsOnly)
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        # dialog.setNameFilter("Text files (*.txt);;All Files (*)")
        dialog.setWindowTitle("Choose directory to save")
        if dialog.exec_():
            dir = dialog.selectedFiles()[0]
            self.le_sd.setText(dir)

    def clickedImportSlot(self):
        # check already working
        # if(self.thread != None or self.automate_dialog.thread != None):
        if(self.thread != None):
            QtWidgets.QMessageBox.warning( self, conf_parser.get("APP", "name"), "The database is updating. Please wait.")
            return

        # choose file
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        dialog = QFileDialog(self)
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        dialog.setNameFilter("Text files (*.txt);;All Files (*)")
        dialog.setWindowTitle("Choose file to import")
        fileName = ''
        if dialog.exec_():
            fileNames = dialog.selectedFiles()
            fileName = fileNames[0]

        # cancel button
        if(len(fileName) < 5):
            return

        if(util.check_import_dea_file(fileName) == 'length'):
            QtWidgets.QMessageBox.warning( self, conf_parser.get("APP", "name"), "Import data file record length has changed or is incorrect.")
            util.smtpSendMessage('Import Error', 'Error: Data file record length changed')
            return
        if(util.check_import_dea_file(fileName) == 'permission'):
            QtWidgets.QMessageBox.warning( self, conf_parser.get("APP", "name"), "Permission denied to the local import file")
            util.smtpSendMessage('Import Error', 'Error: Permission denied to the local import file')
            return
        
        gl_content.dea_import_path = fileName  

        #set ui
        self.pb_build.show()
        self.pb_build.setFormat("Importing DEA data from file %p%")
        self.pb_build.setValue(0)

        # close db
        self.db_data.close()
        self.db_config.close()
        self.db_data = self.db_config = None
        
        # set inital load date
        initial_load = self.ckb_sil.isChecked()

        #start thread
        self.thread = threading.Thread(target=self.importThreadAction,kwargs={'initial_load':initial_load})
        self.thread.setDaemon(True)
        self.thread.start()

    def importThreadAction(self, initial_load):
        util.import_local_dea_file(0, self.importProgressSignal, initial_load)

    def loadingFinishedSlot(self):
        self.loading_dialog.hide()
        self.loading_dialog.timer.stop()
        self.setEnabled(True)

        # set release data
        self.lb_dea_import_date.setText('DEA data import date: ' + gl_content.dea_import_date)
        
        # connect to db
        self.connect_db()

        # thread none
        self.thread = None
        
        # check if db empty, remove initial load date
        if(not self.checkDataEmpty()):
            self.ckb_sil.hide()
            self.lb_sil.hide()
        
        # load saved settings
        # self.loadSettings()
        # self.refreshDDR()
        # self.loadYearMonthComboBox()
        
        # set single shot timer for ui
        # self.setUpdateTimer()

    def closeEvent(self, event):
        # here you can terminate your threads and do other stuff
        super(QMainWindow, self).closeEvent(event)

        #close db
        if(self.db_data != None):
            self.db_data.close()
        if(self.db_config != None):
            self.db_config.close()
        
        #remove temp file
        self.pb_build.hide()
        util.remove_temp_files(gl_content.TEMP_DB_SUFFIX)

        sys.exit()

    # End Slots

    def connect_db(self):
        # main records db
        self.db_data = sqlite3.connect(gl_content.db_temp_path)
        self.cursor_data = self.db_data.cursor()
        
        # config db
        self.db_config = sqlite3.connect(gl_content.conf_temp_path)
        self.cursor_config = self.db_config.cursor()

    def checkDataEmpty(self):
        self.cursor_data.execute('select count(*) from items')
        row = self.cursor_data.fetchone()
        return row[0] == 0

    def handleResponse(self, reply):

        # decode the response data
        data = reply.readAll().data().decode()
        v_result = data[0:1]
        url = "{}&username={}&password={}".format(
            conf_parser.get("URLs", "download"), gl_content.auth_email, gl_content.auth_password)
        if(v_result == "2"):
            QMessageBox.information( 
                self, conf_parser.get("APP", "name"),
                "A new version of License Lookup is available. <br>"
                "Visit <a  href='{}' style='color:#26a9e1'>www.dealookup.com</a> \
                to download the latest version.".format(url)
            )
            return
        if(self.check_update_show_latest and v_result == "1"):
            QMessageBox.information(
                self, conf_parser.get("APP", "name"), 
                "Your version of {} is up to date.".format(conf_parser.get("APP", "name")))
        self.check_update_show_latest = False

    def importProgressSlot(self, value):
        if(value == 200):
            self.pb_build.hide()
            self.lb_dea_import_date.setText('Data Import Date: ' + gl_content.dea_import_date)
            msg = "Successfully imported."
            QtWidgets.QMessageBox.information( self, conf_parser.get("APP", "name"), msg)
            self.connect_db()
            # self.loadYearMonthComboBox()
            # self.refreshDDR()

            # hide initial load button
            if (not self.checkDataEmpty()):
                self.ckb_sil.hide()
                self.lb_sil.hide()

            self.thread = None
        else:
            self.pb_build.setValue(value)

    def firstLoadThread(self):
        # generate template path
        tf = tempfile.NamedTemporaryFile(suffix=gl_content.TEMP_DB_SUFFIX)
        gl_content.db_temp_path = tf.name
        tf.close()

        tf = tempfile.NamedTemporaryFile(suffix=gl_content.TEMP_DB_SUFFIX)
        gl_content.conf_temp_path = tf.name
        tf.close()

        # encrypt db
        pyAesCrypt.decryptFile(gl_content.db_path, gl_content.db_temp_path, gl_content.AES_PASSWORD, gl_content.AES_BUFFER_SIZE)
        pyAesCrypt.decryptFile(gl_content.conf_path, gl_content.conf_temp_path, gl_content.AES_PASSWORD, gl_content.AES_BUFFER_SIZE)

        # load main db
        context = sqlite3.connect(gl_content.db_temp_path)
        cursor = context.cursor()
        cursor.execute('''select * from items where fullName like '%smith%' limit 200''')
        data = cursor.fetchall()
        context.close()

        # load conf db
        context = sqlite3.connect(gl_content.conf_temp_path)
        cursor = context.cursor()    
        cursor.execute('''select * from config where name = 'import_date' ''')
        data = cursor.fetchone()
        import_date = ""
        if(data != None):
            import_date = str(data[1])
        gl_content.dea_import_date = import_date
        context.close()
        
        self.loadingFinishedSignal.emit()

## End Implement UIs



# Entry point of the project
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(util.resource_path(sys, 'icon')))

    gl_content.db_path = util.db_path('data')
    gl_content.conf_path = util.db_path('conf')

    # background build mode
    if (len(sys.argv) == 2 and sys.argv[1] == 'build'):
        # open the build log file
        try:
            log_file = open(util.build_log_path(), "a")
        except Exception as e:
            sys.exit()
        
        # startup log
        current_time = datetime.now()
        current_string = current_time.strftime("%Y/%m/%d %H:%M:%S")

        log_file = log.add_build_log(log_file, "****************************************")
        log_file = log.add_build_log(log_file, "Build started on {}\n".format(current_string))

        # generate db paths
        gl_content.db_path = util.db_path('data')
        gl_content.conf_path = util.db_path('conf')
        if (not os.path.exists(gl_content.db_path) or not os.path.exists(gl_content.conf_path)):
            log_file = log.add_build_log(log_file, "DB does not exists at {}".format(gl_content.db_path))
            sys.exit()
        
        # check the another instance is running
        memory = QSharedMemory(conf_parser.get("APP", "name"))
        if (not memory.create(1)):
            log_file = log.add_build_log(log_file, "Another instance of app is already running.")
            log_file.close()
            sys.exit()
        
        # decrypt database
        tf = tempfile.NamedTemporaryFile(suffix=conf_parser.get("TEMP_SUFFIX", "db"))
        gl_content.db_temp_path = tf.name
        tf.close()
        tf = tempfile.NamedTemporaryFile(suffix=conf_parser.get("TEMP_SUFFIX", "db"))
        gl_content.conf_temp_path = tf.name
        tf.close()
        pyAesCrypt.decryptFile(gl_content.db_path, gl_content.db_temp_path, \
            conf_parser.get("AES", "pass"), conf_parser.get("AES", "buffer_size"))
        pyAesCrypt.decryptFile(gl_content.conf_path, gl_content.conf_temp_path, \
            conf_parser.get("AES", "pass"), conf_parser.get("AES", "buffer_size"))
        
        # check build options first
        # db_conf = sqlite3.connect(gl_content.conf_temp_path)
        # cursor_conf = db_conf.cursor()

    # background update mode
    if (len(sys.argv) == 2 and sys.argv[1] == 'update'):
        pass

    # check if main app is running
    memory = QSharedMemory(conf_parser.get("APP", "name"))
    if (not memory.create(1)):
        QtWidgets.QMessageBox.warning(None, conf_parser.get("APP", "name"), "Another instance of app is already running.")
        sys.exit()

    # regiser dealookup path
    app_settings = QSettings(conf_parser.get("APP", "name"))
    app_settings.setValue("Path", str(pathlib.Path().absolute()))
    del app_settings

    # check the session first
    splash_ui = SplashDialog(None)
    login_ui = None

    if(splash_ui.exec_() == QDialog.Accepted):
        # no session or failed to login
        if(gl_content.auth_email == '' or gl_content.auth_result != '1'):
            login_ui = LoginDialog(None)
            if(login_ui.exec_() == QDialog.Accepted):
                gl_content.main_ui = MainUI()
                gl_content.main_ui.show()
            else:
                sys.exit()
            # gl_content.main_ui = MainUI()
            # gl_content.main_ui.show()
        else: # if there is session, and auth result is true
            gl_content.auth_new_login = False
            gl_content.main_ui = MainUI()
            gl_content.main_ui.show()
        app.exec_()
    else:
        sys.exit()

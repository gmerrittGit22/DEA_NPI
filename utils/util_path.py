

## Begin import packages

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

# built-in packages
import os

from configparser import ConfigParser
## End import packages

conf_parser = ConfigParser()
conf_parser.read('config.ini')


# Paths for Logs
def update_log_path():
    """
    the function to get the log file name for update operation
        reutrn:
            file_path: (String), the path of log file for update operation
    """

    app_setting = QSettings(conf_parser.get("APP", "name"))
    file_name = "update_log.txt"
    path = app_setting.value("Path")
    file_path = os.path.join(path, file_name)
    return file_path


def build_log_path():
    """
    the function to get the log file name for build operation
        reutrn:
            file_path: (String), the path of log file for build operation            
    """

    app_setting = QSettings(conf_parser.get("APP", "name"))
    file_name = "build_log.txt"
    path = app_setting.value("Path")
    file_path = os.path.join(path, file_name)
    return file_path


# Path for Resources
src_paths = {
    'logo': "res/logo.png",
    'icon': "res/main.ico",
    'popup': "res/popup.png",
    'plus': "res/up.png",
    'minus': "res/down.png",
}

def resource_path(sys, resource):
    """
    the function to get the log file name for build operation
        param:
            sys: (module), object of sys module
            resource: (String), type of resource
        reutrn:
            (String), the path of specify resource file         
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("./")
    
    return os.path.join(base_path, src_paths[resource])


# Path for dbs
db_paths = {
    'data': "data/data.db",
    'conf': "data/conf.db",
}

def db_path(db_name):
    """
    the function to get the log file name for build operation
        param:
            db_name: (String), the type of database
        reutrn:
            path: (String), the path of specify database file            
    """

    app_setting = QSettings(conf_parser.get("APP", "name"))
    path = app_setting.value("Path")
    path = os.path.join(path, db_paths[db_name])
    return path

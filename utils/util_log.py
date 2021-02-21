

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

# custom utils
from  utils.util import build_log_path, update_log_path                             

## End import packages


def add_update_log(file, msg):
    """
    the function to output log in update log file
        param:
            file: (TextIOWrapper), the io wrapper for update log file
            msg: (String), log context            
        reutrn:
            file: (TextIOWrapper), the io wrapper for update log file
    """

    file.write("{}\n".format(msg))
    print(msg)
    file.close()
    file = open(update_log_path(), "a")
    return file


def add_build_log(file, msg):
    """
    the function to output log in build log file
        param:
            file: (TextIOWrapper), the io wrapper for build log file
            msg: (String), log context            
        reutrn:
            file: (TextIOWrapper), the io wrapper for build log file
    """

    file.write("{}\n".format(msg))
    print(msg)
    file.close()
    file = open(build_log_path(), "a")
    return file

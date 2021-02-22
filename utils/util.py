
## Begin import packages

import smtplib, ssl
import pathlib
import os
import sqlite3

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

# import global contents
# from config import *
import global_content as gl_content

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

def check_db_files():
    """
    the function to check the database files exist or not
        return:
            (boolean), if data and conf database not exist False, 
                        otherwise True
    """

    path = pathlib.Path().absolute()
    path_data = os.path.join(path, db_paths['data'])
    path_conf = os.path.join(path, db_paths['conf'])
    if (not os.path.exists(path_data) or not os.path.exists(path_conf) ):
        return False
    return True

def remove_temp_files(suffix):
    """
    the function to remove (delete) temp files created
        param:
            suffix: (string), the suffix of temp files
    """
    global gl_content

    tmpdir = os.path.dirname(gl_content.db_temp_path)
    for f in os.listdir(tmpdir):
        if f.endswith(suffix):
            try:
                os.remove(os.path.join(tmpdir, f))
            except Exception as e:
                print('remove temp file exception ', e)

def initSmtp():
    """
    the function to init the SMTP object
    """

    try:
        context = ssl.create_default_context()
        gl_content.smtp_obj = smtplib.SMTP('smtp.mailgun.org', 587)
        gl_content.smtp_obj.starttls(context=context)
        gl_content.smtp_obj.login(conf_parser.get("SMTP", "mail"), conf_parser.get("SMTP", "pass"))
        print('smtp login success')
    except Exception as e:
        print ("Error: unable to connect smtp", e)
        gl_content.smtp_obj = None

def smtpSendMessage(subject, content):
    """
    the function to send the SMTP mail
    """

    # if(SKIP_MAIL):
    #     return

    if(gl_content.smtp_obj == None):
        initSmtp()
    message = 'Subject: {}\n\n{}'.format(subject, content)
    # send
    try:
        gl_content.smtp_obj.sendmail("customerservice@dealookup.com", "appsupport@dealookup.com", message)
        print('succeeded to send email message')
    except Exception as e:
        print("Error: failed to send email message.", e)


#import from local db
#iv: initial value
#custom_signal: signal to update ui
#initial_load: set initial load date
# def import_from_local_file(initial_value, custom_signal, initial_load):
#     """
#     the function to import data from local file
#         param:
#             initial_value: (int), initial value for progress bar
#             custom_singal: (signal), signal to update the ui(progress bar)
#             initial_load: (boolean), set initial load date
#     """

#     global DB_IMPORT_DATE
#     #calc pros range
#     left = 90 -iv
#     import_range = int(left * 0.7)
#     compare_range = int( (left - import_range)/3 )
#     # prepare db
#     cnx = sqlite3.connect(DB_TEMP_PATH)
#     cursor = cnx.cursor()
#     # check if the items table is empty
#     b_old_empty = False  # old table is emtpy
#     cursor.execute('''select count(*) from items ''')
#     record = cursor.fetchone()
#     if (record[0] == 0):
#         b_old_empty = True
#     else:  # if old table is not empty
#         # drop old table
#         cursor.execute('''DROP TABLE IF EXISTS items_old''')
#         # alter  items -> items_old
#         cursor.execute('''ALTER TABLE items RENAME TO items_old''')
#         # create new table items
#         cursor.execute('''CREATE TABLE items
#           (idnumber text, bac text, schedule text, expirationDate text, fullName text, nameAdditional text, address1 text,
#           address2 text, city text, state text, zip text, bac_subcode text, pay_ind text, status text, PRIMARY KEY(idnumber))''')
#     # text data
#     path = IMPORT_PATH
#     file = open(path, 'r')
#     total_count = int(os.stat(path).st_size / ITEM_LENGTH)
#     update_rate = int(total_count / import_range) + 1
#     item_count = 0
#     while True:
#         item_count += 1
#         # for test
#         # if item_count == 3:
#         #     break
#         # Get next line from file
#         line = file.readline()

#         # if line is empty
#         # end of file is reached
#         if not line:
#             break
#         idnumber = line[0:9].strip()
#         bac = line[9:10].strip()
#         schedule = line[10:26].strip()
#         expirationDate = line[26:34].strip()
#         fullName = line[34:74].strip().replace("'", "''")
#         nameAdditional = line[74:114].strip().replace("'", "''")
#         address1 = line[114:154].strip().replace("'", "''")
#         address2 = line[154:194].strip().replace("'", "''")
#         city = line[194:227].strip().replace("'", "''")
#         state = line[227:229].strip()
#         zipCode = line[229:234].strip()
#         bacSub = line[234:235].strip()
#         payInd = line[235:236].strip()
#         status = line[236:244].strip()

#         # line = line.strip()
#         # print("Line{}: idnumber:{}, bac:{}, schedule:{},expd:{}, fn:{}, na:{}, a1:{}, a2:{}, city:{}, state:{}, z:{},bs:{}, pi:{}, status:{}"
#         #     .format(item_count, idnumber,bac, schedule,expirationDate, fullName, nameAdditional, address1, address2, city, state, zipCode, bacSub, payInd, status))
#         # insert
#         sql = ''
#         try:
#             sql = ''' INSERT INTO items VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')
#               '''.format(idnumber, bac, schedule, expirationDate, fullName, nameAdditional, address1, address2, city,
#                          state, zipCode, bacSub, payInd, status)
#             cursor.execute(sql)
#         except sqlite3.OperationalError as e:
#             print('SQL Error :', sql)
#             return
#         # update progress bar
#         if item_count % update_rate == 0 and custom_signal:
#             custom_signal.emit(iv + int(item_count / update_rate))

#         # self.pb_import.setValue( item_count * 100 / total_count  )
#         # commit db
#         if item_count % 50000 == 0:
#             cnx.commit()
#     cnx.commit()


#     if custom_signal:
#         custom_signal.emit(iv + import_range)
#     # if old table is not empty , calculate deactivated,  new, changed
#     if (not b_old_empty):
#         #calculate date first
#         if(DB_IMPORT_DATE == ''):#this error wont appear in 99.99 %
#             DB_IMPORT_DATE = DEFAULT_DB_IMPORT_DATE
#         last_active_date = DB_IMPORT_DATE[6:10] + "/" + DB_IMPORT_DATE[0:2] + "/" + DB_IMPORT_DATE[3:5]
#         added_date = change_date = QDate.currentDate().toString("yyyy/MM/dd")
#         # clear items_deactivated, items_new, items_changed
#         # cursor.execute('''delete from items_deactivated''')
#         # cursor.execute('''delete from items_changed''')
#         # cursor.execute('''delete from items_new''')
#         # process items_deactivated
#         sql = "select items_old.* from items_old  left join items on items_old.idnumber = items.idnumber where items.idnumber IS NULL"
#         cursor.execute(sql)
#         records = cursor.fetchall()
#         update_rate = int(len(records) / compare_range) + 1
#         id = 1
#         print('update_rate', update_rate)
#         for row in records:
#             try:
#                 sql = ''' INSERT INTO items_deactivated(last_active_date,idnumber,bac,schedule,expirationDate,fullName,nameAdditional,address1,address2,city,state,zip,bac_subcode,pay_ind,status) VALUES( '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''\
#                     .format( last_active_date, row[0].replace("'", "''"), row[1].replace("'", "''"),
#                              row[2].replace("'", "''"),
#                              row[3].replace("'", "''"), row[4].replace("'", "''"), row[5].replace("'", "''"),
#                              row[6].replace("'", "''"),
#                              row[7].replace("'", "''"), row[8].replace("'", "''"), row[9].replace("'", "''"),
#                              row[10].replace("'", "''"),
#                              row[11].replace("'", "''"), row[12].replace("'", "''"), row[13].replace("'", "''"))
#                 cursor.execute(sql)
#                 id += 1
#                 # update progress bar
#                 if (id % update_rate == 0 and custom_signal):
#                     custom_signal.emit(iv + import_range  + int(id / update_rate))
#             except sqlite3.OperationalError as e:
#                 print('SQL Error :', sql)
#         cnx.commit()
#         if(custom_signal):
#             custom_signal.emit(iv + import_range + compare_range)
#         # process items_changed
#         sql = '''select items_old.* from items left join items_old on items_old.idnumber = items.idnumber where 
#           items.bac <> items_old.bac OR items.schedule <> items_old.schedule OR items.expirationDate <> items_old.expirationDate OR 
#           items.fullName <> items_old.fullName OR items.nameAdditional <> items_old.nameAdditional OR items.address1 <> items_old.address1 OR 
#           items.address2 <> items_old.address2 OR items.city <> items_old.city OR items.state <> items_old.state OR items.zip <> items_old.zip OR 
#           items.bac_subcode <> items_old.bac_subcode OR items.pay_ind <> items_old.pay_ind'''
#         cursor.execute(sql)
#         records = cursor.fetchall()
#         update_rate = int(len(records) / compare_range) + 1
#         id = 1
#         for row in records:
#             try:
#                 sql = ''' INSERT INTO items_changed(change_date,idnumber,bac,schedule,expirationDate,fullName,nameAdditional,address1,address2,city,state,zip,bac_subcode,pay_ind,status) VALUES( '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''\
#                     .format( change_date, row[0].replace("'", "''"), row[1].replace("'", "''"),
#                              row[2].replace("'", "''"),
#                              row[3].replace("'", "''"), row[4].replace("'", "''"), row[5].replace("'", "''"),
#                              row[6].replace("'", "''"),
#                              row[7].replace("'", "''"), row[8].replace("'", "''"), row[9].replace("'", "''"),
#                              row[10].replace("'", "''"),
#                              row[11].replace("'", "''"), row[12].replace("'", "''"), row[13].replace("'", "''"))
#                 cursor.execute(sql)
#                 id += 1
#                 # update progress bar
#                 if (id % update_rate == 0 and custom_signal):
#                     custom_signal.emit(iv + import_range + compare_range + int(id / update_rate))
#             except sqlite3.OperationalError as e:
#                 print('SQL Error :', sql)
#         cnx.commit()
#         if(custom_signal):
#             custom_signal.emit(iv + import_range + compare_range*2)
#         # process items_new
#         sql = "select items.idnumber from items  left join items_old on items.idnumber = items_old.idnumber where items_old.idnumber IS NULL"
#         cursor.execute(sql)
#         records = cursor.fetchall()
#         update_rate = int(len(records) / compare_range) + 1
#         id = 1
#         for row in records:
#             try:
#                 sql = ''' INSERT INTO items_new(idnumber,added_date) VALUES('{}', '{}')'''.format(row[0].replace("'", "''"), added_date)
#                 cursor.execute(sql)
#                 id += 1
#                 # update progress bar
#                 if (id % update_rate == 0 and custom_signal):
#                     custom_signal.emit(iv + import_range + compare_range*2 + int(id / update_rate))
#             except sqlite3.OperationalError as e:
#                 print('SQL Error :', sql)
#     #drop old db; no necessary any more
#     cursor.execute('''DROP TABLE IF EXISTS items_old''')
#     cnx.commit()
#     #optimize db, vacuum
#     print("Optimizing DB")
#     cursor.execute('''VACUUM''')
#     # final commit, close
#     cnx.commit()
#     file.close()
#     cnx.close()

#     # update release date

#     cnx = sqlite3.connect(DB_CONF_TEMP_PATH)
#     cursor = cnx.cursor()
#     import_date = QDate.currentDate().toString("MM/dd/yyyy")
#     if(DB_IMPORT_DATE == '' and initial_load): #first import
#         DB_IMPORT_DATE = DEFAULT_DB_IMPORT_DATE
#     else:
#         DB_IMPORT_DATE = import_date
#     cursor.execute('''UPDATE config set value='{}' where name='import_date' '''.format(DB_IMPORT_DATE))
#     cnx.commit()
#     cnx.close()
#     # update data , conf db files
#     pyAesCrypt.encryptFile(DB_TEMP_PATH, DB_PATH, AES_PASSWORD, AES_BUFFER_SIZE)
#     pyAesCrypt.encryptFile(DB_CONF_TEMP_PATH, DB_CONF_PATH, AES_PASSWORD, AES_BUFFER_SIZE)
#     # generate signal to update main gui
#     if(custom_signal):
#         custom_signal.emit(200)

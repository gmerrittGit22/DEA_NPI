
## Begin import packages

import smtplib, ssl
from configparser import ConfigParser

# import global contents
from global_content import *

## End import packages

conf_parser = ConfigParser()
conf_parser.read('config.ini')


def initSmtp():
    try:
        context = ssl.create_default_context()
        gl_smtp_obj = smtplib.SMTP('smtp.mailgun.org', 587)
        gl_smtp_obj.starttls(context=context)
        gl_smtp_obj.login(conf_parser.get("SMTP", "mail"), conf_parser.get("SMTP", "pass"))
        print('smtp login success')
    except Exception as e:
        print ("Error: unable to connect smtp", e)
        gl_smtp_obj = None

def smtpSendMessage(subject, content):

    # if(SKIP_MAIL):
    #     return

    if(gl_smtp_obj == None):
        initSmtp()
    message = 'Subject: {}\n\n{}'.format(subject, content)
    # send
    try:
        gl_smtp_obj.sendmail("customerservice@dealookup.com", "appsupport@dealookup.com", message)
        print('succeeded to send email message')
    except Exception as e:
        print("Error: failed to send email message.", e)


# check if db files exist or not
def check_db_files():
    path = pathlib.Path().absolute()
    path_data = os.path.join(path, DB_PATH)
    path_conf = os.path.join(path, DB_CONF_PATH)
    if (not os.path.exists(path_data) or not os.path.exists(path_conf) ):
        return False
    return True

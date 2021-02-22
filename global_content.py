
def initialize():

    ## Begin Global Constants...

    # Aes
    global AES_BUFFER_SIZE
    global AES_PASSWORD
    AES_BUFFER_SIZE = 64 * 1024
    AES_PASSWORD = "password"

    # temp file
    global TEMP_DB_SUFFIX
    global TEMP_ZIP_SUFFIX
    TEMP_DB_SUFFIX = "dnde_tmp"
    TEMP_ZIP_SUFFIX = "zip_dnde_tmp"

    # simulation
    global SIMULATE_LOGIN9
    SIMULATE_LOGIN9 = False

    # import db
    global ITEM_LENGTH
    global DEFAULT_DB_IMPORT_DATE

    ITEM_LENGTH = 246 #length of one item in txt data: 244 + 2(\r\n)
    DEFAULT_DB_IMPORT_DATE = '11/16/2020'

    ## End Global Constants...


    ## Begin Global Variables...

    # Auth
    global auth_email
    global auth_user_sys_id
    global auth_first_name
    global auth_last_name
    global auth_user_company
    global auth_password
    global auth_result
    global auth_new_login
    
    auth_email = None            # user's email
    auth_user_sys_id = None      # user's id
    auth_first_name = None       # user's first name
    auth_last_name = None        # user's last name
    auth_user_company = None     # user's company
    auth_password = None         # user's password
    auth_result = None           # result of authentication
    auth_new_login = True        # login from saved session or not

    # SMTP
    global smtp_obj
    smtp_obj = None               # SMTP object

    # UI
    global main_ui
    main_ui = None

    # database
    global db_path
    global conf_path
    global db_temp_path
    global conf_temp_path
    global db_import_date
    global db_import_path

    db_path = ''
    conf_path = ''
    db_temp_path = None
    conf_temp_path = None
    db_import_date = ''
    db_import_path = ''

    ## End Global variables...

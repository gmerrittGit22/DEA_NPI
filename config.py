

## Begin Global Constants...

# Aes
AES_BUFFER_SIZE = 64 * 1024
AES_PASSWORD = "password"

# temp file
TEMP_DB_SUFFIX = "dnde_tmp"
TEMP_ZIP_SUFFIX = "zip_dnde_tmp"

# simulation
SIMULATE_LOGIN9 = False

## End Global Constants...


## Begin Global Variables...

# Auth
gl_auth_email = None            # user's email
gl_auth_user_sys_id = None      # user's id
gl_auth_first_name = None       # user's first name
gl_auth_last_name = None        # user's last name
gl_auth_user_company = None     # user's company
gl_auth_password = None         # user's password
gl_auth_result = None           # result of authentication
gl_auth_new_login = True        # login from saved session or not

# SMTP
gl_smtp_obj = None               # SMTP object

# UI
gl_main_ui = None

# database
gl_db_path = ''
gl_conf_path = ''
gl_db_temp_path = None
gl_conf_temp_path = None
gl_db_import_date = ''

## End Global variables...

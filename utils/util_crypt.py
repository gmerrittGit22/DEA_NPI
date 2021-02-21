
## Begin import packages

import io

import pyAesCrypt
## End import packages


## Begin Constant Variables

BUFFER_SIZE = 64
PASSWORD = "acer"
## Begin Constant Variables


def encrypt(data):
    """
    the function to encrypt data
        param:
            data: (bytes), the original data need to be encrypted
        return:
            encrypt result
    """

    data = bytes(data, 'utf-8')
    f_iput = io.BytesIO(data)
    f_crypt = io.BytesIO()
    pyAesCrypt.encryptStream(f_iput, f_crypt, PASSWORD, BUFFER_SIZE)

    return f_crypt.getvalue()


def decrypt(data):
    """
    the function to decrypt data
        param:
            data: (bytes), the original data need to be decrypted
        return:
            (string), decrypt result
    """

    length = len(data)
    f_crypt = io.BytesIO(data)
    f_decrypt = io.BytesIO()

    try:
        pyAesCrypt.decryptStream(f_crypt, f_decrypt, PASSWORD, BUFFER_SIZE, length)
    except ValueError as e:
        return ""
    
    result = str(f_decrypt.getvalue())

    # beautify
    length = len(result)
    if (length > 3):
        result = result[2:length - 1]
    else:
        result = ""
    return result

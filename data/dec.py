import pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "password"
# encrypt
#pyAesCrypt.encryptFile("data.db", "data.db.dec", password, bufferSize)
# decrypt
pyAesCrypt.decryptFile("data.db", "data.db.dec", password, bufferSize)
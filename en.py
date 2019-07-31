from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Cipher import AES
import base64
import os

def encrypt(key, filename):
    chunksize = 64*1024
    outputFile = "en_" + filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV =Random.new().read(16)
    """---add IV info ----"""
    print (IV)
    """---add IV info ----"""
    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)
                """---check chunkinfo  ----"""
                print (chunk)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))

def getKey(password):
            hasher = SHA256.new(password.encode('utf-8'))
            return hasher.digest()


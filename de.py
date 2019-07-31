from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Cipher import AES
import base64
import os
import itertools

def decrypt(key, filename,outfile):
    checksize = 64*1024
    with open(filename, 'rb') as targetfile:         
         data = targetfile.read()
         verifyData = data[0:16]
         IV = data[16:32]
         print ('-----text info ------')
         print (data)
         print ('-----file size info ------')
         print (data[0:16])
         print ('-----initial vector info ------')
         print (data[16:32])

         VI = data[16:32]
         filesize = int (data[0:16])
         print ('-----target password info ------')
         encryption = data[32:]
         print (encryption)
         de = AES.new(key, AES.MODE_CBC, IV)
         

         print ('-----decoded info ------')
         decrypted=de.decrypt(encryption)
         print (decrypted)
         with open(outfile, 'wb') as outfile:
            outfile.write(decrypted)


   


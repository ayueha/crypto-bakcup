import os
from tkinter import Tk
from tkinter.filedialog import askopenfile
import argparse
from Crypto.Hash import SHA256
from Crypto import Random
from Crypto.Cipher import AES
from pathlib import Path

def parser():
    result = 0
    parser = argparse.ArgumentParser(description='encryption and decryption ')
    parser.add_argument('type', help='encrypt image [e] or decrypt image [d]')
    parser.add_argument('key' ,help='key information of encryption')
    args = parser.parse_args()

    if args.type=='e':
        result = 1,args.key
    elif args.type=='d':
        result = 2,args.key
    return result


def hexconvert(imageFile,temphex,IV,key):
    outputFile = 'encrypt.txt'
    if os.path.isfile(temphex) == False:
        Path(temphex).touch()
        print (temphex + ' has been generated')

    cmd = 'xxd -p '+imageFile.name + ' > ' + temphex
    os.system(cmd)
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    with open(temphex, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            hexchunk = infile.read()
            chklength = len(hexchunk)%16
            hexchunk += b' ' *(16-chklength)
            outfile.write(IV)
            outfile.write(encryptor.encrypt(hexchunk))
    print (outputFile + ' has been generated')
    os.remove(temphex)
    print ('temporary file' +temphex + ' has been generated')

def imageconvert(encfile,tempimg,key,temphex):
    '''print (encfile.name)'''
    with open(encfile.name, 'rb') as targetfile:
        data = targetfile.read()
        IV = data[0:16]
        encryption = data[16:]
        decryption = AES.new(key, AES.MODE_CBC, IV)
        decrypted=decryption.decrypt(encryption)
        
        with open(temphex, 'wb') as hexfile:
            hexfile.write(decrypted.rstrip())

    cmd = 'xxd -r -p '+temphex+ ' > ' + tempimg
    os.system(cmd)
    print (tempimg + ' has been generated')
    os.remove(temphex)
    print ('temporary file' +temphex + ' has been generated')

def getKey(password):
            hasher = SHA256.new(password.encode('utf-8'))
            return hasher.digest()


if __name__ == '__main__':
    result = parser()

    temphex = 'temp_hex.log'
    tempimg = 'decode_img.jpeg'    
    
    key = getKey(result[1])

    if result[0] == 1:
        Tk().withdraw()
        imageFile = askopenfile()
        if imageFile is not None:
            IV =Random.new().read(16)
            hexconvert(imageFile,temphex,IV,key)
        else:
            print ('No file has been selected ... ')

    elif result[0] == 2:
        Tk().withdraw()
        encfile = askopenfile()
        if encfile is not None:
            imageconvert(encfile,tempimg,key,temphex)
        else:
            print ('No file has been selected ... ')


'''
https://www.vitoshacademy.com/hashing-passwords-in-python/

'''
import argparse
import hashlib
import os
import binascii
import time


def parser():
    parser = argparse.ArgumentParser(description = 'HASH algorithm')
    parser.add_argument('hash', help='choose MD5, SHA1, or SHA256')
    parser.add_argument('path', help='target directory or one file')
    args = parser.parse_args()
    return args.hash,args.path

def encryption(hashtype,path):
    if os.path.isdir(path):
        files = os.listdir(path)
        start = time.time()
        for f in files:
            executeHash(hashtype, f,path)
    else:
        start = time.time()
        executeHash(hashtype,path,'')

    calcSpeed = time.time()-start

    print ('speed of '+ hashtype +':{0}'.format(calcSpeed) + ' sec')

def executeHash(hashtype, hexdump, path):
    if (path==''):
        target = hexdump
    else:
        target = path+'/'+hexdump

    with open(target,'rb') as f:
        plaintext = f.read()

    if hashtype=='MD5':
        salt = hashlib.md5(os.urandom(16)).hexdigest().encode('ascii')
        passwordHash = hashlib.pbkdf2_hmac('MD5',plaintext,salt,100000)
    elif hashtype=='SHA1':
        start = time.time()
        salt = hashlib.sha1(os.urandom(16)).hexdigest().encode('ascii')
        passwordHash = hashlib.pbkdf2_hmac('sha1',plaintext,salt,100000)
    elif hashtype=='SHA256':
        start = time.time()
        salt = hashlib.sha256(os.urandom(16)).hexdigest().encode('ascii')
        passwordHash = hashlib.pbkdf2_hmac('sha256',plaintext,salt,100000)
    
    passwordHash = binascii.hexlify(passwordHash)
    print (salt + passwordHash)
    

if __name__ == '__main__':
    result = parser()

    if result[0]!='':
        encryption(result[0],result[1])
    else:
        print ('HASH oprtions are MD5, SHA1, or SHA256... terminate program')
    


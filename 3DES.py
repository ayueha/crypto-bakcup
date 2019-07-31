#from Crypto.PublicKey import RSA
from Crypto.Cipher import DES3
from Crypto import Random


def TripleDesEnc(key,plaintext):
    IV = Random.new().read(8)
    encrypter=DES3.new(key,DES3.MODE_OFB,IV)
    msg=IV+encrypter.encrypt(text)
    return msg

def TripleDesDec(key,msg):
    IV = msg[0:8]
    encData = msg[8:]
    encrypter=DES3.new(key,DES3.MODE_OFB,IV)
    decode=encrypter.decrypt(encData)
    return decode

def genKey():
    exportKey = Random.new().read(16)
    return exportKey

key = genKey()

text = 'des is no more used for practical'

print ('original test :' + text)

enctext = TripleDesEnc(key,text)

print ('encrypted test :' + enctext)

dectext = TripleDesDec(key,enctext)

print ('decrypted test :' + dectext)

import os
import random

import pyaes, pbkdf2,secrets
import rsa

def RSA():
    public_key,private_key=rsa.newkeys(256)
    f = open("keyPair.key", "wb")

    # print(pub)
    # print(pr)
    f.write(public_key.save_pkcs1("PEM"))
    f.write(private_key.save_pkcs1("PEM"))
    # f.write(str2)
    f.close()
    return public_key,private_key
def AES_Key():
  aes_key=os.urandom(16)
  f=open("key.key","wb")
  f.write(aes_key)
  f.close()
#pub,pr=RSA()
def Encrypt_file(path):
    file=open(path)
    text=file.readlines()
    text=''.join(text)
    file.close()
    print(text)
    g=open("key.key","rb")
    aes_key=g.read()
    g.close()
    iv = 0

    #print(type(iv))
    aes=pyaes.AESModeOfOperationCTR(aes_key, pyaes.Counter(iv))
    ciphertext = aes.encrypt(text)
    y=open(path,"wb")
    y.write(ciphertext)
    y.close()
    #return iv
def Decrypt_File(path):
    file = open(path,"rb")
    ciphertext = file.read()
    #ciphertext = ''.join(ciphertext)
    file.close()
    g = open("key.key", "rb")
    aes_key = g.read()
    g.close()
    iv = 0
   # text=aes.d
    # print(type(iv))
    aes = pyaes.AESModeOfOperationCTR(aes_key, pyaes.Counter(iv))
    text = aes.decrypt(ciphertext)
    y = open(path, "wb")
    y.write(text)
    y.close()
    #


    #pyaes.AESModeOfOperationCBC(text)


def AES_Key_Encrypt():
    f=open("key.key","rb")
    aes_key=f.read()
    #print(len(aes_key))
    f.close()
    g=open("keyPair.key","rb")
    pu = rsa.PublicKey.load_pkcs1(g.read())
    g.close()
    aes_key_enc=rsa.encrypt(aes_key,pu)
    y=open("encryptedKey.key","wb")
    y.write(aes_key_enc)
    y.close()

#RSA()
#AES_Key()
#AES_Key_Encrypt()
Decrypt_File('omar.txt')
#print(pr)
#f.write(str2)


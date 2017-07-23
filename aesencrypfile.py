#!/usr/bin/env python
# coding: utf-8
# aesencrypfile.py

import sys, hashlib, os, base64
from random import randint
from Crypto.Cipher import AES

try:
    fic=sys.argv[1]
except IndexError:
    fic=raw_input('File name : ')

key=raw_input('Encryption Key : ')
hkey=hashlib.sha256(key).digest()
iv=hashlib.sha256(str(randint(64,64*64))).digest()    #[:16]
IV=base64.encodestring(iv)[:16]    # gros pâté
encryption=AES.new(hkey, AES.MODE_CBC, IV)
with open(fic,'r+') as f_in:
    buf=f_in.read()
    count=0
    while True:
        if (len(buf)+count)%16==0:
            break
        count+=1
    tmp=buf+' '*count
aes=fic+'.aes'

with open(aes,'w') as f_out:
    wr=encryption.encrypt(tmp)
    f_out.write(IV+wr)  

print('\n%s : %d bytes.'%(aes,os.path.getsize(aes))),
#if sys.platform != 'win32':
    #print("%s : %s"%(aes,os.system('file '+aes)))
print('Encrypted')


#!/usr/bin/env python
# aesencryptxt.py

import sys, hashlib, os, base64
from random import randint
from Crypto.Cipher import AES

try:
    fic=sys.argv[1]
except IndexError:
    fic=raw_input('Output file name : ')

msg=''
print('Message (CTRL_D to quit) :')
while True:
    lig=sys.stdin.readline()
    if not lig: break
    msg+=lig
key=raw_input('\n\tKey : ')
print
hkey=hashlib.sha256(key).digest()
iv=hashlib.sha256(str(randint(64,64*64))).digest()    #[:16]
IV=base64.encodestring(iv)[:16]
encryption=AES.new(hkey, AES.MODE_CBC, IV)

# Padding #
pad=' '
msg=IV+msg
while True:
    try:
        aes=encryption.encrypt(msg)
        break
    except ValueError:
        pass
    msg+=pad
print aes

with open(fic,'w+') as f:
    f.write(aes)
print('\n%s : %d bytes. Encrypted'%(fic,os.path.getsize(fic)))

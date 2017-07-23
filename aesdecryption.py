#!/usr/bin/env python
# aesdecryption.py

import sys,hashlib,base64
from Crypto.Cipher import AES

try:
    fic=sys.argv[1]
except IndexError:
    fic=raw_input('File to decrypt : ')


try:
    with open(fic,'rb') as f:
        iv=f.read(16)
        key=raw_input('Key : ')
        hkey=hashlib.sha256(key).digest()
        decryption=AES.new(hkey, AES.MODE_CBC, iv)
        msg=f.read()   
        clear=decryption.decrypt(msg) 
        print(clear)
        rep=raw_input('Write file (N/y) ? : ')
        if rep.lower().startswith('y'):
            out=raw_input('File name : ')
            with open(out,'w') as f:
                f.write(clear)        
except IOError, e:
    print(e)
    sys.exit()


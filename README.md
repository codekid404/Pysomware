# Pysomware

Pysomware contains 2 python files
  - ransomware.py
  - decrypt.py

ransomware.py is coded in a way to encrypt all the files and generate a decryption key to be used with decrypt.py
The script also keeps in mind to ignore ransomware.py, the decryptionkey and decrypt.py so that they are not encrypted


Usage

python3 ransomware.py
  - encrypts all the file
  - creates decrpytion key

python3 decrypt.py
  - decrypts all the file making use of the decryptionkey which was generated in the previous step.


Please use with care! I do not encourage using this for illegal purposes!

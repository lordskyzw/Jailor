import os
from cryptography.fernet import Fernet

key = "g2r974sFdeKDkGGdJLuBy48fv2Luqavkz38TwHfZ8TE="


files = os.listdir()

for _ in files:
    if _ == "decryption.py" or _ == "thekey.key":
        continue
    with open(_, "rb") as thefile:
        contents = thefile.read()
        contents_decrypted = Fernet(key).decrypt(contents)
        with open(_, "wb") as thefile:
            thefile.write(contents_decrypted)
    

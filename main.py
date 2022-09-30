#from cryptography.fernet import Fernet
import os
import argparse

#make it read file path from argument
parser = argparse.ArgumentParser(prog='Jailor', usage='main.py <full path to file>', description='This program encrypts folders and files given in the path as arguments')
parser.add_argument('path')
args = parser.parse_args()
itemPath = args.path

target = os.path(itemPath)
print(target)
#key = Fernet.generate_key()

#Fernet.encrypt(key, b"target")


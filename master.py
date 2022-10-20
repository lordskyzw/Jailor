import socket
import threading

FORMAT = "utf-8"
DISCONNECT_MESSAGE ="Disconnected!"
SERVERIP = socket.gethostbyname(socket.gethostname())
PORT = 6969
ADDR = (SERVERIP, PORT)
HEADER = 1024

master = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
master.bind(ADDR)



def reception(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        if msg_length:
            msg_length = int(msg_length)
            msg = master.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            else : thekey = msg
    open("thekey.key", "wb").write(thekey)
    print(thekey)
   
    
def start():
    master.listen()
    print(f"Server is running on {ADDR}")
    while True:
        conn, addr =master.accept()
        thread = threading.Thread(target=reception, args=(conn, addr))
        thread.start()
        print(f"Active Connections: {threading.active_count() - 1}")

print(ADDR)
start()
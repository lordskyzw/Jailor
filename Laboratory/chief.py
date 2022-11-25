import socket
import select


ADDR =(socket.gethostbyname(socket.gethostname), 6969)

socketslist = []


def chatserver():
    chief_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    chief_socket.bind(ADDR)

    socketslist.append(chief_socket)

    chief_socket.listen(10)


    while 1:
        ready_to_read, ready_to_write, in_error = select.select(socketslist, [], [], 0)
        
    for sock in ready_to_read:
        if sock == chief_socket:
            print("New connection")
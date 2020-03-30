import socket
import threading
import sys
s = socket.socket()
host = '10.0.0.54'
port = 1234
user_name = input("Enter user name::")
s.connect((host,port))

s.send(user_name.encode())

clientRunning = True

def receiveMsg(sock):
    serverDown = False
    while clientRunning and (not serverDown):
        try:
            msg = sock.recv(1024).decode()
            print(msg)
        except:
            print('Server is Down.')
            serverDown = True

threading.Thread(target = receiveMsg, args = (s,)).start()
while clientRunning:
    tempMsg = input()
    msg = user_name + '>>' + tempMsg
    s.send(msg.encode())

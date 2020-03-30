import socket
import threading
s = socket.socket()
host = '10.0.0.54'
port = 1234

clients = {}

s.bind((host,port))
s.listen(2)

def handleClient(client, user_name):
    clientConnected = True
    keys = clients.keys()

    while clientConnected:
        try:
            msg = client.recv(1024).decode()
            
            if not '@' in msg:
                for k, v in clients.items():
                    v.send(msg.encode())
            else:        
                for name in keys:
                    if ('@' + name) in msg:
                        msg = msg.replace('@' + name, '')
                        clients.get(name).send(msg.encode())
                     
        except:
            clients.pop(user_name)
            print(user_name + ' has been logged out')
            clientConnected = False
while True:
   
    client, address = s.accept()
    user_name = client.recv(1024).decode()
    print('%s connected to the server' % str(user_name))
    

    if (client not in clients):
        clients[user_name] = client       
        threading.Thread(target=handleClient, args=(client, user_name,)).start()

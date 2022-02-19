import os 
import socket
import threading


HOST = '127.0.0.1' 
PORT = 9090


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))


server.listen()

clients = []

nicknames = []

#broadcast
def broadcast(message):

    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]}")
            broadcast(message.encode('utf-8'))
        except:
            clients.remove(client)
            client.close()
            raise Exception

def recieve():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")

        client.send("NICKNAME".encode('utf-8'))
        nickname = client.recv(1024)
        nicknames.append(nickname)
        clients.append(client)


        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} connected to the server!\n".encode('utf-8'))
        client.send("Connected successfully!".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is running...")

recieve()
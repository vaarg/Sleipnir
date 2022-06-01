#!/bin/python

# Sleipnir v 0.1

import argparse
import socket
import threading

# Server:

def connector():
    while True:
        clientSocket, clientAddress = server.accept()
        print(f"{clientAddress} has connected.")
        clientSocket.send(bytes("Enter in username and then press [ENTER]: ", encoding))
        addresses[clientSocket] = clientAddress
        threading.Thread(target=handler, args=(clientSocket,), daemon=True).start()

def handler(clientSocket):
    username = clientSocket.recv(byteSize).decode(encoding)
    success = f"You have connected as {username}, type '{terminatingStr}' to terminate connection at anypoint."
    clientSocket.send(bytes(success, encoding))
    clients[clientSocket] = username
    message = f"{username} has connected!"
    broadcaster(bytes(message, encoding))
    sending = threading.Thread(target=serverSend, daemon=True)
    sending.start()

    while True:
            message = clientSocket.recv(byteSize)
            if message != bytes("q!", encoding):
                broadcaster(message, username+": ")       
            else:
                clientSocket.send(bytes("q!",encoding))
                clientSocket.close()
                del clients[clientSocket]
                broadcaster(bytes(f"{username} has disconnected.", encoding))
                break

def broadcaster(message, prefix=""):
    print(f"{prefix}{message.decode(encoding)}")
    for sockets in clients:
        sockets.send(bytes(prefix, encoding) + message)

def serverSend():
    while True:
        messageSend = input()
        broadcaster(bytes(messageSend, encoding), "Host: ")

def serverInit():
    global clients, addresses, server, newThread
    clients = {}
    addresses = {}
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print("Awaiting connections...")
    newThread = threading.Thread(target=connector, daemon=True)
    newThread.start()
    newThread.join() 
    server.close()

# Client:

def receiver():
    while True:
        messageRecv = clientSock.recv(byteSize).decode(encoding)
        print(messageRecv)

def clientInit():
    global clientSock
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Connecting to {HOST}:{PORT}.")
    clientSock.connect((HOST,PORT))

    clientThread = threading.Thread(target=receiver, daemon=True)
    clientThread.daemon = True
    clientThread.start()

    while True:
        messageSend = input()
        if messageSend == terminatingStr:
            clientSock.send(bytes(terminatingStr, encoding))
            break
        clientSock.send(bytes(messageSend, encoding))
    print(f"Terminating sequence '{terminatingStr}' entered! Terminating client.")
    clientSock.close()

# [!] Main

parser = argparse.ArgumentParser()
parser.add_argument('-t','-T','--target', required=True, help="target IP")
parser.add_argument('-p','-P','--port', help="target PORT", type=int, default=4444)
parser.add_argument('-s','-S','--server', action='store_true', help="launch as Server")
args = parser.parse_args()

HOST = args.target
PORT = args.port

byteSize = 2048
encoding = "latin-1"
terminatingStr = "q!"

if args.server:
    serverInit()
else:
    clientInit()

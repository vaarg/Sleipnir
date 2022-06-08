#!/bin/python

# Sleipnir v 1.0.1

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

import argparse
import base64
import socket
import threading
import time

# [=] Common:

def passwordSet(passwordSess):
    global password
    password = passwordSess

    if len(password) < 16:
        i = len(password) # 15
        while i < 16:
            password += b'A'
            i += 1
    elif len(password) > 16:
        password = password[0:16]

# [#] Encryption/Decryption:

def encryptMsg(data):
    global ciphered_data
    cipher = AES.new(password, AES.MODE_CBC, iv)
    ciphered_data = cipher.encrypt(pad(data, AES.block_size))
    ciphered_data = base64.encodebytes(ciphered_data)

def decryptMsg(ciphered_data):
    global decrypted_data
    ciphered_data = base64.decodebytes(ciphered_data)
    cipher = AES.new(password, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)

# [<] Server:

def connector():
    while True:
        clientSocket, clientAddress = server.accept()
        print(f"{clientAddress} has connected.")
        addresses[clientSocket] = clientAddress
        threading.Thread(target=handler, args=(clientSocket,clientAddress), daemon=True).start()

def handler(clientSocket, clientAddress):
    username = clientSocket.recv(byteSize).decode(encoding)
    clientSocket.send(bytes("Authenticating...", encoding))
    time.sleep(1)
    clients[clientSocket] = username
    cliPass = clientSocket.recv(byteSize)
    try:
        decryptMsg(cliPass)
        cliPass = decrypted_data 
    except:
        cliPass = ""  
    sending = threading.Thread(target=serverSend, daemon=True)
    sending.start()
    stage = 0

    while True:
        if stage == 0:
            if cliPass == password:
                stage = 1 
                pass       
            else:
                kill = f"{terminatingStr}"
                clientSocket.send(bytes(kill, encoding))
                clientSocket.close()
                del clients[clientSocket]
                broadcaster(bytes(f"{clientAddress} has been disconnected: Incorrect session password.", encoding))
                break
        if stage == 1:
            stage = 2
            success = f"You have successfully connected as {username}! Type '{terminatingStr}' to terminate connection at anypoint."
            time.sleep(1)
            clientSocket.send(bytes(success, encoding))
            message = f"{username} has connected!"
            broadcaster(message.encode(encoding))
            pass
        if stage == 2:
            message = clientSocket.recv(byteSize)
            decryptMsg(message)
            if decrypted_data.decode(encoding) != "q!":
                broadcaster(decrypted_data, username+": ")
            else:
                clientSocket.close()
                del clients[clientSocket]
                disconnect = f"{username} has disconnected."
                broadcaster(disconnect.encode(encoding))
                break


def broadcaster(message, prefix=""):
    print(f"{prefix}{message.decode(encoding)}")
    sendMessage = prefix.encode(encoding) + message
    encryptMsg(sendMessage)
    for sockets in clients:
        sockets.send(ciphered_data)


def serverSend():
    while True:
        messageSend = input()
        broadcaster(bytes(messageSend, encoding), "Host: ")

def serverInit():
    global clients, addresses, server, newThread
    clients = {}
    addresses = {}
    passwordSess = bytes(input("Enter server session password: "), encoding)
    passwordSet(passwordSess)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(maxClients)
    print("Awaiting connections...")
    newThread = threading.Thread(target=connector, daemon=True)
    newThread.start()
    newThread.join() 
    server.close()

# [>] Client:

def receiver():
    count = 0
    while True:
        messageRecv = clientSock.recv(byteSize)
        count += 1
        if count < 3:
            messageRecv = messageRecv.decode(encoding)
            if messageRecv == f"{terminatingStr}":
                break
            print(messageRecv)
        else:
            decryptMsg(messageRecv)
            print(decrypted_data.decode(encoding))
    print(f"Disconnected. Incorrect session password! Type '{terminatingStr}' to terminate program.")

def sender():
    while True:
        messageSend = input()
        if messageSend == terminatingStr:
            encryptMsg(messageSend.encode(encoding))
            clientSock.send(ciphered_data)
            break
        encryptMsg(messageSend.encode(encoding))
        clientSock.send(ciphered_data)
    print(f"Termination sequence '{terminatingStr}' entered! Terminating client.")
    clientSock.close()

def clientInit():
    global clientSock
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Connecting to {HOST}:{PORT}.")
    clientSock.connect((HOST,PORT))

    passwordSess = bytes(input("Enter session password and then press [ENTER]: "), encoding)
    passwordSet(passwordSess)
    encryptMsg(password)
    username = input("Enter username and the press [ENTER]: ")
    clientSock.send(bytes(username, encoding))
    clientSock.send(ciphered_data)

    clientThread = threading.Thread(target=receiver, daemon=True)
    clientThread.daemon = True
    clientThread.start()
    sender()

# [!] Main

parser = argparse.ArgumentParser()
parser.add_argument('-t','-T','--target', required=True, help="target IP")
parser.add_argument('-p','-P','--port', help="target PORT", type=int, default=4444)
parser.add_argument('-s','-S','--server', action='store_true', help="launch as Server")
args = parser.parse_args()

HOST = args.target
PORT = args.port

maxClients = 10
byteSize = 2048
encoding = "latin-1"
terminatingStr = "q!"
iv = 16 * b'\0'

if args.server:
    serverInit()
else:
    clientInit()

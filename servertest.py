
'''
Server Side code

1 - chat
2 - online
3 - offline
'''


from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import subprocess

users = [('admin', 'pass'), ('user', 'pass1'), ('shree', 'shree'), ('jon', 'jon')]
online_users = []

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = SERVER.accept()
        print("%s:%s has connected." % client_address)
        #client.send(bytes("Greetings from the cave! Now type your name and press enter!"))
        addresses[client] = client_address
        logincreds = client.recv(BUFSIZ).decode("utf-8")
        username, password = logincreds.split()
        login = (username, password)
        if login not in users:
            print("Failed Login")
            client.close()
        clients[client] = username
        online_users.append(username)
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = clients[client]
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(welcome.encode())
    broadcastStatus(','.join(online_users))


    while True:
        msg = client.recv(BUFSIZ)
        if msg != "{quit}".encode():
            broadcast(msg, name)
        else:
            client.send("{quit}".encode())
            client.close()
            #online_users.remove(name)
            del online_users[online_users.index(name)]
            #print("before" , clients)
            del clients[client]
            #print("after", clients)
            broadcast("has left the chat.",  name)
            broadcastStatus(','.join(online_users))
            break


def broadcastStatus(name):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(("2" + name).encode())

def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send((prefix + ": " + msg.decode("utf-8")).encode())
        
clients = {}
addresses = {}
online_clients = {}

HOST = ''
PORT = 33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
while True:
    try:
        SERVER.bind(ADDR)
        break
    except:
        subprocess.call(' sudo lsof -t -i tcp:33000 | xargs kill -9', shell = True)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
SERVER.close()
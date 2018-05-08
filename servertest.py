
'''
Server Side code
'''


from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

users = [('admin', 'pass'), ('user', 'pass1')]

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
        Thread(target=handle_client, args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""

    name = clients[client]
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(welcome.encode())
    #msg = "%s has joined the chat!" % name
    #broadcast(msg.decode("utf-8"))

    while True:
        msg = client.recv(BUFSIZ)
        if msg != "{quit}".encode():
            broadcast(msg, name)
        else:
            client.send("{quit}".encode())
            client.close()
            del clients[client]
            broadcast(("%s has left the chat." % name).encode)
            break


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
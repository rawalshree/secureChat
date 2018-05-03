import socket
from time import sleep

global passwords
passwords = [('admin', 'pass'), ('hello', 'world'), ('test', 'test')]

class Server:

    def check_login(self, tuple):
        global passwords
        if tuple in passwords:
            return True 
    

    def connect(self):
        c1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c1.bind(('', 9000))
        c1.listen(5)

        c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c2.bind(('', 9001))
        c2.listen(5)
        print("Waiting For Connection")

        while True:
            try:
                conn, address = c1.accept()
                print("Connection from Client : ", address)
                break
            except:
                print("Waiting for user to connect")
                sleep(3)

        while True:
            try:
                conn, address = c2.accept()
                print("Connection from Client : ", address)
                break
            except:
                print("Waiting for user to connect")
                sleep(3)
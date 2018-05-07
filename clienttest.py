from tkinter import *
import socket
import select
import sys

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print "Correct usage: script, IP address, port number"
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))
 


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        MainMenu(self)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames={}

        for F in (LoginPage, ChatPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()


class LoginPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        usernameLabel = Label(self, text = "Username")
        passwordLabel = Label(self, text = "Password")

        usernameEntry = Entry(self)
        passwordEntry = Entry(self, show="*")

        usernameLabel.grid(row=0, sticky=E)
        usernameEntry.grid(row=0, column=1)

        passwordLabel.grid(row=1, sticky=E)
        passwordEntry.grid(row=1, column=1)

        login = Button(self, text="Login", command = _login_btn_clicked(self))
        login.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        loginCreds = (username, password)

        server.send(loginCreds)






class ChatPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        my_msg = StringVar()  # For the messages to be sent.
        scrollbar = Scrollbar(self)  # To navigate through past messages.
        # Following will contain the messages.
        msg_list = Listbox(self, width=50, yscrollcommand=scrollbar.set)
        user_list = Listbox(self, width=20, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y,)
        msg_list.pack(side=LEFT, fill=BOTH, padx = 10, pady = 20)
        user_list.pack(side=RIGHT, fill=BOTH, padx=10, pady = 20)

        entry_field = Entry(self, textvariable=my_msg)
        entry_field.bind("<Return>")
        entry_field.pack(side=LEFT, anchor=SW)
        send_button = Button(self, text="Send")
        send_button.pack(side=BOTTOM)

        self.grid()


class MainMenu:
    def __init__(self, master):
        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)


app = App()
app.mainloop()
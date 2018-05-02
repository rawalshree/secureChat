from p2pserver import *
from tkinter import messagebox

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

s = Server()

failure_max = 3

def make_entry(parent, caption, width=None, **options):
    tk.Label(parent, text=caption).pack(side=tk.TOP)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
    return entry

def enter(event):
    check_password()

def check_password(failures=[]):
    """ Collect 1's for every failure and quit program in case of failure_max failures """
    #print(user.get(), password.get())
    auth = (user.get(), password.get())
    if s.check_login(auth):
        messagebox.showinfo("Successful", "Login Successful")
        root.withdraw()
        homewindow()
    else:
        messagebox.showerror("Error", "Incorrect Username or password")
        
    failures.append(1)
    if sum(failures) >= failure_max:
        messagebox.showwarning("Login_attempt", "Max login attempts reached")
        root.destroy()
        raise SystemExit('Unauthorized login attempt')
    else:
        root.title('Try again. Attempt %i/%i' % (sum(failures)+1, failure_max))

def homewindow():
    root.title("Chatter")
    messages_frame = tk.Frame(root)
    scrollbar = tk.Scrollbar(messages_frame)  # To navigate through past messages.
    # Following will contain the messages.
    msg_list = tk.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    msg_list.pack(side=tk.LEFT, fill=tk.BOTH)
    msg_list.pack()
    messages_frame.pack()

    entry_field = tk.Entry(root, textvariable=my_msg)
    entry_field.bind("<Return>", send)
    entry_field.pack()
    send_button = tk.Button(root, text="Send", command=send)
    send_button.pack()

    root.protocol("WM_DELETE_WINDOW", on_closing)

def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg))
    if msg == "{quit}":
        client_socket.close()
        root.quit()


root = tk.Tk()
my_msg = tk.StringVar()  # For the messages to be sent.
my_msg.set("Type your messages here.")
root.geometry('300x160')
root.title('Enter your information')
#frame for window margin
parent = tk.Frame(root, padx=10, pady=10)
parent.pack(fill=tk.BOTH, expand=True)
#entrys with not shown text
user = make_entry(parent, "User name:", 16)
password = make_entry(parent, "Password:", 16, show="*")
#button to attempt to login
b = tk.Button(parent, borderwidth=4, text="Login", width=20, pady=8, command=check_password)
b.pack(side=tk.BOTTOM)
password.bind('<Return>', enter)
user.focus_set()
parent.mainloop()


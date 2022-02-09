import socket 
import time
import threading
from tkinter import *
from turtle import width

root = Tk()
root.geometry("400x600")
root.config(bg="white")



def func():
    t = threading.Thread(target=recv)

def recv():
    listensocket = socket.socket()
    port = 3050
    maxconnection = 99
    ip = socket.gethostname()
    print(ip)

    listensocket.bind(('',port))
    listensocket.listen(maxconnection)
    (clientsocket,address)=listensocket.accept()

    while True:
        sendermessage = clientsocket.recv(1024).decode()
        if not sendermessage == "":
            time.sleep(5)
            listbox.insert(0,"client :",sendermessage)

xr = 0

def send():
    global xr
    if xr == 0:
        xr= socket.socket()
        hostname = ""
        port = 4050
        xr.connect((hostname,port))
        msg = messagebox.get()
        listbox.insert(0,"You: "+msg)
        xr.send(msg.encode())
        xr+=1

    else:
        msg = messagebox.get()
        listbox.insert(0,"You: "+msg)
        xr.send(msg.encode)


def threadsending():
    t = threading.Thread(target = send)


startchatimg = PhotoImage(file="send.png",width=230,height=100)
buttons = Button(root, image = startchatimg, command = func,borderwidth=0 )
buttons.place(x=80,y=10)

message = StringVar()
messagebox = Entry(root, textvariable=message,font=('calibre',10,'normal'),border = 2,width=40)
messagebox.place(x=15,y=560)

sendmessageimg = PhotoImage(file="send (1).png")
sendmessagebutton = Button(root,image=sendmessageimg,command=threadsending,borderwidth=0 )
sendmessagebutton.place(x=320,y=540)


listbox = Listbox(root,height=20,width=40)
listbox.place(x=15,y=150)

root.mainloop()

import socket

HEADER = 64            #header size
HOST = "127.0.0.1"     #localhost
PORT = 8080            #port
FORMAT = "utf-8"       #encoding format

name = "Anonymous"


c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST, PORT))

def send(msg):
    msg = msg.encode(FORMAT)
    length = str(len(msg)).encode(FORMAT)
    length += b' ' * (HEADER - len(length))
    c.send(length)
    c.send(msg)
    
def setup():
    global name
    name = input("Enter your name: ")
  
setup()  
while True:
    msg = input()
    msg = name + " > " + msg
    send(msg)
    if (msg == "exit"):
        break
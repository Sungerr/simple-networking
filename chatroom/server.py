import socket
import threading

HEADER = 64            #header size
HOST = "127.0.0.1"     #localhost
# HOST = socket.gethostbyname(socket.gethostname()) #ip address
PORT = 8080            #port
FORMAT = "utf-8"       #encoding format

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

def handle_client(conn, addr):
    print(f"New connection: {addr}")
    while True:
        len = conn.recv(HEADER).decode(FORMAT)
        if len:
            len = int(len)
            data = conn.recv(len).decode(FORMAT)
            
            if (data in "exit"):
                print(f"Connection closed: {addr}")
                conn.close()
                break
            
            print(f"{data}")
            conn.send("Message received".encode(FORMAT))
        
        

def start():
    s.listen()
    print("Server is listening...")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active connections: {threading.active_count() - 1}")

print("Starting server...")
start()

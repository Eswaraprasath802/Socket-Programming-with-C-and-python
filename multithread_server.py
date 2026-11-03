import socket
from threading import Thread 

class TCPServer(Thread):
    def __init__(self, conn, address):
        super().__init__()
        self.conn = conn
        self.address = address

    def run(self):
        print("Client connected:", self.address)
        data = self.conn.recv(1024)
        print("Client says:", data.decode())
        self.conn.sendall(b"Hello Client")
        self.conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen(5)

print("Waiting for clients...")

while True:
    conn, address = server.accept()
    client = TCPServer(conn, address)
    client.start()
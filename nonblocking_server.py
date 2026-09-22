import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))
server.listen(1)

print("1. Server is waiting for a client...")

conn, addr = server.accept()

print("2. Client connected:", addr)

conn.setblocking(False)

print("3. Socket is now NON-BLOCKING")
print("4. Trying to receive data...")

data = conn.recv(1024)

print("5. Data received:", data.decode())

conn.close()
server.close()
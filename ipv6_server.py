import socket

SERVER_IP = "2401:4900:93d0:de5e:fd2a:5c4d:254f:b17b"
PORT = 5000

server = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((SERVER_IP, PORT))

server.listen(5)

print("Server listening...")
print(f"[{SERVER_IP}]:{PORT}")

conn, addr = server.accept()

print("Client connected:", addr)

data = conn.recv(1024)

print("Client:", data.decode())

conn.sendall(b"Hello from IPv6 server")

print("Closing connection...")

conn.close()
server.close()
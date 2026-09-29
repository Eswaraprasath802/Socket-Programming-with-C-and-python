import socket
import time

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 5000))
server.listen(1)

print("Waiting for client...")
conn, addr = server.accept()
print("Connected:", addr)

data = b"ABCDEFGHIJ"

for i in range(0, len(data), 2):
    chunk = data[i:i+2]
    conn.sendall(chunk)
    print("Server sent:", chunk)
    time.sleep(1)

conn.close()
server.close()
import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 5000))

buffer = b""

while True:
    data = sock.recv(2)

    if not data:
        break

    buffer += data

print("Now process:", buffer)

sock.close()
```python
import socket

SERVER_IP = "2401:4900:93d0:de5e:fd2a:5c4d:254f:b17b"
PORT = 5000

# Create IPv6 TCP socket
client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Connect to the IPv6 server
client.connect((SERVER_IP, PORT))

print("Connected to server")

# Send message
client.sendall(b"Hello from IPv6 client")

# Receive response
data = client.recv(1024)

print("Server:", data.decode())

# Close connection
client.close()

print("Connection closed")
```
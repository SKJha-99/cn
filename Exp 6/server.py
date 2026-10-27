import socket

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to an IP address and port
server.bind(("127.0.0.1", 12345))

# Listen for client connections
server.listen(1)
print("Server is waiting for a client...")

# Accept the client connection
conn, addr = server.accept()
print("Connected to:", addr)

# Receive the message from the client
message = conn.recv(1024).decode()
print("Client says:", message)

# Send a reply to the client
conn.send("Hello from Server".encode())

# Close the connection
conn.close()
server.close()

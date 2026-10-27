import socket

# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect(("127.0.0.1", 12345))

# Send a message to the server
client.send("Hello".encode())

# Receive the server's reply
message = client.recv(1024).decode()
print("Server says:", message)

# Close the connection
client.close()

import socket
import os

# Create a UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ("127.0.0.1", 5000)

# Name of the file to send
filename = "sample.txt"

# Send the file name to the server
client.sendto(filename.encode(), server_address)

# Open the file in binary mode
with open(filename, "rb") as file:
    while True:
        # Read file data in blocks
        data = file.read(1024)

        # Stop when the file ends
        if not data:
            break

        # Send the data to the server
        client.sendto(data, server_address)

# Send end-of-file marker
client.sendto(b"EOF", server_address)

print("File sent successfully!")
client.close()
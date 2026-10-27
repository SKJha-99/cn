import socket

# Create a UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the server to an IP address and port
server.bind(("127.0.0.1", 5000))

print("UDP Server is waiting for a file...")

# Receive the file name
filename, client_address = server.recvfrom(1024)
filename = filename.decode()

print("Receiving file:", filename)

# Open a new file to save the received data
with open("received_" + filename, "wb") as file:
    while True:
        # Receive file data
        data, client_address = server.recvfrom(1024)

        # Check for end-of-file marker
        if data == b"EOF":
            break

        # Write received data to the file
        file.write(data)

print("File received successfully!")
server.close()
import socket

# Performs a standard system-level DNS lookup
hostname = 'example.com'
ip_address = socket.gethostbyname(hostname)
print(f"The IP address of {hostname} is {ip_address}")

import socket
import ssl

hostname = 'www.python.org'
# Create default context for client-side security
context = ssl.create_default_context()

# 1. Create a standard TCP connection
with socket.create_connection((hostname, 443)) as sock:
    # 2. Wrap the socket with TLS
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(f"Protocol version: {ssock.version()}")
        # 3. Send/Receive secure data
        ssock.sendall(b"GET / HTTP/1.1\r\nHost: www.python.org\r\n\r\n")
        print(ssock.recv(1024).decode())

import socket
import ssl

# Load server certificate and private key
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

bind_addr = ('localhost', 4443)
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(bind_addr)
server_sock.listen(5)

print(f"Mini TLS Server listening on {bind_addr}...")

while True:
    client_sock, addr = server_sock.accept()
    # Wrap incoming connection with TLS
    secure_conn = context.wrap_socket(client_sock, server_side=True)
    try:
        data = secure_conn.recv(1024)
        print(f"Received secure data: {data.decode()}")
        secure_conn.sendall(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nSecure Hello!")
    finally:
        secure_conn.shutdown(socket.SHUT_RDWR)
        secure_conn.close()

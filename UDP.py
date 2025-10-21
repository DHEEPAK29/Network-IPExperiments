import socket
import time

# PTP standard ports: 319 (Event), 320 (General)
TARGET_IP = "127.0.0.1"
TARGET_PORT = 319 

# 1. Create a UDP socket (AF_INET for IPv4, SOCK_DGRAM for UDP)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # 2. Get high-precision timestamp (T1) in nanoseconds
    t1_ns = time.time_ns()
    
    # 3. Construct packet: PTP timestamps are typically 64-bit integers
    # Here we encode a simple sync message with the timestamp
    message = f"SYNC|{t1_ns}".encode('utf-8')
    
    # 4. Send packet
    sock.sendto(message, (TARGET_IP, TARGET_PORT))
    print(f"Sent T1: {t1_ns} ns to {TARGET_IP}:{TARGET_PORT}")

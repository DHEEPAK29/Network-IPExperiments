import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(("0.0.0.0", 319))
    print("UDP Receiver active on port 319...")
    
    while True:
        # buffer size 1024 bytes
        data, addr = sock.recvfrom(1024)
        # Capture receive timestamp immediately upon arrival
        t2_ns = time.time_ns() 
        
        print(f"Received: {data.decode()} from {addr}")
        print(f"Arrival T2: {t2_ns} ns")

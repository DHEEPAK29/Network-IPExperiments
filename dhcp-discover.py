from scapy.all import *

def handle_dhcp(pkt):
    if DHCP in pkt and pkt[DHCP].options[0][1] == 1:  
        print(f"Discover from {pkt[Ether].src}")
         
        offer_pkt = (
            Ether(src="00:11:22:33:44:55", dst="ff:ff:ff:ff:ff:ff") /
            IP(src="192.168.1.1", dst="255.255.255.255") /
            UDP(sport=67, dport=68) /
            BOOTP(op=2, yiaddr="192.168.1.100", siaddr="192.168.1.1", xid=pkt[BOOTP].xid) /
            DHCP(options=[("message-type", "offer"),
                          ("subnet_mask", "255.255.255.0"),
                          ("router", "192.168.1.1"),
                          ("lease_time", 86400),
                          "end"])
        )
        sendp(offer_pkt, iface="eth0")
 
sniff(filter="udp and port 67", prn=handle_dhcp, iface="eth0")

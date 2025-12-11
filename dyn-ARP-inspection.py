from scapy.all import sniff, ARP

# Mock DHCP Snooping Binding Database (IP: MAC)
# In production, this would be synced from your switch or DHCP server
TRUSTED_BINDINGS = {
    "192.168.1.1": "00:ad:be:ef:01:01",
    "192.168.1.50": "aa:bb:cc:dd:ee:ff",
    "192.168.1.130": "00:11:22:33:44:55"
}

def dai_monitor(pkt):
    if pkt.haslayer(ARP):
        # Extract Sender IP and MAC from the ARP layer
        sender_ip = pkt[ARP].psrc
        sender_mac = pkt[ARP].hwsrc
        
        # Validation Logic
        if sender_ip in TRUSTED_BINDINGS:
            if TRUSTED_BINDINGS[sender_ip] == sender_mac:
                print(f"[OK] Valid ARP from {sender_ip} ({sender_mac})")
            else:
                # This indicates a potential spoofing attempt
                print(f"[ALERT] DAI BLOCK: Spoofed ARP detected!")
                print(f"        IP {sender_ip} is bound to {TRUSTED_BINDINGS[sender_ip]}")
                print(f"        Attacker MAC: {sender_mac}")
        else:
            print(f"[WARN] Unknown IP {sender_ip} attempting ARP. Potential Rogue Host.")

# Sniff ARP packets on the local interface (requires sudo)
print("DAI Simulation Active. Monitoring ARP traffic...")
sniff(filter="arp", prn=dai_monitor, store=0)

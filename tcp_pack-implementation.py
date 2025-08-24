import socket
import struct

def create_tcp_packet(src_ip, dst_ip, src_port, dst_port):
    # --- IP Header ---
    version_ihl = (4 << 4) + 5  # IPv4, 20-byte header
    tos = 0
    tot_len = 40  # 20 (IP) + 20 (TCP)
    id = 54321
    frag_off = 0
    ttl = 255
    proto = socket.IPPROTO_TCP
    check = 0  # Kernel fills this if IP_HDRINCL is used correctly
    saddr = socket.inet_aton(src_ip)
    daddr = socket.inet_aton(dst_ip)
    ip_header = struct.pack('!BBHHHBBH4s4s', version_ihl, tos, tot_len, id, frag_off, ttl, proto, check, saddr, daddr)

    # --- TCP Header ---
    seq = 0
    ack_seq = 0
    doff_res = (5 << 4)  # 20-byte TCP header
    flags = 2  # SYN flag
    window = socket.htons(5840)
    check = 0
    urg_ptr = 0
    tcp_header = struct.pack('!HHLLBBHHH', src_port, dst_port, seq, ack_seq, doff_res, flags, window, check, urg_ptr)

    return ip_header + tcp_header

# Usage: Requires root privileges
# s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
# packet = create_tcp_packet('192.168.1.5', '192.168.1.1', 12345, 80)
# s.sendto(packet, ('192.168.1.1', 0))

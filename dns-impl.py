from dnslib import DNSRecord, QTYPE, RR, A
import socket

def dns_responder(data):
    # 1. Parse the incoming request
    request = DNSRecord.parse(data)
    reply = request.reply()
    qname = request.q.qname
    
    # 2. Match the domain and add an 'A' record
    if str(qname) == "mini.stack.local.":
        reply.add_answer(RR(qname, QTYPE.A, rdata=A("192.168.1.100"), ttl=60))
        print(f"Resolved {qname} to 192.168.1.100")
    
    return reply.pack()

# 3. Start UDP Server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 53)) # Requires sudo/root

print("Miniature DNS Server listening on port 53...")
while True:
    data, addr = sock.recvfrom(512)
    response = dns_responder(data)
    sock.sendto(response, addr)

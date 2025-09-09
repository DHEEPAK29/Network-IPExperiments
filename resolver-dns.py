import dns.resolver

# Query the 'A' record (IPv4 address) for a domain
try:
    result = dns.resolver.resolve('example.com', 'A')
    for ip in result:
        print(f"IP Address: {ip.to_text()}")
except dns.resolver.NXDOMAIN:
    print("Domain does not exist.")

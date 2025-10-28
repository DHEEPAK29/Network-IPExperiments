from pyroute2 import IPRoute

# Initialize IPRoute to interact with the kernel Netlink stack
with IPRoute() as ipr:
    # 1. Define VXLAN parameters
    # VNI (VXLAN Network Identifier): 10
    # Destination port: 4789 (IANA standard)
    # Remote endpoint: 192.168.1.50 (The other VTEP)
    
    try:
        ipr.link("add",
                 ifname="vxlan10",
                 kind="vxlan",
                 vxlan_id=10,
                 vxlan_group="239.1.1.1",  # Multicast group for discovery
                 vxlan_port=4789,
                 vxlan_ttl=16)
        
        # 2. Assign an IP address to the virtual interface
        # Find the index of the newly created interface
        idx = ipr.link_lookup(ifname="vxlan10")[0]
        
        ipr.addr("add", index=idx, address="10.0.0.1", mask=24)
        
        # 3. Bring the interface UP
        ipr.link("set", index=idx, state="up")
        
        print("VXLAN interface 'vxlan10' (VNI 10) is active.")
        
    except Exception as e:
        print(f"Error: {e}")

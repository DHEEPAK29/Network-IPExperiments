from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

# Commands to whitelist a new static device
commands = [
    'arp access-list STATIC_DEVICES',
    'permit ip host 192.168.1.60 mac host aabb.ccdd.eeff',
    'exit',
    'ip arp inspection filter STATIC_DEVICES vlan 10'
]

with ConnectHandler(**device) as net_connect:
    output = net_connect.send_config_set(commands)
    print("Configuration applied successfully.")

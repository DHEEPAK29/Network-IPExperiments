import netmiko
import time

# Define device connection parameters in a dictionary
device = {
    'device_type': 'cisco_ios',
    'ip': 'YOUR_DEVICE_IP',
    'username': 'YOUR_USERNAME',
    'password': 'YOUR_PASSWORD',
}

# Establish the connection
net_connect = netmiko.ConnectHandler(**device)
print(f"Connecting to {device['ip']}")

# Define commands to run
commands = ['show version', 'show ip interface brief']

# Execute commands
for command in commands:
    output = net_connect.send_command(command)
    print(f"\n--- Output for '{command}' ---\n{output}")

# Disconnect
net_connect.disconnect()

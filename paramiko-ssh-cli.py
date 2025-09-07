import paramiko

def run_remote_command(host, user, pwd, cmd):
    client = paramiko.SSHClient()
    # Automatically add unknown host keys (use with caution in production)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        client.connect(hostname=host, username=user, password=pwd)
        stdin, stdout, stderr = client.exec_command(cmd)
        print(stdout.read().decode())
    finally:
        client.close()

# Example usage
run_remote_command('192.168.1.10', 'admin', 'password', 'ls -la')

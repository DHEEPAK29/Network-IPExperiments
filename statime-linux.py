import subprocess

# Start Statime on a specific ethernet interface
process = subprocess.Popen(
    ["sudo", "./statime-linux", "-i", "eth0"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

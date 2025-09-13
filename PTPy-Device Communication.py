from ptpy import PTPy

# Automatically detects connected PTP devices (USB/Serial/IP)
camera = PTPy()

# Fetch device capabilities and current state
print(camera.get_device_info())

# Perform a basic operation within a session
with camera.session():
    camera.initiate_capture()

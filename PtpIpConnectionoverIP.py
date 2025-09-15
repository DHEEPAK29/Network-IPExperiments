from ptpip import PtpIpConnection
from threading import Thread

# Default PTP/IP port is 15740
conn = PtpIpConnection(host='192.168.1.1')
conn.open()

# Run the communication thread to handle background events
comm_thread = Thread(target=conn.communication_thread)
comm_thread.daemon = True
comm_thread.start()

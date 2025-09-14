import time
import socket

# PTP standard ports: 319 (Event), 320 (General)
PTP_EVENT_PORT = 319

def calculate_ptp_sync(t1, t2, t3, t4):
    """
    t1: Master sends Sync (Master time)
    t2: Slave receives Sync (Slave time)
    t3: Slave sends Delay_Req (Slave time)
    t4: Master receives Delay_Req (Master time)
    """
    mean_path_delay = ((t2 - t1) + (t4 - t3)) / 2
    clock_offset = ((t2 - t1) - (t4 - t3)) / 2
    return mean_path_delay, clock_offset
 
t1 = 1700000000000000000  # Sync sent from Master
t2 = 1700000000010000000  # Sync received by Slave
t3 = 1700000000020000000  # Delay_Req sent by Slave
t4 = 1700000000015000000  # Delay_Req received by Master

delay, offset = calculate_ptp_sync(t1, t2, t3, t4)
print(f"Path Delay: {delay} ns | Clock Offset: {offset} ns")

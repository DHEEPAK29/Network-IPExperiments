import asyncio
from aiortc import RTCPeerConnection
import time

async def send_sync_metadata(channel):
    while True:
        # Get nanosecond-precise time from PTP-disciplined system clock
        # CLOCK_REALTIME is preferred when synchronized by phc2sys
        ptp_time_ns = time.clock_gettime_ns(time.CLOCK_REALTIME)
        
        # Send precise timestamp via WebRTC DataChannel
        channel.send(str(ptp_time_ns))
        await asyncio.sleep(0.01) # 100Hz sync updates

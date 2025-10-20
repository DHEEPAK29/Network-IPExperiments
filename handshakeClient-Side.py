import asyncio
import aiohttp
from aiortc import RTCPeerConnection, RTCSessionDescription

async def run_client():
    # 1. Initialize Peer Connection
    pc = RTCPeerConnection()
    
    # Optional: Create a data channel for PTP-synchronized metadata
    channel = pc.createDataChannel("chat")

    # 2. & 3. Generate Offer and Set as Local Description
    offer = await pc.createOffer()
    await pc.setLocalDescription(offer)

    # 4. Signaling: Send Offer to Server
    async with aiohttp.ClientSession() as session:
        payload = {
            "sdp": pc.localDescription.sdp,
            "type": pc.localDescription.type
        }
        async with session.post("http://localhost:8080/offer", json=payload) as response:
            answer_data = await response.json()

            # 5. Receive Answer and Set as Remote Description
            answer = RTCSessionDescription(
                sdp=answer_data["sdp"], 
                type=answer_data["type"]
            )
            await pc.setRemoteDescription(answer)

    print("Handshake complete. P2P connection established.")
    
    # Keep the connection alive
    await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(run_client())

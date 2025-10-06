import asyncio
import aioipfs

async def upload_to_ipfs():
    # Connect to a local Kubo daemon (default port 5001)
    async with aioipfs.AsyncIPFS(host='127.0.0.1', port=5001) as client:
        # Add a file and retrieve its Content Identifier (CID)
        file_cid = await client.add('precision_data.json')
        print(f"File uploaded. CID: {file_cid['Hash']}")
        
        # Pin the content to ensure it remains on the local node
        await client.pin.add(file_cid['Hash'])

asyncio.run(upload_to_ipfs())

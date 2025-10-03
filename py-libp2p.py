import asyncio
from libp2p import new_host

async def main():
    # Create a new libp2p host with default transports (TCP)
    host = new_host()
    print(f"Node started with ID: {host.get_id().to_base58()}")

    # Keep the node running
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())

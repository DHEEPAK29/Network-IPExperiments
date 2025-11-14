import asyncio
from aioquic.quic.configuration import QuicConfiguration
from aioquic.asyncio import connect

async def run_tsq_client():
    # Define custom ALPN for Time Synchronization over QUIC
    # RFC standard for TSQ uses the "tsq" identifier
    configuration = QuicConfiguration(
        is_client=True, 
        alpn_protocols=["tsq"] 
    )

    async with connect("tsq-server.example", 443, configuration=configuration) as protocol:
        # After handshake, check which ALPN was selected
        selected_protocol = protocol._quic.tls.alpn_protocol
        print(f"Handshake successful. Selected ALPN: {selected_protocol}")

from aioquic.quic.configuration import QuicConfiguration
from aioquic.asyncio import connect

async def tsq_sync(host):
    # TSQ leverages QUIC's inherent TLS 1.3 security
    config = QuicConfiguration(is_client=True, alpn_protocols=["tsq"])
    async with connect(host, 443, configuration=config) as client:
        # Time requests are sent over encrypted QUIC streams or datagrams
        pass

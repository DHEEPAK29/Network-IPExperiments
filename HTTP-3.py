import asyncio
from aioquic.asyncio import serve
from aioquic.quic.configuration import QuicConfiguration
from aioquic.h3.connection import H3_ALPN  # Required for protocol negotiation

# 1. Configure QUIC with TLS 1.3 (Self-signed certs work for dev)
configuration = QuicConfiguration(
    is_client=False,
    alpn_protocols=H3_ALPN,  # Standard tokens for HTTP/3
)
configuration.load_cert_chain("cert.pem", "key.pem")

# 2. Start the UDP server (Listening on port 4433)
async def main():
    await serve(
        "::", 4433, 
        configuration=configuration, 
        create_protocol=HttpServerProtocol # Subclass handling H3 events
    )
    await asyncio.Future() # Keep server running

# asyncio.run(main())

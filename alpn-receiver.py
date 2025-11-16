from aioquic.asyncio import serve, QuicConnectionProtocol

class TsqServerProtocol(QuicConnectionProtocol):
    def quic_event_received(self, event):
        # Handle protocol-specific logic here based on established ALPN
        pass

async def run_tsq_server():
    configuration = QuicConfiguration(
        is_client=False, 
        alpn_protocols=["tsq", "h3"] # Supports multiple protocols
    )
    # Load required TLS certificates for QUIC
    configuration.load_cert_chain("cert.pem", "key.pem")

    await serve("::", 443, configuration=configuration, create_protocol=TsqServerProtocol)

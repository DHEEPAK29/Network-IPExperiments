import asyncio
from aioquic.asyncio import serve
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import StreamDataReceived, ConnectionTerminated

class EchoQuicProtocol:
    """
    Simple protocol that echoes data back to client.
    """

    def __init__(self, connection):
        self.connection = connection

    def quic_event_received(self, event):
        if isinstance(event, StreamDataReceived):
            self.connection.send_stream_data(
                stream_id=event.stream_id, 
                data=event.data, 
                end_stream=False
            )

        elif isinstance(event, ConnectionTerminated):
            print("Connection closed")

async def handle_client_connection(connection):
    """
    Called when a new connection is created.
    """
    protocol = EchoQuicProtocol(connection)
    while True:
        event = await connection.wait_for_event()
        if event is None:
            break
        protocol.quic_event_received(event)

async def main():
    configuration = QuicConfiguration(
        is_client=False,
        alpn_protocols=["hq-29"],  # or "h3" prefer HTTP/3
    )

    # QUIC server on UDP port 4433
    await serve(
        host="0.0.0.0",
        port=4433,
        configuration=configuration,
        create_protocol=handle_client_connection,
    )

if __name__ == "__main__":
    asyncio.run(main())

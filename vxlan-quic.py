from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.connection import QuicConnection

# 2026 Pattern: Sending VXLAN encapsulated data via QUIC Datagrams
def send_vxlan_frame(quic_connection, ethernet_frame):
    # RFC 9221: QUIC Datagrams for unreliable/low-latency transport
    quic_connection.send_datagram_frame(ethernet_frame)

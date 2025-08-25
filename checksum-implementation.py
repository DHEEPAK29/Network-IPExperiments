import array

def checksum(data: bytes) -> int:
    # 1. Padding: ensure data is even length
    if len(data) % 2 != 0:
        data += b'\x00'
    
    # 2. Summing: Use "H" for unsigned short (16-bit)
    # array.array("H", data) interprets bytes as 16-bit words
    # On most machines, this will use little-endian; network order is big-endian.
    # To fix this consistently, we sum manually or use htons() logic.
    words = array.array("H", data)
    s = sum(words)
    
    # 3. Handle Overflow (End-around carry)
    # Fold 32-bit sum into 16 bits
    while (s >> 16):
        s = (s & 0xFFFF) + (s >> 16)
    
    # 4. Bitwise NOT (One's Complement)
    return ~s & 0xFFFF

# Usage Example:
# header = b'\x45\x00\x00\x3c\x1c\x46\x40\x00\x40\x06\x00\x00\xac\x10\x0a\x63\xac\x10\x0a\x0c'
# print(hex(checksum(header)))

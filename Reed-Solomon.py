from reedsolo import RSCodec

# Initialize with 10 bytes of Error Correction Code (ECC)
# This allows correcting up to 5 byte-level errors (ECC/2)
rs = RSCodec(10)

# 1. Encoding
message = b"hello world"
encoded = rs.encode(message)
print(f"Encoded: {encoded}")

# 2. Corrupting (Simulate data loss/noise)
# Change the first two characters to illustrate recovery
corrupted = bytearray(encoded)
corrupted[0] = 0
corrupted[1] = 0

# 3. Decoding (Automatic correction)
decoded = rs.decode(corrupted)[0]
print(f"Decoded: {decoded.decode()}") # Output: hello world

import reedsolo

# Initialize Reed-Solomon object with default parameters (RS(255, 223))
# 255 symbols total, 223 data symbols, 32 parity symbols
rs = reedsolo.RSCodec(32)

# Sample data to encode (must be bytes)
data = b"Hello from Reed-Solomon!"

# Encode the data
encoded_data = rs.encode(data)
print("Encoded Data:", encoded_data)

# Introduce some errors (manually flip some bytes)
corrupted = bytearray(encoded_data)
corrupted[5] = 99
corrupted[10] = 88
corrupted[15] = 77

print("Corrupted Data:", corrupted)

# Decode and correct the errors
decoded_data = rs.decode(corrupted)
print("Decoded Data:", decoded_data)

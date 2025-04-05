# Hamming Code

def calculate_parity_bits(data):
    # data = [d3 d2 d1 d0]
    d = [int(b) for b in data]
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p3 = d[1] ^ d[2] ^ d[3]
    return [p1, p2, d[0], p3, d[1], d[2], d[3]]  # [p1 p2 d0 p3 d1 d2 d3]

def detect_and_correct(codeword):
    c = [int(b) for b in codeword]
    p1 = c[0] ^ c[2] ^ c[4] ^ c[6]
    p2 = c[1] ^ c[2] ^ c[5] ^ c[6]
    p3 = c[3] ^ c[4] ^ c[5] ^ c[6]
    error_position = p1 + (p2 << 1) + (p3 << 2)

    if error_position != 0:
        print(f"Error detected at position: {error_position}")
        c[error_position - 1] ^= 1  # Correct the bit
    else:
        print("No error detected.")
    
    # Extract the original 4-bit data
    return [c[2], c[4], c[5], c[6]]

data = "1011"
encoded = calculate_parity_bits(data)
print("Encoded Hamming(7,4) Code:", encoded)

# Introduce an error at position 5 (1-based index)
received = encoded.copy()
received[4] ^= 1
print("Received Codeword with Error:", received)

corrected_data = detect_and_correct(received)
print("Corrected Data:", corrected_data)


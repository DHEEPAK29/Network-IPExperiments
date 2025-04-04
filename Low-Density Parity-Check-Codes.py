import numpy as np
import pyldpc

# code parameters
n = 20  # Length of the codeword
d_v = 2  # Number of ones per column (variable node degree)
d_c = 4  # Number of ones per row (check node degree)

# LDPC matrices
H, G = pyldpc.make_ldpc(n, d_v, d_c, systematic=True, sparse=True)

# random binary message
k = G.shape[1]
message = np.random.randint(0, 2, k)
print("Original Message:", message)

# Encode the message
codeword = pyldpc.encode(G, message, snr=10)
print("Encoded Codeword:", codeword)

# Simulate a noisy channel (add Gaussian noise)
snr = 5
received = pyldpc.channel(codeword, snr)

# Decode the received codeword
decoded = pyldpc.decode(H, received, snr)
print("Decoded Message:", decoded)

# Check if decoding was successful
print("Successful decoding?", np.array_equal(message, decoded))

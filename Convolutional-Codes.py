import numpy as np
from commpy.channelcoding import conv_encode, viterbi_decode
from commpy.channelcoding.convcode import Trellis

# simple rate 1/2 convolutional code
memory = np.array([2])  # Constraint length - 2
g_matrix = np.array([[0b111, 0b101]])  # Generator polynomials in binary

# Create trellis for encoder
trellis = Trellis(memory, g_matrix)

# Input message
message = np.array([1, 0, 1, 1, 0, 1, 0, 0])

# Encode the message
encoded = conv_encode(message, trellis)
print("Encoded message:", encoded)

# Introduce an error (simulate transmission)
received = encoded.copy()
received[3] ^= 1  # Flip one bit

# Decode the received message using Viterbi algorithm
decoded = viterbi_decode(received, trellis, tb_depth=5)
print("Decoded message:", decoded)

# Check correctness
print("Success?", np.array_equal(message, decoded[:len(message)]))

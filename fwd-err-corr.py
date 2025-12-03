from zfec.easyfec import Encoder, Decoder

# k = min blocks needed for recovery, n = total blocks generated
k, n = 3, 5
enc = Encoder(k, n)
dec = Decoder(k, n)

# Data must be a multiple of 'k' bytes (or padded)
data = b"HELLOWORLD!!" # 12 bytes / 3 = 4 bytes per block

# Encode into 5 blocks
blocks = enc.encode(data)

# Simulate losing any 2 blocks (keeping only 3)
partial_blocks = [blocks[0], blocks[2], blocks[4]]
block_nums = [0, 2, 4]

# Recover original data from partial set
recovered = dec.decode(partial_blocks, block_nums)
print(f"Recovered: {recovered}")

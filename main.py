from huffman.frequency import count_frequencies
from huffman.tree import build_huffman_tree
from huffman.codes import generate_codes
from huffman.encoder import write_header, encode_text
from huffman.decoder import read_header, decode_file
import os

input_file = "input.txt"
encoded_file = "encoded.huff"
decoded_file = "decoded.txt"

freq_table, text = count_frequencies(input_file)

# Step 2: Build Huffman Tree
root = build_huffman_tree(freq_table)

# Step 3: Generate Prefix Code Table
code_table = generate_codes(root)

# Step 4: Write Header
write_header(encoded_file, freq_table)

# Step 5: Encode Text
encode_text(encoded_file, text, code_table)

# Step 6: Read Header and Decode File
freq_table = read_header(encoded_file)
decode_file(encoded_file, decoded_file, freq_table)

print(f"Original file size: {len(text)} bytes")
print(f"Encoded file size: {os.path.getsize(encoded_file)} bytes")
print(f"Decoded file matches input: {open(input_file).read() == open(decoded_file).read()}")

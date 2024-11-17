def write_header(output_file, freq_table):
    with open(output_file, 'wb') as file:
        header = str(freq_table).encode()
        file.write(header)
        file.write(b'\n')


def encode_text(output_file, text, code_table):
    with open(output_file, 'ab') as file:
        encoded_bits = ''.join(code_table[char] for char in text)

        padded_encoded_bits = encoded_bits + '0' * ((8 - len(encoded_bits) % 8) % 8)
        byte_array = bytearray(int(padded_encoded_bits[i:i+8], 2) for i in range(0, len(padded_encoded_bits), 8))

        file.write(bytes(byte_array))

from huffman.tree import build_huffman_tree

def read_header(encoded_file):
    with open(encoded_file, 'rb') as file:
        header = file.readline().strip()
        freq_table = eval(header.decode())
    return freq_table


def decode_file(encoded_file, output_file, freq_table):
    root = build_huffman_tree(freq_table)

    with open(encoded_file, 'rb') as file:
        _ = file.readline()
        content = file.read()

    bit_string = ''.join(f"{byte:08b}" for byte in content)

    decoded_text = []
    current = root
    for bit in bit_string:
        current = current.left if bit == '0' else current.right
        if current.is_leaf():
            decoded_text.append(current.char)
            current = root


    with open(output_file, 'w') as file:
        file.write(''.join(decoded_text))

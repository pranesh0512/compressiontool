import unittest
from huffman.frequency import count_frequencies
from huffman.tree import build_huffman_tree
from huffman.codes import generate_codes
from huffman.encoder import write_header, encode_text
from huffman.decoder import read_header, decode_file

class TestHuffmanCoding(unittest.TestCase):
    def test_count_frequencies(self):

        text = "hello"
        expected = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        with open("test_input.txt", "w") as f:
            f.write(text)

        freq_table, _ = count_frequencies("test_input.txt")
        self.assertEqual(freq_table, expected)

    def test_build_huffman_tree(self):

        freq_table = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        root = build_huffman_tree(freq_table)

        # Check root properties
        self.assertEqual(root.freq, 5)
        self.assertIsNone(root.char)
        self.assertIsNotNone(root.left)
        self.assertIsNotNone(root.right)

    def test_generate_codes(self):
        """Test prefix code generation."""
        freq_table = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        root = build_huffman_tree(freq_table)
        code_table = generate_codes(root)

        # Validate the prefix codes
        self.assertEqual(len(code_table), len(freq_table))
        self.assertTrue(all(isinstance(code, str) for code in code_table.values()))

    def test_encode_text(self):
        """Test text encoding."""
        freq_table = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        root = build_huffman_tree(freq_table)
        code_table = generate_codes(root)

        text = "hello"
        encoded_bits = ''.join(code_table[char] for char in text)

        self.assertGreater(len(encoded_bits), 0)
        self.assertTrue(all(bit in "01" for bit in encoded_bits))  # Only 0s and 1s

    def test_decode_file(self):
        text = "hello"
        freq_table = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        root = build_huffman_tree(freq_table)
        code_table = generate_codes(root)

        # Encode
        encoded_bits = ''.join(code_table[char] for char in text)
        padded_encoded_bits = encoded_bits + '0' * ((8 - len(encoded_bits) % 8) % 8)
        byte_array = bytearray(int(padded_encoded_bits[i:i+8], 2) for i in range(0, len(padded_encoded_bits), 8))

        # Decode
        bit_string = ''.join(f"{byte:08b}" for byte in byte_array)
        decoded_text = []
        current = root
        for bit in bit_string:
            current = current.left if bit == '0' else current.right
            if current.is_leaf():
                decoded_text.append(current.char)
                current = root

        decoded_text = ''.join(decoded_text)

        # Validate
        self.assertEqual(decoded_text.strip(), text)

    def test_integration(self):

        input_text = "this is a test"
        with open("test_input.txt", "w") as f:
            f.write(input_text)

        # Perform steps
        freq_table, text = count_frequencies("test_input.txt")
        root = build_huffman_tree(freq_table)
        code_table = generate_codes(root)


        encoded_file = "test_encoded.huff"
        write_header(encoded_file, freq_table)
        encode_text(encoded_file, text, code_table)

        freq_table = read_header(encoded_file)
        decode_file(encoded_file, "test_output.txt", freq_table)
        with open("test_output.txt", "r") as f:
            decoded_text = f.read()

        self.assertEqual(input_text, decoded_text)

if __name__ == "__main__":
    unittest.main()

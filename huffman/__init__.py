class HuffmanFileError(Exception):
    def __init__(self, message):
        super().__init__(message)


def count_frequencies(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        raise HuffmanFileError("Error: File not found")
    except Exception as e:
        raise HuffmanFileError(f"Error reading the file: {e}")

    freq_table = {}
    for char in text:
        freq_table[char] = freq_table.get(char, 0) + 1

    return freq_table, text



class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.left is None and self.right is None


def build_huffman_tree(freq_table):

    nodes = [Node(char, freq) for char, freq in freq_table.items()]

    # Build the tree
    while len(nodes) > 1:

        nodes.sort(key=lambda x: x.freq)

        left = nodes.pop(0)
        right = nodes.pop(0)

        combined_freq = left.freq + right.freq
        new_node = Node(None, combined_freq, left, right)

        nodes.append(new_node)

    return nodes[0]




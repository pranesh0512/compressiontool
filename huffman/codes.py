def generate_codes(node, prefix="", code_table=None):
    if code_table is None:
        code_table = {}

    if node.is_leaf():
        code_table[node.char] = prefix
    else:
        generate_codes(node.left, prefix + "0", code_table)
        generate_codes(node.right, prefix + "1", code_table)

    return code_table

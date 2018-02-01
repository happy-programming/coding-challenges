"""
https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

class Node:
    def __init__(self,  data, freq):
        self.data = data
        self.freq = freq
        self.left = None
        self.right = None


# Test Case

root = Node('$', 5)
root.left = Node('$', 2)
root.right = Node('A', 3)
root.left.left = Node('B', 1)
root.left.right = Node('C', 1)

decodeHuff(root, '1001011')

"""

# Recursion


def get_path(code_decoder, node, path_string):
    if is_leaf(node):  # you can also check if node.data == '\0' in this case
        code_decoder[path_string] = node.data
        return
    else:
        if node.left is not None:
            get_path(code_decoder, node.left, path_string + '0')
        if node.right is not None:
            get_path(code_decoder, node.right, path_string + '1')


def is_leaf(node):
    if node.left is None and node.right is None:
        return True
    else:
        return False


def decoder(code_decoder, input_string):
    x = 0
    decoded_chars = []
    while x < len(input_string):
        y = 1
        while x + y <= len(input_string):
            if str(input_string[x:x + y]) in code_decoder.iterkeys():
                decoded_chars.append(code_decoder[str(input_string[x:x + y])])
                x = x + y
                break
            else:
                y += 1

    decoded_string = ''.join(decoded_chars)
    return decoded_string


def decodeHuff(root, s):
    if root is None:
        return 'Error. Root can not be null'

    code_decoder = {}
    get_path(code_decoder, node=root, path_string='')

    print decoder(code_decoder, s)





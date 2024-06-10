import heapq
from collections import Counter, defaultdict

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(s):
    freq = Counter(s)
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(freq=node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    return heap[0]

def build_huffman_codes(node, prefix="", huffman_code={}):
    if node:
        if node.char:
            huffman_code[node.char] = prefix
        build_huffman_codes(node.left, prefix + "0", huffman_code)
        build_huffman_codes(node.right, prefix + "1", huffman_code)
    return huffman_code

def huffman_encoding(s):
    root = build_huffman_tree(s)
    huffman_code = build_huffman_codes(root)
    encoded_string = ''.join(huffman_code[char] for char in s)
    return encoded_string, huffman_code

s = "this is an example for huffman encoding"
encoded_string, huffman_code = huffman_encoding(s)
print(f"Encoded string: {encoded_string}")
print(f"Huffman codes: {huffman_code}")

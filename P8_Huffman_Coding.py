import heapq
from collections import defaultdict
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.freq < other.freq
def build_frequency_dict(data):
    freq_dict = defaultdict(int)
    for char in data:
        freq_dict[char] += 1
    return freq_dict
def build_priority_queue(freq_dict):
    pq = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(pq)
    return pq
def build_huffman_tree(pq):
    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        merged_node = Node(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(pq, merged_node)
    return pq[0]

def build_huffman_codes(node, code="", codes={}):
    if node is not None:
        if node.char is not None:
            codes[node.char] = code
        build_huffman_codes(node.left, code + "0", codes)
        build_huffman_codes(node.right, code + "1", codes)
    return codes
def huffman_compress(data):
    freq_dict = build_frequency_dict(data)
    pq = build_priority_queue(freq_dict)
    huffman_tree = build_huffman_tree(pq)
    huffman_codes = build_huffman_codes(huffman_tree)
    compressed_data = ""
    for char in data:
        compressed_data += huffman_codes[char]
    return compressed_data, huffman_codes
def huffman_decompress(compressed_data, huffman_codes):
    reversed_codes = {code: char for char, code in huffman_codes.items()}
    decompressed_data = ""
    current_code = ""
    for bit in compressed_data:
        current_code += bit
        if current_code in reversed_codes:
            decompressed_data += reversed_codes[current_code]
            current_code = ""
    return decompressed_data
# Example Usage:
data = "abracadabra"
compressed_data, huffman_codes = huffman_compress(data)
print("Original Data:", data)
print("Compressed Data:", compressed_data)
print("Huffman Codes:", huffman_codes)
decompressed_data = huffman_decompress(compressed_data, huffman_codes)
print("Decompressed Data:", decompressed_data)

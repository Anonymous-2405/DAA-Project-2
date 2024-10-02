import heapq
import random
from time import time_ns

class Node:
    def __init__(self, symbol=None, frequency=0):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def create_huffman_tree(symbol_frequency):
    heap = [Node(symbol, freq) for symbol, freq in symbol_frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged_node = Node(frequency=left.frequency + right.frequency)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(heap, merged_node)

    return heap[0]

def generate_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}
    if node is not None:
        if node.symbol is not None:
            codes[node.symbol] = current_code
        generate_codes(node.left, current_code + "0", codes)
        generate_codes(node.right, current_code + "1", codes)
    return codes

def huffman_encoding(symbol_frequency):
    root = create_huffman_tree(symbol_frequency)
    return generate_codes(root)

def main():
    input_sizes = [999, 1000, 9999, 10000, 99999, 100000, 999999, 1000000]
    
    for n in input_sizes:
        symbols = [chr(i) for i in range(n)]
        symbol_frequency = {symbol: random.randint(1, 1000) for symbol in symbols}
        
        start_time = time_ns()
        huffman_codes = huffman_encoding(symbol_frequency)
        end_time = time_ns()
        
        total_time_taken = end_time - start_time
        print(f"\nNumber of Symbols (n): {n}")
        print(f"Time taken: {total_time_taken} nanoseconds")

if __name__ == "__main__":
    main()

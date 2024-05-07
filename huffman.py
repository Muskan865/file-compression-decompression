from helper_functions import *

def build_huffman_tree(chars, freqs):
    # Create an empty min heap
    min_heap = []
    # Push each character and its frequency into the min heap
    for i in range(len(chars)):
        heappush(min_heap, (freqs[i], chars[i]))

    print("min heap1: ", min_heap)

    # Build the Huffman tree by combining nodes with the smallest frequencies
    while len(min_heap) > 1:
        node1 = heappop(min_heap)  # Pop the node with the smallest frequency
        node2 = heappop(min_heap)  # Pop the next node with the smallest frequency
        merged_freq = node1[0] + node2[0]  # Combine the frequencies of the two nodes
        merged_node = (merged_freq, '', node1, node2)  # Create a new node with the combined frequency and the two nodes as children
        heappush(min_heap, merged_node)  # Push the new node back into the min heap

    print("min heap1: ", min_heap)
    # Return the root of the Huffman tree
    return heappop(min_heap)


def compress_text(text, root):
    # Generate Huffman codes for each character in the tree
    codes = {}
    generate_codes(root, "", codes)

    # Compress the input text using the generated codes
    compressed_text = ""
    for char in text:
        compressed_text += codes[char]
    return compressed_text


def generate_codes(node, code, codes):
    # Recursively generate Huffman codes for each character in the tree
    if len(node) < 2:
        return
    if node[1]:
        codes[node[1]] = code
    if len(node) > 2 and node[2]:   # node has a left child 
        generate_codes(node[2], code + "0", codes)
    if len(node) > 3 and node[3]:   # node has a right child 
        generate_codes(node[3], code + "1", codes)


def decompress_text(compressed_text, root):
    # Decompress the input text using the Huffman tree
    decompressed_text = ""
    current_node = root
    for bit in compressed_text:
        if bit == "0":
            if current_node[2] is not None:  # Check if left child exists
                current_node = current_node[2]
                
        elif bit == "1":
            if current_node[3] is not None:  # Check if right child exists
                current_node = current_node[3]
                
        if len(current_node) == 2:  # Check if current node is a leaf
            decompressed_text += current_node[1]  # Append character to decompressed text
            current_node = root  # Reset current node to the root for next iteration
            
    return decompressed_text


def print_huffman_codes(node, code):
    # Recursively print the Huffman codes for each character in the tree
    if len(node) < 2:
        return
    if node[1]:
        print(f"Character: {node[1]}, Code: {code}")
    if len(node) > 2 and node[2]:
        print_huffman_codes(node[2], code + "0")
    if len(node) > 3 and node[3]:
        print_huffman_codes(node[3], code + "1")
        
def main():
    # Read input text file
    try:
        with open("sample.txt", "r") as input_file:
            text = input_file.read()
    except FileNotFoundError:
        # print("File not found")
        exit(1)

    # Count frequencies of characters
    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1
    sorted_dict = dict(sorted(char_freq.items(), key=lambda x: x[1]))

    # Build Huffman tree
    chars = list(sorted_dict.keys())
    freqs = list(sorted_dict.values())
    root = build_huffman_tree(chars, freqs)

    # Should print character frequencies
    print("Character Frequencies:")
    for char, freq in char_freq.items():
        print(f"Character: {char}, Frequency: {freq}")

    # Should print Huffman codes
    print("\nHuffman Codes:")
    print_huffman_codes(root, "")

    # Compress the text
    compressed_text = compress_text(text, root)
    print(f"\nCompressed Text: {compressed_text}")

    # Write compressed text to a file
    try:
        with open("compressed_file.txt", "w") as compressed_file:
            compressed_file.write(compressed_text)
    except IOError:
        print("Error writing compressed text to file")
        exit(1)

    # Read compressed text from file
    try:
        with open("compressed_file.txt", "r") as compressed_file:
            compressed_text = compressed_file.read()
    except FileNotFoundError:
        print("Compressed file not found")
        exit(1)

    # Decompress the text using the original Huffman tree
    decompressed_text = decompress_text(compressed_text, root)
    print(f"\nDecompressed Text: {decompressed_text}")

    # Write decompressed text to a file
    try:
        with open("decompressed_file.txt", "w") as decompressed_file:
            decompressed_file.write(decompressed_text)
    except IOError:
        print("Error writing decompressed text to file")
        exit(1)

    
if __name__ == "__main__":
    main()

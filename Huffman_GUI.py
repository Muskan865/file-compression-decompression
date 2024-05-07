import tkinter as tk
from tkinter import filedialog, messagebox
from huffman import*
import graphviz

#########-------------------------------COMPRESSION--------------------------------------------##########
#This function opens a dialogue box that ask to select the file and when the file is selected, it updates the entry path file with the file.
def select_file():
    file_path = filedialog.askopenfilename(title="Select Text File") #opens the dialogue box
    if file_path: #checks if the file is non empty.
        entry_file_path.delete(0, tk.END) #Deletes any previous content.
        entry_file_path.insert(tk.END, file_path) #Insert the new file (path)

#This function compresses the selected file and show error if no file is selected.
def compress_file():
    file_path = entry_file_path.get() #Retrieves the file path or get content of the file path.
    if not file_path: #checks if file is empty.
        messagebox.showerror("Error", "Please select a file.") #if file is empty then the message box will appear this message.
        return

    try: #Normal input read. i.e. Will start reading the input if appropriate file is given.
        with open(file_path, "r") as input_file:
            text = input_file.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.") #If the written file is not found then raise this message
        return

    
    #Starts compressing the file.
    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1
    sorted_dict = dict(sorted(char_freq.items(), key=lambda x: x[1]))

    chars = list(sorted_dict.keys()) #make a list of characters.
    freqs = list(sorted_dict.values()) #make a list of frequencies.
    global root_1
    root_1 = build_huffman_tree(chars, freqs) #Builds a binary tree through which the encoding will be done.

    compressed_text = compress_text(text, root_1) #Compresses text by generating teh codes.

    save_path = filedialog.asksaveasfilename(title="Save Compressed File", defaultextension=".txt") #Creates a file dialogue window which will ask the location to save the compressed file.
    if save_path: #Checks if safe path is not emoty i.e. the user has chooses a location to save the file.
        try:
            with open(save_path, "w") as compressed_file: #A file will be created in which the compressed text will be written.
                compressed_file.write(compressed_text) #Writes the compressed text in compressed file.
            messagebox.showinfo("Success", "File compressed and saved successfully.") #After writing the compressed text in the file it will give this message.
        except IOError:
            messagebox.showerror("Error", "Error writing compressed text to file.") #Give error whenever there are issues with the upper block. i.e. File corruption, memory issue, file directory issue and etc.


# Create main window
root = tk.Tk() #Creates the main window.
root.title("Huffman Coding- Compression") #Give the title as "Huffman Coding"

# Create widgets
label_file_path = tk.Label(root, text="Select File:") #Label is associated with main window which will be in the main window and ask to select the file that is to be compressed.
label_file_path.grid(row=0, column=0, padx=5, pady=5) #These give the position in which this label should be. x and y, row and column; padx and pady creates a box or pad arounf the text so it look prominent.

entry_file_path = tk.Entry(root, width=50) #Creates a rectangle in which the file path will be written, it will display characters horizontally.
entry_file_path.grid(row=0, column=1, padx=5, pady=5)

button_browse = tk.Button(root, text="Browse", command=select_file) #This is the button that will allow user to search in its computer.
button_browse.grid(row=0, column=2, padx=5, pady=5)

button_compress = tk.Button(root, text="Compress", command=compress_file)#This button will start compressing the file whenever hit.
button_compress.grid(row=1, column=1, padx=5, pady=5)

# Run the main event loop
root.mainloop() #Starts the complete process.


########------------------------------TREE VISUALIZATION---------------------------------------##########
from tkinter import scrolledtext
#Show huffman tree
class HuffmanTreeVisualizer:
    def __init__(self, master): #Initialize the newly created object.
        self.master = master #Allows the class instance to acess the master widget (e.g the root window) throughout its method.
        master.title("Huffman Tree Visualization") #Set the title to "Huffman Tree Visualizer" of master widget.

        self.text_area = scrolledtext.ScrolledText(master, width=40, height=20) #Creates a multi line widget that can be scrolled.
        self.text_area.pack() #Packs the scrolled text widget into the master widget.

    def append_text(self, text): #This method is to append the text in Scrolled Text widget.
        self.text_area.insert(tk.END, text) #Appends the provided text in Scorlled text widget at the end of the current content.
        self.text_area.insert(tk.END, "\n") #adds a new line character.
        self.text_area.see(tk.END)  # Scroll to the end

def visualize_huffman_tree(root, visualizer): #Root= root node of the huffman tree, visualizer: "append text" object for text based visualization.
    dot = graphviz.Digraph() #Diagraph: makes a directed graph to visualize the huffman tree.
    visualize_huffman_tree_helper(root, dot) #recursive call to form a tree starting from node to edges.
    dot.render('huffman_tree', format='png', cleanup=True) #makes an image in which graph will be given, cleanup=True: Temporary files will be deleted after the use.
    visualizer.append_text("Huffman Tree Visualization:") #Append the given text in visualizer by append method.
    visualizer.append_text("Check the 'huffman_tree.png' file for the visualization.") #Same as above line.

def visualize_huffman_tree_helper(node, dot): #node: the current node that is to be traversed, dot: The diagraph object to represemt tree.
    if node[1]:  # If it's a leaf node
        dot.node(str(id(node)), str(node[1])) #it will add an object representing leaf node, id will give 0s and 1s that will be labeled and node[1] is character.
    else: #if not a leaf node.
        dot.node(str(id(node)), '')
        if node[2]:  # Left child
            visualize_huffman_tree_helper(node[2], dot) #recursive call to add node and label to the visual tree.
            dot.edge(str(id(node)), str(id(node[2])), label="0") #adds an edge from current node to left child labeling it as 0.
        if node[3]:  # Right child
            visualize_huffman_tree_helper(node[3], dot) #recursive call to add node and label to the visual tree.
            dot.edge(str(id(node)), str(id(node[3])), label="1")#adds an edge from current node to right child labeling it as 1.

def main():
    root = tk.Tk() #creates the main window.
    visualizer = HuffmanTreeVisualizer(root) #gives the root window to the class to work on this window.
    
    # Read input text file
    try:
        with open("sample.txt", "r") as input_file:
            text = input_file.read()
    except FileNotFoundError:
        visualizer.append_text("File not found") #Visualizer states that File not Found by append text method.
        return

    char_freq = {}
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1
    sorted_dict = dict(sorted(char_freq.items(), key=lambda x: x[1]))

    chars = list(sorted_dict.keys()) #make a list of characters.
    freqs = list(sorted_dict.values()) #make a list of frequencies.
    root_node = build_huffman_tree(chars, freqs) #Builds a binary tree through which the encoding will be done.

    # Visualize Huffman tree
    visualize_huffman_tree(root_node, visualizer) #calls the function giving it a proper window in which huffman tree would be visualized.

    root.mainloop()

if __name__ == "__main__":
    main()


#####------------------------------------DECOMPRESSION----------------------------------------------#####
#visualize the exact same work as compression, just performs decompression.
def select_file():
    file_path = filedialog.askopenfilename(title="Select Text File")
    if file_path:
        entry_file_path.delete(0, tk.END)
        entry_file_path.insert(tk.END, file_path)

def decompress_file():
    file_path = entry_file_path.get()
    if not file_path:
        messagebox.showerror("Error", "Please select a file.")
        return

    try:
        with open(file_path, "r") as input_file:
            compressed_text = input_file.read()
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
        return

    decompressed_text = decompress_text(compressed_text, root_1)


    save_path = filedialog.asksaveasfilename(title="Save Decompressed File", defaultextension=".txt")
    if save_path:
        try:
            with open(save_path, "w") as decompressed_file:
                decompressed_file.write(decompressed_text)
            messagebox.showinfo("Success", "File decompressed and saved successfully.")
        except IOError:
            messagebox.showerror("Error", "Error writing decompressed text to file.")

# Create main window
root = tk.Tk()
root.title("Huffman Coding - Decompression")

# Create widgets
label_file_path = tk.Label(root, text="Select Compressed File:")
label_file_path.grid(row=0, column=0, padx=5, pady=5)

entry_file_path = tk.Entry(root, width=50)
entry_file_path.grid(row=0, column=1, padx=5, pady=5)

button_browse = tk.Button(root, text="Browse", command=select_file)
button_browse.grid(row=0, column=2, padx=5, pady=5)

button_decompress = tk.Button(root, text="Decompress", command=decompress_file)
button_decompress.grid(row=1, column=1, padx=5, pady=5)

# Run the main event loop
root.mainloop()

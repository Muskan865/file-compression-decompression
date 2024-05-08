# Huffman Coding Implementation

This project implements Huffman coding, a popular algorithm for lossless data compression, in Python. It includes functionalities for text compression, visualization of the Huffman tree, and text decompression.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages: `tkinter`, `graphviz`

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/huffman-coding.git
    ```

2. Navigate to the project directory:

    ```bash
    cd huffman-coding
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Compression**:
    - Launch the Huffman coding GUI by running the `main_gui.py` script.
    - Click the "Browse" button to select the text file you want to compress.
    - Once the file is selected, click the "Compress" button to initiate the compression process.
    - A file dialog will appear, allowing you to choose the location to save the compressed file. Specify the destination and click "Save".
    - A success message will be displayed upon successful compression.

2. **Visualization**:
    - Upon running the GUI, the Huffman tree visualization window will automatically appear, showing the graphical representation of the Huffman tree structure.

3. **Decompression**:
    - To decompress a file, launch the Huffman coding GUI by running the `main_gui.py` script.
    - Click the "Browse" button to select the compressed file you want to decompress.
    - Once the file is selected, click the "Decompress" button to initiate the decompression process.
    - A file dialog will appear, allowing you to choose the location to save the decompressed file. Specify the destination and click "Save".
    - A success message will be displayed upon successful decompression.

**Note**: Ensure that you have the necessary Python dependencies installed (`tkinter`, `graphviz`, etc.) before running the GUI.

## File Structure

- `main.py`: Contains the Huffman coding implementation for text compression and decompression.
- `huffman.py`: Module with functions for building Huffman trees, compressing text, and decompressing text.
- `main_gui.py`: GUI interface for interacting with the Huffman coding implementation.
- `helper_functions.py`: Helper functions used in the main scripts.
- `sample.txt`: Sample input text file for testing compression and decompression.
- `README.md`: Instructions and information about the project.

## Acknowledgments

- Inspired by [Huffman Coding](https://en.wikipedia.org/wiki/Huffman_coding)
- Special thanks to Nigarish Naveed and Hijab Fatima for working with me on this project.

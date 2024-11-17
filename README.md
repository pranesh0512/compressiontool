Setup and Usage
Prerequisites
Python 3.8 or higher.
Installation
Clone this repository:
bash
Copy code
git clone git@github.com:pranesh0512/compressiontool.git
cd huffman-encoding
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Usage
Encoding a File
Run the following command to encode a text file:

bash
Copy code
python main.py encode --input sample.txt --output encoded_output.bin
Decoding a File
Run the following command to decode an encoded file:

bash
Copy code
python main.py decode --input encoded_output.bin --output decoded_output.txt
Example
Input file: sample.txt
Contents:

Copy code
hello
Output file: encoded_output.bin
Binary contents: Huffman tree + encoded data.

Decoded file: decoded_output.txt
Contents:

Copy code
hello
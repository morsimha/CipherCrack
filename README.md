# ChiperCrack

ChiperCrack is a cryptographic analysis tool designed to decode encrypted messages using XOR operations and known plaintext attacks. The tool takes hexadecimal-encoded messages and performs XOR-based decryption, allowing users to uncover hidden plaintexts.

## Features

- **Hexadecimal to ASCII Conversion:** Converts hexadecimal-encoded messages to ASCII for easier manipulation and analysis.
- **XOR Operations:** Perform XOR between two ASCII strings, with the flexibility to adjust the starting index for more refined analysis.
- **Crib Dragging:** Automate the process of crib dragging, allowing users to input expected plaintexts and find potential matches in encrypted messages.
- **Command-Line Interface:** Simple, interactive command-line interface for entering expressions and analyzing encrypted messages.

# Example 1: XOR two ASCII strings with a key
m1 = "hi how are you? dog.\t2"
m2 = "this is great secret!"
key = "abcdefg"
mc1 = XOR_2_ASCII(m1, key)
mc2 = XOR_2_ASCII(m2, key)
print(mc1, mc2)

# Example 2: Convert a hexadecimal message back to ASCII
hex_msg = "0b434c1147"
ascii_msg = convert_to_ascii(hex_msg)
print(ascii_msg)




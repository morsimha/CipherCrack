
def convert_to_ascii(hex_msg): #  decode (return to ascii
    ascii_msg = ''.join([chr(int(''.join(c), 16)) for c in zip(hex_msg[0::2], hex_msg[1::2])]).replace(';', '\n- ')

    return ascii_msg

def XOR_2_ASCII(a, b,index =0):
    b = b[index:]
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def crib_2_str(c_1, c_2):
    found = False
    c_1_ascii = convert_to_ascii(c_1)
    c_2_ascii = convert_to_ascii(c_2)
    c1_x_c2_new = XOR_2_ASCII(c_1_ascii, c_2_ascii)

    #words: it was, the , enter,  in t, like, if pl, he i
    for letter, value in list(enumerate(c1_x_c2_new)):
        final = XOR_2_ASCII("i am ", c1_x_c2_new, letter)

        if all((123 > ord(c) >= 32) for c in final):
            print("#####################found: " + final)
            print("index: ", letter)
            found = True
        break

    return found


if __name__ == '__main__':
    messages_names = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"]
    messages_content = []
    with open ("encrypted_messages.txt", "r") as file:
        for line in file:
            if not line.startswith("Message"):
                messages_content.append(line.strip())

    messages = {}
    for index, value in enumerate(messages_names):
        messages[value] = messages_content[index]
    print(messages)

    for name, message in messages.items():
        for name2, message2 in messages.items():
            if name < name2: # no repetitions
                found = crib_2_str(message, message2)
                if found:
                    print(f"for message {name} and {name2}\n")

#     m1 = "hi how are you? dog.\t2"
#     m2 = "this is great secret!"
#     key = "abcdefg"
#     mc1 = XOR_2_ASCII(m1, key)
#     mc2 = XOR_2_ASCII(m2, key)
#     print(mc1, mc2)
#     py2 = "CG"
#     py2_rec = convert_to_ascii(py2)
#     print(py2_rec)
#    # mc1.encode('hex')
# def XOR_2_ASCII(a, b):
#     if len(a) > len(b):
#         return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
#     else:
#         return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

# m1 = "hi how are you? dog.\t2"
# m2 = "this is great secret!"
# key = "abcdefg"
# mc11 = XOR_2_ASCII(m1,key)
# mc1 = '\x0bC\x0c\x11G'
# mc2 = '\x15\x17E\x0f\x14'
# mc22 = XOR_2_ASCII(m2,key)
# mc22 = mc22.encode('hex')
# mc22 = mc22.decode('hex')
#
# # print(mc1, mc2)
# print("first",mc11)
# mc1 = mc1.encode('hex')
# mc11 = mc11.encode('hex')
# print("after encode",mc11)
# print("after decode",mc11.decode(('hex')))
# recover = ''.join([chr(int(''.join(c), 16)) for c in zip(mc11[0::2], mc11[1::2])]).replace(';', '\n- ')
# print("after recovery ",recover)
# first_xor = XOR_2_ASCII(recover,mc22)
# sec_xor = XOR_2_ASCII(first_xor,"secret")
# print(sec_xor)
#
#
#

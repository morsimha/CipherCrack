
def convert_to_ascii(hex_msg): #  decode (return to ascii
    ascii_msg = ''.join([chr(int(''.join(c), 16)) for c in zip(hex_msg[0::2], hex_msg[1::2])]).replace(';', '\n- ')

    return ascii_msg

def XOR_2_ASCII(a, b,index =0):
    b = b[index:]
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def crib_2_str(c_1, c_2, exp):
    found = False
    c_1_ascii = convert_to_ascii(c_1)
    c_2_ascii = convert_to_ascii(c_2)
    c1_x_c2_new = XOR_2_ASCII(c_1_ascii, c_2_ascii)

    for letter, value in list(enumerate(c1_x_c2_new)):
        final = XOR_2_ASCII(exp, c1_x_c2_new, letter)

        if all((123 > ord(c) >= 32) for c in final):
            print("Found expression: " + final)
            print("from index: ", letter)
            found = True
        break
        #  comment break if need to iterate the whole string
    return found


if __name__ == '__main__':
    messages_names = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"]
    messages_content = []
    with open("encrypted_messages.txt", "r") as file:
        for line in file:
            if not line.startswith("Message"):
                messages_content.append(line.strip())

    messages = {}
    for index, value in enumerate(messages_names):
        messages[value] = messages_content[index]
    #  print(messages)
    expression = "replace me"
    while expression != "":
        expression = input("Enter your expression: ")
        for name, message in messages.items():
            for name2, message2 in messages.items():
                if name < name2:  # no repetitions
                    found = crib_2_str(message, message2, expression)
                    if found:
                        print(f"End of results for message {name} and {name2}\n")


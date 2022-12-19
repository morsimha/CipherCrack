
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
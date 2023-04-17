fh = open('text.txt')
try:
    print(fh.readline())
finally:
    fh.close()

with open('text.txt', 'r', encoding='utf-8') as fh:
    print(fh.readline())


# 10101010

s = b'hello'
print(type(s))

byte_string = b'Hello world'


byte_str = 'some text'.encode()
print(byte_str)

numbers = [0, 128, 255]
byte_numbers = bytes(numbers)
print(byte_numbers)

for i in [0, 128, 255]:
    print(hex(i))



print(ord('a'))
print(chr(120))

s = 'Привіт!'
utf_8 = s.encode()
print(utf_8)

utf_16 = s.encode('utf-16')
print(utf_16)

string_from_utf_16 = utf_16.decode('utf-16')
print(string_from_utf_16)


byte_array = bytearray(b'Kill Tom!')
byte_array[0] = ord('B')
byte_array[5] = ord('K')
print(byte_array)
print(str(byte_array))


# U+00EA or U+0065 U +0302
print('ё' == 'ё')

with open('data.bin', 'wb') as fh:
    fh.write(b'Hello world!')

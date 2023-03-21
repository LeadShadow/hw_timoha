# pop(key) -> повертає значення елементу і видаляє пару ключ-значення з словника

chars = {
    'a': 1,
    'b': 2
}
b_num = chars.pop('b')
print(b_num)
print(chars)

# update(another_dict) -> розширює словник значеннями з іншого словника
chars = {
    'a': 1,
    'b': 2
}
chars.update({'c': 3})
print(chars)

# copy()
chars = {
    'a': 1,
    'b': 2
}
chars_copy = chars.copy()
print(chars == chars_copy)


# get(key[, default]) -> не викликає помилку, якщо ключа немає в словнику
# повертає значення default, якщо не знайшов ключа в словнику, default=None
chars = {
    'a': 1,
    'b': 2
}
c_idx = chars.get('c', 2)
print(c_idx)
# print(chars['c'])


numbers = {
    1: 'one',
    2: 'two',
    3: 'three'
}

for k in numbers:
    print(k, end=' ')

print()
for k in numbers.keys():
    print(k, end=' ')

print()
for v in numbers.values():
    print(v, end=' ')

print()
for key, value in numbers.items():
    print(f'{key}: {value}')
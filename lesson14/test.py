clean = '    something    '.strip()
print(clean)

dogs_text = 'All dogs bark like dogs'
print(dogs_text.replace('dogs', 'cats'))

test = 'TestHook'
print(test.removeprefix('Test'))
print(test.removeprefix('Hook'))

print(test.removesuffix('Hook'))
print(test.removesuffix('Test'))

number = input('Enter number: ')

if number.isdigit():
    print(10 + int(number))
else:
    print('Не число')

try:
    print(10 + int(number))
except ValueError:
    print('Не число')


print('1111'.count('1'))

print('sasha samus'.title())
print('i like python.'.capitalize())

print(ord('х'))
print(ord('ю'))
map = {ord('х'): 'h', ord('ю'): 'u'}
translated = 'хю'.translate(map)
print(translated)

# борщ -> borsch
# кіт -> kit


for i in range(16):
    s = 'int: {0: d}, hex: {0:#x}, oct: {0:#o}, bin: {0:#b}'.format(i)
    print(s)


for num in range(12):
    print('{:^9} {:^9} {:^9}'.format(num, num ** 2, num ** 3))


s = '{name} {last_name}'.format(name='Dilan', last_name='Bob')
print(s)

print('|{:<10}|{:*^10}|{:>10}|'.format('left', 'center', 'right'))

# тут відбуваються певні математичні операції і результат їх заноситься в змінну x
x = 8 ** 2 + 4 * (2 + 2)  # 80
print(x)
y = 70
print(y)
# None -> пустий тип
a = None
# Числа -> integer(int->цілі числа(1, 5, 38, 324, 12)), float(дробові числа(1.254, 6.7132, 8.9))
# boolean(bool) -> логічний тип(True or False) -> (1, 0)
# string(str) -> рядки('hello world')
s = 'didn\'t'  # didn't
s1 = 'Hello'
s2 = 'World'
joined_string = s1 + ' ' + s2  # HelloWorld
print(joined_string)
joined_string = f'{s1}, {s2}' # Hello, World
print(joined_string)
# 1 спосіб створити змінну з типом bool
a = True
b = False
# 2 спосіб створити змінну з типом bool
age = 18
adult1 = age >= 18  # True

age = 15
adult2 = age >= 18  # False


a = 3
b = 5
print(a < b)  # True
print(a > b)  # False
print(a <= b)  # True
print(a >= b)  # False
print(a == b)  # False
print(a != b)  # True

# Вбудовані функції в пайтоні
print('hello world', 'hello world')
y = int(input('Введіть значення: '))  # 10101100011010100110
print(type(y))  # type(y) -> class 'str'  '10'
print(y > 10)
# int(), float(), str(), bool()

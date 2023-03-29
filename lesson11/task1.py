# set
a = set()
# {'key': value} {1, 2, 3, 4, 5}

a = set('hello')
print(a)

b = {1, 2, 3, 4, 4}
print(b)



# add(elem) -> додає елемент в множину
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)

# remove(elem) -> видаляє елемент з множини, викликає помилку, якщо такого елементу немає
numbers = {1, 2, 3}
numbers.remove(3)
print(numbers)

# discard(elem) -> видаляє елемент з множини і не викликає помилку, якщо його немає
numbers = {1, 2, 3}
numbers.discard(4)
print(numbers)

a = set('hello')
print(a)

b = set('hi there!')
print(b)

print(a & b)

print(a ^ b)

print(a | b)

# tuple
points = {
    (0, 0): 'O',
    (1, 1): 'A',
    (2, 2): 'B'
}

not_empty = (1, 2, 3)
a = (1,)
print(type(a))

# string
game_string = "My 'Game'"

s = 'Hello world'
print(s[0])
print(s[-1])


# s[0] = 'Q'

# для того щоб перевести всі букви рядка в верхній регістр використовується метод upper
s = 'Hello'
print(s.upper())


# для переведення в нижній регістр використовується метод lower()
s = 'Some Text'
print(s.lower())


# для того щоб перевірити, що рядок починається з підрядка є метод startswith
s = 'Bill Jons'
print(s.startswith('B'))

phone_numer = '+380937316048'
print(phone_numer.startswith('+380'))

# щоб перевірити, що рядок закінчується підрядком, використовуємо метод endswith
s = 'hello.docx'
if s.endswith('jpg'):
    print('Це фотографія!')


# Загальні властивості для всіх колекцій
# 1 перевірка на входження

password = 'samus134'
if 'qwerty' in password or '123' in password:
    print('This password is to weak!')

prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23}
is_prime = 4 in prime_numbers
print(is_prime)

user = {
    'name': 'Sasha',
    'surname': 'Samus',
    'age': 20
}

if 'age' in user:
    print(f'User is {user["age"]} years old.')


# 2 кількість елементів

password = input('Password: ')
if len(password) < 8:
    print('Your password is too short')



# 3 перебір всіх елементів колекції в циклі for
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet:
    print(char)

print('-----------')
some_iterable = ['a', 'b', 'c']

for i in some_iterable:
    print(i)

odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)

# Впорядкованість
a = 'test'

print(a[0])

# Змінність
# Унікальність

# створення пустого списка
my_list = list()
print(my_list)
my_list1 = []
print(my_list1)

some_iterable = ['a', 'b', 'c']
first_letter = some_iterable[0]
second_letter = some_iterable[1]
last_letter = some_iterable[2]
print(first_letter, second_letter, last_letter)
# -0 -> 0

first_letter = some_iterable[-3]
second_letter = some_iterable[-2]
last_letter = some_iterable[-1]
print(first_letter, second_letter, last_letter)

some_iterable[1] = 'x'
print(some_iterable)

# зрізи(slice)
some_str = 'This is awesome string'
first_five = some_str[0:5]
print(first_five)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2:10:3]
print(odd_numbers, even_numbers, three_numbers)

numbers_copy = numbers[:]
print(numbers_copy == numbers)

letters = ['a', 'b']
letters.append('c')
print(letters)

num = [1, 2]
num.clear()
print(num)

# додавання елементу в кінець списка list.append(elem)
letters = ['a', 'b']
letters.append('c')
print(letters)

# видалення елементу зі списку, викличе помилку, якщо такого елемента немає в спискові
chars = ['a', 'b']
chars.remove('b')
print(chars)

# повернути і-й елемент і видалити його зі списку list.pop(i). За замовчуванням і = -1
chars = ['a', 'b']
chars.pop(1)
print(chars)


# розширити список a_list елементами з b_list: a_list.extend(b_list)
chars = ['a', 'b']
numbers = [[1], 2]

chars.extend(numbers)
print(chars)

# вставити х на позицію з індексом і: my_list.insert(i, x)
chars = ['a', 'b']
chars.insert(1, 'c')
print(chars)

# очистити список my_list.clear()

# знайти індекс першого елементу в спискові рівного x: index = my_list.index(x)
chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c')
print(c_ind)

count = 0
for i in chars:
    if i == 'c':
        break
    count += 1
print(count)

# повернути кількість елементів в спискові рівних x: x_number = my_list.count(x)
chars = ['a', 'a', 'a', 'd']
a_count = chars.count('a')
print(a_count)

count = 0
for i in chars:
    if i == 'a':
        count += 1

print(count)
print('aaa'.count('a'))

# відсортувати список по зростанню: my_list.sort(key=None, reverse=False)
chars = ['a', 'b', 'z', 'x', 'd', 'A', 'B', 'Z', 'X', 'D']
print(sorted(chars))
chars.sort()
print(chars)

# змінити порядок елементів в спискові на зворотній: my_list.reverse()
chars = ['t', 'a', 'c']
chars.reverse()
print(','.join(chars))

# повернути копію списка copy_list = list.copy()

chars = ['a', 'b']
chars_copy = chars.copy()
chars.remove('a')
print(chars_copy)
print(chars_copy == chars)
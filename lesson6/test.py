def say(message, times=1):
    print(message * times)


say('Привіт! ')
say('Світ! ', 5)

# Змінна кількість параметрів


def total(a=5, *numbers, **phone_book):
    print('a ==', a)
    # прохід по всіх елементах кортежу
    for item in numbers:
        print('item ==', item)

    # прохід по всіх елементах словника
    for first, second in phone_book.items():
        print(first, second)


total(10, 1, 2, 3, Jack=1123, Sasha=2828, Misha=1025)

# Контейнери для збереження аргументів функцій

# Кортеж -> це впорядковані незмінні множини елементів
my_tuple1 = tuple()
print(my_tuple1)
my_tuple2 = ()
print(my_tuple2)

not_empty = (1, 2, 4)
print(not_empty)

print(not_empty[0])
print(not_empty[1])
print(not_empty[2])


# Словники -> це контейнер, який зберігає пари ключ-значення

# Ваше ім'я: Sasha

empty_dict1 = {}
print(empty_dict1)
empty_dict2 = dict()
print(empty_dict2)

some_dict = {
    'key': 'value',
    1: 'one',
    2: 'two'
}

not_empty_dict = {'key': 'value'}
not_empty_dict['new_key'] = 'new_value'
print(not_empty_dict)

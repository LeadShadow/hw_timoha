def interval_generator(x, y):
    while x <= y:
        yield x
        x += 1


file_to_ten_generator = interval_generator(5, 10)
print(next(file_to_ten_generator))
print(next(file_to_ten_generator))
print(next(file_to_ten_generator))
print(next(file_to_ten_generator))
print(next(file_to_ten_generator))
print(next(file_to_ten_generator))


file_to_ten_generator = interval_generator(5, 10)
for i in file_to_ten_generator:  # file_to_ten_generator -> 5, 6, 7, 8, 9, 10
    print(i)

print('----------')
for i in range(5, 11):
    print(i)

# лямбда функції
# sum_lambda = lambda x, y: x + y


# def sum_(x, y):
#     return x + y
#
#
# sum_lambda = sum_(5, 10)


# map
numbers = [1, 2, 3, 4, 5]


def pow_():
    num = []
    for i in numbers:
        num.append(i ** 2)
    return num


for i in map(lambda x: x ** 2, numbers):  # map(...) -> 1, 4, 9, 16, 25
    print(i)


# filter
for i in filter(lambda x: x % 2, range(1, 11)):
    print(i)

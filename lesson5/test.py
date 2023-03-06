print('hello world')
print('hello world')


def say_hello():
    print('Привіт, світ!')


# say_hello1 = say_hello()
# print(say_hello1)
say_hello()

def print_max(a, b):
    if a > b:
        print(f'a = {a} максимальне')
    elif b > a:
        print(f'b = {b} максимальне')
    else:
        print(f"{b} == {a}")

print_max(b=50, a=50)
# print_max(3, 4) -> пряма передача значень
# x = 5,  y = 5,  print_max(x, y) -> непряма передача значень
x = 10
# def sum_num(a):
#     x = x + 10
#     print(x + a)


# sum_num(5)

def func(x):
    print('x ==', x) # x == 10
    x = 2 # 2
    print('Заміняємо глобальне значення х на', x) # 2

func(x)
print(x)


def sum_a_b(a, b):
    return a + b


sum = sum_a_b(10, 20)  # sum_a_b(10, 20) -> 30
print(sum)

def func_1(a, b=5, c=10):
    print(f'a == {a}, b == {b}, c == {c}')

func_1(10, 20, 30)
a = 10
a = 20
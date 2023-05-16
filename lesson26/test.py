# Функція як об'єкт першого класу

def func(x, y):
    return x + y


result = func
result1 = result(10, 10)
print(result1)


def sum_func(x, y):
    return x + y


def sub_func(x, y):
    return x - y


def func2(x, y, func):
    return func(x, y)


sum_result = func2(10, 10, sum_func)
sub_result = func2(20, 10, sub_func)

print(sum_result)
print(sub_result)

operators = {'+': sum_func, '-': sub_func}


def get_operator(operator):
    return operators.get(operator, 'Unknown operator')


sum_action = get_operator('+')
print(sum_action(10, 10))

sub_action = get_operator('-')
print(sub_action(10, 10))

mul_action = get_operator('*')
try:
    print(mul_action(10, 10))
except TypeError:
    print('Було повернено не функцію')


SOME_VAR = 1


def func(x):
    SOME_VAR = x
    print(SOME_VAR)


def procedure():
    print(SOME_VAR)


# 'x': 2
procedure()
func(5)
print(SOME_VAR)


GLOBAL_SCOPE_VAR = 1


def func():
    enclosed_scope_var = 2

    def inner():
        inner_var = 3


# Замикання
def adder(value):
    def inner(x):
        return x + value
    return inner


two_adder = adder(2)
print(two_adder(3))
print(two_adder(5))


# Карірування
def handle_operations(x, y, operator):
    if operator == '-':
        return x - y
    elif operator == "+":
        return x + y


print(handle_operations(10, 10, '-'))
print(handle_operations(10, 10, '+'))

def sum_func(x, y):
    return x + y


def sub_func(x, y):
    return x - y


def func2(x, y, func):
    return func(x, y)


operators = {'+': sum_func, '-': sub_func}


def get_operator(operator):
    return operators.get(operator, 'Unknown operator')

sum_action = get_operator('+')
print(sum_action(10, 10))

sub_action = get_operator('-')
print(sub_action(10, 10))


# Декоратори


def logged_func(func):
    def wrapper(x, y):
        print(f'Called with {x}, {y}')
        result = func(x, y)
        print(f'result: {result}')
        return result
    return wrapper


@logged_func
def complicated(x, y):
    return x / y
# complicated_ = logged_func(complicated)
# print(complicated_(10, 10))


print(complicated(10, 10))


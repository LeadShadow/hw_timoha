# MRO - Method Resolution Order
from collections import UserList, UserDict, UserString
import string


class A:
    x = 'I am A class'


class B:
    x = 'I am B class'
    y = 'I exist only in B'


class C(A, B):
    c = 'I exist only in C'


c = C()
print(c.c)
print(c.y)
print(c.x)


class A:
    x = 'I am A class'


class B:
    x = 'I am B class'
    y = 'I exist only in B'


class C(B, A):
    c = 'I exist only in C'


c = C()
print(c.c)
print(c.y)
print(c.x)


class ValueSearchDict(UserDict):
    def has_in_values(self, value):
        return value in self.data.values()


as_dict = ValueSearchDict()
as_dict['a'] = 1
as_dict.update({'b': 2})
print(as_dict.has_in_values(1))
print(as_dict.has_in_values(2))
print(as_dict.has_in_values(3))
# numbers = [1, 2, 3, 4]
# result = 1 in numbers
# print(result)
#
# letters = ['a', 'b', 'c', 'd']
#
#
# def value(str):
#     if str in ('a', 'b', 'c'):
#         print('hello world')


class CountList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))
        # sum_ = 0
        # for i in self.data:
        #     sum_ += int(i)
        # return sum_


countable = CountList([1, 2, '3', '4', 5, '6'])
print(countable.sum())


class TruncatedString(UserString):
    MAX_LEN = 7

    def truncated(self):
        self.data = self.data[:self.MAX_LEN]


ts = TruncatedString('Hello world')
ts.truncated()
print(ts)


class TruncatedString:
    MAX_LEN = 7

    def __init__(self, value):
        self.value = value

    def truncated(self):
        self.value = self.value[:self.MAX_LEN]


ts = TruncatedString('Hello world')
ts.truncated()
print(ts.value)


def input_number():
    num = 0
    while True:
        try:
            num = int(input('Enter integer number: '))
            return num
        except ValueError:
            print(f'"{num}" is not a number. Try again')


input_number()


class NameTooShortError(Exception):
    pass


class NameStartFromLowError(Exception):
    """Виникає коли ми пишемо з маленької літери ім'я"""


def input_error(func):
    def wrapper(name):
        try:
            func(name)
        except NameTooShortError:
            print("Ім'я дуже коротке")
        except NameStartFromLowError:
            print("Ім'я починається з маленької літери")
    return wrapper


@input_error
def enter_name(name):
    if len(name) < 3:
        raise NameTooShortError
    if name[0] not in string.ascii_uppercase:
        raise NameStartFromLowError


name = input('Enter name: ')
enter_name(name)

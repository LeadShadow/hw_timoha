from pathlib import Path
from decimal import Decimal


class User:
    name = 'Sasha'
    age = 18


user1 = User()
print(user1.name)
print(user1.age)

user2 = User()
user2.name = 'Misha'
print(user2.name)
print(user2.age)


class User:
    name = 'Sasha'
    age = 18

    def say_name(self):
        print(f'Hi I am {self.name} and I am {self.age} years old')

    def set_age(self, age):
        self.age = age


bob = User()
bob.name = 'Bob'

bob.say_name()

bob.set_age(25)

bob.say_name()


class Human:
    name = ''

    def hello(self, value):
        if self.name:
            return f'Hello {value}! I am {self.name}'
        return f'Hello {value}'


bill = Human()
print(bill.hello('John'))

bill.name = 'Bill'
print(bill.hello('John'))


class User:
    def __init__(self, name):
        self.__name = ''


user1 = User('Sasha')
# print(User.__init__().__name)


class Human:
    name = ''

    def voice(self):
        print(f'Hello! My name is {self.name}')


class Developer(Human):
    field_description = 'My Programming Language'
    language = ''

    def make_some_code(self):
        print(f'{self.field_description} is {self.language}')


class PythonDeveloper(Developer):
    language = 'Python'


class JsDeveloper(Developer):
    language = 'JS'


p_dev = PythonDeveloper()
p_dev.name = 'Sasha'
p_dev.voice()
p_dev.make_some_code()

js_dev = JsDeveloper
js_dev.voice(JsDeveloper)
js_dev.make_some_code(JsDeveloper)


class Sum:
    def __init__(self, field):
        self.first = field.first
        self.second = field.second

    def do_sum(self):
        return self.first[0] + self.second


class Fields:
    def __init__(self, first, second):
        self.first = first,
        self.second = second


field1 = Fields(1000, 2000)
sum = Sum(field1)
print(sum.do_sum())

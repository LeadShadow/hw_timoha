from collections import UserDict


class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def say_hello(self):
        return f'Hello I am {self.name}'


bill = Human('Bill')
print(bill.say_hello())
print(bill.age)

tom = Human('Tom', 20)
print(tom.say_hello())
print(tom.age)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point ({self.x}, {self.y})'


a = Point(10, 10)
print(a)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point ({self.x}: {self.y})'

    def __str__(self):
        return f'Point ({self.x}, {self.y})'


a = Point(10, 10)
print(a)

print(repr(a))
print(str(a))


class ListedValuesDict:
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = [value]

    def __getitem__(self, key):
        result = str(self.data[key][0])
        for value in self.data[key][1:]:
            result += ', ' + str(value)
        return result


dict1 = ListedValuesDict()
dict1[1] = 'a'
dict1[1] = 'b'
print(dict1[1])


class Adder:
    def __init__(self, add_value):
        self.add_value = add_value

    def __call__(self, new_value):
        return self.add_value + new_value


two_adder = Adder(2)
print(two_adder(5))


# __enter__ -> викликається коли інтерпретатор заходить в менеджер контексту(with -> as)

# __exit__ -> викликається коли інтерпретатор виходить з блоку менеджера контексту

class Session:
    def __init__(self, addr, port=8080):
        self.connected = True
        self.addr = addr
        self.port = port

    def __enter__(self):
        print(f'Connected to {self.addr}: {self.port}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connected = False
        if exc_type is not None:
            print('Some Error')
        else:
            print('No problem')


localhost_session = Session('localhost')
with localhost_session as session:
    print(session is localhost_session)
    print(localhost_session.connected)


class Iterable:
    MAX_VALUE = 10

    def __init__(self):
        self.current_value = 0

    def __next__(self):
        if self.current_value < self.MAX_VALUE:
            self.current_value += 1
            return self.current_value
        raise StopIteration


class CustomIterator:
    def __iter__(self):
        return Iterable()


c = CustomIterator()
for i in c:
    print(i)


class Secret:
    public_field = 'this is public'
    _private_field = 'avoid using this please'
    __real_secret = 'I am hidden'


s = Secret()
print(s.public_field)
print(s._private_field)
print(s._Secret__real_secret)


class PositiveNumber:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value > 0:
            self.__value = new_value
        else:
            print('Only numbers greater zero accepted')


p = PositiveNumber()
p.value = 1
print(p.value)
p.value = -1
p._PositiveNumber__value = -1
print(p.value)

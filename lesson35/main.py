# Задание
# В этом домашнем задании мы:
#
# Добавим поле для дня рождения Birthday. Это поле не обязательное, но может быть только одно.
# Добавим функционал работы с Birthday в класс Record, а именно функцию days_to_birthday,
# которая возвращает количество дней до следующего дня рождения.
# добавим функционал проверки на правильность приведенных значений для полей Phone, Birthday.
# Добавим пагинацию (постраничный вывод) для AddressBook для ситуаций, когда книга очень большая
# и надо показать содержимое частями, а не всё сразу. Реализуем это через создание итератора по
# записям.
# Критерии приёма:
# AddressBook реализует метод iterator, который возвращает генератор по записям AddressBook и
# за одну итерацию возвращает представление для N записей.
# Класс Record принимает ещё один дополнительный (опциональный) аргумент класса Birthday
# Класс Record реализует метод days_to_birthday, который возвращает количество дней до
# следующего дня рождения контакта, если день рождения задан.
# setter и getter логику для атрибутов value наследников Field.
# Проверку на корректность веденного номера телефона в setter для value класса Phone.
# Проверку на корректность веденного дня рождения в setter для value класса Birthday.
from collections import UserDict
import re
from datetime import datetime
import colorama

N = 3
class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'

    def __eq__(self, other) -> bool:
        return self.value == other.value


class Name(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        def is_code_valid(phone_code: str) -> bool:
            if phone_code[0:2] in ('03', '04', '05', '06', '09') and phone_code[2] != '0' and phone_code != '039':
                return True
            return False
        result = None
        phone = value.removeprefix('+').replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
        if phone.isdigit():
            if phone.startswith('0') and len(phone) == 10 and is_code_valid(phone[:3]):
                result = '+38' + phone
            elif phone.startswith('380') and len(phone) == 12 and is_code_valid(phone[2:5]):
                result = '+' + phone
            elif 10 <= len(phone) <= 14 and not phone.startswith('0') and not phone.startswith('380'):
                result = '+' + phone
        if result is None:
            raise ValueError(f'Неправильний тип значення {value}')
        self.__value = value


class Birthday(Field):
    def __str__(self):
        if self.value is None:
            return 'Unknown'
        else:
            return f'{self.value: %d %b %Y}'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        if value is None:
            self.__value = None
        else:
            try: # 11-28-2004
                self.__value = datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                try: # 28.11.2004
                    self.__value = datetime.strptime(value, "%d.%m.%Y").date()
                except ValueError:
                    raise DateIsNotValid

class Record:
    def __init__(self, name: Name, phones=[], birthday=None) -> None:
        self.name = name
        self.phone_list = phones
        self.birthday = birthday

    def __str__(self) -> str:
        return f'User \033[35m{self.name.value}\033[0m - Birthday {self.birthday}\n' \
               f'Phones: {", ".join([phone for phone in self.phone_list])}'

    def add_phone(self, phone: Phone) -> None:
        self.phone_list.append(phone)

    def del_phone(self, phone: Phone) -> None:
        self.phone_list.remove(phone)

    def edit_phone(self, phone: Phone, new_phone: Phone) -> None:
        self.phone_list.remove(phone)
        self.phone_list.append(new_phone)

    def days_to_birthday(self, birthday):
        if birthday.value is None:
            return None
        this_day = date.today()
        birthday_day = date(this_day.year, birthday.value.month, birthday.value.day)
        if birthday_day < this_day:
            birthday_day = date(this_day.year + 1, birthday.value.month, birthday.value.day)
        return (birthday_day - this_day).days


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def iterator(self, days=0):
        index, print_block = 1, '-' * 50 + '\n'
        for record in self.data.values():
            if days == 0 or (record.birthday.value is not None and record.days_to_birthday(record.birthday) <= days):
                print_block += str(record) + '\n'
                if index < N:
                    index += 1
                else:
                    yield print_block
                    index, print_block = 1, '-' * 50 + '\n'
        yield print_block



class PhoneUserAlreadyExists(Exception):
    """You cannot add an existing phone number to a user"""

class DateIsNotValid(Exception):
    """You cannot add an invalid date"""


class InputError:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, contacts, *args):
        try:
            return self.func(contacts, *args)
        except IndexError:
            return 'Error! Give me name and phone please!'
        except KeyError:
            return 'Error! User not found!'
        except ValueError:
            return 'Error! Phone number is incorrect'
        except PhoneUserAlreadyExists:
            return 'Error! You cannot add an existing phone number to a user'
        except DateIsNotValid:
            return 'Error! Date is not valid'


def verify_phone(phone: str) -> str:
    new_phone = re.sub(r'\+|\(|\)|-| |[a-zA-Zа-яА-Я]', '', phone)
    return new_phone


def hello(*args: tuple) -> str:
    return 'Hello! How can I help you?'


# add (Sasha)
@InputError
def add_contact(contacts: AddressBook, *args: tuple) -> str:
    name, phone = Name(args[0]), Phone(args[1])
    phone = verify_phone(phone.value)
    if name.value in contacts:
        if phone in contacts[name.value].phone_list:
            raise PhoneUserAlreadyExists
        else:
            contacts[name.value].add_phone(phone)
            return f'Add phone {phone} to user {name}'
    else:
        if len(args) > 2:
            birthday = Birthday(args[2])
        else:
            birthday = Birthday(None)
        contacts[name.value] = Record(name, [phone], birthday)
        return f'Add user {name} with phone number {phone}'

@InputError
def add_birthday(contacts, *args):
    name, birthday = args[0], args[1]
    contacts[name].birthday = Birthday(birthday)
    return f'Add/modify birthday {contacts[name].birthday} to user {name}'


@InputError
def days_to_user_birthday(contacts, *args):
    name = args[0]
    if contacts[name].birthday.value is None:
        return 'User has no birthday'
    return f'{contacts[name].days_to_birthday(contacts[name].birthday)} days to user {name} birthday'


def show_birthday(contacts, *args):
    days = int(args[0])
    result = f'List of users with birthday in {days} days:\n'
    print_list = contacts.iterator(days)
    for item in print_list:
        result += f'{item}'
    return result

@InputError
def change_contact(contacts, *args):
    name, old_phone, new_phone = args[0], args[1], args[2]
    new_phone = verify_phone(new_phone)
    contacts[name].edit_phone(old_phone, new_phone)
    return f"Change user's {name} phone number from {old_phone} to {new_phone}"


@InputError
def del_phone(contacts, *args):
    name, phone = args[0], args[1]
    contacts[name].del_phone(verify_phone(phone))
    return f'Delete phone {phone} from user {name}'


@InputError
def show_phone(contacts: dict, *args) -> str:
    name = args[0]
    return f'{contacts[name]}'


def show_all(contacts: dict, *args) -> str:
    if not contacts:
        return 'AdressBook is empty'
    result = 'List of all users: \n'
    print_list = contacts.iterator()
    for item in print_list:
        result += f'{item}'
    return result


def goodbye(*args) -> None:
    return None


def help(*args) -> str:
    return """Command format:
help or ? - help
hello - greeting
add <name> <phone> <birthday> - add user to dictionary
change <name> <phone> - change user's phone number
birthday name birthday - add/modify the user's birthday
days to birthday name - show how many days to the user's birthday
show birthday days N - show the user's birthday in the next N days
del <name> <phone> - delete the user's phone number
show <name> - show the user's phone number
show all - all contacts
close or . or exit or stop - exit the program"""


def unknown_command(*args):
    return 'Unknown command!'


COMMANDS = {hello: ['hello'], add_contact: ['add '], change_contact: ['change '], show_phone: ['phone '],
            help: ['?', 'help'], show_all: ['show all'], goodbye: ['good bye', 'close', 'exit', 'stop', '.'],
            del_phone: ['del '], add_birthday: ['birthday'], days_to_user_birthday: ['days to birthday'],
            show_birthday: ['show birthday days']}


def command_parser(user_command: str) -> (str, list):
    for key, values in COMMANDS.items():
        for value in values:
            if user_command.lower().startswith(value):
                args = user_command[len(value):].split()
                return key, args
    else:
        return unknown_command, []


def main():
    contacts = AddressBook()
    while True:
        user_command = input('Enter command: ')
        command, data = command_parser(user_command)
        print(command(contacts, *data), '\n')
        if command is goodbye:
            break


if __name__ == "__main__":
    main()

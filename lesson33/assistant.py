from collections import UserDict
import re


class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'

    def __eq__(self, other) -> bool:
        return self.value == other.value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phones=[]) -> None:
        self.name = name
        self.phone_list = phones

    def __str__(self) -> str:
        return f'User {self.name.value} - Phones: {", ".join([phone for phone in self.phone_list])}'

    def add_phone(self, phone: Phone) -> None:
        self.phone_list.append(phone)

    def del_phone(self, phone: Phone) -> None:
        self.phone_list.remove(phone)

    def edit_phone(self, phone: Phone, new_phone: Phone) -> None:
        self.phone_list.remove(phone)
        self.phone_list.append(new_phone)


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record


class PhoneUserAlreadyExists(Exception):
    """You cannot add an existing phone number to a user"""


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
        contacts[name.value] = Record(name, [phone])
        return f'Add user {name} with phone number {phone}'



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
    result = 'List of all users: '
    for key in contacts:
        result += f'\n{contacts[key]}'
    return result

def goodbye(*args) -> None:
    return None


def help(*args) -> str:
    return """Command format:
help or ? - help
hello - greeting
add <name> <phone> - add user to dictionary
change <name> <phone> - change user's phone number
del <name> <phone> - delete the user's phone number
show <name> - show the user's phone number
show all - all contacts
close or . or exit or stop - exit the program"""

def unknown_command(*args):
    return 'Unknown command!'
COMMANDS = {hello: ['hello'], add_contact: ['add '], change_contact: ['change '], show_phone: ['phone '],
            help: ['?', 'help'], show_all: ['show all'], goodbye: ['good bye', 'close', 'exit', 'stop', '.'],
                                                                   del_phone: ['del ']}


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
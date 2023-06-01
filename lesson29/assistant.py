from handlers import *

# hello, add_contact, change_contact, show_phone, show_all, goodbye
COMMANDS = {'hello': hello, 'add': add_contact, 'change': change_contact, 'phone': show_phone, 'show all': show_all,
            'exit': goodbye, 'close': goodbye, '.': goodbye, 'stop': goodbye, 'help': help, '?': help}


def main():
    contacts = {}
    while True:
        user_command = input('Enter command: ')
        for key in COMMANDS:
            if user_command.lower().startswith(key):
                args = user_command[len(key):].split()
                result = COMMANDS.get(key, None)  # add_contact
                result = result(contacts, *args)
                if result is None:
                    print('Good bye!')
                    exit(0)
                print(result)
                break
        else:
            print('Unknown command! Enter again')


if __name__ == "__main__":
    main()

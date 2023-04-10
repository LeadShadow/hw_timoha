import re

def sanitize_phone_number(phone: str) -> str:
    new_phone = re.sub(r'\+|\(|\)|-| |[a-zA-Zа-яА-Я]', '', phone)
    return new_phone


def check_phone(phone: str) -> bool:
    if phone.isdigit():
        return True
    else:
        return False

flag = sanitize_phone_number('    +38(050)123 -32-34вв  ')
print(flag)
if flag:
    print('You have a message from our site')
else:
    print("We can't send a message on this number")

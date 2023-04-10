# Ваша компания проводит маркетинговые кампании с помощью SMS рассылок.
# Автоматический сбор телефонных номеров с базы данных формирует определенный
# список. Но клиенты оставляют свои номера в произвольном виде:
#
#   "    +38(050)123-32-34",
#   "     0503451234",
#   "(050)8889900",
#   "38050-111-22-22",
#   "38050 111 22 11   ",
# Сервис рассылок прекрасно понимает и может отправить SMS-ку клиенту,
# только если телефонный номер содержит цифры. Необходимо реализовать функцию
# sanitize_phone_number, которая будет принимать строку с телефонным номером и
# нормализовать его, т.е. будет убирать символы (, -, ), + и пробелы.


def sanitize_phone_number(phone: str) -> str:
    new_phone = phone.strip().removeprefix('+').replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
    return new_phone


def check_phone(phone: str) -> bool:
    if phone.isdigit():
        return True
    else:
        return False

flag = check_phone(sanitize_phone_number('    +38(050)123 -32-34dd  '))
if flag:
    print('You have a message from our site')
else:
    print("We can't send a message on this number")
# if __name__ == "__main__":
#     print(check_phone(sanitize_phone_number('    +38(050)123 -32-34  ')))

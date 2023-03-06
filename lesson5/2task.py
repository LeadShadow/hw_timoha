# Пусть нам необходимо создать рассылку приглашений на мероприятие.
# Сообщение для каждого участника одинаковое, нам необходимо менять только имя приглашенного.
# Вполне очевидно, что для формирования такого сообщения, лучше использовать функцию.
# Создайте функцию invite_to_event, которая принимает имя приглашенного username и
# будет возвращать f-строку:

# "Dear {username}, we have the honour to invite you to our event".


def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event"


letter = invite_to_event('Sasha')
letter1 = invite_to_event('Misha')
letter2 = invite_to_event('Vasya')
letter3 = invite_to_event('Vova')
letter4 = invite_to_event('Oksana')
letter5 = invite_to_event('Yana')
print(letter)
print(letter1)
print(letter2)
print(letter3)
print(letter4)
print(letter5)

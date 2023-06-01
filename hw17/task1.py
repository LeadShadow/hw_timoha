# Есть список contacts, элементы которого — словари контактов следующего вида:
#
#     {
#     "name": "Allen Raymond",
#     "email": "nulla.ante@vestibul.co.uk",
#     "phone": "(992) 914-3792",
#     "favorite": False,
# }
# Словарь содержит имя пользователя, его email, телефонный номер и свойство — избранный
# контакт или нет.
#
# Создайте функцию get_favorites(contacts), которая будет возвращать список, содержащий
# только избранные контакты. Используйте при этом функцию filter, чтобы отфильтровать по полю
# favorite только избранные контакты.
def get_favorites(contacts):
    favorites = filter(lambda contact: contact.get('favorite', False), contacts)
    return list(favorites)
contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "(123) 456-7890",
        "favorite": True,
    },
    {
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "phone": "(987) 654-3210",
        "favorite": True,
    }
]

favorite_contacts = get_favorites(contacts)


if __name__ =='__main__':
 print(favorite_contacts)
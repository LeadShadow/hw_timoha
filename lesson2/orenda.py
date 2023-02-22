# Користувач хоче орендувати автомобіль для того, щоб він зміг це зробити, йому треба вказати своє
# ім'я, і щоб його вік був більше 18 і було водійське посвідчення


name = input("Введіть своє ім'я: ")
age = int(input("Введіть свій вік: "))
has_driver_licence = input('Чи маєте ви водійське посвідчення? Нічого не пишіть, якщо немає: ')

if has_driver_licence == 'Є':
    has_driver_licence = True
elif has_driver_licence == 'Немає':
    has_driver_licence = False
# True and True and True
if name and age >= 18 and has_driver_licence:
    print(f'User {name} can rent a car')
else:
    print('User can\'t rent a car')

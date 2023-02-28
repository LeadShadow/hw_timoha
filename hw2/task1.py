# У нас є три логічні змінні.
# Перша визначає статус користувача is_active, що дорівнює True або False.
# Друга is_admin визначає, чи є у користувача права адміністратора булевого типу.
# Третя is_permission — чи дозволено доступ, теж булевого типу. True or False
# Приведіть змінні is_active, is_admin та is_permission до булевого вигляду.

# Надайте змінної access, значення, яке покаже, чи є доступ користувача.
# Використовуйте логічні оператори.

# Адміністратор завжди має доступ незалежно від значень змінних is_admin і is_active.

# Користувач має доступ тільки якщо is_permission дорівнює True і is_active також дорівнює True

is_active = bool(int(input("Введіть статус користувача (1 - активний, 0 - неактивний): ")))
is_admin = bool(int(input("Чи є користувач адміністратором? (1 - так, 0 - ні): ")))
is_permission = bool(int(input("Чи має користувач дозвіл на доступ? (1 - так, 0 - ні): ")))

# Перевірити, чи має користувач доступ
access = is_admin or is_active and is_permission
# if is_admin or is_active and is_permission:
#     access = True
# elif not is_active:
#     access = False
# else:
#     access = False

# Вивести результат
print("Доступ користувача:", access)

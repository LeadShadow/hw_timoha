# В модуле работы с функциями мы писали функцию get_fullname для составления полного имени.
# Выполним небольшое продолжение задачи и напишем функцию is_check_name, которая принимает
# два параметра (fullname, first_name) и возвращает логическое True или False.
# Это результат проверки, является ли строка first_name префиксом строки fullname.
# Функция is_check_name строго относится к регистру букв, то есть «Sam» и «sam»
# для неё разные имена.

# fullname='Oleksandr Samus', first_name='Oleksandr'

def is_check_name(fullname: str, first_name: str) -> bool:
    return fullname.startswith(first_name)


if __name__ == "__main__":
    print(is_check_name(fullname='Samus Oleksandr', first_name='Oleksandr'))
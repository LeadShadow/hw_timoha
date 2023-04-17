# Пусть у нас есть текстовый файл, который содержит данные с месячной заработной платой по
# каждому разработчику компании.

# Пример файла:

# Alex Korp,3000
# Nikita Borisenko,2000
# Sitarama Raju,1000
# Как видим, структура файла — это фамилия разработчика и значение его заработной платы,
# разделенной запятой.

# Разработайте функцию total_salary(path) (параметр path - путь к файлу), которая будет разбирать
# построчно файл и возвращать общую сумму заработной платы всех разработчиков компании.

# Требования к задаче:

# функция total_salary возвращает значение типа float
# для чтения файла функция total_salary использует только метод readline
# мы пока не используем менеджер контекста with

def total_salary(path: str):
    file = open(path, 'r', encoding='utf-8')
    result = 0
    while True:
        line = file.readline()  # 'Alex Korp,3000'
        if not line:
            break
        result += int(line.split(',')[1])
    file.close()
    return result


if __name__ == "__main__":
    print(total_salary('test.txt'))
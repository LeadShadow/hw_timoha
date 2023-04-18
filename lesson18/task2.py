# В предыдущей задаче мы записали сотрудников в файл в следующем виде:
#
# Robert Stivenson, 28
# Alex Denver, 30
# Drake Mikelsson, 19
# Выполним теперь обратную задачу и создадим функцию read_employees_from_file(path),
# которая будет читать данные из файла и возвращать список сотрудников в виде:
#
# ['Robert Stivenson, 28', 'Alex Denver, 30', 'Drake Mikelsson, 19']
# Помните про присутствие символа конца строки \n при чтении данных из файла. Его
# необходимо убирать при добавлении прочитанной строки в список.
#
# Требования:
#
# прочтите содержимое файла, используя режим "r".
# мы пока не используем менеджер контекста with
# верните из функции список сотрудников из файла
from pathlib import Path


def read_employees_from_file(path):
    file = open(path, 'r', encoding='utf-8')
    result = []
    while True:
        line = file.readline().strip()
        if not line:
            break
        result.append(line)
    file.close()
    return result


if __name__ == "__main__":
    path = Path('text.txt')
    print(read_employees_from_file(path))




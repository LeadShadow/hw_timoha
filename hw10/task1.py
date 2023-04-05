# Напишите функцию parse_folder, она принимает единственный параметр path,
# который является объектом Path. Функция должна просканировать директорию path и
# вернуть кортеж из двух списков. Первый — это список файлов внутри директории, второй —
# список директорий.
#
# Пример вывода функции:
#
# (['.gitignore', 'readme.md'],
#  ['.git', '.idea', '.vscode', 'module-01', 'module-02', 'module-03', 'module-04', 'module-05', 'module-06', 'module-07',
#   'module-08', 'module-09', 'module-10', 'module-11', 'module-12'])

def parse_folder(path):
    files = []
    folders = []

    return files, folders
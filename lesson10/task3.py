# Написати функцію useless(list) де параметр list буде випадковий список
# Знайти в цьому списку максимальне значення і розділити його на довжину списка
# my_list = [1, 2, 3]

def useless(list: list) -> float:
    max_ = 0
    for i in list:
        if i > max_:
            max_ = i
    return max_ / len(list)


if __name__ == "__main__":
    print(useless([1, 3, 5, 9, 11, 15, 4, 6]))
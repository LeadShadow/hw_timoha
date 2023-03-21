# При анализе данных часто возникает необходимость избавиться от экстремальных значений,
# прежде чем начать работать с данными дальше. Напишите функцию prepare_data, которая удаляет
# из переданного списка наибольшее и наименьшее значение, сортирует его в порядке возрастания
# и возвращает измененный список в качестве результата.

list_ = [2, 4, 1, 3, 5]
print(max(list_))
def prepare_data(my_list: list) -> list:
    my_list.remove(max(my_list))  # max(my_list) -> 5
    my_list.remove(min(my_list))  # min(my_list) -> 1
    my_list.sort()
    return my_list  # sorted(my_list) -> [2, 3, 4]


if __name__ == "__main__":
    print(prepare_data(list_))
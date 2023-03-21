# є випадковий список, потрібно представити його в зворотньому напрямку
# [1, 3, 5] -> [5, 3, 1]


def reverser(my_list: list) -> list:
    my_list.reverse()
    return my_list


if __name__ == "__main__":
    print(reverser([1, 3, 5]))
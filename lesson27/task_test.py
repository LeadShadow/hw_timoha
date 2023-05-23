# [100, -200, 400, 500, -300]

def payment(my_list: list) -> int:
    result = 0
    for i in my_list:
        if i > 0:
            result += i
    return result


if __name__ == "__main__":
    print(payment([100, -200, 400, 500, -300]))



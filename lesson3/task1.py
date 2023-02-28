while True:
    number = input('number = ')
    number = int(number)
    if number == 0:
        break
    while True:
        print(number)
        number -= 1
        if number < 0:
            break

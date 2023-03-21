from random import randint


# треба вгадати число від 0 до n

def game(n: int):
    count = 0
    goal = randint(0, n)
    while True:
        answer = int(input(f'Вгадайте задуманне число від 0 до {n}: '))
        count += 1
        if answer > goal:
            print('Ваше число більше задуманного')
        elif answer < goal:
            print('Ваше число менше задуманного')
        else:
            print(f'Вітаю! Ви вгадали число за {count} кроки')
            break


if __name__ == "__main__":
    game(20)
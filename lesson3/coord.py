x = int(input('X: '))
y = int(input('Y: '))


if x >= 0:
    if y >= 0:
        print('Перша чверть')
    else:
        print('Четверта чверть')
else:
    if y >= 0:
        print('Друга чверть')
    else:
        print('Третя чверть')
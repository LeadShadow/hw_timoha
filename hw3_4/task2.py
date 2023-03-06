# Строка — это итерируемый объект, а, значит, мы можем использовать ее в цикле for.
# Подсчитайте в заданной строке message количество вхождений символа из переменной search.
# Результат поместите в переменную result.

message = 'I like play computer games'
search = 'p'
count = 0

for i in message:
    if i == search:
        count += 1

print(count)
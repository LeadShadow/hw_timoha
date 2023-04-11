fh = open('test_file.txt')


print(fh)
fh.close()

# 'r' - відкриття на читання (значення за замовчуванням)
# 'w' - відкриття на запис, зміст файла видаляється, якщо файлу не існує, створюється новий
# 'x' - відкриття на запис, якщо файла не існує - помилка
# 'a' - відкриття на дозапис, інформація додається в кінець файлу
# 'b' - відкриття в двійковому режимі
# 't' - відкриття в текстовому режимі (значення за замовчуванням)
# '+' - відкриття на читання і запис


fh = open('test.txt', 'w')
symbols_written = fh.write('hello!')
print(symbols_written)
fh.close()


fh = open('test1.txt', 'w+')
fh.write('hello!')
fh.seek(0)

first_two_symbols = fh.read(2)
print(first_two_symbols)  # he
fh.close()



fh = open('test1.txt', 'w')
fh.write('hello!')
fh.close()

fh = open('test1.txt', 'r')
all_file = fh.read()
print(all_file)
fh.close()



fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r')
while True:
    line = fh.readline()
    if not line:
        break
    print(line, end='')

fh.close()
print()
fh = open('test.txt', 'w')
fh.write('first line\nsecond line\nthird line')
fh.close()

fh = open('test.txt', 'r', encoding='utf-8')
lines = fh.readlines()
print(lines)

fh.close()

with open('test.txt', 'w', encoding='utf-8') as fh:
    fh.write('hello world!')

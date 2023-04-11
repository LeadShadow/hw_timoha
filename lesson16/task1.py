fh = open('test.txt', 'w')
fh.write('hello world!')
fh.close()


fh = open('test.txt', 'r')
while True:
    symbol = fh.read(1)
    if len(symbol) == 0:
        break
    print(symbol)

fh.close()
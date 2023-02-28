x = int(input('X: '))
y = int(input('Y: '))


if x == 0:
    print("X can't be equal to zero")
    x = int(input('X: '))
    if x == 0:
        print("X can't be equal to zero")
        x = int(input('X: '))
        if x == 0:
            print("X can't be equal to zero")
            x = int(input('X: '))
            if x == 0:
                print("X can't be equal to zero")
                x = int(input('X: '))

result = y / x

# цикл for
fruit = 'apple'
for ch in fruit:
    print(ch)

# цикл while
a = 1
while a <= 5:
    print(a)
    a = a + 1  # a = 1 + 1,   a = 2 + 1,  a = 3 + 1

while x == 0:
    print("X can't be equal to zero")
    x = int(input('X: '))

result = y / x



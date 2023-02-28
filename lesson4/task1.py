age = input('How old are you?: ')
try:
    age = int(age)
    if age >= 18:
        print('You are adult already')
    else:
        print('You are infant yet.')
except ValueError:
    print(f'{age} is not a number')

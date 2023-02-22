# число 0 приводиться до типу False

money = 0

if money:
    print(f"You have {money} on your bank account")
else:
    print('You have no money')

# None приводиться до False

result = None

if result:
    print(result)
else:
    print('Result is None')

# пустий контейнер(пустий рядок('') і тд тп) приводиться до типу False
user_name = input('Enter your name: ') # ''

if user_name:
    print(f'Hello, {user_name}')
else:
    print('Hi Anonim!')


print('hello world')
value = '0'
try:
    value = int(value)
    print(20423423 / value)
except ValueError:
    print(f'value {value} is not a number')
except ZeroDivisionError:
    print(ZeroDivisionError)
else:
    print(value > 0)
finally:
    print('This will be printed anyway')

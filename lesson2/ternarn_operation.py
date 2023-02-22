is_nice = True

s = 'nice' if is_nice else 'not nice'


if is_nice:
    s = 'nice'
else:
    s = 'not nice'


some_data = 'Data'
message = some_data or 'Не було ніяких даних' # True or True
print(message)
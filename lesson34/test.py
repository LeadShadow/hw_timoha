import pickle
import json
import csv
# Серіалізація об'єктів в пайтоні

# expenses = {
#     'hotel': 600,
#     'breakfast': 300,
#     'taxi': 150,
#     'lunch': 150
# }
#
# file_name = 'expenses.txt'
# with open(file_name, 'w', encoding='utf-8') as fh:
#     for key, value in expenses.items():
#         fh.write(f'{key}|{value}\n')

file_name = 'expenses.txt'
expenses = {}
with open(file_name, 'r') as fh:
    raw_expenses = fh.readlines()
    for line in raw_expenses:
        key, value = line.split('|')
        expenses[key] = int(value)


print(expenses)

some_data = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}
byte_strings = pickle.dumps(some_data)
print(byte_strings)
unpacked = pickle.loads(byte_strings)

print(unpacked == some_data)  # True
print(unpacked is some_data)  # False

file_name = 'data.bin'

with open(file_name, 'wb') as fh:
    pickle.dump(some_data, fh)


with open(file_name, 'rb') as fh:
    unpacked = pickle.load(fh)

print(unpacked == some_data)  # True
print(unpacked is some_data)  # False


class Human:
    def __init__(self, name):
        self.name = name


bob = Human('Bob')
decoded_bob = pickle.dumps(bob)

encoded_bob = pickle.loads(decoded_bob)
print(bob.name == encoded_bob.name)

some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}
byte_strings = json.dumps(some_data)
unpacked = json.loads(byte_strings)

print(unpacked == some_data)  # True
print(unpacked is some_data)  # False

print(unpacked['key'] == some_data['key'])
print(unpacked['a'] == some_data['a'])
print(unpacked['2'] == some_data[2])
print(unpacked['tuple'] == [5, 6])


file_name = 'data.json'
with open(file_name, 'w') as fh:
    json.dump(some_data, fh)


with open(file_name, 'r') as fh:
    unpacked = json.load(fh)


print(unpacked)

with open('eggs.csv', 'w', newline='') as fh:
    spam_writer = csv.writer(fh)
    spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

with open('eggs.csv', newline='') as fh:
    spam_reader = csv.reader(fh)
    for row in spam_reader:
        print(', '.join(row))


with open('names.csv', 'w', newline='') as fh:
    field_names = ['first_name', 'last_name', 'age']
    writer = csv.DictWriter(fh, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'first_name': 'Sasha', 'last_name': 'Samus', 'age': 18})
    writer.writerow({'first_name': 'Sasha', 'last_name': 'Samus', 'age': 18})
    writer.writerow({'first_name': 'Sasha', 'last_name': 'Samus', 'age': 18})
    writer.writerow({'first_name': 'Sasha', 'last_name': 'Samus', 'age': 18})


with open('names.csv', newline='') as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        print(row['first_name'], row['last_name'], row['age'])

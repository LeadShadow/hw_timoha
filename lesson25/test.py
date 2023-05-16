import collections

# namedtuple
person = ('Sasha', 'Samus', 18, 'Keletskya', '10101')
print(person[3])
Person = collections.namedtuple('Person1', ['name', 'last_name', 'age', 'street', 'index'])

person = Person('Sasha', 'Samus', 18, 'Keletskya', '10101')
print(person.name)
print(person.last_name)
print(person[3])


class Person:
    def __init__(self, name, last_name, age, street, index):
        self.name = name
        self.last_name = last_name,
        self.age = age,
        self.street = street,
        self.index = index


person1 = Person('Sasha', 'Samus', 18, 'Keletskya', '10101')
print(person1.name)

# Counter
# 4: 4
student_mark = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_mark:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1

print(mark_counts)


student_mark = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_mark)
print(mark_counts)
print(mark_counts.most_common(1))
print(mark_counts.most_common(2))

# defultdict
words = ['apple', 'cut', 'beer', 'lion', 'lama', 'cat', 'bear', 'dog', 'wolf', 'pull']
grouped_words = {}

for word in words:
    char = word[0]
    if char not in grouped_words:
        grouped_words[char] = []
    grouped_words[char].append(word)


print(grouped_words)

words = ['apple', 'cut', 'beer', 'lion', 'lama', 'cat', 'bear', 'dog', 'wolf', 'pull']
grouped_words = collections.defaultdict(list)

for word in words:
    char = word[0]
    grouped_words[char].append(word)

print(grouped_words)

# deque

d = collections.deque(maxlen=5)
d.append('last')
d.appendleft('first')
# list1.insert(0, 'first')
d.insert(1, 'middle')
print(d)
for i in d:
    print(i)
print(d.pop())
print(d.popleft())
print(d)


# Comprehensions
sq = []
for i in range(1, 5+1):
    sq.append(i ** 2)

print(sq)

sq = [i ** 2 for i in range(1, 6)]
print(sq)

numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i: i ** 2 for i in numbers}
print(sq)
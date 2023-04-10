import re


s = 'I am 18 years old 189'
age = re.search(r'\d+', s)
print(age.group())


s = 'I bought 7 nuts for 6$ and 10 bolts for 3$'
numbers = re.findall(r'\d+', s)
print(numbers)

p = re.sub(r'(blue|white|red)', 'colour', 'blue socks and red shoes')
print(p)
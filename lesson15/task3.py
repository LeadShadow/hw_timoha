'''
Метод: sub
'''

import re

s = 'The best language is C++'

p = re.sub(r'(javascipt|JavaScript|Java|java|C\+\+|c\+\+|c#|C#)', 'Python', s)

print(p)
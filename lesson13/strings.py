this_is_string = 'Hi there!'

the_same_string = "Hi there!"

print(the_same_string == this_is_string)

print('didn\'t')


text = """
This is first line
Second line
Third line
"""
print(text)

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh'''

print(song)

print(('spam', 'eggs') == 'spam eggs')

# \n -> переведення рядка
# \f -> переведення сторінки
# \r -> повернення каретки
# \t -> горизонтальна табуляція
# \v -> вертикальна табуляція

s = 'Hi there!'

start = 0
end = 7
print(s.find('er'))
print(s.find('q'))

print(s.index('er'))
# print(s.index('q'))

s = 'Some words'
print(s.rfind('o'))


s = 'I am learning strings in Python. Some new methods got now.'
sentences = s.split('. ')

print(sentences)

text = '. '.join(sentences)
print(text)

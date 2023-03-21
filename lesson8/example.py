import sys
from example1 import say_hello


def main():
    print('You imported example1.py')
    say_hello('user')

for arg in sys.argv:
    print(arg)

if __name__ == "__main__":
    main()


# get_numbers_ticket(min, max, quantity)
# min != < 1
# max != > 1000
# quantity min < quantity < max
from random import randrange


def get_numbers_ticket(min_, max_, quantity):
    if not (min_ < quantity < max_) or (min_ < 1 or max_ > 1000) or (quantity > max_ - min_):
        return []
    result = set()
    while len(result) < quantity:
        bowl = randrange(min_, max_ + 1)
        if len(result) != quantity:
            result.add(bowl)
    return sorted(result)


if __name__ == "__main__":
    print(get_numbers_ticket(1, 10, 5))



# 3! -> 3 * 2! -> 3 * 2 * 1! -> 3 * 2 * 1
# 5! -> 5 * 4! -> 5 * 4 * 3! -> 5 * 4 * 3 * 2! -> 5 * 4 * 3 * 2 * 1! -> 5 * 4 * 3 * 2 * 1


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)



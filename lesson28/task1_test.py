from time import time


def pow_(n, k):
    cache = {}
    if n in cache:
        result = cache[n]
        result = result ** k
    else:
        result = n ** k
        cache[n] = result
    return result


if __name__ == "__main__":
    time1 = time()
    print(pow_(4327847283785345345353453453453453, 4234))
    print(time() - time1)
    time1 = time()
    print(pow_(4327847283785345345353453453453453, 4235))
    print(time() - time1)

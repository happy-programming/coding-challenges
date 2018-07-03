def bad_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return bad_fibonacci(n-1) + bad_fibonacci(n-2)


def good_fibonacci(n, storage):
    if storage[n] > -1:
        return storage[n]

    storage[n] = good_fibonacci(n-1, storage) + good_fibonacci(n-2, storage)
    return storage[n]


if __name__ == '__main__':
    storage = [0, 1]
    for x in xrange(2, 500):
        storage.append(-1)

    print bad_fibonacci(30)
    print good_fibonacci(499, storage)

def exclusive_product(arr):
    if len(arr) <= 1:
        return []
    left = []
    right = []
    product = 1

    for x in xrange(0, len(arr)):
        product *= arr[x]
        left.append(product)

    product = 1
    for x in xrange(len(arr)-1, -1, -1):
        product *= arr[x]
        right.append(product)

    right = right[::-1]

    answer = [right[1]]

    for x in xrange(1, len(arr)-1):
        answer.append(left[x-1]*right[x+1])

    answer.append(left[-2])
    return answer


if __name__ == '__main__':
    arr = map(int, raw_input().strip().split(' '))
    print exclusive_product(arr)

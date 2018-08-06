#
import sys


def max_min(k, arr):
    k = k - 1
    arr = sorted(arr)
    answer = sys.maxint

    for x in xrange(0, len(arr) - k):
        if arr[x + k] - arr[x] < answer:
            answer = arr[x + k] - arr[x]

    return answer


if __name__ == '__main__':
    n = int(raw_input())
    k = int(raw_input())
    arr = []

    for _ in xrange(n):
        arr.append(int(raw_input()))

    print max_min(k, arr)

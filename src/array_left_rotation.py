"""
https://www.hackerrank.com/challenges/array-left-rotation/problem
"""
if __name__ == "__main__":
    size_array, number_of_rotation = map(int, raw_input().strip().split(' '))
    arr = map(int, raw_input().strip().split(' '))
    number_of_rotation = number_of_rotation % size_array
    for x in xrange(number_of_rotation, size_array):
        print arr[x],
    for x in xrange(0, number_of_rotation):
        print arr[x],

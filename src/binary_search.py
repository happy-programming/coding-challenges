"""
Binary search
Array must be sorted
-1 means element not found

"""

import bisect


# Return any position of the element
def binary_search(arr, element):
    i = 0
    j = len(arr)-1

    while i <= j:
        mid = i + (j-i)/2  # Remember this
        if arr[mid] == element:
            return mid
        else:
            if arr[mid] < element:
                i = mid+1  # +1
            else:
                j = mid-1  # -1

    return -1


# Return any position of the element
def binary_search_recursive(arr, i, j, element):
    if i > j:
        return -1

    mid = i + (j-i)/2  # Remember this

    if arr[mid] == element:
        return mid
    else:
        if arr[mid] < element:
            return binary_search_recursive(arr, mid+1, j, element)
        else:
            return binary_search_recursive(arr, i, mid-1, element)


# Return first position from left
def python_binary_search(arr, element):
    index = bisect.bisect_left(arr, element)

    if index != len(arr) and arr[index] == element:
        return index

    return -1


if __name__ == '__main__':
    input_arr = [1, 2, 2, 3, 3, 4, 5, 6, 7, 7, 7, 7, 7, 8]
    search = 7

    print python_binary_search(input_arr, search)
    print binary_search(input_arr, search)
    print binary_search_recursive(input_arr, 0, len(input_arr)-1, search)

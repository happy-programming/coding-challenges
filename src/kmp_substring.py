"""
in operator complexity in python
https://stackoverflow.com/questions/18139660/python-string-in-operator-implementation-algorithm-and-time-complexity

KMP algorithm
https://www.youtube.com/watch?v=GTJr8OvyEVQ
When mis match , Is there a suffix which is also a prefix !!

"""

"""
Time complexity O(n)
Space complexity O(n)
"""


def build_prefix_suffix(arr):
    if len(arr) == 0:
        return -1

    i = 0
    j = 1
    prefix_suffix = [0]
    while j < len(arr):
        if arr[i] == arr[j]:
            i += 1
            prefix_suffix.append(i)
            j += 1

        else:
            if i == 0:
                prefix_suffix.append(0)
                j += 1
            else:
                i = prefix_suffix[i - 1]

    return prefix_suffix

"""
Return first occurrence of substring.
Time Complexity O(m+n)  ->  in this O(n) is because of building prefix_suffix_array.
where m is length of haystack
n is length of needle
Space Complexity O(n) -> because of prefix_suffix_array
"""


def kmp(haystack, needle):
    needle_length = len(needle)
    haystack_length = len(haystack)

    if haystack is None or needle is None or needle_length == 0 or needle_length > haystack_length :
        return -1

    prefix_suffix = build_prefix_suffix(needle)

    find_length = 0
    i = 0
    j = 0

    while i < haystack_length and j < needle_length:
        if haystack[i] == needle[j]:
            find_length += 1
            i += 1
            j += 1
        else:
            find_length = 0
            if j == 0:
                i += 1
            else:
                j = prefix_suffix[j - 1]

    if find_length == needle_length:
        return i-needle_length
    else:
        return -1

print build_prefix_suffix('abacabc')

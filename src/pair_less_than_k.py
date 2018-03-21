"""
For a given array of n element.Return the number of pair such that L_i + L_j <= K where i!=j.
i = 0-len(L)
j = 0-len(L)
"""


def pair_count(L, K):
    L.sort()

    i = 0
    j = len(L)-1

    count = 0

    while i < j:
        if L[i] + L[j] > K:
            count = count + i
            j -= 1
        else:
            i += 1

    if i == len(L):
        if L[i] + L[j] <= K:
            count = ((i*(i+1))/2)
            return count

    if j == 0:
        return count

    count = count + ((j*(j+1))/2)

    return count

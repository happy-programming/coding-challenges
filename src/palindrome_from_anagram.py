"""
https://www.hackerrank.com/challenges/game-of-thrones/problem

"""


def game_of_thrones(s):
    letters_count = {}
    for letter in s:
        if letter in letters_count:
            letters_count[letter] = letters_count[letter] + 1
        else:
            letters_count[letter] = 1
    odd_count = 0
    for count in letters_count.itervalues():
        if count % 2 != 0:
            odd_count += 1
        if odd_count == 2:
            return 'NO'

    return 'YES'


def game_of_thrones_xor(s):
    if s is None or len(s) == 0:
        return 'YES'

    xor = s[0]

    for x in xrange(1, len(s)):
        xor = xor ^ s[x]

    if xor in s:
        return 'YES'

    return 'NO'


s = raw_input().strip()
result = game_of_thrones_xor(s)
print(result)

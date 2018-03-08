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


s = raw_input().strip()
result = game_of_thrones(s)
print(result)

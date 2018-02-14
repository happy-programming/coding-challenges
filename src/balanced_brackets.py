"""
https://www.hackerrank.com/challenges/balanced-brackets/problem

Assumption
Input will only contain these characters (,[,{,),],}

"""


def isBalanced(s, close_open):
    stack = []
    for x in xrange(len(s)):
        if s[x] not in close_open.iterkeys():
            stack.append(s[x])
        else:
            if len(stack) > 0 and stack[-1] == close_open[s[x]]:
                stack.pop(-1)
            else:
                return 'NO'
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == "__main__":
    close_open = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    t = int(raw_input().strip())
    for a0 in xrange(t):
        s = raw_input().strip()
        result = isBalanced(s, close_open)
        print result

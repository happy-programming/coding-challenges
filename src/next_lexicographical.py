def bigger_is_greater(word_list):
    l = len(word_list)
    i = -1

    for x in xrange(l - 1, 0, -1):
        if word_list[x - 1] < word_list[x]:
            i = x - 1
            break

    if i >= 0:
        for x in xrange(l - 1, i - 1, -1):
            if word_list[i] < word_list[x]:
                temp = word_list[i]
                word_list[i] = word_list[x]
                word_list[x] = temp
                return ''.join(word_list[0:i+1]) + ''.join(word_list[i+1:l][::-1])

    return 'no answer'


T = int(raw_input().strip())
for t in xrange(T):
    input_str = raw_input().strip()
    print bigger_is_greater(list(input_str))

def modified_binary_search(unique_scores, element, left, right):
    if right < 0:
        return -1
    if left >= len(unique_scores):
        return -1

    middle = left + (right - left)/2

    if middle+1<len(unique_scores) and element < unique_scores[middle] and element > unique_scores[middle+1]:
        return middle+1

    if element < unique_scores[middle]:
        return modified_binary_search(unique_scores, element, middle+1, right)

    if middle > 0 and element > unique_scores[middle] and element < unique_scores[middle-1]:
            return middle

    if element > unique_scores[middle]:
        return modified_binary_search(unique_scores, element, left, middle-1)

    return middle

int(raw_input())
scores = map(int, raw_input().rstrip().split())
unique_scores = []
unique_scores.append(scores[0])
for x in xrange(1, len(scores)):
    if scores[x] != scores[x-1]:
        unique_scores.append(scores[x])

int(raw_input())
alice = map(int, raw_input().rstrip().split())
for alice_score in alice:
    rank = modified_binary_search(unique_scores, alice_score, 0, len(unique_scores)-1)
    if rank == -1:
        if alice_score >= unique_scores[0]:
            print 1
        else:
            print len(unique_scores)+1
    else:
        print rank+1

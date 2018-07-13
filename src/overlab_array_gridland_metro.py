# Version 1
# https://www.hackerrank.com/challenges/gridland-metro/problem


def gridland_metro(k, track):
    train_map = {}
    for x in xrange(k):
        r = track[x][0]
        c1 = track[x][1]
        c2 = track[x][2]

        # Not needed if c1 is always less than c2
        if c1 > c2:
            temp = c1
            c2 = temp
            c1 = c2

        if r in train_map:
            adjusted = False
            for list_index in xrange(0, len(train_map[r])):
                current_cols = train_map[r][list_index]
                # condition 1 left
                if c2 < current_cols[0]:
                    continue

                # condition 2 right
                if c1 > current_cols[1]:
                    continue

                # condition 3 middle
                if c2 <= current_cols[1] and c1 >= current_cols[0]:
                    adjusted = True
                    break

                # condition 4 extend in left for sure
                if c1 < current_cols[0]:  # no need to check c2 because of condition 1
                    adjusted = True
                    current_cols[0] = c1
                    current_cols[1] = max(c2, current_cols[1])
                    break

                # condition 5 - extend in right for sure
                if c2 > current_cols[1]:  # no need to check c1 because of condition 2
                    adjusted = True
                    current_cols[1] = c2
                    current_cols[0] = min(c1, current_cols[0])
                    break

            if not adjusted:
                train_map[r].append([c1, c2])

            # train_map[r] = defragment(train_map[r])

        else:
            train_map[r] = [[c1, c2]]

    lamp_post = 0

    for key, value in train_map.iteritems():
        for cols in value:
            lamp_post += cols[1] - cols[0] + 1

    return lamp_post


# Not necessary
def defragment(list_of_cols):
    list_of_cols = sorted(list_of_cols, key=lambda x: x[0])
    defragmented_list = [list_of_cols[0]]
    for x in xrange(1, len(list_of_cols)):
        if defragmented_list[-1][1] > list_of_cols[x][0]:
            defragmented_list[-1][1] = list_of_cols[x][1]
        else:
            defragmented_list.append(list_of_cols[x])
    return defragmented_list


if __name__ == '__main__':
    nmk = raw_input().split()
    n = int(nmk[0])
    m = int(nmk[1])
    k = int(nmk[2])
    track = []

    for _ in xrange(k):
        track.append(map(int, raw_input().strip().split()))

    print (n*m) - gridland_metro(k, track)

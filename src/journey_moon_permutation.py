def permutation_count(countries):
    pair_count = 0
    total_length = 0
    total_countries = len(countries)

    for x in xrange(total_countries):
        total_length = total_length + len(countries[x])

    for x in xrange(0, total_countries):
        current_count = len(countries[x])
        country_count = current_count * (total_length - current_count)
        pair_count = pair_count + country_count

    return pair_count/2


if __name__ == "__main__":
    n, p = map(int, raw_input().strip().split(' '))
    countries = {}
    for x in xrange(p):
        a1, a2 = map(int, raw_input().strip().split(' '))
        foundA1 = -1
        foundA2 = -1
        for k, c in countries:
            if a1 in c:
                c.add(a2)
                foundA1 = True, k
            if a2 in c:
                c.add(a1)
                foundA2 = True, k

        if not foundA1[0] and not foundA2[0]:
            countries.append(set([a1, a2]))

        if foundA1 and foundA2:


    for x in xrange(n):
        found = False
        for c in countries:
            if x in c:
                found = True
                break
        if not found:
            countries.append([x])

    print permutation_count(countries)

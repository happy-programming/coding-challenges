#!/bin/python

rc = int(raw_input().strip())
bot_row, bot_col = map(int,raw_input().strip().split(' '))
grid = []
prince_row, prince_col = None, None
for i in xrange(0, rc):
    row = list(raw_input().strip())
    for x in xrange(0, len(row)):
        if row[x] == 'p':
            prince_row, prince_col = i, x

    grid.append(row)

distance_row = bot_row - prince_row
distance_col = bot_col - prince_col


def next_move(distance_row, distance_col):
    if distance_row > 0:
        return "UP"

    if distance_col > 0:
        return "LEFT"

    if distance_row < 0:
        return "DOWN"

    if distance_col < 0:
        return "RIGHT"

print next_move(distance_row, distance_col)

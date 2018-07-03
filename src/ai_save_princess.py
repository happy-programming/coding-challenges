rc = int(raw_input().strip())
grid = []
prince_row, prince_col = None, None
for i in xrange(0, rc):
    row = list(raw_input().strip())
    for x in xrange(0, len(row)):
        if row[x] == 'p':
            prince_row, prince_col = i, x

    grid.append(row)

bot_row = rc / 2
bot_col = rc / 2

distance_row = bot_row - prince_row
distance_col = bot_col - prince_col

answer = []

if distance_row > 0:
    for x in xrange(0, distance_row):
        answer.append("UP")

    if distance_col > 0:
        for x in xrange(0, distance_col):
            answer.append("LEFT")
    if distance_col < 0:
        for x in xrange(0, abs(distance_col)):
            answer.append("RIGHT")

if distance_row < 0:
    for x in xrange(0, abs(distance_row)):
        answer.append("DOWN")

    if distance_col > 0:
        for x in xrange(0, distance_col):
            answer.append("LEFT")
    if distance_col < 0:
        for x in xrange(0, abs(distance_col)):
            answer.append("RIGHT")

for move in answer:
    print move

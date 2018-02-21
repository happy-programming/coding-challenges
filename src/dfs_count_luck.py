"""
https://www.hackerrank.com/challenges/count-luck/problem
"""
def is_valid_move(i, j, row, col, matrix):
    if i < 0 or i >= row:
        return 0
    if j < 0 or j >= col:
        return 0
    if matrix[i][j] == 'X':
        return 0

    return 1


def wave_required(i, j, row, col, matrix):
    down = is_valid_move(i+1, j, row, col, matrix)
    up = is_valid_move(i-1, j, row, col, matrix)
    right = is_valid_move(i, j+1, row, col, matrix)
    left = is_valid_move(i, j-1, row, col, matrix)

    if down+up+right+left > 1:
        return True
    else:
        return False


def min_dis(a, b, c, d):
    return max([a, b, c, d])


def new_position(i, j, row, col, matrix):
    if is_valid_move(i+1, j, row, col, matrix):
        return i+1, j
    if is_valid_move(i-1, j, row, col, matrix):
        return i-1, j
    if is_valid_move(i, j+1, row, col, matrix):
        return i, j+1
    return i, j-1


def DFS(i, j, count, row, col, matrix):
    if is_valid_move(i, j, row, col, matrix) == 0:
        return count

    if matrix[i][j] == '*':
        return count

    if matrix[i][j] == '.':
        matrix[i][j] = 'X'
        if not wave_required(i, j, row, col, matrix):
            i, j = new_position(i, j, row, col, matrix)
            return DFS(i, j, count, row, col, matrix)
        else:
            return min_dis(
                DFS(i + 1, j, count + 1, row, col, matrix),
                DFS(i - 1, j, count + 1, row, col, matrix),
                DFS(i, j + 1, count + 1, row, col, matrix),
                DFS(i, j - 1, count + 1, row, col, matrix)
            )


def print_result(shortest_path, ron_guess):
    if shortest_path == ron_guess:
        print 'Impressed'
    else:
        print 'Oops!'


if __name__ == "__main__":
    test_case = int(raw_input().strip())
    for t in xrange(test_case):
        n_row, n_col = map(int, raw_input().strip().split(' '))
        matrix = []
        start_find = False
        for x in xrange(n_row):
            col = list(raw_input().strip())
            if not start_find:
                for y in xrange(len(col)):
                    if col[y] == 'M':
                        start_row = x
                        start_col = y
                        start_find = True
                        col[y] = '.'
            matrix.append(col)

        ron_guess = int(raw_input().strip())
        shortest_path = DFS(start_row, start_col, 0, n_row, n_col, matrix)
        print_result(shortest_path, ron_guess)

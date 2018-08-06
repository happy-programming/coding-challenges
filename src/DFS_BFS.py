"""
DFS Depth first search will tel you if a path exist or no, it will give the shortest path if only
one path exist , like in a maze.
In this example , if you apply DFS , it will give you wrong answer for shortest path, because more
than one shortest path exist.
    matrix = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 9],
    ]

--------------------------------------------------------------------------------------------------------

But in this example , DFS will give you correct answer because only one shortest path exist.
    matrix = [
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 9],
    ]

Answer is 7

Complexity:-
==========================================================================================================

BFS will always give you shortest path.

Useful Links
https://medium.com/basecs/deep-dive-through-a-graph-dfs-traversal-8177df5d0f13

"""
import sys
import Queue


def is_valid_move(i, j, row, col, matrix):
    if i < 0 or i >= row:
        return False
    if j < 0 or j >= col:
        return False

    # if some places are forbidden, also if that place is covered
    if matrix[i][j] == 0:
        return False

    return True


def min_dis(a, b, c, d):
    return min([a, b, c, d])


# Can't give shortest path/distance if more than one path exist
def DFS(i, j, count, row, col, matrix):
    if not is_valid_move(i, j, row, col, matrix):
        return sys.maxint

    if matrix[i][j] == 9:
        return count

    if matrix[i][j] == 1:
        matrix[i][j] = 0
        return min_dis(
            DFS(i + 1, j, count + 1, row, col, matrix),
            DFS(i - 1, j, count + 1, row, col, matrix),
            DFS(i, j + 1, count + 1, row, col, matrix),
            DFS(i, j - 1, count + 1, row, col, matrix)
        )


# Always give shortest path/distance
def BFS(matrix):
    if not len(matrix) > 0:
        None

    row = len(matrix)
    col = len(matrix[0])
    count = 0

    bfs_queue = Queue.Queue()
    bfs_queue.put([0, 0, count, [0, 0]])

    while not bfs_queue.empty():
        current_pos = bfs_queue.get()
        i = current_pos[0]
        j = current_pos[1]
        count = current_pos[2]

        if not is_valid_move(i, j, row, col, matrix):
            continue

        if matrix[i][j] == 9:
            return count

        if matrix[i][j] == 1:
            matrix[i][j] = 0

        bfs_queue.put([i+1, j, count+1])
        bfs_queue.put([i-1, j, count+1])
        bfs_queue.put([i, j+1, count+1])
        bfs_queue.put([i, j-1, count+1])


if __name__ == "__main__":
    matrix = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 9],
    ]

    # Correct shortest distance
    shortest_dis = BFS(matrix)
    if shortest_dis is None:
        print -1
    else:
        print shortest_dis

    matrix = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 9],
    ]

    # Wrong shortest distance
    shortest_dis = DFS(0, 0, 0, len(matrix), len(matrix[0]), matrix)
    if shortest_dis == sys.maxint:
        print -1
    else:
        print shortest_dis

    matrix = [
        [1, 1, 1, 0, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 0, 1, 9],
    ]

    # Correct shortest distance
    shortest_dis = DFS(0, 0, 0, len(matrix), len(matrix[0]), matrix)
    if shortest_dis == sys.maxint:
        print -1
    else:
        print shortest_dis


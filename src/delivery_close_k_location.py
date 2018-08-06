import sys
import Queue


def get_distance(i, j, x, y):
    return abs(i - x) ** 2 + abs(j - y) ** 2


def select_closest(destination_distance, k):
    destination_distance = sorted(destination_distance, key=lambda x: x[2])
    return destination_distance[0:k]


def minimum_weight(current_list, mst_set):
    min_weight = sys.maxint
    min_index = None

    for v in xrange(0, len(current_list)):
        if current_list[v] < min_weight and v not in mst_set:
            min_weight = current_list[v]
            min_index = v

    return min_index


def prim_algo(graph):
    mst_set = set()
    current_vertex = 0
    mst_set.add(current_vertex)
    current_list = graph[current_vertex]
    path_vertices = []

    for x in xrange(0, len(current_list)):
        path_vertices.append(current_vertex)
        next_vertex = minimum_weight(current_list, mst_set)
        if next_vertex is None:
            return path_vertices
        mst_set.add(next_vertex)
        current_vertex = next_vertex
        current_list = graph[current_vertex]

    return path_vertices


def update_distance(destination):
    for index in xrange(0, len(destination)):
        destination[index].append(get_distance(0, 0, destination[index][0], destination[index][1]))

    return destination


def convert_adjency_matrix(destination):
    destination.insert(0, [0, 0, 0])
    adjency_matrix = []
    for index_i in xrange(0, len(destination)):
        temp = []
        for index_j in xrange(0, len(destination)):
            distance = get_distance(
                destination[index_i][0], destination[index_i][1],
                destination[index_j][0], destination[index_j][1]
            )
            temp.append(distance)

        adjency_matrix.append(temp)

    return adjency_matrix


def run():
    test_case = [
        [1, -3],
        [1, 2],
        [3, 4]
    ]

    X = 3

    test_case = [
        [3, 6],
        [2, 4],
        [5, 3],
        [2, 7],
        [1, 8],
        [7, 9]
    ]

    test_case = update_distance(test_case)
    test_case = select_closest(test_case, X)

    test_graph = convert_adjency_matrix(test_case)

    """
    For checking prim's algo
    test_graph = [[0, 2, 0, 6, 0],
                  [2, 0, 3, 8, 5],
                  [0, 3, 0, 0, 7],
                  [6, 8, 0, 0, 9],
                  [0, 5, 7, 9, 0],
                  ]


    for t in xrange(0, len(test_graph)):
        row = test_graph[t]
        for tt in xrange(0, len(row)):
            if row[tt] == 0:
                row[tt] = sys.maxint
                
    """

    path_vertices = prim_algo(test_graph)
    path_coordinates = []

    for x in path_vertices:
        path_coordinates.append([test_case[x][0], test_case[x][1]])

    print path_coordinates[1:]


def dijkstra(graph):
    visited = set()
    dijkstra_queue = Queue.Queue()
    current_vertex = 0
    current_list = graph[current_vertex]

    visited.add(current_vertex)

    dijkstra_queue.put([current_vertex, 0, -1])

    while not dijkstra_queue.empty():
        current = dijkstra_queue.get()

        current_vertex = current[0]
        visited.add(current_vertex)

        current_distance = current[1]

        current_list = graph[current_vertex]

        for x in xrange(current_list):
            if x not in visited and current_list[x] > current_list[]




    return


run()

def adjacency_list_to_matrix(adj_l):
    size = len(adj_l.keys())
    matrix = []

    for _ in range(size):
        row = [0] * size
        matrix.append(row)

    for key, values in adj_l.items():
        for value in values:
            matrix[key][value] = 1
    
    for _ in range(size):
        print(matrix[_])

    return matrix
print(adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]}))
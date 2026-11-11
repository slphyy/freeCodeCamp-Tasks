def dfs(matrix, node):
    stack = [node]
    visited = set()
    order = []

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        order.append(current)

        for neighbor, value in enumerate(matrix[current]):
            if value == 1 and neighbor not in visited:
                stack.append(neighbor)

    return order


print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))

def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []
    queens = []          # queens[row] = column
    cols = set()
    diag = set()         # row - col is constant along a "\" diagonal
    anti_diag = set()    # row + col is constant along a "/" diagonal

    def place(row):
        if row == n:
            solutions.append(queens.copy())
            return

        for col in range(n):
            if col in cols or row - col in diag or row + col in anti_diag:
                continue

            queens.append(col)
            cols.add(col)
            diag.add(row - col)
            anti_diag.add(row + col)

            place(row + 1)

            queens.pop()
            cols.remove(col)
            diag.remove(row - col)
            anti_diag.remove(row + col)

    place(0)
    return solutions
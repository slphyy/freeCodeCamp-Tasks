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
            solutions.append(queens.copy()) #caso base
            return

        for col in range(n):
            if col in cols or row - col in diag or row + col in anti_diag:
                continue # diag and anti_diag are just sets to mantain the diagonal values of the column 

            queens.append(col)
            cols.add(col)
            diag.add(row - col)
            anti_diag.add(row + col) #adding values so the position check works

            place(row + 1)

            queens.pop()
            cols.remove(col) #resets if it doesnt show a solution
            diag.remove(row - col)
            anti_diag.remove(row + col)

    place(0)
    return solutions

dfs_n_queens(4)
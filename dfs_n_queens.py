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
                continue # a diagonal e a anti_diagonal ela nada 
                         #mais nada menos é do que um conjunto que guarda as posições diagonais da coluna para a comparação

            queens.append(col)
            cols.add(col)
            diag.add(row - col)
            anti_diag.add(row + col) # conjunto de verificações

            place(row + 1)

            queens.pop()
            cols.remove(col) #remover as verificações se n der em nd
            diag.remove(row - col)
            anti_diag.remove(row + col)

    place(0)
    return solutions

dfs_n_queens(4)
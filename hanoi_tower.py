def hanoi_solver(discs):
    first = list(range(discs, 0, -1))
    second = []
    third = []
    lines = []

    def record():
        lines.append(f'{first} {second} {third}')

    def move(n, source, target, spare):
        if n == 0:
            return
        move(n - 1, source, spare, target)
        target.append(source.pop())
        record()
        move(n - 1, spare, target, source)

    record()                                   
    move(discs, first, third, second)
    return '\n'.join(lines)

hanoi_solver(3)
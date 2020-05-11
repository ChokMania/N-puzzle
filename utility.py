def is_valid(sol, x, y):
    n = len(sol[0])
    if (x == n or y == n or sol[y][x] != 0):
        return (0)
    return (1)
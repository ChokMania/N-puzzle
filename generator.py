import numpy as np
import random
import utility

def gen_puzzle(n):
    puzzle = []
    numbers = []
    for i in range (n**2):
        numbers.append(i)
    for i in range(n**2):
        rand = random.randint(0, len(numbers) - 1)
        puzzle.append(numbers[rand])
        numbers.pop(rand)
    return(puzzle)

def cycle(sx, sy):
    if (sx == 1 and sy == 0):
        return (0, 1)
    elif (sx == 0 and sy == 1):
        return (-1, 0)
    elif (sx == -1 and sy == 0):
        return (0, -1)
    else:
        return (1, 0)

def gen_solution(n):
    sol = np.zeros((n, n))
    i = 1
    x, y = [0, 0]
    sx, sy = [1, 0]
    while i != n**2:
        if (utility.is_valid(sol, x + sx, y + sy) == 0):
            sx, sy = cycle(sx, sy)
        sol[y][x] = i
        i += 1
        x += sx
        y += sy
    return sol
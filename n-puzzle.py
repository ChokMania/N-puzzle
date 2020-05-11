import sys
import random

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

if __name__ == "__main__":
    n = 3
    puzzle = gen_puzzle(n)
    print(puzzle)
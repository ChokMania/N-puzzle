import sys
import random
import numpy as np
import generator

if __name__ == "__main__":
    n = 3
    #puzzle = gen_puzzle(n)
    #print(puzzle)
    solution = generator.gen_solution(n)
    print(solution)
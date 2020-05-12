import numpy as np
import generator
import utility

def	get_listed_coords(n):
	target = generator.gen_solution(n)
	print(target)
	x_crd = np.zeros((n**2))
	y_crd = np.zeros((n**2))
	for i in range(n):
		for j in range(n):
			x_crd[int(target[j][i])] = i
			y_crd[int(target[j][i])] = j
	return (x_crd, y_crd)

def	manhattan_dist(grid, n, x_tar, y_tar):
	dist = 0
	for i in range(n):
		for j in range(n):
			nbr = int(grid[j][i])
			if nbr != 0:
				dist += int(abs(j - y_tar[nbr])) + int(abs(i - x_tar[nbr]))
	return dist

def solve(grid, n):
	x_tar, y_tar = get_listed_coords(n)
	print(grid)
	print(manhattan_dist(grid, n, x_tar, y_tar))

n = 3
grid = generator.gen_puzzle(n, 100)
solve(grid, n)
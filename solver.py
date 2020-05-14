import numpy as np
import generator
import utility
import random
import operator

def	get_listed_coords(n):
	target = generator.gen_solution(n)
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

class Node:
	def __init__(self, parent, grid, h_score, dist):
		self.parent = parent
		self.grid = grid
		self.h_score = h_score
		self.dist = dist
		self.total = h_score + dist


def solve(grid, n):
	solution = generator.gen_solution(n)
	x_tar, y_tar = get_listed_coords(n)
	open_list = [Node(None, grid, manhattan_dist(grid, n, x_tar, y_tar), 0)]
	closed_list = {}
	max_ol = 0
	done = False
	while (open_list and not done):
		if (len(open_list) > max_ol):
			max_ol = len(open_list)
		open_list = sorted(open_list, key=operator.attrgetter('total'))
		parent = open_list[0]
		for move in utility.get_moves(parent.grid):
			if (np.array_equal(move, solution)):
				done = True
				print("Solved!\n", move, "\nNumber of moves:", parent.dist + 2, "\nOpen list max length:", max_ol, "\nClosed list length:", len(closed_list))
				break
			if (not np.array2string(np.concatenate(move)) in closed_list):
				child = Node(parent, move, manhattan_dist(move, n, x_tar, y_tar), parent.dist + 1)
				open_list.append(child)
				del child
		closed_list[np.array2string(np.concatenate(parent.grid))] = parent
		open_list.pop(0)


n = 3
grid = generator.gen_puzzle(n, 100)
print("Grid to solve:")
print(grid, "\n")
solve(grid, n)
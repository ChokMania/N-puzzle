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
	h_score = manhattan_dist(grid, n, x_tar, y_tar)
	parent = Node(None, grid, manhattan_dist(grid, n, x_tar, y_tar), 0)
	open_list = []
	for move in utility.get_moves(grid):
		child = Node(parent, move, manhattan_dist(move, n, x_tar, y_tar), parent.dist)
		open_list.append(child)
		del child
	closed_list = [parent]
	done = False
	while (open_list and not done):
		open_list = sorted(open_list, key=operator.attrgetter('total'))
		parent = open_list[0]
		for move in utility.get_moves(parent.grid):
			accept = True
			if (np.array_equal(move, solution)):
				done = True
				print("Yay!\n", move, parent.dist + 1)
				break
			for c in closed_list:
				if np.array_equal(c.grid, move):
					accept = False
					break
			if (accept):
				child = Node(parent, move, manhattan_dist(move, n, x_tar, y_tar), parent.dist + 1)
				open_list.append(child)
				del child
		closed_list.append(parent)
		open_list.pop(0)


n = 4
grid = generator.gen_puzzle(n, 100)
print(grid)
solve(grid, n)
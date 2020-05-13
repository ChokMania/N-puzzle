import numpy as np
import generator
import utility
import random

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


def solve(grid, n):
	x_tar, y_tar = get_listed_coords(n)
	h_score = manhattan_dist(grid, n, x_tar, y_tar)
	parent = Node(None, grid, manhattan_dist(grid, n, x_tar, y_tar), 0)
	open_list = []
	for move in utility.get_moves(grid):
		child = Node(parent, move, manhattan_dist(move, n, x_tar, y_tar), parent.dist)
		open_list.append(child)
		del child
	closed_list = [parent]
	print("Generated puzzle is:\n", grid, "\n")
	for n in open_list:
		print("\n", n.parent, n.grid, n.h_score, n.dist)
		print("")
	done = False
	#while (open_list and not done):
		

n = 3
grid = generator.gen_puzzle(n, 100)
solve(grid, n)
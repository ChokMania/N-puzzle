import numpy as np

def is_valid_or_empty(sol, x, y):
	n = len(sol[0])
	if (x == n or y == n or sol[y][x] != 0):
		return (0)
	return (1)

def is_valid(sol, x, y):
	n = len(sol[0])
	if (x == n or y == n):
		return (0)
	return (1)

def get_empty(state):
	x = 0
	while x != len(state[0]):
		y = 0
		while y != len(state[0]):
			if (state[y][x] == 0):
				return (x, y)
			y += 1
		x += 1

def get_moves(state):
	x, y = get_empty(state)
	poss = []
	if is_valid(state, x + 1, y):
		new_poss = state.copy()
		new_poss[y][x], new_poss[y][x + 1] = new_poss[y][x + 1], new_poss[y][x]
		poss.append(new_poss)
	if is_valid(state, x - 1, y):
		new_poss = state.copy()
		new_poss[y][x], new_poss[y][x - 1] = new_poss[y][x - 1], new_poss[y][x]
		poss.append(new_poss)
	if is_valid(state, x, y + 1):
		new_poss = state.copy()
		new_poss[y][x], new_poss[y + 1][x] = new_poss[y + 1][x], new_poss[y][x]
		poss.append(new_poss)
	if is_valid(state, x, y - 1):
		new_poss = state.copy()
		new_poss[y][x], new_poss[y - 1][x] = new_poss[y - 1][x], new_poss[y][x]
		poss.append(new_poss)
	return (poss)
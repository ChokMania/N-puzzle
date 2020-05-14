import sys, random, argparse, re
import numpy as np
import generator, utility

def check_file(file):
	try:
		with open(file, "r", encoding='utf-8-sig') as f:
			data = f.read()
			ds, i = data.split("\n"), 0
			size = 3
			numbers = []
			for line in ds:
				line = re.sub(r"[\s\t]+", ' ', line).strip()
				if line != "" and line.strip()[0] != "#":
					if i == 0:
						n = line.split()
						if len(n) != 1:
							raise ValueError()
						size = int(n[0])
						array = np.zeros((size, size))
					else:
						check = line.find("#")
						if check != -1:
							line = line[:check]
						app = list(eval(line.replace(" ", ", ")))
						if len(app) != size:
							raise ValueError()
						array[i - 1] = app
					i += 1
			array = np.round(array.transpose()).astype(int)
			if i != size + 1 or np.array_equal(np.sort(np.concatenate(array)), np.array(range(0, size * size))) == False:
				raise ValueError()
			return array.transpose()
	except:
		print("Error")
		exit()

def is_solvable(map, verbose) :
	puzzle = np.concatenate(map)
	solved_full = generator.gen_solution(map.shape[0])
	solved = np.concatenate(np.int64(solved_full))
	inversion = 0
	if verbose == True:
		print(f"Puzzle: \n{map}\n\nSolved: \n{np.int64(solved_full)}\n")
	for i in range(len(puzzle) - 1):
		count = 0
		for j in range(i + 1, len(puzzle)) :
			vi = puzzle[i]
			vj = puzzle[j]
			if np.where(solved == vi) > np.where(solved == vj):
				count += 1
		if verbose == True:
			print(f"the {puzzle[i]} gives us {count} inversions")
		inversion += count
	blank_puzzle = utility.get_empty(map)
	blank_solved = utility.get_empty(solved_full)
	if verbose == True:
		print(f"\nPuzzle: {puzzle}\nSolved: {solved}\nShape : {map.shape[0]}\nBlank Position (column, row):\n\tPuzzle {blank_puzzle}\n\tSolved: {blank_solved}\nCount of inversions: {inversion}\n")
	blank = abs(blank_puzzle[1] - blank_solved[1]) + abs(blank_puzzle[0] - blank_solved[0])
	if blank % 2 == 0 and inversion % 2 == 0:
		return True
	if blank % 2 == 1 and inversion % 2 == 1:
		return True
	return False

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--map", type=check_file, help="")
	parser.add_argument("-v", "--visu", action="store_true", help="Enable visualisation")
	parser.add_argument("-vb", "--verbose", action="store_true", help="verbose")
	parser.add_argument("-g", "--generate", type=int, help="Generate")
	parser.add_argument("-i", "--iteration", type=int, help="iteration")
	args = parser.parse_args()
	if args.map is None:
		if args.generate == None:
			n = 4
			print(f"Puzzle has been created with size = {n} by default", end="")
		else:
			n = int(args.generate)
			print(f"Puzzle has been created with size = {n}", end="")
		i = int(args.iteration) if args.iteration is not None and int(args.iteration) < 1 else 100
		print(f" and mixed with {i} iterations")
		args.map = generator.gen_puzzle(n, i)
	if is_solvable(args.map, args.verbose) == False:
		print("Puzzle is unsolvable")
		exit()

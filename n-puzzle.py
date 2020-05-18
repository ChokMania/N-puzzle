import argparse, check, time
import generator, solver, visu

def manager(args):
	if args.greedy and args.uniform:
		print("Can't solve using both greedy and uniform")
		exit()
	if args.map is None:
		if args.generate == None:
			n = 3
			print(f"Puzzle has been created with size = {n} by default", end="")
		else:
			n = int(args.generate)
			print(f"Puzzle has been created with size = {n}", end="")
		i = int(args.iteration) if args.iteration is not None and int(args.iteration) < 1 else 100
		print(f" and mixed with {i} iterations")
		args.map = generator.gen_puzzle(n, i)
	if check.is_solvable(args.map, args.verbose) == False:
		print("Puzzle is unsolvable")
		exit()
	return args.map

def npuzzle(args):
	grid = manager(args)
	t_start = time.time()
	steps = solver.solve(grid, len(grid[0]), args.heuristic, args.greedy, args.uniform, args.verbose)
	if args.time:
		print ("This took %.2f seconds" % (time.time() - t_start))
	if (steps):
		print("\nMoves to solution:")
		for state in steps:
			print(state, "\n")
	else:
		print("Already solved from the start")
	if args.visu:
		visu.visu(grid, steps, len(grid[0]))

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--map", type=check.file, help="")
	parser.add_argument("-v", "--visu", action="store_true", help="Enable visualisation")
	parser.add_argument("-vb", "--verbose", action="store_true", help="verbose")
	parser.add_argument("-g", "--generate", type=int, help="Generate")
	parser.add_argument("-i", "--iteration", type=int, help="iteration")
	parser.add_argument("-gr", "--greedy", action="store_true", help="greedy search")
	parser.add_argument("-un", "--uniform", action="store_true", help="uniform search")
	parser.add_argument("-t", "--time", action="store_true", help="time")
	parser.add_argument("-hf", "--heuristic", default="Manhattan", choices=["Manhattan", "Euclidian", "Tiles out-of-place"], help="Heuristic function choice, (default: %(default)s)")
	args = parser.parse_args()
	npuzzle(args)
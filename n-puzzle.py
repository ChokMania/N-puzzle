import argparse
import generator, check

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--map", type=check.file, help="")
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
	if check.is_solvable(args.map, args.verbose) == False:
		print("Puzzle is unsolvable")
		exit()
	#solver

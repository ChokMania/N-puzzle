import argparse
import generator, check

def manager(args):
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
	h_dic = {0:"Manhattan Distance", 1:"Other1", 2:"Other2"}
	while True:
		try:
			heuristic = int(input(f"Choose your heuristic function:\n1- {h_dic[0]}\n2- {h_dic[1]}\n3- {h_dic[2]}\n\nChoice: ")) - 1
			if heuristic > 2 or heuristic < 0:
				raise ValueError
			break 
		except ValueError as e:
			print("Select one of the possibilities")
	if args.verbose == True:
		print(f"\nHeuristic function : {h_dic[heuristic]}")
	return args.map, heuristic

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--map", type=check.file, help="")
	parser.add_argument("-v", "--visu", action="store_true", help="Enable visualisation")
	parser.add_argument("-vb", "--verbose", action="store_true", help="verbose")
	parser.add_argument("-g", "--generate", type=int, help="Generate")
	parser.add_argument("-i", "--iteration", type=int, help="iteration")
	parser.add_argument("-g", "--greedy", action="store_true", help="greedy search")
	parser.add_argument("-t", "--time", action="store_true", help="time")
	args = parser.parse_args()
	grid, heuristic = manager(args)
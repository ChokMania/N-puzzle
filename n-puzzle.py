import sys, random, argparse, re
import numpy as np
import generator

def check_file(file):
	try:
		with open(file, "r") as f:
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
			if i != size + 1 or not np.array_equal(np.sort(np.concatenate(array)), np.array(range(0, size * size))):
				raise ValueError()
			return array.transpose()
	except:
		print("Error")
		exit()


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--map", type=check_file, help="")
	parser.add_argument("-v", "--visu", action="store_true", help="Enable visualisation")
	parser.add_argument("-g", "--generate", type=int, help="Generate")
	parser.add_argument("-i", "--iteration", type=int, help="iteration")
	args = parser.parse_args()
	if args.map is None:
		if args.generate == None:
			n = 3
			print("Puzzle has been created with size = 3 by default", end="")
		else:
			n = int(args.generate)
			print(f"Puzzle has been created with size = {n}", end="")
		i = int(args.iteration) if args.iteration is not None and int(args.iteration) < 1 else 100
		print(f" and mixed with {i} iterations")
		solution = generator.gen_puzzle(n, i)
		print(solution)
	else :
		print(args.map)

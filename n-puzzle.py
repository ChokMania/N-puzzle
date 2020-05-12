import sys
import random
import numpy as np
import generator
import argparse
import re

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
			return array
	except:
		print("Error")
		exit()


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--map", type=check_file, help="")
	parser.add_argument("-v", "--visu", action="store_true", help="Enable visualisation")
	parser.add_argument("-g", "--generate", type=int, help="Generate")
	args = parser.parse_args()
	if args.map is None:
		if args.generate == None:
			n = 3
			print("Puzzle has been created with size = 3 by default")
		else:
			n = int(args.generate)
			print(f"Puzzle has been created with size = {n}")
		solution = generator.gen_solution(n)
		print(solution)
	else :
		print(args.map)

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
			for line in ds:
				line = re.sub(r"[\s\t]+", ' ', line).strip()
				if line.strip()[0] != "#":
					if i == 0:
						n = line.split()
						if len(n) != 1:
							raise ValueError()
						array = np.zeros((int(n[0]), int(n[0])))
					else:
						array[i - 1] = list(eval(line.replace(" ", ", ")))
					i += 1
			#print(f"FILE : \n{data}\n")
			#print(f"Array returned : \n{array}\n")
			#print(f"Comments: \n{comments}")
			return array
	except ValueError as e:
		print(e)
		print("Error only one number on first line of puzzle for the size")
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


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

def is_solvable(map) :
	map2 = np.int64(map)
	shape = utility.get_empty(np.int64(map))
	map2[shape[1]][shape[0]] = -1
	arr = generator.gen_line(map.shape[0], map2)
	inversion = 0
	for i in range(len(arr) - 1):
		count = 0
		if arr[i] != 0:
			for j in range(i + 1, len(arr)) :
				if arr[i] > arr[j] and arr[j] != 0:
					count += 1
			#print(f"the {arr[i]} gives us {count} inversions")
			inversion += count
	blank = int(map.shape[0]) - int(utility.get_empty(np.int64(map))[1])
	print(f"Array : {arr}\nShape : {map.shape[0]}\nBlank Position : {blank}\nCount of inversions: {inversion}\n\n")
	#print(f"MOD:\nmap.shape : {map.shape[0] % 2}\tblank : {blank % 2}\t"
	print(f"inversion : {inversion % 2}")
	if map.shape[0] % 2 == 1 and inversion % 2 == 0:
		print("Solvable")
	elif map.shape[0] % 2 == 0 and blank % 2 == 0 and inversion % 2 == 1:
		print("Solvable")
	elif map.shape[0] % 2 == 0 and blank % 2 == 1 and inversion % 2 == 0:
		print("Solvable")
	else:
		print("Unsolvable")
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
			n = 4
			print(f"Puzzle has been created with size = {n} by default", end="")
		else:
			n = int(args.generate)
			print(f"Puzzle has been created with size = {n}", end="")
		i = int(args.iteration) if args.iteration is not None and int(args.iteration) < 1 else 100
		print(f" and mixed with {i} iterations")
		map = generator.gen_puzzle(n, i)
		is_solvable(map)
	else :
		is_solvable(args.map)



# n-puzzle[(subject)](https://cdn.intra.42.fr/pdf/pdf/13342/en.subject.pdf)

## Introduction

The goal of this project is to solve the N-puzzle ("taquin" in French) game using the A* search algorithm or one of its variants.

You start with a square board made up of N*N cells. One of these cells will be empty, the others will contain numbers, starting from 1, that will be unique in this instance of the puzzle.

Your search algorithm will have to find a valid sequence of moves in order to reach the final state, a.k.a the "snail solution", which depends on the size of the puzzle (Example below). While there will be no direct evaluation of its performance in this instance of the project, it has to have at least a vaguely reasonable perfomance : Taking a few second to solve a 3-puzzle is pushing it, ten seconds is unacceptable.
The only move one can do in the N-puzzle is to swap the empty cell with one of its neighbors (No diagonals, of course. Imagine you’re sliding a block with a number on it towards an empty space).

## Objective

Implement the A* search algorithm (or one of its variants, you’re free to choose) to solve an N-puzzle, with the following constraints: 3 N-Puzzle Solve it better than a 60-year-old drunkard

• You have to manage various puzzle sizes (3, 4, 5, 17, etc ...). The higher your program can go without dying a horrible, horrible death, the better.

• You have to manage both randomly determined states (of your own generation of course), or input files that specify a starting board, the format of which is described in the appendix.

• The cost associated with each transition is always 1. 

• The user must be able to choose between at LEAST 3 (relevant) heuristic functions. The Manhattan-distance 		heuristic is mandatory, the other two are up to you. By "relevant" we mean they must be admissible (Read up on what this means) and they must be something other than "just return a random value because #YOLO".
 
 • At the end of the search, the program has to provide the following values: 
 ◦ Total number of states ever selected in the "opened" set (complexity in time) 
◦ Maximum number of states ever represented in memory at the same time during the search (complexity in 		size)
◦ Number of moves required to transition from the initial state to the final state, according to the search
◦ The ordered sequence of states that make up the solution, according to the search
◦ The puzzle may be unsolvable, in which case you have to inform the user and exit

### Install
<pre>
<code>https://github.com/ChokMania/N-puzzle.git
python -m pip install -r requirements.txt</code></pre> 

### Usage
<pre><code>
usage: n-puzzle.py [-h] [-m file] [-vi] [-vb] [-g size] [-i number]
                   [-gr | -un] [-d] [-t]
                   [-hf {Manhattan,Euclidian,Tiles out-of-place}]

optional arguments:
  -h, --help            show this help message and exit
  -m file, --map file
  -vi, --visu           Enable visualization
  -vb, --verbose        Enable verbose (may slow the algorithm down)
  -g size, --generate size
                        Generate a n-size puzzle
  -i number, --iteration number
                        Choose the number of scrambling moves
  -gr, --greedy         Enable greedy search
  -un, --uniform        Enable uniform-cost search
  -d, --debug
  -t, --time            Print the algorithm's execution time
  -hf {Manhattan,Euclidian,Tiles out-of-place},
	  --heuristic {Manhattan,Euclidian,Tiles out-of-place}
						Heuristic function choice, (default: Manhattan)
</code></pre>

## Authors
[Aleksi Gautier](https://github.com/Kelias-42) et [Julien Dumay](https://github.com/ChokMania/)

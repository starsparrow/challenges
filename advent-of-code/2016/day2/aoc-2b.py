#! /usr/bin/env python

# Advent of Code - Day 2: Bathroom Security - Puzzle A
# starsparrow

# Get our keypress instructions from the input file
f = open('input', 'r')
instructions = [list(line.strip()) for line in f.readlines()]
f.close()

# Set up our button relations...maybe there's a more clever way to do this?
buttonrel = { # The only thing different about puzzle B is a more complex map
	1: {'U': 1, 'D': 3, 'L': 1, 'R': 1},
	2: {'U': 2, 'D': 6, 'L': 2, 'R': 3},
	3: {'U': 1, 'D': 7, 'L': 2, 'R': 4},
	4: {'U': 4, 'D': 8, 'L': 3, 'R': 4},
	5: {'U': 5, 'D': 5, 'L': 5, 'R': 6},
	6: {'U': 2, 'D': 'A', 'L': 5, 'R': 7},
	7: {'U': 3, 'D': 'B', 'L': 6, 'R': 8},
	8: {'U': 4, 'D': 'C', 'L': 7, 'R': 9},
	9: {'U': 9, 'D': 9, 'L': 8, 'R': 9},
	'A': {'U': 6, 'D': 'A', 'L': 'A', 'R': 'B'},
	'B': {'U': 7, 'D': 'D', 'L': 'A', 'R': 'C'},
	'C': {'U': 8, 'D': 'C', 'L': 'B', 'R': 'C'},
	'D': {'U': 'B', 'D': 'D', 'L': 'D', 'R': 'D'}
}

num_to_press = 5 # The number we always start from
code = [] # Initialize the final code 

# Main section
for line in instructions:
	for instruction in line:
		num_to_press = buttonrel[num_to_press][instruction]
	code.append(num_to_press)

print(code)		

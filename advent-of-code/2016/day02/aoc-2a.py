#! /usr/bin/env python

# Advent of Code - Day 2: Bathroom Security - Puzzle A
# starsparrow

# Get our keypress instructions from the input file
f = open('input', 'r')
instructions = [list(line.strip()) for line in f.readlines()]
f.close()

# Set up our button relations...maybe there's a more clever way to do this?
buttonrel = {
	1: {'U': 1, 'D': 4, 'L': 1, 'R': 2},
	2: {'U': 2, 'D': 5, 'L': 1, 'R': 3},
	3: {'U': 3, 'D': 6, 'L': 2, 'R': 3},
	4: {'U': 1, 'D': 7, 'L': 4, 'R': 5},
	5: {'U': 2, 'D': 8, 'L': 4, 'R': 6},
	6: {'U': 3, 'D': 9, 'L': 5, 'R': 6},
	7: {'U': 4, 'D': 7, 'L': 7, 'R': 8},
	8: {'U': 5, 'D': 8, 'L': 7, 'R': 9},
	9: {'U': 6, 'D': 9, 'L': 8, 'R': 9}
}

num_to_press = 5 # The number we always start from
code = [] # Initialize the final code 

# Main section
for line in instructions:
	for instruction in line:
		num_to_press = buttonrel[num_to_press][instruction]
	code.append(num_to_press)

print(code)

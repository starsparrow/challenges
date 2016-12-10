#! /usr/bin/env python

# Advent of Code - Day 3: Squares With Three Sides - Puzzle A
# starsparrow

# Read in our list of triangle sides
f = open('input', 'r')
triangles = [line.strip() for line in f.readlines()]
f.close()

# Initialize our list of valid triangles to count at the end
valid_triangles = []

# Loop through each row of sides, clean up whitespace, and do the math
# to determine whether or not each row represents a valid triange. If
# so, append to our list of valid triangles.
for triangle in triangles:
	sides = triangle.split(" ")
	while '' in sides:
		sides.remove('')
	for side in sides:
		sides[sides.index(side)] = int(side)
	if ((sides[0] + sides[1] > sides[2]) and
		(sides[1] + sides[2] > sides[0]) and
		(sides[0] + sides[2] > sides[1])):
			valid_triangles.append(sides)

# Get our answer!
print(len(valid_triangles))

#! /usr/bin/env python

# Advent of Code - Day 3: Squares With Three Sides - Puzzle A
# starsparrow

f = open('input', 'r')
triangles = [line.strip() for line in f.readlines()]
f.close()

valid_triangles = []
invalid_triangles = []

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
	else:
		invalid_triangles.append(sides)

print(len(valid_triangles))

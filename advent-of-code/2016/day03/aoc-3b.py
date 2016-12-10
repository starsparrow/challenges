#! /usr/bin/env python

# Advent of Code - Day 3: Squares With Three Sides - Puzzle B
# starsparrow

# Read in our list of triangle sides
f = open('input', 'r')
rows = [line.strip() for line in f.readlines()]
f.close()

# There are three columns, so three things we need to loop through later
# Maybe I could have done this as a dict to make things a bit cleaner?
staging_a = []
staging_b = []
staging_c = []

# Initialize our list of valid triangles to count at the end
valid_triangles = []

# Clean up whitespace and get all of the column data into staging lists
for row in rows:
	sides = row.split(" ")
	while '' in sides:
		sides.remove('')
	for side in sides:
		sides[sides.index(side)] = int(side)
	staging_a.append(sides[0])
	staging_b.append(sides[1])
	staging_c.append(sides[2])

# Go through each staging list (representing one column in original data) and
# group them into threes. If the three sides represent a valid triangle,
# throw them into a sublist and append to valid_triangles
for queue in [staging_a, staging_b, staging_c]:
	while len(queue) > 0:
		if ((queue[0] + queue[1] > queue[2]) and
			(queue[1] + queue[2] > queue[0]) and
			(queue[0] + queue[2] > queue[1])):
				valid_triangles.append([
					queue[0],
					queue[1],
					queue[2]
				])
		for _ in range(0,3):
			queue.remove(queue[0])

# Get our answer!
print(len(valid_triangles))

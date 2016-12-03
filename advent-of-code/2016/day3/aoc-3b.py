#! /usr/bin/env python

# Advent of Code - Day 3: Squares With Three Sides - Puzzle B
# starsparrow

f = open('input', 'r')
rows = [line.strip() for line in f.readlines()]
f.close()

staging_a = []
staging_b = []
staging_c = []

valid_triangles = []

for row in rows:
	sides = row.split(" ")
	while '' in sides:
		sides.remove('')
	for side in sides:
		sides[sides.index(side)] = int(side)
	staging_a.append(sides[0])
	staging_b.append(sides[1])
	staging_c.append(sides[2])

for queue in [staging_a, staging_b, staging_c]:
	while len(queue) > 0:
		if ((queue[0] + queue[1] > queue[2]) and
			(queue[1] + queue[2] > queue[0]) and
			(queue[0] + queue[2] > queue[1])):
				valid_triangles.append([queue[0],
					queue[1],
					queue[2]])
		else:
			invalid_triangles.append([queue[0],
					queue[1],
					queue[2]])
		for _ in range(0,3):
			queue.remove(queue[0])

print(len(valid_triangles))

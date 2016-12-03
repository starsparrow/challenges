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
invalid_triangles = []

for row in rows:
	sides = row.split(" ")
	while '' in sides:
		sides.remove('')
	for side in sides:
		sides[sides.index(side)] = int(side)
	staging_a.append(sides[0])
	staging_b.append(sides[1])
	staging_c.append(sides[2])

while len(staging_a) > 0:
	if ((staging_a[0] + staging_a[1] > staging_a[2]) and
		(staging_a[1] + staging_a[2] > staging_a[0]) and
		(staging_a[0] + staging_a[2] > staging_a[1])):
			valid_triangles.append([staging_a[0],
				staging_a[1],
				staging_a[2]])
	else:
		invalid_triangles.append([staging_a[0],
				staging_a[1],
				staging_a[2]])
	staging_a.remove(staging_a[0])
	staging_a.remove(staging_a[0])
	staging_a.remove(staging_a[0])

print(len(valid_triangles))
	

#! /usr/bin/env python

# Advent of Code - Day 1: No Time for a Taxicab - Puzzle A
# starsparrow

# Read and parse data for later use by our functions
f = open('input', 'r')
directions = f.read().split(sep=", ")
f.close()

for direction in directions:
	directions[directions.index(direction)] = [direction[0:1],
		int(direction[1:len(direction)])]

# Initialize LZ
location = [0, 0]
heading = 0

def turn(currentheading, turndirection):
	'''Takes current heading, the direction to turn (R/L),
	and returns new heading in degrees'''
	
	if (turndirection == 'R'):
		newheading = currentheading + 90
	elif (turndirection == 'L'):
		newheading = currentheading - 90

	# Handle heading overflow
	if (newheading == 360):
		newheading = 0
	elif (newheading == -90):
		newheading = 270

	return newheading

def go(location, currentheading, blocks):
	'''Takes current location, direction faced, and number of blocks to travel,
	then travels forward that many blocks. Returns end location'''

	if (currentheading == 0):
		newlocation = [location[0], location[1] + blocks]
	elif (currentheading == 90):
		newlocation = [location[0] + blocks, location[1]]
	elif (currentheading == 180):
		newlocation = [location[0], location[1] - blocks]
	elif (currentheading == 270):
		newlocation = [location[0] - blocks, location[1]]

	return newlocation

def travel(location, heading):
	'''Takes start location and follows all instructions in input file
	and returns final location'''

	for direction in directions:
		heading = turn(heading, direction[0])
		location = go(location, heading, direction[1])
	return location

def taxidistance(a, b):
	'''Gets the distance from point a to point b in blocks'''

	return sum([abs(a[0]), abs(a[1]), abs(b[0]), abs(b[1])])


# Main section
print("End location: {0}\nDistance from LZ: {1}".format(travel(location, heading),
	taxidistance(location, travel(location, heading))))
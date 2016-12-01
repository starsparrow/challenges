#! /usr/bin/env python

# Advent of Code - Day 1: No Time for a Taxicab - Puzzle B
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

# Let's log our journey
travellog = []

# How 'bout some functions?
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

def move(location, currentheading, blocks):
	'''Takes current location, direction faced, and number of blocks to travel,
	then travels forward that many blocks, logging each step along the way.
	Returns end location'''

	for i in range(0, blocks):
		if (currentheading == 0):
			location = [location[0], location[1] + 1]
		elif (currentheading == 90):
			location = [location[0] + 1, location[1]]
		elif (currentheading == 180):
			location = [location[0], location[1] - 1]
		elif (currentheading == 270):
			location = [location[0] - 1, location[1]]	
		
		if (location in travellog):
			visitedlocation = location
			visitedlocation.append('*')
			travellog.append(visitedlocation)
		else:
			travellog.append(location)
	
	return location

def journey(location, heading):
	'''Takes start location and follows all instructions in input file
	and returns final location'''

	for direction in directions:
		heading = turn(heading, direction[0])
		location = move(location, heading, direction[1])
	return location

def taxidistance(a, b):
	'''Gets the distance from point a to point b in blocks'''

	return sum([abs(a[0]), abs(a[1]), abs(b[0]), abs(b[1])])

# Main section
endlocation = journey([0,0], 0)

print("End location: {0}\nDistance from LZ: {1}".format(endlocation,
	taxidistance(location, endlocation)))

for entry in travellog:
	if (len(entry) > 2):
		print("{}\t\t{}\t\tYou've been here before. Distance from origin: {}".format(
			travellog.index(entry), entry, taxidistance(location, entry)))
	else:
		print("{}\t\t{}".format(travellog.index(entry), entry))

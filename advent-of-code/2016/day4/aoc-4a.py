#! /usr/bin/env python

# Advent of Code 2016 - Day 4: Security Through Obscurity - Puzzle A
# starsparrow

import collections

# Read in our room data
f = open('input', 'r')
data = [line.strip() for line in f.readlines()]
f.close()

# Parse the data into a dict for easier access later
rooms = {}
for line in [line.split('-') for line in data]:
    lastitem = line[len(line) - 1].split('[')
    name = "".join(line[:line.index(line[len(line) - 1])])
    sectorid = lastitem[0]
    roomhash = lastitem[1].rstrip(']')
    rooms[name] = {'sectorid': sectorid, 'hash': roomhash}

def is_real_room(roomname, roomhash):
    frequency = {}
    for letter in list(roomname):
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1
    print(frequency)

# Main section
#for room in rooms:
#print("{} {} {}".format(room,
#                            rooms[room]['sectorid'],
#                            rooms[room]['hash']))

print(is_real_room('aaaabbnnmmiqweryp', 'asdf'))
    

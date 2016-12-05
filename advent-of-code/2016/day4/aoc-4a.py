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
    '''Calculate roomname hash, compare to provided hash, return true/false'''
    frequency = {}
    for letter in list(roomname):
        if letter not in frequency:
            frequency[letter] = 1
        else:
            frequency[letter] += 1
    highest_freq = sorted(frequency.values(), reverse=True)[0]

    reverselookup = {}
    for number in range(highest_freq, 0, -1):
       reverselookup[number] = []
    for letter in frequency:
        reverselookup[frequency[letter]].append(letter)

    mostcommon = []
    longhash = []
    for number in range(highest_freq, 0, -1):
        mostcommon.append(sorted(reverselookup[number]))
    mostcommon = [item for item in mostcommon if len(item) > 0] # Remove empties
    for item in mostcommon:
        longhash += item

    return roomhash == "".join(longhash)[:5]

# Main section
sectorids = []
for room in rooms:
    if is_real_room(room, rooms[room]['hash']):
        sectorids.append(int(rooms[room]['sectorid']))

print(sum(sectorids))

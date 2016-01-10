# starsparrow
# adventofcode puzzle 7-1

import re
import string

# Read in the text file of instructions
with open('input.txt', 'r') as f:
    while True:
        read_data = f.read().splitlines()
        if not read_data:
            break
        stringlist = read_data

# From the list of text commands, split into [source/operation, dest] list
commands = []
for j in stringlist:    
    commands.append(j.split(' -> '))
for command in commands:
    command[0] = command[0].split(' ')        
        
# Initialize all of our wires with signals of 0 (may not use all wires)
wires = {}
letters = list(string.ascii_lowercase)
for letter in letters:
    wires['%s' % (letter)] = 0
for letter1 in letters:
    for letter2 in letters:
        wires['%s%s' % (letter1, letter2)] = 0

# If the source is a wire, translate it to its signal, or make signal an int
def getsignal(source):
    if re.search('[0-9]+', str(source)):
        return int(source)
    elif re.search('[a-z]+', str(source)):
        return int(wires[source])

# Direct signal input    
def opdirect(signal, dest):
    wires[dest] = signal

# NOT operation        
def opnot(signal, dest):
    wires[dest] = ~ signal

# AND operation    
def opand(signal1, signal2, dest):
    wires[dest] = signal1 & signal2

# OR operation    
def opor(signal1, signal2, dest):
    wires[dest] = signal1 | signal2

# LSHIFT operation    
def oplshift(signal1, signal2, dest):
    wires[dest] = signal1 << signal2

# RSHIFT operation    
def oprshift(signal1, signal2, dest):
    wires[dest] += signal1 >> signal2

# Determine what operation to do for each command

# testcommands = [[[100], 'a']]

for command in commands:
    if str(command[0][0]) == 'NOT':
        signal = getsignal(command[0][1])
        dest = command[1]
        opnot(signal, dest)
    elif len(command[0]) == 1:
        signal = getsignal(command[0][0])
        dest = command[1]
        opdirect(signal, dest)
    elif len(command[0]) == 3:
        signal1 = getsignal(command[0][0])
        signal2 = getsignal(command[0][2])
        dest = command[1]
        operation = command[0][1]
        if operation == 'AND':
            opand(signal1, signal2, dest)
        elif operation == 'OR':
            opor(signal1, signal2, dest)
        elif operation == 'LSHIFT':
            oplshift(signal1, signal2, dest)
        elif operation == 'RSHIFT':
            oprshift(signal1, signal2, dest)

for wire in sorted(wires):
	print('%s : %s' % (wire, wires[wire]))     

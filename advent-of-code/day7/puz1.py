# starsparrow
# adventofcode puzzle 7-1

import re
import string

INSTRUCTION-SET = ['AND', 'OR', 'NOT', 'RSHIFT', 'LSHIFT']

# Read in the text file of instructions
with open('input.txt', 'r') as f:
    while True:
        read_data = f.read().splitlines()
        if not read_data:
            break
        stringlist = read_data

# From the list of text commands, split into [source/operation, dest] list
commands = []
for string in stringlist:    
    commands.append(string.split(' -> '))
for command in commands:
    command[0] = command[0].split(' ')        
        
# Initialize all of our wires with signals of 0 (may not use all wires)
wires = {}
letters = list(string.ascii_lowercase)
for letter1 in letters:
    for letter2 in letters:
        wires['%s%s' % (letter1, letter2)] = 0
        
# If the source is a wire, translate it to its signal, or make signal an int
def getsignal(source):
    if re.search('[0-9]+', source):
        return int(source)
    elif re.search('[a-z]+', source):
        return wires[source]

# Direct signal input    
def op-direct(signal, dest):
    pass

# NOT operation        
def op-not(signal, dest):
    pass

# AND operation    
def op-and(signal1, signal2, dest):
    pass

# OR operation    
def op-or(signal1, signal2, dest):
    pass

# LSHIFT operation    
def op-lshift(signal1, signal2, dest):
    pass

# RSHIFT operation    
def op-rshift(signal1, signal2, dest):
    pass

# Determine what operation to do for each command   
for command in commands:
    if command[0][0] == 'NOT':
        signal = getsignal(command[0][1])
        dest = command[1]
        op-not(signal, dest)
    elif len(command[0]) == 1:
        signal = getsignal(command[0][0])
        dest = getsignal(command[1])
        op-direct(signal, dest)
    elif len(command[0]) == 3:
        signal1 = getsignal(command[0][0])
        signal2 = getsignal(command[0][2])
        dest = command[1]
        operation = command[0][1]
        if operation == 'AND':
            op-and(signal1, signal2, dest)
        elif operation == 'OR':
            op-or(signal1, signal2, dest)
        elif operation == 'LSHIFT':
            op-lshift(signal1, signal2, dest)
        elif operation == 'RSHIFT':
            op-rshift(signal1, signal2, dest)
        
        
    
        
        
        
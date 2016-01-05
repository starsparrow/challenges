# starsparrow
# adventofcode puzzle 6-1

import re

with open('input.txt', 'r') as f:
	while True:
		read_data = f.read().splitlines()
		if not read_data:
			break
		stringlist = read_data

for string in stringlist:
	print(string)
	
#example instructions:
#
#toggle 461,550 through 564,900
#turn off 370,39 through 425,839
#turn on 370,39 through 425,839

#pseudocode:
#
#if string contains toggle, trim left 7
#elif string contains turn off, trim left 9
#elif string contains turn on, trim left 8
#
#slice next 7 characters, trim space from right, those are the coords for one corner
#
#trim space (if there), through, and another space from left
#
#remainder is coords for other corner
# starsparrow
# adventofcode puzzle 5-2
# now with more regex!

import re

with open('input.txt', 'r') as f:
	while True:
		read_data = f.read().splitlines()
		if not read_data:
			break
		stringlist = read_data
	
def isNice(string):
	
	def twoDoubles(string):
		isMatch = False
		letters = list(string)
		
		combos = []
		i = 0
		while i < len(letters) - 1:
			combos.append('%s%s' % (letters[i], letters[i+1]))
			i += 1	
		
		for combo in combos:
			pattern = '%s.*%s' % (combo, combo)
			if re.search(pattern, string):
				isMatch = True
		return isMatch
	
	def hasSandwich(string):
		isMatch = False
		letters = list(string)
		for letter in letters:
			pattern = '%s.%s' % (letter, letter)
			if re.search(pattern, string):
				isMatch = True
		return isMatch
	
	if twoDoubles(string) and hasSandwich(string):
		return True

nicestrings = 0

for string in stringlist:
	if isNice(string):
		nicestrings += 1
		
print(nicestrings)
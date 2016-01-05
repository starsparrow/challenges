# starsparrow
# adventofcode puzzle 5-1

with open('input.txt', 'r') as f:
	while True:
		read_data = f.read().splitlines()
		if not read_data:
			break
		stringlist = read_data
	
def isNice(string):
	
	def threeVowels(string):
		vowels = ['a', 'e', 'i', 'o', 'u']
		vowelcount = 0
		for letter in list(string):
			if letter in vowels:
				vowelcount += 1
		
		if vowelcount > 2:
			return True
		else:
			return False
			
	def doubleLetter(string):
		containsdouble = 0
		for letter in list(string):
			if letter + letter in string:
				containsdouble += 1
		
		if containsdouble > 0:
			return True
		else:
			return False
			
	def badLetters(string):
		badcombos = ['ab', 'cd', 'pq', 'xy']
		containsbadcombo = 0
		for combo in badcombos:
			if combo in string:
				containsbadcombo += 1
		
		if containsbadcombo > 0:
			return True
		else:
			return False
	
	if threeVowels(string) and doubleLetter(string) and not badLetters(string):
		return 1
	else:
		return 0

		
nicestrings = 0

for string in stringlist:
	if isNice(string) == 1:
		nicestrings += 1
		
print(nicestrings)




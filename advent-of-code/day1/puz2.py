# starsparrow
# adventofcode puzzle 1-2

instructions = []

with open('puzzleinput.txt', 'r') as f:
	while True:
		read_data = f.read(1)
		if not read_data:
			break
		instructions.append(read_data)

position = 1
currentFloor = 0
targetFloor = -1
		
for i in instructions:
	if i == '(':
		currentFloor += 1
	elif i == ')':
		currentFloor -= 1
	else:
		print("Weird error that you shouldn't see")
	
	if currentFloor == targetFloor:
		print(position)
		break
	else:
		position += 1
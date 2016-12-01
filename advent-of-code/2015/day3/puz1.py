# starsparrow
# adventofcode puzzle 3-1

moves = []

with open('input.txt', 'r') as f:
	while True:
		read_data = f.read(1)
		if not read_data:
			break
		moves.append(read_data)
		
# print(moves)

x = 0
y = 0
map = {'0,0': 1}
	
def log(xcoord, ycoord, history):
	coords = str(xcoord) + ',' + str(ycoord)
	if coords in map:
		history[coords] += 1
	else:
		history[coords] = 1
	return history
	
for move in moves:
	if move == '^':
		y += 1
	elif move == 'v':
		y -= 1
	elif move == '<':
		x += 1
	elif move == '>':
		x -= 1
	else:
		print("Error that you shouldn't ever see")
	map = log(x,y,map)
		
		
print(len(map))

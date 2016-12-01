# starsparrow
# adventofcode puzzle 3-2

moves = []

with open('input.txt', 'r') as f:
	while True:
		read_data = f.read(1)
		if not read_data:
			break
		moves.append(read_data)
		
santaMoves = []
robosantaMoves = []

i = 1

for move in moves:
	if i % 2 == 1:
		santaMoves.append(move)
	else:
		robosantaMoves.append(move)
	i += 1

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

# Processing santa's moves first...	
for move in santaMoves:
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

# Reset starting coords for roboSanta moves
x = 0
y = 0

# Now to process roboSanta's moves...
for move in robosantaMoves:
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

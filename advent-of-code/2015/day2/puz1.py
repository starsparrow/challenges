# starsparrow
# adventofcode puzzle 2-1

with open('2-1input.txt', 'r') as f:
	while True:
		read_data = f.read().splitlines()
		if not read_data:
			break
		boxlist = read_data

		
totalArea = 0		

for box in boxlist:
		dimensions = box.split('x')
		
		l = int(dimensions[0])
		w = int(dimensions[1])
		h = int(dimensions[2])
		
		newDimensions = sorted([l, w, h])
		
		l = newDimensions[0]
		w = newDimensions[1]
		h = newDimensions[2]
		
		totalArea += (2*l*w + 2*w*h + 2*h*l + l*w)
		
print(totalArea)
		
		
		
		

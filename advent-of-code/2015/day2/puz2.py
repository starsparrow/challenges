# starsparrow
# adventofcode puzzle 2-2

with open('input.txt', 'r') as f:
	while True:
		read_data = f.read().splitlines()
		if not read_data:
			break
		boxlist = read_data

totalArea = 0
totalRibbon = 0

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
		totalRibbon += ((2*l + 2*w) + (l*w*h))
		
print(str(totalArea) + " square feet of paper needed")
print(str(totalRibbon) + " feet of ribbon needed")

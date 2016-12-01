# starsparrow
# adventofcode puzzle 6-1

# Read in the text file of lighting commands from Santa
with open('input.txt', 'r') as f:
    while True:
        read_data = f.read().splitlines()
        if not read_data:
            break
        stringlist = read_data

# Convert input data to list of lists with format [command, corner1, corner2]
commands = []
for string in stringlist:
    string = string.replace('turn ', '')
    string = string.replace(' through ', ' ')
    commands.append((string.split(' ')))

# Initialize the light grid    
lightgrid = {}
for i in range(0,1000000):
    lightgrid[i] = 0
    
# Return the lightid given the x,y coordinates of the light
def getlightid(coord):
    x = coord[0]
    y = coord[1]
    lightid = (1000 * y) + x
    return lightid

# Takes coords of corner lights and returns list of lightids for the rectangle
def getlightlist(corner1, corner2):    
    unpackedcorner1 = corner1.split(',')
    unpackedcorner2 = corner2.split(',')
    
    xmin = int(unpackedcorner1[0])
    xmax = int(unpackedcorner2[0])
    ymin = int(unpackedcorner1[1])
    ymax = int(unpackedcorner2[1])
    xcoordlist = []
    ycoordlist = []  
    for i in range(xmin, xmax + 1):
        xcoordlist.append(i)    
    for i in range(ymin, ymax + 1):
        ycoordlist.append(i)
    
    lightcoordlist = []
    for y in ycoordlist:
        for x in xcoordlist:
            lightcoordlist.append([x, y])
    
    lightidlist = []
    for lightcoord in lightcoordlist:
        lightidlist.append(getlightid(lightcoord))
    
    return lightidlist
    
# Take a lightid and manipulate it according to the supplied command
def operatelight(lightid, command):
    if command == 'on':
        lightgrid[lightid] = 1
    elif command == 'off':
        lightgrid[lightid] = 0
    elif command == 'toggle':
        lightgrid[lightid] = abs(lightgrid[lightid] - 1)
    else:
        print('Error! Invalid command "%s"' % command)
 
# Execute all of the commands
for command in commands:
    lights = getlightlist(command[1], command[2])
    for light in lights:
        operatelight(light, command[0])

print(sum(1 for j in lightgrid.values() if j == 1))
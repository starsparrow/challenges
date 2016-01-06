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
    unpackedcoord = coord.split(',')
    x = int(unpackedcoord[0])
    y = int(unpackedcoord[1])
    lightid = (1000 * y) + x
    return lightid

# Takes lightid of corner lights and returns a list of lightids for the square
## FIXME: RETURNS WAY TOO MANY LIGHTS BECAUSE I AM DUMB
def getlightlist(corner1, corner2):    
    lightlist = []
    if corner1 <= corner2:
        for i in range(corner1, corner2 + 1):
            lightlist.append(i)
    else:
        print('Error! corner 1 greater than corner 2. Clean up input file.')
    return lightlist
    
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
for command in testcommands:
    lights = getlightlist(getlightid(command[1]), getlightid(command[2]))
    for light in lights:
        operatelight(light, command[0])

print(sum(1 for j in lightgrid.values() if j == 1))


### TESTING ###        

testcommands = [['toggle', '0,0', '999,999']
               ,['off', '499,499', '500,500']
              ]
        
# # Execute all of the commands
# for command in testcommands:
    # lights = getlightlist(getlightid(command[1]), getlightid(command[2]))
    # for light in lights:
        # operatelight(light, command[0])

# for i in range(0,101):
    # print(lightgrid[i])      

# print(getlightlist(getlightid('499,499'), getlightid('500,500')))
    
# print(sum(1 for j in lightgrid.values() if j == 1))
        

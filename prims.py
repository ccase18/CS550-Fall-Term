#sources
	#https://stackoverflow.com/questions/19641579/python-convert-tuple-to-string - how to use tuples for coords
	#https://stackoverflow.com/questions/21867303/how-to-split-a-list-of-2-tuples-into-two-lists - how to use tuples for coords

from random import * 

def drawBorders(height, width, grid): #draws the borders for the grid
	i = 2 #since we have to leave actual spaces inbetween each border of the grid, each intersection is prointed every 2 spots on the grid. 
	while i < (width-2): #top 
		grid[0][i] = '═╦═' #every other spot an intersection is printed
		i = i + 2

	i = 1
	while i < (width-1): #top
		grid[0][i] = '═══'#at every other spot, a blank or stright connector is printed. these connectors are the borders between cells and what are actually removed
		i = i + 2

	i = 2
	while i < (width-2): #bottom
		grid[height-1][i] = '═╩═'
		i = i+2

	i = 1
	while i < (width-1): #bottom
		grid[height-1][i] = '═══'
		i = i+2


	i = 2
	while i < (height-2): #left
		grid[i][0] = '╠═'
		i = i+2

	i = 1
	while i < (height-1): #left
		grid[i][0] = '║ '
		i = i+2

	i = 2
	z = 2
	while i < (height-2): #left
		while z < (width - 1):
			grid [i][z] = '   '
			z = z + 2
		i = i + 2
		z = 2

	i = 2
	z = 1
	while i < (height-2): #middle
		while z < (width - 1):
			grid [i][z] = '═══'
			z = z + 2
		i = i + 2
		z = 1

	i = 2
	z = 2
	while i < (height-1): #middle
		while z < (width - 1):
			grid [i][z] = '═╬═'
			z = z + 2
		i = i + 2
		z = 2

	i = 1
	z = 1
	while i < (height-1): #middle
		while z < (width - 1):
			grid [i][z] = '   '
			z = z + 2
		i = i + 2
		z = 1

	i = 1
	z = 2
	while i < (height-1): #middle
		while z < (width - 1):
			grid [i][z] = ' ║ '
			z = z + 2
		i = i + 2
		z = 2


	i = 2
	while i < (height-2): #right
		grid[i][width-1] = '═╣'
		i = i+2

	i = 1
	while i < (height-1): #right
		grid[i][width-1] = ' ║'
		i = i + 2

	grid[0][width-1] = '═╗' #topright

	grid[0][0] = '╔═' #topleft

	grid[height-1][0] = '╚═' #bottomleft

	grid[height-1][width-1] = '═╝' #bottomright


def printGrid(alist): #function that prints out the grid
	for i in range(len(alist)):
		for j in range(len(alist[0])):
			print(alist[i][j], end='')
		print('')

def markPoint(x,y): #intilaizer
		inCell.append(tuple([y,x])) #add the coords to incell 
		addFrontier(x,y)#run addfrontier
	


def addFrontier(x,y): #if a cell isnt a border, or already an incell or frontier cell, add it to the frontier
	if tuple([y,x-2]) not in frontier and tuple([y,x-2]) not in inCell and x-2 > 0:
		frontier.append(tuple([y,x-2])) 
		#print('frontleft')
	if tuple([y,x+2]) not in frontier and tuple([y,x+2]) not in inCell and x+2 < width:
		frontier.append(tuple([y,x+2])) 
		#print('frontright')
	if tuple([y-2,x]) not in frontier and tuple([y-2,x]) not in inCell and y-2 > 0:
		frontier.append(tuple([y-2,x])) 
		#print('frontdown')
	if tuple([y+2,x]) not in frontier and tuple([y+2,x]) not in inCell and  y+2 < height:
		frontier.append(tuple([y+2,x])) 
		#print('frontup')

	newFront(frontier)


def newFront(frontier): 
	new = randrange(0,(len(frontier))) #pick a random set of coords from the frontier
	atuple = tuple(frontier[new])
	ycoords,xcoords = map(list,zip(*frontier)) #https://stackoverflow.com/questions/21867303/how-to-split-a-list-of-2-tuples-into-two-lists
	x = xcoords[new]
	y = ycoords[new]
	
	if len(frontier) != 0:
		frontier.remove(atuple)

		if tuple([y,x-2]) in inCell: #based on where the incell which touches the chosen frontier cell, get the x and y coords
			nearestCell(tuple([y,x-2]),y,x)

		if tuple([y,x+2]) in inCell:
			nearestCell(tuple([y,x+2]),y,x)

		if tuple([y+2,x]) in inCell:
			nearestCell(tuple([y+2,x]),y,x)

		if tuple([y-2,x]) in inCell:
			nearestCell(tuple([y-2,x]),y,x)

def nearestCell(tuple,y,x): #gets the x and y coords of the incell
	iny,inx = tuple	
	if len(frontier) != 0:
		createWalls(iny,inx,y,x) #change the walls based on those coords


def createWalls(iny,inx,y,x): #based on where the incell is relative to the chosen front cell, change the walls 
	#print(iny,inx,y,x)
	if x > inx:
		#print('right')
		grid [y][x-1] = '   '
		markPoint(x,y) #repeat the function for the new frontier cell with the wall removed - end result is a maze
	elif x < inx:
		#print('left')
		grid [y][x+1] = '   '
		markPoint(x,y)
	elif y < iny:
		#print('down')
		grid [y+1][x] = '   '
		markPoint(x,y)
	elif y > iny:
		#print('up')
		grid [y-1][x] = '   '
		markPoint(x,y)
		

def inCellRight(x,y,inx,iny):
	#print('right')
	grid [x+1][y] = '   '
	markPoint(x,y)

def inCellLeft(x,y,inx,iny,):
	#print('left')
	grid [x-1][y] = '   '
	markPoint(x,y)

def inCellDown(x,y,inx,iny):
	#print('down')
	grid [x][y-1] = '   '
	markPoint(x,y)
 
def inCellUp(x,y,inx,iny):
	#print('right')
	grid [x][y+1] = '   '
	markPoint(x,y)
	

def createEndpoints(): #this removes the corners to give the maze a start and end point in the corners
	grid [0][0] = '  '
	if grid [0][1] == ' ╠═':
		grid [0][1] = ' ╔═'
	if grid [1][0] == '═╦═':
		grid[1][0] = ' ╔═'

	grid [height-1][width-1] = '   '
	if grid [height-2][width-1] == '═╣ ':
		grid [height-2][width-1] = '═╝ '
	if grid [height-1][width-2] == '═╩═':
		grid [height-1][width-2] = '═╝ '


try: #gets the width 
	width = int(input('Enter a width for the maze from 5 and 13: '))
except ValueError:
	width = int(input('Please enter an integer: '))

try: #gets the height
	height = int(input('Enter a height for the maze from 5 and 13: '))
except ValueError:
	height = int(input('Please enter an integer: '))

if width > 13: #width and height have to be between 5 and 14
	width = 13
	print('width changed to 14')
elif width < 5:
	width = 5
	print('width changed to 5')

if height > 13:
	height = 13
	print('height changed to 14')
elif height < 5:
	height = 5
	print('height changed to 5')

grid = [] #creates the grid
frontier = [] #creates the frontier list
inCell = [] #creates the incell list
borders = [] #creates a list of borders

i = 0
height = ((int(height) * 2) + 1) #multiplies the height and width by two 
width = ((int(width) * 2) + 1)
for i in range (0,height): #fills the grid
	row = [' '] * width
	grid.append(row)

for i in range(0,width-1): #fills the borders list with all borders
	borders.append(tuple([i,0]))
	borders.append(tuple([i,height-1]))
for i in range(0,height-1):
	borders.append(tuple([0,i]))
	borders.append(tuple([height-1,i]))

drawBorders(height, width, grid) #creates the grid

markPoint(1,1) #chooses at the top left of the grid and marks it as an incell 

createEndpoints() #create the endpoints

printGrid(grid) #prints out the finished grid
import itertools
world = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]

def isAlive(input, row, column):
	if(row<0 or column<0):
		return False
	try:
		if(input[row][column]==1):
			return True
	except IndexError:
		return False


def get_alive_nighbours_count(arr,row,column):
	allcells = list(itertools.product([row-1,row,row+1],[column-1,column,column+1]))
	#print(allcells)
	neighbours = [position for position in allcells if (position[0], position[1]) != (row, column) ]
	#print(neighbours)
	alive_nighbours = [position for position in neighbours if isAlive(arr,position[0],position[1])]
	#print(alive_nighbours)
	return len(alive_nighbours)

def print_world(pw):
	for r in pw:
		for cell in r:
			print(cell, end='')
		print()
def get_next_gen_value(w1,row,col):
	alive_nighbours = get_alive_nighbours_count(w1,row,col)
	if w1[row][col]==0 and alive_nighbours==3:
		return 1
	elif w1[row][col]==1 and (alive_nighbours==3 or alive_nighbours==2):
		return 1
	else:
		return 0

def get_next_generation(w):
	new_world = [ [get_next_gen_value(w,r,c) for r in range(len(w))] for c in range(len(w[0])) ]
	return new_world



#print(get_neighbours(1,1))
print(get_alive_nighbours_count(world,1,1)) # 2
print(get_alive_nighbours_count(world,0,0)) # 0
print(get_alive_nighbours_count(world,2,1)) # 3
print(get_alive_nighbours_count(world,2,2)) # 2
print('*******')
print_world(world)
print('*******')
print_world(get_next_generation(world))

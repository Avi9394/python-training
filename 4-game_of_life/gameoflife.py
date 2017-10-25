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
	
def get_neighbours(row,column):
	n = list(itertools.product([row-1,row,row+1],[column-1,column,column+1]))
	n.remove((row,column))
	return n


def get_alive_nighbours_count(arr,neighbours):
	count=0
	for p in neighbours:
		if(isAlive(arr,p[0],p[1])):
			count= count+1
	return count
def print_world(world):
	for r in world:
		for cell in r:
			print(cell, end='')
		print()

def get_next_generation(w):
	#new_world = w
	new_world = []
	#print_world(world)
	for r in range(len(w)):
		row=[]
		for c in range(len(w[0])):
			alive_nighbours=get_alive_nighbours_count(w,get_neighbours(r,c))
			#print(alive_nighbours)
			if w[r][c]==0 and alive_nighbours==3 :
				row.append(1)
			elif w[r][c]==1 and (alive_nighbours==3 or alive_nighbours==2) :
				row.append(1)
			else:
				row.append(0)
		new_world.append(row)
	return new_world



#print(get_neighbours(1,1))
#print(get_alive_nighbours_count(world,get_neighbours(1,1))) # 0
print('*******')
print_world(world)
print('*******')
print_world(get_next_generation(world))
#print(get_alive_nighbours_count(world,get_neighbours(0,0))) # 0
#print(get_alive_nighbours_count(world,get_neighbours(2,1))) # 3
#print(get_alive_nighbours_count(world,get_neighbours(2,2))) # 2
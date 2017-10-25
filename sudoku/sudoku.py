class IllegalBoardStateException:
	pass

class Cell:
	def __init__(self, position):
		self.position = position
		self.possibilities = [1 ,2, 3, 4, 5, 6, 7, 8, 9]
	@property
	def value(self):
		if len(self.possibilities)==1:
			return self.possibilities[0];

	@value.setter
	def value(self, val):
		self.possibilities = [val]

	def eliminate(self, val):
		try:
			self.possibilities.remove(val)
		except ValueError:
			pass
	def block(self):
		return (self.position[0] // 3) * 3 + (self.position[1] // 3)
	def is_same_row(self, cell2):
		return self.position[0] == cell2.position[0]
	def is_same_col(self,cell2):
		return self.position[1] == cell2.position[1]
	def is_same_block(self, cell2):
		return self.block() == cell2.block()

class Board:
	def __init__(self):
		self.cells = {(row, col) : Cell((row,col)) for row in range(9) for col in range(9)}	
	def is_complete(self):
		return all([self.cells[position].value != None for position in self.cells])

	def load(self, initial_state):
		for row in range(9):
			for col in range(9):
				cell_value = initial_state[ row*9 + col]
				if cell_value != ".":
					self.cells[(row, col)].value = int(cell_value)

	def __setitem__(self, key, val):
		cell = self.cells[key]
		cell.value = val
		for position in self.related_cells(cell):
			c = self[position]
			if not c.value:
				c.eliminate(val)
				if c.value:
					self[position] = c.value

	def __getitem__(self, key):
		return self.cells[key]

	def related_cells(self, cell):
		return [c.position for c in self.cells.values() 
		if (cell.is_same_row(c) or cell.is_same_col(c) or cell.is_same_block(c)) and c.position != cell.position] 









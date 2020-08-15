from Game import BOARD, APPLE

class Node:
	def __init__(self, board, snake, parent=None, move=None):
		self.parent = parent
		self.children = []
		self.move   = move
		self.board  = board
		self.snake  = snake

		if self.parent:
			self.depth = self.parent.depth + 1
		else:
			self.depth = 0

		self.cost = None

		self.moves = ['up', 'down', 'left', 'right']


	def make_move(self, move):
		y, x = self.snake[-1]
		if move == 'up':
			y -= 1
		elif move == 'down':
			y += 1
		elif move == 'left':
			x -= 1
		elif move == 'right':
			x += 1

		_max = len(self.board)
		if all(i >= 0 and i < _max for i in (x, y)):
			i = self.board[y][x]

			return y, x, i

		return None, None, None


	def regular_prod_factory(self, visited):
		legal = []
		for move in self.moves:
			y, x, i = self.make_move(move)
				
			if i in [BOARD, APPLE] and (y, x) not in visited:
				legal.append(move)

		return legal


	def a_star_prod_factory(self):
		legal = []
		for move in self.moves:
			y, x, i = self.make_move(move)
			
			if i in [BOARD, APPLE]:
				legal.append(move)

		return legal
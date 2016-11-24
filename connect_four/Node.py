import math


class Node:
	def __init__(self, board, depth=0, parent=None, move=None, alpha=(-math.inf), beta=math.inf):
		self.parent   = parent
		self.move     = move
		self.board    = board

		self.alpha = alpha
		self.beta = beta

		self.moves = [x for x in range(len(self.board))]

		self.depth = depth

		if self.depth % 2 == 0:
			self.type_ = 'max'
		else:
			self.type_ = 'min'


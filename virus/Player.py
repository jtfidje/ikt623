import numpy as np
from Peg import Peg


class Player:
	def __init__(self, id, start_pegs, mark):
		self.id = id
		self.mark = mark
		self.pegs = []

		for pos in start_pegs:
			peg = Peg(pos, self.mark)
			self.pegs.append(peg)

	
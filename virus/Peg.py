import numpy as np


class Peg:
	def __init__(self, pos, mark):
		self.mark = mark
		self.counter = 5
		self.pos = pos


	def decay(self):
		self.counter -= 1
		if self.counter <= 0:
			return True
		return False

	def move(self, direction):
		moves = {
			 'N': [np.array([-1, 0])],
			 'S': [np.array([1, 0])],
			 'W': [np.array([0, -1])],
			 'E': [np.array([0, 1])],

			'NN': [np.array([-1, 0]), np.array([-1, 0])],
			'NE': [np.array([-1, 0]), np.array([0, 1])],
			'NW': [np.array([-1, 0]), np.array([0, -1])],

			'SS': [np.array([1, 0]), np.array([1, 0])],
			'SE': [np.array([1, 0]), np.array([0, 1])],
			'SW': [np.array([1, 0]), np.array([0, -1])],

			'WW': [np.array([0, -1]), np.array([0, -1])],
			'WS': [np.array([1, 0]), np.array([0, -1])],
			'WN': [np.array([0, -1]), np.array([-1, 0])],

			'EE': [np.array([0, 1]), np.array([0, 1])],
			'EN': [np.array([0, 1]), np.array([-1, 0])],
			'ES': [np.array([0, 1]), np.array([1, 0])],
		}

		return moves[direction]
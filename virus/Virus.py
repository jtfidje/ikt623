import numpy as np
from Player import Player


BOARD = '-'
SIZE = 10

class Virus:
	def __init__(self, player_1, player_2):
		self.player_1 = player_1
		self.player_2 = player_2
		
		self.create_board()


	def create_board(self):
		self.board = [[BOARD for _ in range(SIZE)] for _ in range(SIZE)]

		# Set starter-positions for both players
		for p_1, p_2 in zip(self.player_1.pegs, self.player_2.pegs):
			self.board[p_1.pos[0]][p_1.pos[1]] = p_1.mark
			self.board[p_2.pos[0]][p_2.pos[1]] = p_2.mark


	def update_board(self, peg):
		self.board[peg.pos[0]][peg.pos[1]] = peg.mark


	def check_legal(self, pos):
		_max = len(self.board)
		if all(i < 0 or i > _max for i in pos):
			return False

		


	def check_adjacent(self, peg):
		pass


	def move_one(self, player, peg, direction):
		moves = peg.move(direction)
		new_pos = peg.pos
		for move in moves:
			new_pos += move

		if self.check_legal(new_pos):
			pass



	def move_two(self, peg, moves):
		pass


	def __repr__(self):
		return (
			'\n'
			.join([''
			.join(['{:3}'
			.format(item)
			for item in row]) 
			for row in self.board
			]))


if __name__ == '__main__':
	player_1 = Player(1, [np.array([0,0]), np.array([-1,-1])], 'O')
	player_2 = Player(2, [np.array([0,-1]), np.array([-1,0])], 'X')
	v = Virus(player_1, player_2)
	print(v)


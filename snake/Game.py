import random
import numpy as np

import Config as cfg

BOARD = 0
APPLE = 1
ROCK  = 2
SNAKE = 3

class Game:
	def __init__(self, board_size, snake_len):
		self.board_size = board_size
		self.snake_len = snake_len

		self.snake = [
			(int(board_size / 2), i) 
			for i in range(self.snake_len)
		]

		self.rock_pos = None
		self.apple_pos = None

		self.create_board()
		self.draw_snake()
		self.spawn_apple()

		if cfg.ROCK_MODE != 'none':
			self.spawn_rock()


	def random_position(self):
		x = random.randrange(len(self.board))
		y = random.randrange(len(self.board))

		while self.board[y][x] != BOARD:
			x = random.randrange(len(self.board))
			y = random.randrange(len(self.board))

		return (y, x)


	def draw_snake(self):
		for pos in self.snake:
			self.board[pos] = SNAKE

		#if len(self.snake) > self.snake_len:
		snake_head = (self.snake[-1][0],
					  self.snake[-1][1])

		if snake_head == self.apple_pos and cfg.SNAKE_MODE == 'grow':
			# Skip deletion of tail
			pass
		else:
			snake_tail = (self.snake[0][0],
					      self.snake[0][1])	
			self.board[snake_tail] = BOARD
			del self.snake[0]
	

	def spawn_apple(self):
		pos = self.random_position()
		self.board[pos] = APPLE
		self.apple_pos = pos


	def spawn_rock(self):
		if self.rock_pos:
			self.board[self.rock_pos] = BOARD
		
		pos = self.random_position()
		self.rock_pos = pos
		self.board[pos] = ROCK


	def create_board(self):
		self.board = np.array(
			[np.zeros(self.board_size, dtype=np.int8) 
			for _ in range(self.board_size)]
		)

	def move_snake(self, move):
		y = self.snake[-1][0]
		x = self.snake[-1][1]
		
		if move == 'up':
			y -= 1
		elif move == 'down':
			y += 1
		elif move == 'left':
			x -= 1
		elif move == 'right':
			x += 1

		self.snake.append((y, x))
		self.draw_snake()

	def __repr__(self):
		# Fancy-pants function for printing the game board
		return (
			'\n'
			.join([''
			.join(['{:3}'
			.format(item)
			.replace(str(BOARD), cfg.BOARD)
			.replace(str(APPLE), cfg.APPLE)
			.replace(str(ROCK), cfg.ROCK)
			.replace(str(SNAKE), cfg.SNAKE) 
			for item in row]) 
			for row in self.board
			]))
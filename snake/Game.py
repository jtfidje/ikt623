import random
import numpy as np

import Config as cfg

BOARD = cfg.BOARD
APPLE = cfg.APPLE
ROCK  = cfg.ROCK
SNAKE = cfg.SNAKE

class Game:
	def __init__(self, board_size, snake_len):
		self.board_size = board_size
		self.snake_len = snake_len

		self.snake = [
			(int(board_size / 2), i) 
			for i in range(self.snake_len)
		]

		self.create_board()
		self.draw_snake()
		self.spawn_apple()
		self.spawn_rock()


	def random_position(self):
		x = random.randrange(len(self.board))
		y = random.randrange(len(self.board))

		while self.board[y][x] != BOARD:
			x = random.randrange(len(self.board))
			y = random.randrange(len(self.board))

		return y, x


	def draw_snake(self):
		for y, x in self.snake:
			self.board[y][x] = SNAKE

		if len(self.snake) > self.snake_len:
			y = self.snake[0][0]
			x = self.snake[0][1]	
			self.board[y][x] = BOARD
			del self.snake[0]


	def spawn_apple(self):
		y, x = self.random_position()
		self.board[y][x] = APPLE
		self.apple_pos = (y, x)


	def spawn_rock(self):
		y, x = self.random_position()
		self.board[y][x] = ROCK
		self.rock_pos = (y, x)


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
			.replace(str(BOARD), "-")
			.replace(str(APPLE), "@")
			.replace(str(ROCK) , "#")
			.replace(str(SNAKE), "o") 
			for item in row]) 
			for row in self.board
			]))
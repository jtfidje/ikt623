import os
import random
import time

from AI import AI
from Game import Game, COLS, ROWS, PLAYER_1, PLAYER_2

game = Game()

def print_ending(game):
	if game.winner == 'Draw':
		print('\nGame ended in draw!')
	else:
		print('\n{} won the game!'.format(game.winner))

def print_game(game):
	os.system('clear')
	print(game)
	time.sleep(0.2)

def random_play():
	game.__init__()
	i = 0
	while not game.check_winner():
		i += 1

		player = PLAYER_1 if i % 2 else PLAYER_2

		# Make player move
		while not game.put_piece(random.randrange(0, COLS), player):
			pass
		
		print_game(game)

	print_ending(game)

def pvp():
	game.__init__()
	i = 0

	print(game)
	while not game.check_winner():
		i += 1

		player = PLAYER_1 if i % 2 else PLAYER_2

		# Make player move
		while True:
			try:
				move = int(input('\n{} - Enter col:'.format(player))) - 1
			except ValueError:
				continue
			except EOFError:
				import sys; sys.exit()

			if game.put_piece(move, player):
				break
		
		print_game(game)

	print_ending(game)

def pve():
	ai = AI(PLAYER_1, PLAYER_2)
	i = 0
	game.__init__()

	while not game.check_winner():
		i += 1

		if i % 2:
			# TODO: Get AI turn
			# player = PLAYER_1
			# move =
			move = ai.search(game)
			player = PLAYER_1
			game.put_piece(move, PLAYER_1)

		else:
			# Make player move
			while True:
				try:
					move = int(input('\n{} - Enter col:'.format(PLAYER_2))) - 1
				except ValueError:
					continue
				except EOFError:
					import sys; sys.exit()

				if game.put_piece(move, PLAYER_2):
					break
		
		print_game(game)
		print(ai.pred)

	print_ending(game)


def ave():
	ai = AI(PLAYER_1, PLAYER_2)
	i = 0
	game.__init__()

	while not game.check_winner():
		i += 1

		if i % 2:
			# TODO: Get AI turn
			# player = PLAYER_1
			# move =
			move = ai.search(game)
			player = PLAYER_1
			game.put_piece(move, PLAYER_1)

		else:
			while not game.put_piece(random.randrange(0, COLS), PLAYER_2):
				pass
		
		print_game(game)
		print(ai.pred)

	print_ending(game)

def ava():
	ai_1 = AI(PLAYER_1, PLAYER_2, max_depth=5)
	ai_2 = AI(PLAYER_2, PLAYER_1, max_depth=2)
	i = 0
	game.__init__()

	while not game.check_winner():
		i += 1

		if i % 2:
			# TODO: Get AI turn
			# player = PLAYER_1
			# move =
			move = ai_1.search(game)
			game.put_piece(move, PLAYER_1)
		else:
			move = ai_2.search(game)
			game.put_piece(move, PLAYER_2)
		
		print_game(game)

	print_ending(game)


if __name__ == '__main__':
#	ave()
#	pvp()
	pve()
#	ava()
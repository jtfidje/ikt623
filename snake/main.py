import os
import time

from Game import Game
from Search import Search
import Config as cfg

game = Game(cfg.BOARD_SIZE, cfg.SNAKE_LEN)
search = Search(game)

times = []

try:
	i = 1
	while True:
		start = time.time()
	#	moves = search.depth_first()
	#	moves = search.breadth_first()
		moves = search.a_star()
		stop = time.time()

		delta = stop - start
		times.append(delta)
		print(game)
		while moves:
			move = moves.pop()
			os.system('clear')
			game.move_snake(move)
			print(f'  Score: {i}')
			print(f'  Nodes: {len(search.visited_states)}')
			print(f'  Time : {delta:0.4f}')
			print(game)
			time.sleep(cfg.WAIT)
		
		game.spawn_apple()
		
		if cfg.ROCK_MODE == 'dynamic':
			game.spawn_rock()
		
		# Reset global search variables
		search.__init__(game)
		i += 1
except KeyboardInterrupt:
	avg = sum(times) / len(times)
	print(f'\n\nAverage search time: {avg}\n\n')

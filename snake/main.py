import os
import time

from Game import Game
from Search import Search

SNAKE_LEN = 10
BOARD_SIZE = 20
WAIT = 0.1

game = Game(BOARD_SIZE, SNAKE_LEN)
search = Search(game)

times = []

for i in range(10000):
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
		print('  Score:', i)
		print('  Nodes:', len(search.visited_states))
		print('  Time :', delta)
		print(game)
		time.sleep(WAIT)
	
	game.spawn_apple()
	# Reset global search variables
	search.__init__(game)

print(sum(times) / len(times))

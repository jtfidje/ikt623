# Game element representations
BOARD = '-'
APPLE = '@'
ROCK  = '#'
SNAKE = 'o'

SNAKE_LEN = 3    # Start-length of the snake
BOARD_SIZE = 20  # How big the board will be ( BOARD_SIZE x BOARD_SIZE )
WAIT = 0.1       # Determines the game refresh rate.

# Available rock modes:
# 'dynamic': Spawns a new random rock each time the snake eats an apple
# 'static':  Spawns a rock at the beginning of the game that never moves
# 'none':    No rock is spawned
ROCK_MODE = 'dynamic'

# Available snake modes:
# 'grow':   Normal snake that grows when it eats an apple
# 'static': Static snake that stays the same length the entire game
SNAKE_MODE = 'grow'
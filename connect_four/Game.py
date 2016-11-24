COLS = 7
ROWS = 6

BOARD    = '-'
PLAYER_1 = 'X'
PLAYER_2 = 'O'


class Game:
	def __init__(self):
		self.winner = None
		self.create_board()
 

	def create_board(self):
		self.board = [[BOARD for _ in range(ROWS)] for _ in range(COLS)]


	def put_piece(self, col, piece):
		try:
			row = self.board[col].index(BOARD)
			self.board[col][row] = piece
			return True
		except (ValueError, IndexError):
			return False


	def check_winner(self, board=None):
		if not board:
			board = self.board

		# Check draw
		if BOARD not in [col[-1] for col in board]:
			self.winner = 'Draw'
			return True

		# Check horizontal
		for row in range(ROWS):
			for col in range(COLS - 3):
				window = []
				for i in range(col, col + 4):
					window.append(board[i][row])
				if self.check_window(window):
					return True
				
		# Check vertical
		for col in range(COLS):
			for i in range(ROWS - 3):
				window = board[col][i:i + 4]
				if self.check_window(window):
					return True
		
		# Check diagonal
		for col in range(COLS):
			for row in range(ROWS):
				if col + 3 < COLS and row < ROWS - 3:
					window = [board[col + i][row + i] for i in range(4)] 
					if self.check_window(window):
						return True

				if row >= 3 and col < COLS - 3:
					window = [board[col + i][row - i] for i in range(4)]
					if self.check_window(window):
						return True

		return False


	def check_window(self, window):
		mark = window[0] if window[0] != BOARD else None
		if all(i == mark for i in window):
			self.winner = mark
			return True
		return False


	def __repr__(self):
		return (
			'\n'
			.join([''
			.join(['{:3}'
			.format(self.board[col][row])
			for col in range(COLS)]) 
			for row in range(ROWS - 1, -1, -1)
			]))

if __name__ == '__main__':
	game = Game()
	
	print(game)
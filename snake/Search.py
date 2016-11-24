import pdb

import math
import copy
from Node import Node


class Search:
	def __init__(self, game):

		self.nodes = []
		self.closed = []
		self.visited_states = []
		self.game = copy.copy(game)

		self.init_root()


	def init_root(self):
		# Create initial root node. 
		self.node = Node(self.game.board, self.game.snake)
		self.evaluate(self.node)
		self.nodes.append(self.node)
		self.visited_states.append(self.game.snake[-1])
		
	
	def regular_branch(self):
		# Call node production, brancing each node into
		# every legal move from current game state.
		moves = self.node.regular_prod_factory(self.visited_states)

		for move in moves:
			# Copy game states to prohibit mem. reference errors
			self.game.board = copy.copy(self.node.board)
			self.game.snake = copy.copy(self.node.snake)

			self.game.move_snake(move)
			
			# Create new child-node after move and do necessary bookkeeping
			child_node = Node(self.game.board, self.game.snake, self.node, move)
			self.nodes.append(child_node)
			self.visited_states.append(self.game.snake[-1])

			# Check if solution has been found
			if self.game.snake[-1] == self.game.apple_pos:
				return True
		
		return False


	def a_star_branch(self):
		moves = self.node.a_star_prod_factory()

		for move in moves:
			# Copy game states to prohibit mem. reference errors
			self.game.board = copy.copy(self.node.board)
			self.game.snake = copy.copy(self.node.snake)

			self.game.move_snake(move)
			
			# Create new child-node after move and do necessary bookkeeping
			child_node = Node(self.game.board, self.game.snake, self.node, move)
			self.evaluate(child_node)
			snake_pos = child_node.snake[-1]
			
			# First check if soution has been found...
			if snake_pos == self.game.apple_pos:
				
				self.node = child_node
				return True

			# Now check if this state has been visited before. If true - check if new cost is lower
			if snake_pos in self.visited_states:
				node = [n for n in (self.closed + self.nodes) if n.snake[-1] == snake_pos][0]
				if child_node.cost < node.cost:
					node.parent = child_node.parent
					node.move = child_node.move
					node.parent.children.append(node)
					self.update_cost(node)

			else:
				self.nodes.append(child_node)
				self.node.children.append(child_node)
				self.visited_states.append(snake_pos)

		return False


	
	def backtrack(self):
		# Backtrack every node to its parent, saving 
		# each move that lead to the node in a list.
		moves = []
		while self.node.parent:
			moves.append(self.node.move)
			self.node = self.node.parent
		return moves

	
	def update_cost(self, node):
		node.depth = node.parent.depth + 1
		self.evaluate(node)
		for child in node.children:
			self.update_cost(child)


	def estimate_cost(self):
		i = self.game.apple_pos
		j = self.node.snake[-1]
		_1 = math.sqrt(math.pow((i[0] - j[0]), 2) + math.pow((i[1] - j[1]), 2))
		_2 = (i[0] - j[0]) + (i[1] - j[1])
		h = (_1 + _2) / 2
		return math.fabs(h)

	def evaluate(self, node=None):
		if not node:
			node = self.node

		g = node.depth
		h = self.estimate_cost()
		node.cost = (g + h)

	
	def breadth_first(self):
		# Start Breadth-first search
		while True:
			# Select nodes from list as a 'queue'
			self.node = self.nodes[0]; del self.nodes[0]

			# regular branch returns true if solution is found
			# Save last node object in nodes-list to self.node
			if self.regular_branch():
				self.node = self.nodes.pop()
				break 						

		return self.backtrack()	# Returns a list of moves leading to solution

	
	def depth_first(self):
		# Start Depth-first search
		while True:
			# Select nodes from list as a 'stack'
			self.node = self.nodes.pop()

			# regular_branch returns true if solution is found
			# Save last node object in nodes-list to self.node
			if self.regular_branch():
				self.node = self.nodes.pop()
				break
		
		return self.backtrack()	# Returns a list of moves leading to solution

	
	def a_star(self):
		# Start A* Search
		while True:
			# Select node from list with lowest cost
			lowest = self.nodes[0]
			for node in self.nodes:
				if node.cost < lowest.cost:
					lowest = node

			self.node = self.nodes.pop(self.nodes.index(lowest))
			self.closed.append(self.node)
			
			if self.a_star_branch():
				# Solution will be set by branch method
				break
			
		return self.backtrack()


			

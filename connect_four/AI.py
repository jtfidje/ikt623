import copy
from Node import Node


class AI:
    def __init__(self, piece, opponent, max_depth=4):
        # Game pieces.
        self.ai = piece
        self.opponent = opponent
        self.stack = []
        self.max_depth = max_depth

    def branch(self, node):
        # Set the correct player pice by checking tree depth
        piece = self.ai if node.type_ == 'max' else self.opponent

        # Loop through all columns and try to place a pice, creating children nodes.
        move = node.moves.pop()
        self.game.board = copy.deepcopy(node.board)

        if self.game.put_piece(move, piece):
            node = Node(
                board  = self.game.board,
                depth  = node.depth + 1,
                move   = move,
                alpha  = node.alpha,
                beta   = node.beta
            )

            if self.game.check_winner():
                # Score the node based on win / loss / draw
                score = self.calc_heuristics()
            elif node.depth == self.max_depth:
                score = self.game.max_score
            else:
                score = None

            # Check if this is a terminal node
            if score != None:
                # Check if parent node should update its alpha / beta
                if self.update_alpha_beta(score, node.type_):
                    # If update occured...
                    # If root-node was updated - update best move
                    if node.depth == 1:
                            self.move = node.move
                            self.pred = self.stack[0].alpha
                    # Check if tree can be pruned
                    else:
                        self.prune(node.type_)
            else:
                self.stack.append(node)

    def calc_heuristics(self):
        # Score the leaf node
        winner = self.game.winner
        if winner == self.opponent:
             return -1
        elif winner == 'Draw':
             return 1
        elif winner == self.ai:
             return 2

        # TODO: Implement a score '3' if
        #       AI wins and have a possible
        #		win another place. (X X X -)

    def update_alpha_beta(self, score, type_):
        if type_ == 'max' and score < self.stack[-1].beta:
            # MAX
            self.stack[-1].beta = score
            return True
        elif type_ == 'min' and score > self.stack[-1].alpha:
            # MIN
            self.stack[-1].alpha = score
            return True
        else:
            return False

    def prune(self, type_):
        if (type_ == 'max' and self.stack[-1].beta < self.stack[-2].alpha) or \
           (type_ == 'min' and self.stack[-1].alpha > self.stack[-2].beta):
            # Delete the 'parent node'.
            del self.stack[-1]

    def search(self, game):
        # Initialize internal game states
        self.game = copy.deepcopy(game)
        self.stack.append(Node(self.game.board))

        while self.stack:
            # Get the deepest node in the tree / node at top of stack
            node = self.stack[-1]

            if node.moves:
                # Branch if moves available
                self.branch(node)
            else:
                del self.stack[-1]

                if not self.stack:
                    break

                # Remove node from stack if no moves left.
                # Check to see if we need to update alpha / beta of next element.
                # (This is in case the next element only had one child)
                score = node.alpha if node.type_ == 'max' else node.beta
                if self.update_alpha_beta(score, node.type_):
                    if node.depth == 1:
                        self.move = node.move
                        self.pred = self.stack[0].alpha
                    if node.depth > 1:
                        self.prune(node.type_)

        # When algorithm is done, return the best current move found
        return self.move

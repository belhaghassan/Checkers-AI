import copy 
import math 
import random 
import datetime
from copy import deepcopy
import pygame

from checkersGame import * 
from constants import * 

RED = (255, 0, 0)
BLACK = (0,0,0)

def minimax(position, depth, max_player, game):
	if depth == 0 or position.terminate() != None:
		return position.evaluate(), position

	if max_player:
		maxEval = -math.inf
		best_move = None
		for move in actions(position, RED, game):
			evaluation = minimax(move, depth-1, False, game)[0]
			maxEval = max(maxEval, evaluation)
			if maxEval == evaluation:
				best_move = move

		return maxEval, best_move

	else:
		minEval = math.inf
		best_move = None
		for move in actions(position, BLACK, game):
			evaluation = minimax(move, depth-1, True, game)[0]
			minEval = min(minEval, evaluation)
			if minEval == evaluation:
				best_move = move

		return minEval, best_move
'''
def alphaBetaSearch(self, depth, game):
	#debugging
	# collect statistics for the search
	self.positiveInf = math.inf
	self.negativeInf = -math.inf
    self.currentDepth = 0
    self.maxDepth = 0
    self.numNodes = 0
    self.maxPruning = 0
    self.minPruning = 0

    self.bestMove = []
    self.depth = depth

    starttime = datetime.datetime.now()
    v = self.maxValue(state, negativeInf, positiveInf, self.depth)

    print("Time = " + str(datetime.datetime.now() - starttime))
    print("selected value " + str(v))
    print("(1) max depth of the tree = {0:d}".format(self.maxDepth))
    print("(2) total number of nodes generated = {0:d}".format(self.numNodes))
    print("(3) number of times pruning occurred in the MAX-VALUE() = {0:d}".format(self.maxPruning))
    print("(4) number of times pruning occurred in the MIN-VALUE() = {0:d}".format(self.minPruning))

    return self.bestMove

#RED 
def maxValue(self, alpha, beta, depth):
	self.currentDepth += 1 
	self.maxDepth = max(self.maxDepth, self.currentDepth)
	self.numNodes += 1

	v = -math.inf
	#apply logic from minimax algorithm here for the checker's game 
	for a in actions()

	if v >= beta:
		self.maxPruning += 1 
		self.currentDepth -= 1
		return v
	alpha = max(alpha, v)

	self.currentDepth -= 1 
	return v

#BLACK aka us 
def minValue(self, alpha, beta, depth):
	self.currentDepth += 1 
	self.maxDepth = max(self.maxDepth, self.currentDepth)
	self.numNodes += 1

	v = math.inf
	#apply logic from minimax algorithm here for the checker's game 

	#pruning section 
	#pruning section should be inside the for loop 
	if v <= alpha:
		self.minPruning += 1
		self.currentDepth -= 1
		return v
	beta = min(beta, v) 

	self.currentDepth -= 1
	return v 
'''


#Figured out the stupid simulate moves 
def result(piece, move , board, game, skip):
	board.move(piece, move[0], move[1])
	if skip:
		board.remove(skip)

	return board

def actions(board, color, game):
	moves = []

	for piece in board.listPieces(color):
		valid_moves = board.validMoves(piece)
		for move, skip in valid_moves.items():
			# draw_moves(game, board, piece)
			temp_board = deepcopy(board)
			temp_piece = temp_board.get_piece(piece.row, piece.col)
			new_board = result(temp_piece, move, temp_board, game, skip)
			moves.append(new_board)

	return moves

def draw_moves(game, board, piece):
	valid_moves = board.validMoves(piece)
	board.draw(game.win)
	pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
	game.validMoves(valid_moves.keys())
	pygame.display.update()


import copy 
import math 
import random 
import datetime

from checkersGame import * 
from constants import * 

class AIPlayer():
	def __init__(self, game, difficulty):
		self.game = game
		self.difficulty = difficulty

	def getMoveDifficulty(self):
		if self.difficulty == 1:
			return self.easyDiff()
		else:
			return self.hardDiff()

	def easyDiff(self):
		state = AIGameState(self.game)
		moves = state.getActions(False)
		index = random.randrange(len(moves))
		basicMove = moves[index]
		return basicMove[0], basicMove[1], basicMove[2], basicMove[3]

	def hardDiff(self):
		state = AIGameState(self.game)
		depthLimit = self.computeDepthLimit(state)
		hardMove = self.alphaBetaSearch(state, depth)
		return hardMove[0], hardMove[1], hardMove[2], hardMove[3]

	def computeDepthLimit(self, state):
		checkersRemaining = len(state.AICheckers) + len(state.humanCheckers) 
		return 26 - checkersRemaining

	def alphaBetaSearch(self, state, depthLimit)
		#debugging
		self.currentDepth = 0 
		self.maxDepth = 0 
		self.numnodes = 0 
		self.maxPruning = 0 
		self.minPruning = 0 

		self.bestMove = []
		self.depthLimit = depthLimit

		starttime = datetime.datetime.now()
		v = self.maxValue(state, -1000, 1000, self.depthLimit)

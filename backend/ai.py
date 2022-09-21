from game import Game
import random
from tree import Tree
from math import exp
import numpy as np

class AI:
    def __init__(self, game):
        self.game = game

    def getAction(self):
        print("탐색중입니다...")
        tree = Tree(self.game.copy())
        pos = tree.pos
        W, N = tree.mcts()
        p = [w/n for w, n in zip(W, N)]
        softmax = [exp(i) for i in p] # softmax
        s = sum(softmax)
        softmax = [i/s for i in softmax]
        # print(softmax)
        # assert sum(softmax) == 1
        ix = np.random.choice([i for i in range(len(softmax))], p=softmax)
        x, y = pos[ix]
        return x,y
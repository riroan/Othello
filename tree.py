from game import Game
import random
import time


class Tree:
    def __init__(self, game):
        self.game: Game = game
        self.children = []

        self.N = []  # 방문 횟수
        self.W = []  # 그 노드를 선택했더니 이긴 횟수
        
        self.pos = []

        self.maxTime = 5  # 5초동안 탐색

        self.init()

    def init(self):
        cand = self.game.getCand()
        for x, y in cand:
            game = self.game.copy()
            game.process(x, y)
            self.children.append(game)
            self.pos.append((x,y))
            self.N.append(0)
            self.W.append(0)

    def mcts(self):
        start = time.time()

        while time.time() - start <= self.maxTime:
            ix = random.choice([i for i in range(len(self.children))])
            game = self.children[ix]
            winner = self.simulation(game.copy())
            if winner == self.game.player:
                self.W[ix] += 1
            self.N[ix]+=1
        return self.W, self.N

    def simulation(self, game: Game):
        while not game.winner:
            cand = list(game.getCand())
            if not cand:
                game.winner = 3- game.player
                break
            x, y = random.choice(cand)
            game.process(x, y)
        return game.winner

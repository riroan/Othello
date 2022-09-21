from game import Game
from ai import AI

SIZE = 8
arr = [[0] * SIZE for i in range(SIZE)]


def check(x, y):
    return 0 <= x < SIZE and 0 <= y < SIZE

print("!!! 모든 좌표는 0부터 시작 !!!")
while 1:
    x, y = map(int, input("구멍 좌표를 입력하세요.(종료는 -1, -1): ").split())
    if x < 0 or y < 0:
        break
    if not check(x,y):
        continue
    arr[x][y] = -1

while 1:
    first = int(input("선공 : 1, 후공 : 0 -> "))
    if first in [0, 1]:
        break


game = Game(arr)
x, y = -1, -1
while not game.winner:
    if first:
        game.display(x, y)
        game.getXY()

        if game.winner:
            break

        agent = AI(game)
        x, y = agent.getAction()
        game.process(x, y)
    else:
        game.display(x, y)
        agent = AI(game)
        x, y = agent.getAction()
        game.process(x, y)

        if game.winner:
            break

        game.getXY()

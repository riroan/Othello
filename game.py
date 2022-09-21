class Game:
    def __init__(self, board, init=True):
        self.arr = board
        self.size = len(self.arr)
        self.player = 1

        self.winner = 0

        if init:
            self.arr[3][4] = 1
            self.arr[4][3] = 1
            self.arr[3][3] = 2
            self.arr[4][4] = 2

    def copy(self):
        board = [i.copy() for i in self.arr]
        game = Game(board, False)
        game.player = self.player
        game.winner = self.winner
        return game

    def check(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def getCand(self):
        s = set()
        p = self.player
        e = 3-self.player
        arr = self.arr
        for x in range(self.size):
            for y in range(self.size):
                if arr[x][y] != 0:
                    continue
                for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
                    flag = 0
                    tx, ty = x, y
                    exists = 0
                    while 1:
                        tx += dx
                        ty += dy
                        if not self.check(tx, ty):
                            break
                        if arr[tx][ty] in [0, -1]:
                            break
                        if arr[tx][ty] == e:
                            exists += 1
                        if arr[tx][ty] == p:
                            if exists:
                                flag = 1
                            break
                    if flag:
                        s.add((x, y))
                        break
        return s

    def getXY(self):
        cand = self.getCand()
        if not cand:
            print(f"Player {3-self.player} Win")
            self.winner = 3-self.player
            return
        while 1:
            print(cand)
            x, y = map(int, input("좌표 입력 (예 : 0 2): ").split())
            if (x, y) not in cand or not self.check(x, y):
                print("올바르지 않은 좌표입니다.")
                continue
            self.process(x, y)
            break

    def process(self, x, y):
        arr = self.arr
        p = self.player
        e = 3 - self.player
        self.arr[x][y] = self.player
        self.player = 3-self.player
        brr = []
        for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
            flag = 0
            tx, ty = x, y
            exists = 0
            crr = []
            while 1:
                tx += dx
                ty += dy
                if not self.check(tx, ty):
                    break
                if arr[tx][ty] in [0, -1]:
                    break
                if arr[tx][ty] == e:
                    exists += 1
                    crr.append((tx, ty))
                if arr[tx][ty] == p:
                    if exists:
                        flag = 1
                    break
            if flag:
                brr.extend(crr)
        for x, y in brr:
            arr[x][y] = p

    def display(self, x=-1, y=-1):
        print("  \033[31m", end="")
        print(*[i for i in range(self.size)])
        for i in range(self.size):
            print(f"\033[31m{i}\033[37m", end="")
            for j in range(self.size):
                if i == x and y == j:
                    if self.arr[i][j] == -1:
                        print(f" \033[31m@\033[37m", end="")
                    else:
                        print(f" \033[31m{self.arr[i][j]}\033[37m", end="")
                else:
                    if self.arr[i][j] == -1:
                        print(f" @", end="")
                    else:
                        print(f" {self.arr[i][j]}", end="")
            print()
        print()

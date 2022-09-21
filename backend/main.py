from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from game import Game
from ai import AI

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

game = None


class Item(BaseModel):
    arr: list
    first: int


@app.post("/")
async def func1(item: Item):
    global game
    game = Game(item.arr)

    return game.arr


class Item2(BaseModel):
    arr: list
    x: int
    y: int


@app.post("/play")
async def func2(item: Item2):
    global game
    arr = item.arr
    x = item.x
    y = item.y
    if x>= 0 and y>=0:
        game.process(x, y)
    else:
        game = Game(arr)
    for i in game.arr:
        print(*i)
    agent = AI(game)
    x, y = agent.getAction()
    game.process(x, y)
    game.display()
    return game.arr

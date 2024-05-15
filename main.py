from ball import Ball
from paddle import Paddle
from brick import Brick
# from board import Board
from scoreboard import ScoreBoard
from turtle import mainloop, Screen
from constants import *


def init_board():
    screen = Screen()
    screen.setup(width=MAX_WIDTH, height=MAX_HEIGHT)
    screen.bgcolor("black")
    screen.title("Breakdown")
    return screen


def main():

    screen = init_board()
    paddle = Paddle()

    screen.listen()
    screen.onkeypress(fun=paddle.go_right, key="Right")
    screen.onkeypress(fun=paddle.go_left, key="Left")
    screen.update()

    screen.mainloop()


if __name__ == "__main__":
    main()

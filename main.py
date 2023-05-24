from ball import Ball
from paddle import Paddle
from brick import Brick
# from board import Board
from scoreboard import ScoreBoard
from turtle import mainloop, Screen


def init_board():
    screen = Screen()
    screen.setup(width=700, height=700)
    screen.bgcolor("black")
    screen.title("Breakdown")
    screen.tracer(0)
    return screen


def main():
    screen = init_board()
    paddle = Paddle()
    screen.update()

    screen.listen()
    screen.onkeypress(fun=paddle.go_right, key="Right")
    screen.onkeypress(fun=paddle.go_left, key="Left")
    screen.update()


if __name__ == "__main__":
    main()
    mainloop()

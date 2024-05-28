from ball import Ball
from paddle import Paddle
from brick import Brick
from board import Board
from scoreboard import ScoreBoard
from turtle import mainloop, Screen
from constants import *
from turtle import Shape
from time import sleep
import random as rn


def detect_collision():
    if abs(ball.xcor()) + ball.radius >= abs(board.border_x):
        ball.bounce_y()

    # Normalize distance and check limits
    dst_paddle_ball = abs(ball.xcor() - paddle.xcor()) - ball.radius
    dist_paddle_ball_y = abs(ball.ycor() - paddle.ycor()) - ball.radius
    touch_ball_paddle = dst_paddle_ball <= paddle.size_x and dist_paddle_ball_y <= paddle.size_y
    if touch_ball_paddle or ball.ycor() + ball.radius >= board.border_y:
        ball.bounce_x()


def init_shapes():
    size = (MAX_WIDTH - OFFSET_BOARD) / ROW_BRICKS
    poly1 = ((0, 10), (size, 10), (size, -10), (0, -10))
    for color in COLORS_BRICK:
        s = Shape("compound")
        s.addcomponent(poly1, color, "white")
        board.screen.register_shape(f"brick_{color}", s)


def init_bricks() -> list:
    all_bricks = []
    for j in range(0, TOTAL_ROWS):
        for i in range(0, ROW_BRICKS):
            idx_color = rn.randint(0, len(COLORS_BRICK) - 1)
            shape = f"brick_{COLORS_BRICK[idx_color]}"
            new_brick = Brick(shape, idx_color)
            new_brick.goto(-(MAX_WIDTH - OFFSET_BOARD)/2 + new_brick.size_x*i, 25 + 20*j)
            all_bricks.append(new_brick)
    return all_bricks


def lose():
    print("Game Over")


def main():
    board.screen.listen()
    board.screen.onkey(fun=paddle.go_right, key="Right")
    board.screen.onkey(fun=paddle.go_left, key="Left")

    board.screen.update()
    playing = True
    while playing:
        sleep(TIMER_SLEEP)
        ball.move()
        if ball.ycor() <= -board.border_y:
            playing = False
            lose()
            continue
        detect_collision()

    board.screen.mainloop()


if __name__ == "__main__":
    board = Board()
    paddle = Paddle()
    ball = Ball(board)
    init_shapes()
    bricks = init_bricks()
    main()

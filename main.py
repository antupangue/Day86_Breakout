from ball import Ball
from paddle import Paddle
from brick import Brick
from board import Board
from scoreboard import ScoreBoard
from turtle import mainloop, Screen
from constants import *
from time import sleep


def detect_collision():
    if abs(ball.xcor() + ball.radius) >= board.border_x:
        return "y"

    # Normalize distance and check limits
    dst_paddle_ball = abs(ball.xcor() - paddle.xcor()) - ball.radius
    dist_paddle_ball_y = abs(ball.ycor() - paddle.ycor()) - ball.radius
    touch_ball_paddle = dst_paddle_ball <= paddle.size_x and dist_paddle_ball_y <= paddle.size_y
    if touch_ball_paddle or ball.ycor() + ball.radius >= board.border_y:
        return "x"


def bounce_y():
    in_angle = 360 - ball.heading()
    out_angle = ball.heading() - (180 - 2*in_angle)
    ball.setheading(out_angle)


def bounce_x():
    in_angle = 360 - ball.heading()
    out_angle = ball.heading() + 2*in_angle
    ball.setheading(out_angle)

def lose():
    print("Game Over")


def main():
    board.screen.listen()
    board.screen.onkey(fun=paddle.go_right, key="Right")
    board.screen.onkey(fun=paddle.go_left, key="Left")

    board.screen.update()
    playing = True
    while playing:
        sleep(0.1)
        ball.move()
        if ball.ycor() <= -board.border_y:
            playing = False
            lose()
        if detect_collision() == "y":
            bounce_y()
        elif detect_collision() == "x":
            bounce_x()

    board.screen.mainloop()


if __name__ == "__main__":
    board = Board()
    paddle = Paddle()
    ball = Ball(board)
    main()

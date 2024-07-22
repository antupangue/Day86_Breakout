from ball import Ball
from paddle import Paddle
from brick import Brick
from board import Board
from scoreboard import ScoreBoard
from constants import *
from turtle import Shape
from time import sleep
import random as rn
from math import acos, degrees


def detect_collision():
    """
    Detect collisions between the ball and other objects and walls.
    :return:
    """
    # Bounce walls
    if abs(ball.xcor()) + ball.radius >= abs(board.border_x):
        ball.bounce_y()
    elif ball.ycor() + ball.radius >= board.border_y:
        ball.bounce_x()

    # Bounce paddle
    # Normalize distance and check limits
    dst_paddle_ball = abs(ball.xcor() - paddle.xcor()) - ball.radius
    dist_paddle_ball_y = abs(ball.ycor() - paddle.ycor()) - ball.radius
    touch_ball_paddle = dst_paddle_ball <= paddle.size_x and dist_paddle_ball_y <= paddle.size_y
    if touch_ball_paddle or ball.ycor() + ball.radius >= board.border_y:
        dist_x = ball.xcor()-paddle.xcor()
        if abs(dist_x) < paddle.size_x:
            # Variable outside angle, depending on distance to paddle center
            alpha = degrees(acos(dist_x/paddle.size_x))
            if 0 < alpha < 180:
                ball.setheading(alpha)
            # Avoid outside angles of 0 or 180
            else:
                curr_heading = ball.heading()
                ball.setheading(curr_heading + 180)

    elif touch_ball_paddle and paddle.ycor() - paddle.size_y < ball.ycor() < paddle.ycor() + paddle.size_y:
        ball.bounce_y()

    # Bounce brick
    # Find the closest brick
    min_idx = 0
    min_brick = bricks[min_idx]
    dist_min = ball.dist_brick(min_brick)
    for idx, brick in enumerate(bricks):
        # Check if brick is the closest
        dist_current = ball.dist_brick(brick)
        if dist_current < dist_min:
            min_idx = idx
            min_brick = bricks[min_idx]
            dist_min = dist_current

    # Check collision with brick
    dist_x = abs(min_brick.xcor() - ball.xcor())
    touch_x_brick = dist_x <= min_brick.size_x + ball.radius
    dist_y = abs(min_brick.ycor() - ball.ycor())
    touch_y_brick = dist_y <= min_brick.size_y + ball.radius
    if touch_x_brick and touch_y_brick:
        # Check if bounce y
        if (min_brick.ycor() - min_brick.size_y) < ball.ycor() < (min_brick.ycor() + min_brick.size_y):
            ball.bounce_y()
        # Bounce X
        else:
            ball.bounce_x()

        # Reduce brick hit points
        min_brick.hitpoints -= 1
        if min_brick.hitpoints <= 0:
            score.add_score(min_brick.color_score)
            min_brick.hideturtle()
            bricks.pop(min_idx)


def init_shapes():
    """
    Initialize the different types of bricks (different colors). It register the shape turtle.
    :return:
    """
    size = (MAX_WIDTH - OFFSET_BOARD) / ROW_BRICKS
    poly1 = ((size/2, WIDTH_BRICK), (size/2, -WIDTH_BRICK), (-size/2, -WIDTH_BRICK), (-size/2, WIDTH_BRICK))
    for color in COLORS_BRICK:
        s = Shape("compound")
        s.addcomponent(poly1, color, "white")
        board.screen.register_shape(f"brick_{color}", s)


def init_bricks() -> list:
    """
    It generates all the required bricks according to the desired Rows and Size of the board. This is parametrized in
    the file constants.py
    :return: a list containing all bricks
    """
    all_bricks = []
    for j in range(0, TOTAL_ROWS):
        for i in range(0, ROW_BRICKS):
            idx_color = rn.randint(0, len(COLORS_BRICK) - 1)
            shape_name = f"brick_{COLORS_BRICK[idx_color]}"
            new_brick = Brick(shape_name, idx_color)
            new_brick.goto(-(MAX_WIDTH - OFFSET_BOARD - new_brick.size_x)/2 + new_brick.size_x*i, 25 + WIDTH_BRICK*2*j)
            all_bricks.append(new_brick)
    return all_bricks


def lose():
    """
    Clean all elements in the screen and print final score and GAME OVER message.
    :return:
    """
    for brick in bricks:
        brick.hideturtle()
    ball.hideturtle()
    paddle.hideturtle()
    score.print_score()
    score.print_gameover()


def win():
    """
    Clean the screen, print final score and YOU WIN message.
    :return:
    """
    ball.hideturtle()
    paddle.hideturtle()
    score.print_score()
    score.print_win()


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
        if len(bricks) == 0:
            playing = False
            win()
        detect_collision()

    board.screen.mainloop()


if __name__ == "__main__":
    init_heading = rn.randint(200, 300)
    board = Board()
    paddle = Paddle()
    ball = Ball(board, init_heading)
    init_shapes()
    bricks = init_bricks()
    score = ScoreBoard()
    main()

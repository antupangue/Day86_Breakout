from turtle import Turtle, Screen
from constants import *
from math import sqrt


class Ball(Turtle):
    def __init__(self, screen, init_heading):
        super().__init__()
        self.board = screen
        self.shape("circle")
        self.color("white")
        self.radius = self.get_shapepoly()[0][0]
        self.penup()
        self.setheading(init_heading)
        self.speed(0)

    def dist_brick(self, brick: Turtle) -> float:
        distance = sqrt((self.xcor()-brick.xcor())**2+(self.ycor()-brick.ycor())**2)
        return distance

    def move(self):
        self.forward(STEP_BALL)

    def bounce_x(self):
        in_angle = 360 - self.heading()
        out_angle = self.heading() + 2 * in_angle
        self.setheading(out_angle)

    def bounce_y(self):
        in_angle = 360 - self.heading()
        out_angle = self.heading() - (180 - 2 * in_angle)
        self.setheading(out_angle)
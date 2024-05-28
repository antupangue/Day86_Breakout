from turtle import Turtle, Screen
from constants import *


class Ball(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.board = screen
        self.shape("circle")
        self.color("white")
        self.radius = self.get_shapepoly()[0][0]
        self.penup()
        self.setheading(-50)
        self.speed(0)


    def move(self):
        self.forward(STEP_BALL)
        # self.board.screen.ontimer(self.move, TIMER_BALL)

    def bounce_x(self):
        in_angle = 360 - self.heading()
        out_angle = self.heading() + 2 * in_angle
        self.setheading(out_angle)

    def bounce_y(self):
        in_angle = 360 - self.heading()
        out_angle = self.heading() - (180 - 2 * in_angle)
        self.setheading(out_angle)
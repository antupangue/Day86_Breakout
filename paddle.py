from turtle import Turtle
from constants import *


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=6, stretch_len=0.5)
        self.pu()
        self.setheading(90)
        self.goto(0, -300)
        self.size_x = abs(self.get_shapepoly()[0][0])
        self.size_y = abs(self.get_shapepoly()[0][1])

    def go_right(self):
        x_coord = self.xcor() + STEP
        if x_coord + self.size_x < MAX_WIDTH/2:
            self.goto(x_coord, self.ycor())

    def go_left(self):
        x_coord = self.xcor() - STEP
        if abs(x_coord) + self.size_x < MAX_WIDTH/2:
            self.goto(x_coord, self.ycor())

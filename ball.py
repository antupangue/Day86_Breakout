from turtle import Turtle, Screen
from constants import *


class Ball(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.board = screen
        self.shape("circle")
        self.color("white")
        self.speed(2)
        self.radius = self.get_shapepoly()[0][0]
        self.penup()
        self.setheading(70)

    def move(self):
        self.forward(STEP_BALL)
        # self.board.screen.ontimer(self.move, TIMER_BALL)

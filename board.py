from turtle import Screen
from turtle import Turtle
from constants import *


class Board:
    def __init__(self):
        self.screen = Screen()
        self.border_x = (MAX_WIDTH - OFFSET_BOARD)/2
        self.border_y = (MAX_HEIGHT - OFFSET_BOARD)/2
        self.screen.setup(width=MAX_WIDTH, height=MAX_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Breakdown")
        self.__create_board()

    def __create_board(self):
        border = Turtle()
        border.hideturtle()
        border.speed(0)
        border.pencolor("white")
        border.pu()
        border.setpos(-self.border_x, self.border_y)
        border.pd()
        border.setpos(self.border_x, self.border_y)
        border.setpos(self.border_x, -self.border_y)
        border.setpos(-self.border_x, -self.border_y)
        border.setpos(-self.border_x, self.border_y)

    def stop(self):
        self.screen.exitonclick()

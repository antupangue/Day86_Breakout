from turtle import Turtle, Shape, Screen
from constants import *


class Brick(Turtle):
    def __init__(self, shape, idx_color):
        super().__init__()
        self.speed(0)
        self.size_x = (MAX_WIDTH - OFFSET_BOARD) / ROW_BRICKS
        self.size_y = 20
        self.shape(shape)
        self.hitpoints = idx_color + 1
        self.pu()
        self.setheading(90)




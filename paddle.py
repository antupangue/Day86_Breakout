from turtle import Turtle
STEP = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=6, stretch_len=0.5)
        self.pu()
        self.setheading(90)
        self.goto(0, -300)

    def go_right(self):
        x_coord = self.xcor() + STEP
        self.goto(x_coord, self.ycor())

    def go_left(self):
        x_coord = self.xcor() - STEP
        self.goto(x_coord, self.ycor())

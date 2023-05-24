from turtle import Screen


class Board:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=700, height=700)
        self.screen.bgcolor("black")
        self.screen.title("Breakdown")
        self.screen.tracer(0)

    def stop(self):
        self.screen.exitonclick()

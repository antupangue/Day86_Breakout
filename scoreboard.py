from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")

    def add_score(self, value):
        """
        Add to the current score
        :param value: is the index of the color of the broken brick
        :return:
        """
        self.score += value * 100

    def print_score(self):
        """
        Print final score of the game
        :return:
        """
        self.goto(-25, 200)
        self.write("SCORE:", align="center", font=("Courier", 80, "normal"))
        self.goto(-25, 100)
        self.write(self.score, align="center", font=("Courier", 80, "normal"))

    def print_gameover(self):
        """
        Print game over message
        :return:
        """
        self.goto(-25, 0)
        self.color("red")
        self.write("GAME OVER", align="center", font=("Courier", 80, "normal"))

    def print_win(self):
        """
        Print victory message
        :return:
        """
        self.goto(-25, 0)
        self.color("green")
        self.write("YOU WIN!!!", align="center", font=("Courier", 80, "normal"))

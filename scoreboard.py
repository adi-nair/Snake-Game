from turtle import Turtle
from food import Food


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 24, "normal"))

    def end_game(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over Score: {self.score}", False, align="center", font=("Arial", 24, "normal"))
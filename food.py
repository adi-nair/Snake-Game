from turtle import Turtle
import random


class Food(Turtle):  # made turtle the super class so no need to initial an object of turtle

    def __init__(self):  # inheritance
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.randomise_location()

    def randomise_location(self):
        x_cor = random.randint(-260, 260)
        y_cor = random.randint(-260, 260)
        self.goto(x_cor, y_cor)
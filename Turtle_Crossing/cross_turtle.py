import random
from turtle import Turtle


class crossing_turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.goto(0,-270)
        self.shape("turtle")
        self.color("black")

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(),new_y)


    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(),new_y)
       
        
from turtle import Screen, Turtle
import random

turtle = Turtle()
directions = [0,90,180,270]
turtle.width('3')
colours = ["yellow", "orange", "red", "green", "blue", "purple", "black", "gray", "brown"]


for i in range(0,50):
    turtle.color(random.choice(colours))
    turtle.forward(50)
    turtle.right(random.choice(directions))

screen = Screen()
screen.exitonclick()
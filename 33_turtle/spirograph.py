from turtle import Turtle, Screen
import random

turtle = Turtle()

colours = ["yellow", "orange", "red", "green", "blue", "purple", "black", "gray", "brown"]

turtle.speed('fastest')

for i in range (0,36):
    turtle.color(random.choice(colours))
    turtle.circle(100)
    turtle.setheading(turtle.heading() + 10)

screen = Screen()




screen.exitonclick()
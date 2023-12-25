# import colorgram
# rgb_colour = []

# colours = colorgram.extract(r'C:\Users\vaisl\OneDrive\Desktop\Vaibhav\Python Learning\Course Projects\33_turtle\image.jpg',15)

# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r ,g ,b)
#     rgb_colour.append(new_colour)

# print(rgb_colour)


colours = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33)]

import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255) #The colormode attribute is for the file turtle
turtle.speed('fastest')

turtle = Turtle()
turtle.hideturtle()

turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
turtle.pendown()

for i in range(1,101):
    turtle.dot(20,random.choice(colours))
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()

    if i%10 == 0:
        turtle.penup()
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen = Screen()
screen.exitonclick()
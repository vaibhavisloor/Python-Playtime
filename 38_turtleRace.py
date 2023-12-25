from turtle import Turtle,Screen
import turtle
import random

turtle.setup(700,700)

turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()

is_race_on = False

user_choice =False

y_cor = [-200,-100,0,100,200,300]

all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-300,y=y_cor[turtle_index])
    all_turtles.append(new_turtle)


user_choice = screen.textinput(title="Hello",prompt="Which colour turtle will win ? Enter your choice ")


if user_choice:
     is_race_on = True

while is_race_on:
     for turtle in all_turtles:
          if turtle.xcor() > 330:
               is_race_on = False
               winning_colour = turtle.pencolor()
               if winning_colour == user_choice:
                    print(f"Congratulations !! {winning_colour} has won the game")
               else:
                    print(f"You lost . {winning_colour} has won the game")     
          else:
               turtle.forward(random.randint(0,10))          
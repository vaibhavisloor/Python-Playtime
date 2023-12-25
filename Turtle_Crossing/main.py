from turtle import Turtle,Screen
from cross_turtle import crossing_turtle
from cars import Car
from scoreboard import Scoreboard
import time


screen = Screen()
screen.tracer(0)
screen.bgcolor("white")
screen.setup(600,600)
screen.title("Turtle crossing road")

player = crossing_turtle()

screen.listen()
screen.onkeypress(player.move_up,"Up")
screen.onkeypress(player.move_down,"Down")

new_car = Car()


scoreboard=Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    new_car.create_car()
    new_car.move_car()

    for car in new_car.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 300 :
        scoreboard.update_level()
        new_car.level -= 1
        player.goto(0,-270)

    if scoreboard.level == 10:
        scoreboard.you_win()
        game_is_on = False




screen.exitonclick()
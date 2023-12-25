from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)


left_paddle = (-285,0)
right_paddle = (280,0)

paddle1 = Paddle(left_paddle)
paddle2 = Paddle(right_paddle)
ball = Ball()


screen.listen()
screen.onkeypress(paddle1.go_up,"w")
screen.onkeypress(paddle1.go_down,"s")
screen.onkeypress(paddle2.go_up,"Up")
screen.onkeypress(paddle2.go_down,"Down")

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    scoreboard.update_scoreboard()
    paddle1.check_paddle()
    paddle2.check_paddle()
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.xcor() > 250 and ball.distance(paddle2) < 50) or (ball.xcor() < -260 and ball.distance(paddle1) < 50):
        ball.bounce_x() 

    if (ball.xcor() > 310):    
        ball.reset_position()
        ball.bounce_y()
        ball.bounce_x()
        scoreboard.l_score_inc()

    if (ball.xcor() < -310):
        ball.reset_position()
        ball.bounce_y()
        ball.bounce_x()
        scoreboard.r_score_inc()




    time.sleep(0.04)
screen.exitonclick()
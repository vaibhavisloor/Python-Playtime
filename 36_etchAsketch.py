from turtle import Turtle,Screen

turt = Turtle()

def move_forward():
    turt.setheading(90)
    turt.forward(10)
    
def move_left():
    turt.setheading(180)
    turt.forward(10)

def move_right():
    turt.setheading(0)
    turt.forward(10)

def move_backwards():
    turt.setheading(270)
    turt.forward(10)    

screen = Screen()

screen.onkeypress(move_forward,'w')
screen.onkeypress(move_left,'a')
screen.onkeypress(move_backwards,'s')
screen.onkeypress(move_right,'d')
screen.listen()
screen.exitonclick()

    

from turtle import Turtle,Screen

turt = Turtle()

def move_forward():
    turt.forward(10)
    
def move_left():
    turt.setheading(turt.heading() + 10)

def move_right():
    turt.setheading(turt.heading() - 10)

def move_backwards():
    turt.backward(10)    

def clear_screen():
    turt.reset()
    
screen = Screen()

screen.listen()
screen.onkeypress(move_forward,'w')
screen.onkeypress(move_left,'a')
screen.onkeypress(move_backwards,'s')
screen.onkeypress(move_right,'d')
screen.onkeypress(clear_screen,'c')
screen.exitonclick()

    

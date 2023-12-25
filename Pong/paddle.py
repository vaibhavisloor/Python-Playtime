from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(4,0.8)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y= self.ycor() + 15
        self.goto(self.xcor(),new_y)


    def go_down(self):
        new_y= self.ycor() - 15
        self.goto(self.xcor(),new_y)   

    def check_paddle(self):
        if (self.ycor() > 253): 
            self.sety(253)  
        elif (self.ycor() < -253):
            self.sety(-253) 

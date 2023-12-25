from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-220,250)
        self.hideturtle()
        self.level = 1
        self.write(f"Level : {self.level}", align="center", font= ("Courier",15,"normal"))

    def update_level(self):
        self.clear()
        self.level +=1
        self.write(f"Level : {self.level}", align="center", font= ("Courier",15,"normal")) 

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font= ("Courier",30,"normal")) 

    
    def you_win(self):
        self.goto(0,0)
        self.write("You win", align="center", font= ("Courier",30,"normal"))     
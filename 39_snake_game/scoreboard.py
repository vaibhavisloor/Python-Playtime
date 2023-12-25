from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier',24, 'normal')

class scoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        with open("39_snake_game\data.txt") as data:
           self.highscore = int(data.read())
        self.goto(0,260)
        self.hideturtle()
        self.increase_score()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.highscore}", align=ALIGN, font=FONT)  

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGN, font=FONT)   

    def increase_score(self):
        self.score +=1
        self.clear()     
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("39_snake_game\data.txt","w") as data:
                data.write(f"{self.highscore}")
        self.score = 0 
        self.update_scoreboard()    

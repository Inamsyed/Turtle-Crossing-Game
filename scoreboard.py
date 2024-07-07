from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMNET = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.score = 0
        self.write(f"Level : {self.score}", align=ALIGNMNET, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", align=ALIGNMNET, font=FONT)

    def game_over(self):
        self.goto(0,30)
        self.write(f"GAME OVER", align=ALIGNMNET, font=FONT)
FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.color("black")
        self.refresh()


    def refresh(self):
        self.clear()
        self.goto(0, 250)
        your_score = (f"SCORE: {self.score}")
        self.write(your_score, move=False, align="center",font=FONT)

    def get_point(self):
        self.score += 1

    def game_over(self):

        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=FONT)








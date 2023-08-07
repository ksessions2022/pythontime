from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 500)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(300, 500)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_paddle_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_paddle_score(self):
        self.r_score += 1
        self.update_scoreboard()

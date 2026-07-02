from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.tell_info()

    def update_scoreboard(self):
        self.clear()
        self.goto(0,225)
        self.write(self.score, align="center", font=("Courier", 50, "bold"))
        self.goto(300,240)
        self.write("❤⁠"*self.lives, align="center", font=("Courier", 25, "bold"))

    def point(self):
        self.score += 50
        self.update_scoreboard()

    def tell_info(self):
        self.clear()
        self.goto(0,225)
        self.write("PRESS ⬆ TO START", align="center", font=("Courier", 50, "bold"))

    def lost_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,225)
        self.write("GAME OVER", align="center", font=("Courier", 50, "bold"))

    def win(self):
        self.clear()
        self.goto(0,225)
        self.write("YOU WON!", align="center", font=("Courier", 50, "bold"))

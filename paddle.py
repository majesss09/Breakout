from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(1,5,0)
        self.penup()
        self.goto(0,-200)

    def moveleft(self):
        self.goto(self.xcor()-30,self.ycor())

    def moveright(self):
        self.goto(self.xcor()+30,self.ycor())
        
    
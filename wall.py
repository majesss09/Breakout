from turtle import Turtle

class Wall(Turtle):
    def __init__(self, coordinates, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(1,5,0)
        self.penup()
        self.goto(coordinates)

        
    
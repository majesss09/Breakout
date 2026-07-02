from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.goto(0,-180)

    def bounce_y(self):
        self.y_move *= -1

    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0,0)
    
    def paddle_bounce(self, pos):
        self.bounce_y()
        #-50 -30 -20  0  20  30  50
        if pos > -20 and pos <= 0:
            self.y_move = 15
            self.x_move = -2
        elif pos < 20 and pos > 0:
            self.y_move = 15
            self.x_move = 2

        elif pos > -30 and pos < -20:
            self.y_move = 7
            self.x_move = -12
        elif pos < 30 and pos > 20:
            self.y_move = 7
            self.x_move = 12

        elif pos < -30:
            self.y_move = 6
            self.x_move = -15
        elif pos > 30:
            self.y_move = 6
            self.x_move = 15

        self.goto(self.xcor()+self.x_move,self.ycor()+10)



from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from time import sleep as wait
from scoreboard import Scoreboard
from wall import Wall

def turn_on_game():
    global game_is_on, stop
    game_is_on = True
    stop = False

    scoreboard.update_scoreboard()

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)


paddle = Paddle()

walls = [[] for _ in range(5)]

for i in range(-3,4):
    walls[0].append(Wall((i*110, 225), "red"))

for i in range(-3,4):
    walls[1].append(Wall((i*110, 200), "orange"))

for i in range(-3,4):
    walls[2].append(Wall((i*110, 175), "yellow"))

for i in range(-3,4):
    walls[3].append(Wall((i*110, 150), "green"))

for i in range(-3,4):
    walls[4].append(Wall((i*110, 125), "blue"))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.moveleft,"Left")
screen.onkey(paddle.moveright,"Right")



waiting_time = 0.05
game_is_on = False

while game_is_on == False:
    wait(waiting_time)
    screen.update()
    ball.goto(paddle.xcor(),paddle.ycor()+20)
    screen.onkey(turn_on_game,"Up")

while game_is_on == True:
    wait(waiting_time)
    screen.update()
    ball.move()

    if ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.ycor() < -180:
        ball.paddle_bounce(pos=-(paddle.xcor()-ball.xcor()))
    
    if ball.xcor() > 360 or ball.xcor() < -360:
        ball.bounce_x()

    if ball.ycor() < -280:
        scoreboard.lost_life()
        if scoreboard.lives < 1:
            scoreboard.game_over()
            game_is_on = False
        else:
            stop = True
            
            while stop == True:
                wait(waiting_time)
                screen.update()
                ball.goto(paddle.xcor(),paddle.ycor()+20)
                screen.onkey(turn_on_game,"Up")


    for row_idx, row in enumerate(walls):
        for wall in row[:]:
            dx = abs(ball.xcor() - wall.xcor())
            dy = abs(ball.ycor() - wall.ycor())
            if dx < 60 and dy < 20:
                ball.bounce_y()
                wall.hideturtle()
                wall.goto(1000, 1000)
                try:
                    row.remove(wall)
                except ValueError:
                    pass
                scoreboard.point()

    
    if walls == [[] for _ in range(5)]:
        screen.update()
        scoreboard.win()
        game_is_on = False
    




screen.exitonclick()


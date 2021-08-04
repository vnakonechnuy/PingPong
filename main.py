from turtle import Screen
from turtle import Turtle
from paddle import Paddle
import time
from ball import Ball
from score import Score

def center():
    line = Turtle()
    line.speed('fastest')
    line.penup()
    line.pencolor('white')
    line.pensize(7)
    line.setpos(0, 300)
    line.setheading(270)
    while line.ycor() > -300:
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(40)

score_1 = Score((-50, 270))
score_2 = Score((40, 270))
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()
center()
player_1 = Paddle((-360, 0))
player_2 = Paddle((360, 0))
ball = Ball()
screen.onkey(key='w', fun=player_1.move_up)
screen.onkey(key='s', fun=player_1.move_down)
screen.onkey(key='Up', fun=player_2.move_up)
screen.onkey(key='Down', fun=player_2.move_down)


game_is_on = True

while game_is_on:
    time.sleep(0.01)
    ball.move()
    score_1.write_score()
    score_2.write_score()
    screen.update()
    # Попадання мяча в стіну
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce()

    # Гол
    elif ball.xcor() >= 360 or ball.xcor() <= -360:
        if ball.ycor() > 0:
            score_1.score += 1
        elif ball.ycor() < 0:
            score_1.score += 1
        ball.go_to_start()

    # Зчитуєм попадання мяча в ракетку
    if ball.xcor() < -350 and ball.distance(player_1) < 50:
        print(ball.heading())
        ball.bounce_paddle()
    elif ball.xcor() > 350 and ball.distance(player_2) < 50:
        ball.bounce_paddle()







screen.exitonclick()
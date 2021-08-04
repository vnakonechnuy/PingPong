from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.shapesize(0.7)
        self.penup()
        self.y_move = 5
        self.x_move = 3

    def go_to_start(self):
        self.speed('fastest')
        self.goto(0, 0)
        self.speed(10)
        time.sleep(2)
        self.move()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_paddle(self):

        self.x_move *= -1



from turtle import Turtle



class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('white')
        self.penup()
        self.speed(1)
        self.goto(pos)


    def move_up(self):
        xpos = self.xcor()
        ypos = self.ycor()
        self.goto(x=xpos, y=ypos + 30)

    def move_down(self):
        xpos = self.xcor()
        ypos = self.ycor()
        self.goto(x=xpos, y=ypos - 20)



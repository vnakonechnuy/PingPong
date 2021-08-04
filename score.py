from turtle import Turtle


class Score(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.goto(pos)
        self.pensize(10)
        self.score = 0

    def write_score(self):
        self.clear()
        self.write(str(self.score), font=('Arial', 20, 'normal'))


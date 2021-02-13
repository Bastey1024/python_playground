from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.pu()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_pos = self.xcor()
        self.y_pos = self.ycor()




    def start(self):
        self.setheading(random.choice([random.randint(-240,-200),random.randint(0,40)]))

    def move(self):

        self.forward(9)

    def collision(self):
        self.setheading(-(self.heading()+random.randint(0,1)))
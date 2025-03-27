from turtle import Turtle
import random

colors = ["lime", "blue", "yellow", "red", "orange"]


class Cars(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape("square")
        self.color(random.choice(colors))
        self.shapesize(1, 3)
        self.penup()
        self.setx(420)
        self.sety(random.randrange(-280, 280, 20))
        self.move_speed = -1 * speed

    def move(self):
        self.goto(self.xcor() + self.move_speed, self.ycor())

    def is_crashed(self, turtle):
        return (-40 < self.xcor() < 50) and (turtle.ycor() + 20 >= self.ycor() >= turtle.ycor())

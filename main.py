import random
import time
from turtle import Turtle, Screen

from cars import Cars
from level import Level

screen = Screen()
screen.setup(800, 600)
screen.tracer(0)
tim = Turtle("turtle")
tim.penup()
tim.goto(0, -280)
tim.setheading(90)
tim.color("green")
cars = []
level = Level()


def move_tim():
    tim.goto(tim.xcor(), tim.ycor() + 20)


def next_level():
    if tim.ycor() >= 300:
        level.increase_level()
        tim.teleport(0, -280)
        return True

    return False


screen.listen()
screen.onkey(fun=move_tim, key="Up")
speed = 10
should_continue = True

while should_continue:
    if random.randint(0, 5) % 3 == 0:
        cars.append(Cars(speed))
    for car in cars:
        car.move()
        if car.is_crashed(tim):
            should_continue = False

    if next_level():
        for car in cars:
            car.clear()
            car.hideturtle()
        cars.clear()
        speed += 10

    screen.update()
    time.sleep(0.1)

screen.exitonclick()

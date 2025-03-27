from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 250)
        self.level_text = 1
        self.write(f"Level: {self.level_text}",align="center",font=("Arial", 20, "normal"))
        self.hideturtle()

    def increase_level(self):
        self.level_text += 1
        self.clear()
        self.write(f"Level: {self.level_text}",align="center",font=("Arial", 20, "normal"))
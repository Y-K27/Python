from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed(0)
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 265)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 265)
        self.goto(random_x, random_y)
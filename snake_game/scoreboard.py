from email.charset import ALIASES
from turtle import Turtle

ALIGNMENT = 'center'
FOUNT = ("Arial", 16, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.teleport(-300,270)
        self.forward(600)
        self.penup()
        self.goto(0, 270)
        self.score_count = 0
        self.high_score = 0
        self.open_file()
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score_count} | High score: {self.high_score}",
                   align=ALIGNMENT,
                   font=FOUNT)
        self.add_top_line()


    def increase_score(self):
        self.score_count += 1
        self.update_score()

    def add_top_line(self):
        self.teleport(-300, 270)
        self.pendown()
        self.color("white")
        self.forward(600)
        self.penup()
        self.teleport(0, 270)

    def game_is_over(self):
        self.goto(0, 0)
        self.write('GAME IS OVER',
                   False,
                   align=ALIGNMENT,
                   font=FOUNT)

    def reset(self):
        if self.score_count > self.high_score:
            self.high_score = self.score_count
            self.save_score()
        self.score_count = 0
        self.update_score()

    def open_file(self):
        with open("data.txt") as data_file:
            self.high_score = int(data_file.read())
            data_file.close()

    def save_score(self):
        with open("data.txt", "w") as data_file:
            data_file.write(str(self.high_score))
            data_file.close()
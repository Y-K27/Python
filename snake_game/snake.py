from turtle import Turtle

SEGMENTS_SIZE = 20
MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.the_snake_segments = []
        self.create_snake()
        self.head = self.the_snake_segments[0]

    def create_snake(self):
        for snake_index in STARTING_POSITION:
            self.add_segment(snake_index)

    def add_segment(self, position):
        part = Turtle(shape="square")
        part.color("green")
        part.penup()
        part.goto(position)
        self.the_snake_segments.append(part)

    def increase_snake_size(self):
        self.add_segment(self.the_snake_segments[-1].position())

    def move(self):
        for part_index in range(len(self.the_snake_segments) - 1, 0, -1):
            x = self.the_snake_segments[part_index - 1].xcor()
            y = self.the_snake_segments[part_index - 1].ycor()
            self.the_snake_segments[part_index].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for segment in self.the_snake_segments:
            segment.hideturtle()
        self.the_snake_segments.clear()
        self.create_snake()
        self.head = self.the_snake_segments[0]

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
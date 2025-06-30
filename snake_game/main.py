import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.increase_snake_size()
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 260 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    #detect collision with the tail
    for segment in snake.the_snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
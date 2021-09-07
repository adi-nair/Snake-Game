from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME!")
screen.tracer(0)

snake = Snake()
food = Food()
board = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game = True
while is_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Snake getting food
    if snake.head.distance(food) < 15:
        food.randomise_location()
        snake.elongate()
        snake.update_tail()
        board.score += 1
        board.update()

    # Snake hitting a wall
    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
        print("You have hit a wall")
        is_game = False
        board.end_game()

    # Snake hitting part of itself

    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 10:
            is_game = False
            board.end_game()


screen.exitonclick()

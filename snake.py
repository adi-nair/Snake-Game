from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]
        self.tail = self.snake_parts[len(self.snake_parts) - 1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.increment_length(position)

    def update_tail(self):
        self.tail = self.snake_parts[len(self.snake_parts) - 1]

    def increment_length(self, position):
        snake = Turtle()
        snake.penup()
        snake.shape("square")
        snake.color("white")
        snake.goto(position)
        self.snake_parts.append(snake)

    def elongate(self):
        pos = (self.tail.xcor(), self.tail.ycor())
        self.increment_length(pos)

    def move(self):
        for num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[num - 1].xcor()
            new_y = self.snake_parts[num - 1].ycor()
            self.snake_parts[num].goto(new_x, new_y)
            # moving the last snake body position to the previous ones eg 9th position is 10th
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
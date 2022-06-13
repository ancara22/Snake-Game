from snake_class import Snake
from turtle import Turtle, Screen
from food import Food
import time
from scorebord import Scoreboard

# Set the window
########################################
window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.tracer(0)
scorebord = Scoreboard()

# Set the snake
########################################
snake = Snake()
snake.create_segments()
snake.move()


# Set the food
########################################
food = Food()



# Set control
########################################
window.listen()
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")

s = 586
t = Turtle()
t.goto(-297, -290)
t.color("white")
t.pensize(10)
t.forward(s)
t.left(90)
t.forward(s)
t.left(90)
t.forward(s)
t.left(90)
t.forward(s)
t.left(90)
t.hideturtle()

# MOVE
########################################
border = 280

game_over = True
while game_over:
    window.update()
    time.sleep(0.2)
    snake.move()

    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scorebord.increase_score()
        window.update()

    if snake.turtles[0].xcor() > border \
            or snake.turtles[0].xcor() < - border \
            or snake.turtles[0].ycor() > border \
            or snake.turtles[0].ycor() < - border:
        game_over = False
        scorebord.game_over()

    for segment in snake.turtles[1:-1]:
        if snake.turtles[0].distance(segment) < 10:
            game_over = False
            scorebord.game_over()



window.exitonclick()

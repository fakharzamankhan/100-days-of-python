#Screen Setup and Snake body creation

from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("purple")
screen.title("Super Snake Game")
screen.tracer(0)
snake =Snake()
food =Food()
scoreboard = ScoreBoard()




screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect  collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect Collision with Wall
    if snake.head.xcor() > 285 or snake.head.xcor() <-285 or snake.head.ycor() >285 or snake.head.ycor() <-285:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()

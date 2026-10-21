from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("blue")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

scoreboard = Scoreboard()
scoreboard.goto(0, -200)
scoreboard.write(f"You have 5 Turns in Total!", align="center", font=("Courier", 20, "normal"))


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.r_score > scoreboard.set_score or scoreboard.l_score > scoreboard.set_score:
        scoreboard.game_over()
        if scoreboard.r_score > scoreboard.l_score:
            scoreboard.goto(0, -200)
            scoreboard.write(f"Winner is Right player with score {scoreboard.r_score}", align="center", font=("Courier", 20, "normal"))
        else:
            scoreboard.goto(0, -200)
            scoreboard.write(f"Winner is Left player with Score {scoreboard.l_score}", align="center", font=("Courier", 20, "normal"))

        game_is_on=False

screen.exitonclick()

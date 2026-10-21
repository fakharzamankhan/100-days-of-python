from turtle import Turtle, Screen
timmy = Turtle()
screen = Screen()
timmy.color("red")
timmy.shape("turtle")
timmy.shapesize(1)
timmy.speed(1)

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

screen.exitonclick()




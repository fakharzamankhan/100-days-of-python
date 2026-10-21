import turtle as t
import random

tim=t.Turtle()

colors= ["red","green","blue","orange","yellow","pink","black"]
directions = [0,90,180,270,360]
tim.pensize(15)
tim.speed("fastest")
for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))


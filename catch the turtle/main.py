import turtle
import random


turtle_run = turtle.Turtle()
screen = turtle.Screen()
screen.title("catch turtle")
screen.bgcolor("light blue")
turtle_run.up()

turtle_run.shape("turtle")

for i in range(60) :
    turtle_run.forward(random.randint(0,75))
    turtle_run.right(random.randint(0,360))
    turtle_run.left(random.randint(0,360))




turtle.done()




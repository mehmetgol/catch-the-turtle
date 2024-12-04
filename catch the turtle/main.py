import turtle
import random


# screen
screen = turtle.Screen()
screen.setup(width=750, height=750)
screen.title("Catch the Turtle Game")
screen.bgcolor("light blue")

# turtles
turtle_run = turtle.Turtle()
time_turtle2 = turtle.Turtle()
time0 = turtle.Turtle()
timereduce = turtle.Turtle()
reduceScore = turtle.Turtle()
Score0 = turtle.Turtle()

turtle_run.shape("turtle")
time_turtle2.shape("turtle")
time0.shape("turtle")
timereduce.shape("turtle")
reduceScore.shape("turtle")
Score0.shape("turtle")

Score0.color("brown3")
time0.color("chartreuse4")
time_turtle2.color("green")
timereduce.color("chartreuse3")
reduceScore.color("brown")

# turtle speed
time_turtle2.speed(0)
turtle_run.speed(0)
time0.speed(0)
timereduce.speed(0)
reduceScore.speed(0)
Score0.speed(0)

Score0.penup()
turtle_run.penup()
time_turtle2.penup()
time0.penup()
timereduce.penup()
reduceScore.penup()

# score and time
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score = 0
score_display.write(f"Skor: {score}", align="center", font=("Arial", 24, "normal"))

TimeTurtle = turtle.Turtle()
TimeTurtle.hideturtle()
TimeTurtle.penup()
TimeTurtle.goto(0, 235)
time = 20
TimeTurtle.write(f"Time: {time}", align="center", font=("Arial", 24, "normal"))

# boundry
BOUNDARY = 300


def check_boundary(turtle_instance):
    x, y = turtle_instance.xcor(), turtle_instance.ycor()
    if x < -BOUNDARY:
        turtle_instance.setx(-BOUNDARY)
    elif x > BOUNDARY:
        turtle_instance.setx(BOUNDARY)
    if y < -BOUNDARY:
        turtle_instance.sety(-BOUNDARY)
    elif y > BOUNDARY:
        turtle_instance.sety(BOUNDARY)

# turtle moving
def moveTarget():
    turtle_run.forward(random.randint(20, 50))
    turtle_run.setheading(random.randint(0, 360))
    check_boundary(turtle_run)
    screen.ontimer(moveTarget, 200)  # 0.2 saniyede bir tekrar

def timeTarget():
    time_turtle2.forward(random.randint(20, 50))
    time_turtle2.setheading(random.randint(0, 360))
    check_boundary(time_turtle2)
    screen.ontimer(timeTarget, 200)
def doingTime0() :
    time0.forward(random.randint(20, 50))
    time0.setheading(random.randint(0, 360))
    check_boundary(time0)
    screen.ontimer(doingTime0, 200)
def timeReducef() :
    timereduce.forward(random.randint(20, 50))
    timereduce.setheading(random.randint(0, 360))
    check_boundary(timereduce)
    screen.ontimer(timeReducef, 200)
def reduceSkoreMove():
    reduceScore.forward(random.randint(20, 50))
    reduceScore.setheading(random.randint(0, 360))
    check_boundary(reduceScore)
    screen.ontimer(reduceSkoreMove, 200)
def Score0move():
    Score0.forward(random.randint(20, 50))
    Score0.setheading(random.randint(0, 360))
    check_boundary(Score0)
    screen.ontimer(Score0move, 200)

# timer
def countdown():

    global time
    global score
    TimeTurtle.clear()
    if time > 0:
        time -= 1
        score_display.write(f"Skor: {score}", align="center", font=("Arial", 24, "normal"))
        TimeTurtle.write(f"Time: {time}", align="center", font=("Arial", 24, "normal"))

        screen.ontimer(countdown, 1000)
    else:
        time = 20
        score =0
        score_display.clear()
        TimeTurtle.clear()
        countdown()


# onclick
def Score1(x, y):
    global score
    if turtle_run.distance(x, y) < 20:
        score += 1
        score_display.clear()
        #score_display.write(f"Skor: {score}", align="center", font=("Arial", 24, "normal"))
        turtle_run.goto(random.randint(-BOUNDARY, BOUNDARY), random.randint(-BOUNDARY, BOUNDARY))

def time3(x, y):
    global time
    if time_turtle2.distance(x, y) < 20:
        time += 5
        time = time - 2
        TimeTurtle.clear()
        TimeTurtle.write(f"Time: {time}", align="center", font=("Arial", 24, "normal"))
        time_turtle2.goto(random.randint(-BOUNDARY, BOUNDARY), random.randint(-BOUNDARY, BOUNDARY))

def time0function(x, y):
    global time
    if time0.distance(x, y) < 20:
        time = time - time
        time0.clear()
        time_turtle2.goto(random.randint(-BOUNDARY, BOUNDARY), random.randint(-BOUNDARY, BOUNDARY))
def reduceTime(x, y):
    global time
    if  timereduce.distance(x, y) < 20:
        time -= 5
        time +=2
        TimeTurtle.write(f"Time: {time}", align="center", font=("Arial", 24, "normal"))
        timereduce.clear()

        timereduce.goto(random.randint(-BOUNDARY, BOUNDARY), random.randint(-BOUNDARY, BOUNDARY))
def reduce_skore(x, y):
    global score
    if reduceScore.distance(x, y) < 20:
        score -= 2
        score_display.clear()
        score_display.write(f"Skor: {score}", align="center", font=("Arial", 24, "normal"))
        reduceScore.goto(random.randint(-BOUNDARY, BOUNDARY), random.randint(-BOUNDARY, BOUNDARY))
def score0function(x, y):
    global score
    if Score0.distance(x, y) < 20:
        score = score - score
        Score0.clear()
        score_display.clear()
        Score0.goto(random.randint(-BOUNDARY, BOUNDARY), random.randint(-BOUNDARY, BOUNDARY))

# connecting onclick
turtle_run.onclick(Score1)
time_turtle2.onclick(time3)
time0.onclick(time0function)
timereduce.onclick(reduceTime)
reduceScore.onclick(reduce_skore)
Score0.onclick(score0function)

#move
moveTarget()
timeTarget()
doingTime0()
timeReducef()
reduceSkoreMove()
Score0move()

countdown()

screen.mainloop()

turtle.done()

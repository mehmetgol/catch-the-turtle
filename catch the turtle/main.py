import turtle
import random

turtle_run = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=600, height=600)
#time_turtle = turtle.Turtle()
#time_turtle.up()
screen.title("catch turtle")
screen.bgcolor("light blue")

turtle_run.up()

width = screen.window_width() // 2
height = screen.window_height() // 2
turtle_run.shape("turtle")

turtle_run.goto(0, 250)
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)  # Ekranın üst kısmına yerleştir
score_display.write(f"Skor: {score}", align="center", font=("Arial", 24, "normal"))


turtle_run.goto(0,0)
def moveTarget() :
    for i in range(60) :
        turtle_run.forward(random.randint(0,75))
        turtle_run.right(random.randint(0,360))
        turtle_run.left(random.randint(0,360))
time = 5
time_turtle = turtle.Turtle()
time_turtle.hideturtle()
time_turtle.penup()
time_turtle.goto(0, 230)


def countdown():
    global time
    time_turtle.clear()
    if time > 0:
        time_turtle.write(f"Time: {time}", align="center", font=("Arial", 24, "normal"))
        time -= 1
        screen.ontimer(countdown, 1000)  # 1 saniye sonra tekrar çağır
    else:
        time_turtle.write("Time's up!", align="center", font=("Arial", 24, "normal"))
        while True :
            turtle_run.home()


countdown()
time_turtle.write(f"time: {time}", align ="center", font = ("arial",24,"normal"))
def check_hit(x, y):
    global score

    if turtle_run.distance(x, y) < 20:

        score += 1
        score_display.clear()
        score_display.write(f"Skor: {score}", align="center", font=("Arial", 24, "normal"))
        moveTarget()
        turtle_run.onclick()

turtle_run.onclick(check_hit)
moveTarget()
check_hit(0,19)
turtle.done()




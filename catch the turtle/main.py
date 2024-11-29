import turtle
import random


# Ekran ayarları
screen = turtle.Screen()
screen.setup(width=750, height=750)
screen.title("Catch the Turtle Game")

# Kaplumbağalar
turtle_run = turtle.Turtle()
time_turtle2 = turtle.Turtle()

turtle_run.shape("turtle")
time_turtle2.shape("turtle")

time_turtle2.color("green")

time_turtle2.speed(0)
turtle_run.speed(0)

turtle_run.penup()
time_turtle2.penup()

# Skor ve zaman göstergeleri
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 260)
score = 0
#score_display.write(f"Skor: {score}", align="center", font=("Arial", 24, "normal"))

TimeTurtle = turtle.Turtle()
TimeTurtle.hideturtle()
TimeTurtle.penup()
TimeTurtle.goto(0, 235)
time = 20
TimeTurtle.write(f"Time: {time}", align="center", font=("Arial", 24, "normal"))

# Sınır ayarları
BOUNDARY = 300

# Sınır kontrol fonksiyonu
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

# Kaplumbağa hareketleri
def moveTarget():
    turtle_run.forward(random.randint(20, 50))
    turtle_run.setheading(random.randint(0, 360))
    check_boundary(turtle_run)
    screen.ontimer(moveTarget, 200)  # 0.2 saniyede bir tekrar

def timeTarget():
    time_turtle2.forward(random.randint(20, 50))
    time_turtle2.setheading(random.randint(0, 360))
    check_boundary(time_turtle2)
    screen.ontimer(timeTarget, 200)  # 0.2 saniyede bir tekrar

# Zamanlayıcı


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


# Tıklama olayları
def check_hit(x, y):
    global score
    if turtle_run.distance(x, y) < 20:
        score += 1
        score_display.clear()
        score_display.write(f"Skor: {score}", align="center", font=("Arial", 24, "normal"))
        turtle_run.goto(random.randint(-BOUNDARY, BOUNDARY), random.randint(-BOUNDARY, BOUNDARY))

def check_hit2(x, y):
    global time
    if time_turtle2.distance(x, y) < 20:
        time += 5
        time = time - 2
        TimeTurtle.clear()
        TimeTurtle.write(f"Time: {time}", align="center", font=("Arial", 24, "normal"))
        time_turtle2.goto(random.randint(-BOUNDARY, BOUNDARY), random.randint(-BOUNDARY, BOUNDARY))

# Tıklama işlevlerini kaplumbağalara bağlama
turtle_run.onclick(check_hit)
time_turtle2.onclick(check_hit2)

moveTarget()
timeTarget()
countdown()

screen.mainloop()

turtle.done()

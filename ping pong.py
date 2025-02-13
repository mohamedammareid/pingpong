import turtle
import time
import _tkinter  # For catching TclError

# Initialize screen
wind = turtle.Screen()
wind.title("Ping Pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)  # Disable automatic updates

# Racket 1
racket1 = turtle.Turtle()
racket1.speed(0)
racket1.shape("square")
racket1.color("blue")
racket1.shapesize(stretch_wid=5, stretch_len=1)
racket1.penup()
racket1.goto(-350, 0)

# Racket 2
racket2 = turtle.Turtle()
racket2.speed(0)
racket2.shape("square")
racket2.color("red")
racket2.shapesize(stretch_wid=5, stretch_len=1)
racket2.penup()
racket2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2.0  # Moderate ball speed
ball.dy = 2.0

# Score
score1 = 0
score2 = 0

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(f"Player 1: {score1}  Player 2: {score2}",
            align="center", font=("Courier", 24, "normal"))

# Functions for paddle movement
def racket_1_up():
    y = racket1.ycor()
    if y < 250:
        racket1.sety(y + 30)

def racket_1_down():
    y = racket1.ycor()
    if y > -250:
        racket1.sety(y - 30)

def racket_2_up():
    y = racket2.ycor()
    if y < 250:
        racket2.sety(y + 30)

def racket_2_down():
    y = racket2.ycor()
    if y > -250:
        racket2.sety(y - 30)

# Keyboard binding
wind.listen()
wind.onkeypress(racket_1_up, "w")
wind.onkeypress(racket_1_down, "s")
wind.onkeypress(racket_2_up, "Up")
wind.onkeypress(racket_2_down, "Down")

# Main game loop wrapped to handle window closure gracefully
try:
    while True:
        wind.update()  # Manual screen update

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score1 += 1
            score.clear()
            score.write(f"Player 1: {score1}  Player 2: {score2}",
                        align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score2 += 1
            score.clear()
            score.write(f"Player 1: {score1}  Player 2: {score2}",
                        align="center", font=("Courier", 24, "normal"))

        # Paddle collision checking
        if (340 < ball.xcor() < 350) and (racket2.ycor() - 50 < ball.ycor() < racket2.ycor() + 50):
            ball.setx(340)
            ball.dx *= -1

        if (-350 < ball.xcor() < -340) and (racket1.ycor() - 50 < ball.ycor() < racket1.ycor() + 50):
            ball.setx(-340)
            ball.dx *= -1

        # Control the frame rate
        time.sleep(0.01)

except (turtle.Terminator, _tkinter.TclError):
    print("Game closed gracefully.")

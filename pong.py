import turtle
import winsound

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  #stops the window from automatically updating, important for speed

score_a = 0
score_b = 0

paddle_hits = 0

paddle_a = turtle.Turtle()
paddle_a.speed(0)  #speed of animation, set to max
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()    #stops turtle from drawing a line
paddle_a.goto(-350, 0)   #0,0 in the middle

paddle_b = turtle.Turtle()
paddle_b.speed(0)  #speed of animation, set to max
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)  #speed of animation, set to max
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2    #delta (change) speed, make move up and diagonally 2 pixels
ball.dy = 0.2

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier",24, "bold"))

def paddle_a_up():
    y = paddle_a.ycor()  #returns the y coordinate, increases as you go up, decreases as you go down
    if y < 295 and y > -310:
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y < 310 and y > -295:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 295 and y > -310:
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y < 310 and y > -295:
        y -= 20
        paddle_b.sety(y)

win.listen()  #keyboard binding, listens for keyboard events
win.onkeypress(paddle_a_up, "w")  #case-sensitive, won't work if capslock is on
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

while score_a < 10 and score_b < 10:
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1   #reverses the direction
        winsound.PlaySound("Impact11.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("Impact11.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:   #if the ball goes past the paddle on right, it will go back to the centre and change direction
        ball.goto(0, 0)
        #ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        winsound.PlaySound("Explosion5.wav", winsound.SND_ASYNC)
        paddle_hits = 0
        ball.dx = -0.2

    if ball.xcor() < -390:
        ball.goto(0, 0)
        #ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "bold"))
        winsound.PlaySound("Explosion5.wav", winsound.SND_ASYNC)
        paddle_hits = 0
        ball.dx = 0.2

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        winsound.PlaySound("OldSchool30.wav", winsound.SND_ASYNC)
        paddle_hits += 1
        if paddle_hits < 6:
            ball.dx *= -1
            ball.dx -= 0.05
        else:
            ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        winsound.PlaySound("OldSchool30.wav", winsound.SND_ASYNC)
        paddle_hits += 1
        if paddle_hits < 6:
            ball.dx *= -1
            ball.dx += 0.05
        else:
            ball.dx *= -1

pen.clear()

if score_a > score_b:
    pen.write("Player A Wins!!", align="center", font=("Courier", 24, "bold"))
    pen.goto(0, 220)
    pen.write("Click anywhere to exit", align="center", font=("Courier", 24, "bold"))
    winsound.PlaySound("GameOver4.wav", winsound.SND_ASYNC)
else:
    pen.write("Player B Wins!!", align="center", font=("Courier", 24, "bold"))
    pen.goto(0, 220)
    pen.write("Click anywhere to exit", align="center", font=("Courier", 24, "bold"))
    winsound.PlaySound("GameOver4.wav", winsound.SND_ASYNC)

turtle.Screen().exitonclick()
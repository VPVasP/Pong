import turtle
import os

#setup the screem
wn = turtle.Screen()
wn.title("PongPython")
wn.bgcolor("grey")
wn.setup(width=800, height=600)
wn.tracer(0)

#score variables
player1score = 0
player2score = 0

#paddle1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("black")
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)

#paddle2

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("black")
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#display scores
ScoreDisplay = turtle.Turtle()
ScoreDisplay.speed(0)
ScoreDisplay.shape("square")
ScoreDisplay.color("black")
ScoreDisplay.penup()
ScoreDisplay.hideturtle()
ScoreDisplay.goto(0, 260)
ScoreDisplay.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#function to move the paddles
def paddle_a_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle_a_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle_b_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle_b_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

#keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#game loop
while True:
    wn.update()
    
    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

  
    if ball.xcor() > 350:
        player1score += 1
        ScoreDisplay.clear()
        ScoreDisplay.write("Player A: {}  Player B: {}".format(player1score, player2score), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        player2score += 1
        ScoreDisplay.clear()
        ScoreDisplay.write("Player A: {}  Player B: {}".format(player1score, player2score), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    #paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50:
        ball.dx *= -1 

    
    elif ball.xcor() > 340 and ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50:
        ball.dx *= -1
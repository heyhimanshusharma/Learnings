import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = -0.2

# Function
def paddle_a_up():
    y = paddle_a.ycor() # Get the Y co-ord
    y += 20 # Add 20 pixels to Y co-ord
    paddle_a.sety(y) # sets paddle_a to new y

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20 # Subtracts 20 pixels to the Y co-ord
    paddle_a.sety(y) # sets paddle_b to new y

# Similar function for paddle_b
def paddle_b_up():
    y = paddle_b.ycor() # Get the Y co-ord
    y += 20 # Add 20 pixels to Y co-ord
    paddle_b.sety(y) # sets paddle_a to new y

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20 # Subtracts 20 pixels to the Y co-ord
    paddle_b.sety(y) # sets paddle_b to new y

# Keyboard binding
wn.listen()     # Listens to keyboard press
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

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
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisons
    if (ball.xcor() > 340 and ball.xcor() > 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
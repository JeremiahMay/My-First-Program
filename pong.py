

import turtle
import random

wn = turtle.Screen() 
wn.title("Pong by Jeremiah May") 
wn.bgcolor('black') 
wn.setup(width=800, height=600) 
wn.tracer() 


# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") # sets the shape of the object
paddle_a.color("white") # sets the color of the object
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup() # stops turtle from drawing a line
paddle_a.goto(-350, 0) # sets the starting location
# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square") # sets the shape of the object
paddle_b.color("white") # sets the color of the object
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
# stretch_wid/len multiplies the object default value by 5
# stretch_wid =5 would make width 100, len = 1, keeps it at its default
paddle_b.penup() # stops turtle from drawing a line
paddle_b.goto(350, 0) # sets the starting location


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle") # sets the shape of the object
ball.color("white") # sets the color of the object
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup() # stops turtle from drawing a line
ball.goto(0, 0) # sets the starting location
ball.dx = 3
ball.dy = 3


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("Player 1: 0  Player 2: 0", align= "center", font=("courier",24,"normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor() # returns the y coordinate
    y += 20 # adds 20 pixels to y coordinate
    paddle_a.sety(y) # .sety() sets the y coordinate to what you want
    
def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor() # returns the y coordinate
    y += 20 # adds 20 pixels to y coordinate
    paddle_b.sety(y) # .sety() sets the y coordinate to what you want
    
def paddle_b_down():
    y = paddle_b.ycor()
    y += -20
    paddle_b.sety(y)
    
# Keyboard Binding
wn.listen() # tells python to listen for keyboard inputs
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")# Up is the up arrow key
wn.onkeypress(paddle_b_down,"Down")# Down is the down arrow key

# main game loop
while True:
    wn.update() # updates screen after each loop
    direction = [-1,1]
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
   
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
   
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= random.choice(direction)
        score_a += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a,score_b), align= "center", font=("courier",24,"normal"))
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= random.choice(direction)
        score_b += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_a,score_b), align= "center", font=("courier",24,"normal"))
    
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

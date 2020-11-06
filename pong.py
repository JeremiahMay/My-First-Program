# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 22:42:53 2020

@author: jimid
"""

import turtle
import random

wn = turtle.Screen() # creates a screen to use
wn.title("Pong by Jeremiah") # sets the title of the screen
wn.bgcolor('black') # changes the background color
wn.setup(width=800, height=600) # sets the size of the window
wn.tracer() # stops the windown from updating allowing for manual update
# this speeds up the game

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") # sets the shape of the object
paddle_a.color("white") # sets the color of the object
# normal default value of a object is 20
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
# stretch_wid/len multiplies the object default value by 5
# stretch_wid =5 would make width 100, len = 1, keeps it at its default
paddle_a.penup() # stops turtle from drawing a line
paddle_a.goto(-350, 0) # sets the starting location
# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square") # sets the shape of the object
paddle_b.color("white") # sets the color of the object
# normal default value of a object is 20
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
# normal default value of a object is 20
ball.shapesize(stretch_wid=1,stretch_len=1)
# stretch_wid/len multiplies the object default value by 5
# stretch_wid =5 would make width 100, len = 1, keeps it at its default
ball.penup() # stops turtle from drawing a line
ball.goto(0, 0) # sets the starting location
ball.dx = 3
ball.dy = 3
# 'd' means delta or change, 'x' and 'y' stand for the coordinates 
# this means the everytime the ball moves it will move by 2px
# x postive makes it move to the right
# x negative makes it move to the left
# y postive makes it move up
# y negative makes it move down

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
    # to move the ball you need to find the y coordinate
    y = paddle_a.ycor() # returns the y coordinate
    y += 20 # adds 20 pixels to y coordinate
    paddle_a.sety(y) # .sety() sets the y coordinate to what you want
    
def paddle_a_down():
    y = paddle_a.ycor()
    y += -20
    paddle_a.sety(y)
    
def paddle_b_up():
    # to move the ball you need to find the y coordinate
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
# when the user presses key "w" it will call what is inside the parameters
# in this case it calls paddle_a_up which moves the paddle 20px up

# main game loop
while True:
    wn.update() # updates screen after each loop
    direction = [-1,1]
    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    # gets the current x coordinate and adds the value of ball.dx
    ball.sety(ball.ycor() + ball.dy)
    
    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # this reverses the direction of the ball
        # since dy = 2, dy * -1 = -2
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # since a player scores when the ball goes past the left or right paddle
    # we want the ball to go back to the middle and start moving again
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
    # ball and paddle collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
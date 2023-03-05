# Pong using Python3

import turtle
import winsound

win = turtle.Screen() #To create a window
win.title("  PONG by Abhilash_Hari  ")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0) #Inorder to fasten the game

# Score
score_a = 0
score_b = 0

# Paddle A Code
paddle_a = turtle.Turtle()#creates a python turtle object
paddle_a.speed(0) #To Set the speed of graphics to max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #To change the size of paddle (By defalut the size is 20*20)
paddle_a.penup() #Turtle usually draw a line  as moving so to avoid it is lifted up
paddle_a.goto(-350,0) #The paddle to start at coordinate(-350,0)

# Paddle B Code
paddle_b = turtle.Turtle()
paddle_b.speed(0) #To Set the speed of graphics to max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1) #To change the size of paddle
paddle_b.penup() #Draw a line as moving
paddle_b.goto(350,0) #The paddle to start at coordinate(350,0)


# Ball Code
ball = turtle.Turtle()
ball.speed(0) #To Set the speed of graphics to max
ball.shape("square")
ball.color("red")
ball.penup() #To avoid drawing of line as moving
ball.goto(0,0) #The ball to start at coordinate(0,0)
ball.dx = 0.08 #Movement of ball through x-axis by 0.08 pixels at a time
ball.dy = 0.08 #Movement of ball through y-axis by 0.08 pixels at a time

# Pen Code
pen = turtle.Turtle()
pen.speed(0) #To set the animation speed to max
pen.color("white")
pen.penup() #Don't want to show line
pen.hideturtle() #Hide the turtle
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier",24,"normal"))

# Function for Paddle Movement
def paddle_a_up(): #Defining paddle_a function
	y = paddle_a.ycor() #Gives current y-coordinate value to y
	y += 30 #Change(add) y-coordinate by 30pixels 
	paddle_a.sety(y) #Sets the paddle to the current updated postion of y-coordinate

def paddle_a_down(): #Defining paddle_a function
	y = paddle_a.ycor() #Gives current y-coordinate value to y
	y -= 30 #Change(subtract) y-coordinate by 30pixels 
	paddle_a.sety(y) #Sets the paddle to the current updated postion of y-coordinate

def paddle_b_up(): #Defining paddle_b function
	y = paddle_b.ycor() #Gives current y-coordinate value to y
	y += 30 #Change(add) y-coordinate by 30pixels 
	paddle_b.sety(y) #Sets the paddle to the current updated postion of y-coordinate

def paddle_b_down(): #Defining paddle_b function
	y = paddle_b.ycor() #Gives current y-coordinate value to y
	y -= 30 #Change(subtract) y-coordinate by 30pixels 
	paddle_b.sety(y) #Sets the paddle to the current updated postion of y-coordinate

# Keyboard Binding
win.listen() #To listen to keyboard input
win.onkeypress(paddle_a_up,"w") #When the keyboard presses lowercase "w" call the paddle_a_up function
win.onkeypress(paddle_a_down,"s") #When the keyboard presses lowercase "s" call the paddle_a_down function
win.onkeypress(paddle_b_up,"o") #When the keyboard presses lowercase "o" call the paddle_b_up function
win.onkeypress(paddle_b_down,"l") #When the keyboard presses lowercase "l" call the paddle_b_down function



# Main Game Loop
while True:
	win.update() #Updates through every loop

	#Move the ball
	ball.setx(ball.xcor() + ball.dx) #The ball moves from (0,0) by 0.08 pixels across x-axis
	ball.sety(ball.ycor() + ball.dy) #The ball moves from (0,0) by 0.08 pixels across y-axis

	# Border Checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1 #Reverse the direction of the ball
		
	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1 #Reverse the direction of the ball
	
	if ball.xcor() > 390:
		ball.goto(0,0) #Place the ball back to (0,0)
		ball.dx *= -1 #Reverse the direction of the ball
		score_a += 1
		pen.clear() #Clear the existing value
		pen.write("Player A: {}   Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))

	if ball.xcor() < -390:
		ball.goto(0,0) #Reverse the direction of the ball
		ball.dx *= -1 #Reverse the direction of the ball
		score_b += 1
		pen.clear() #Clears the existing value
		pen.write("Player A: {}   Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))

	# Paddle and Ball Collision Code
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
		ball.setx(340)
		ball.dx *= -1
	
	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
		ball.setx(-340)
		ball.dx *= -1
		

	

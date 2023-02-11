# Pong using Python3

import turtle

win = turtle.Screen()
win.title("  PONG by Abhilash_Hari  ")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0) #Inorder to fasten the game


# Paddle A Code
paddle_a = turtle.Turtle()
paddle_a.speed(0) #To Set the speed of graphics to max
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #To change the size of paddle
paddle_a.penup() #Draw a line as moving
paddle_a.goto(-350,0) #The paddle to start at coordinate(-350,0)

# Paddle B Code
paddle_b = turtle.Turtle()
paddle_b.speed(0) #To Set the speed of graphics to max
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1) #To change the size of paddle
paddle_b.penup() #Draw a line as moving
paddle_b.goto(350,0) #The paddle to start at coordinate(350,0)


#Ball Code
ball = turtle.Turtle()
ball.speed(0) #To Set the speed of graphics to max
ball.shape("square")
ball.color("red")
ball.penup() #Draw a line as moving
ball.goto(0,0) #The ball to start at coordinate(0,0)
ball.dx = 0.01#Movement of ball through x-axis by 0.07 pixels at a time
ball.dy = -0.01#Movement of ball through y-axis by 0.07 pixels at a time



# Function for Paddle Movement
def paddle_a_up(): #Defining paddle_a function
	y = paddle_a.ycor() #Gives y-coordinate value to y
	y += 20 #Change(add) y-coordinate by 20pixels 
	paddle_a.sety(y) #Sets the paddle to the current updated postion of y-coordinate

def paddle_a_down(): #Defining paddle_a function
	y = paddle_a.ycor() #Gives y-coordinate value to y
	y -= 20 #Change(subtract) y-coordinate by 20pixels 
	paddle_a.sety(y) #Sets the paddle to the current updated postion of y-coordinate

def paddle_b_up(): #Defining paddle_b function
	y = paddle_b.ycor() #Gives y-coordinate value to y
	y += 20 #Change(add) y-coordinate by 20pixels 
	paddle_b.sety(y) #Sets the paddle to the current updated postion of y-coordinate

def paddle_b_down(): #Defining paddle_b function
	y = paddle_b.ycor() #Gives y-coordinate value to y
	y -= 20 #Change(subtract) y-coordinate by 20pixels 
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

	# Move the ball
	ball.setx(ball.xcor() + ball.dx) #The ball moves from (0,0) by 0.07 pixels across x-axis
	ball.sety(ball.ycor() + ball.dy) #The ball moves from (0,0) by 0.07 pixels across y-axis
	
	# Border Checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball.ycor() > -290:
		ball.sety(-290)
		ball.dy *= -1

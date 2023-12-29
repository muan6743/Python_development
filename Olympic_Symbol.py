import turtle

# Set the thickness for each ring
ring_thickness = 10

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(10)

# Set the initial position of the turtle
t.penup()
t.goto(-100, 0)
t.pendown()

# Draw the first ring (blue)
t.color("blue")
t.pensize(ring_thickness)
t.circle(50)

# Move to the next position to draw the second ring
t.penup()
t.goto(50, 0)
t.pendown()

# Draw the second ring (black)
t.color("black")
t.pensize(ring_thickness)
t.circle(50)

# Move to the next position to draw the third ring
t.penup()
t.goto(200, 0)
t.pendown()

# Draw the third ring (red)
t.color("red")
t.pensize(ring_thickness)
t.circle(50)

# Move to the next position to draw the fourth ring
t.penup()
t.goto(-25, -50)
t.pendown()

# Draw the fourth ring (yellow)
t.color("yellow")
t.pensize(ring_thickness)
t.circle(50)

# Move to the next position to draw the fifth ring
t.penup()
t.goto(125, -50)
t.pendown()

# Draw the fifth ring (green)
t.color("green")
t.pensize(ring_thickness)
t.circle(50)

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()

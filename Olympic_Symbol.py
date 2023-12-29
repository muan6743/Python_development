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


# Keep the window open
turtle.done()

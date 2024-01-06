# Import the required modules
import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Race")

# Set up the racing track
track = turtle.Turtle()
track.shape("classic")  # Use the 'classic' shape for the track
track.penup()
track.goto(-200, 200)
track.pendown()
track.speed(0)
track.color("black")
track.width(3)
track.right(90)
for _ in range(21):
    track.forward(20)
    track.penup()
    track.forward(20)
    track.pendown()

# Create the turtles
turtles = []
colors = ["red", "blue", "green", "yellow", "orange"]
y_positions = [180, 140, 100, 60, 20]

# Set the specs and speed for each turtle
for i in range(5):
    turtle = turtle.Turtle()
    turtle.shape("turtle")  # Use the 'turtle' shape for the turtles
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-200, y_positions[i])
    turtle.pendown()
    turtle.speed(random.randint(1, 5))  # Set the speed of the turtle using randint()

    turtles.append(turtle)

turtle.done()

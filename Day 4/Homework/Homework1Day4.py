import turtle
import random

def draw_rectangle(turtle, x, y, width, height, color):
    """Draws a rectangle."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_house(turtle, start_x, start_y):
    """Draws a house with a door and two windows."""
    # House base
    draw_rectangle(turtle, start_x, start_y, 100, 100, "lightgray")
    
    # Roof
    turtle.fillcolor("maroon")
    turtle.begin_fill()
    turtle.goto(start_x, start_y + 100)
    turtle.goto(start_x + 50, start_y + 150)
    turtle.goto(start_x + 100, start_y + 100)
    turtle.goto(start_x, start_y + 100)
    turtle.end_fill()

    # Door
    draw_rectangle(turtle, start_x + 40, start_y, 20, 40, "brown")

    # Windows
    draw_rectangle(turtle, start_x + 10, start_y + 60, 20, 20, "lightblue")
    draw_rectangle(turtle, start_x + 70, start_y + 60, 20, 20, "lightblue")

def draw_garden(turtle, x, y, width, height):
    """Draws a simple garden."""
    draw_rectangle(turtle, x, y, width, height, "green")

def draw_sun(turtle, x, y):
    """Draws the sun."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("yellow")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

def draw_star(turtle, x, y):
    """Draws a star."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(20)
        turtle.right(144)
    turtle.end_fill()

# Setup the screen
turtle.bgcolor("sky blue")
artist = turtle.Turtle()
artist.speed(0)  # Fastest drawing speed

# Draw houses
house_positions = [(-300, -100), (-100, -100), (100, -100)]
for pos in house_positions:
    draw_house(artist, *pos)

# Draw garden in front of houses
draw_garden(artist, -350, -150, 700, 50)

# Draw the sun
draw_sun(artist, 200, 200)

# Draw stars
for _ in range(20):
    x = random.randint(-300, 300)
    y = random.randint(0, 300)
    draw_star(artist, x, y)

artist.hideturtle()  # Hide the turtle after drawing
turtle.done()

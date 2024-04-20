from turtle import*

def my_square():
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)
    forward(50)
    left(90)

def move_cursor(x, y):
    penup()
    goto(x, y)
    pendown()

my_square()

move_cursor(0,100)

my_square()

move_cursor(-100, 100)

my_square()

move_cursor(-100, 0)

my_square()

exitonclick()
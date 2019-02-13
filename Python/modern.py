import turtle
import random

turtle.colormode(255)

r = 0
g = 0
b = 0
x = 0
y = 0
width = 0
height = 0

def pick_color():
    global r
    global g
    global b
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
def pick_loc():
    global x
    global y
    x = random.randint(-150, 100)
    y = random.randint(-150, 100)
def pick_dim():
    global width
    global height
    width = random.randint(0,75)
    height = random.randint(0,75)

for i in range(20):
    pick_loc()
    turtle.penup()
    turtle.goto(x , y)
    turtle.pendown()
    turtle.begin_fill()
    pick_color()
    turtle.color(r , g , b)    
    pick_dim()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.end_fill()

turtle.exitonclick()




import turtle
import random

turtle.colormode(255)

r = 255
g = 255
b = 255
turtle.speed('fastest')
turtle.penup()
turtle.goto(100, -100)
turtle.left(120)
turtle.pendown()
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(57.8)
turtle.left(90)
turtle.forward(173)
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()
turtle.left(60)
turtle.forward(173)
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
turtle.right(120)
turtle.forward(173)
turtle.penup()
turtle.goto(0, 0)
turtle.left(60)
turtle.goto(0, -150)
turtle.right(90)
turtle.pendown()
i = 150
for x in range(255):
    turtle.color(r, g, b)
    turtle.circle(i)
    i += 0.5
    r -= 1

turtle.exitonclick()
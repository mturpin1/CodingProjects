import turtle
import random

turtle.shape('turtle')
turtle.color('green', 'blue')
for x in range(40):
    x = random.randint(-100,100)
    y = random.randint(-100,100)
    turtle.goto(x,y)

turtle.exitonclick()
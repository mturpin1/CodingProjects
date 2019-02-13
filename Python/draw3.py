import random
import turtle

turtle.colormode(225)

r = random.randint(0,225)
g = random.randint(0,225)
b = random.randint(0,225)

turtle.shape('turtle')
turtle.color(r, g, b)

turtle.exitonclick()
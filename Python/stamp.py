import turtle
import random
turtle.colormode(255)
turtle.shape('turtle')
for x in range(40):
    r = random.randint(0, 225)
    g = random.randint(0, 225)
    b = random.randint(0, 225)
    x = random.randint(-150, 100)
    y = random.randint(-150, 100)
    turtle.penup()
    turtle.goto(x , y)
    turtle.color(r , g , b)
    turtle.stamp()
turtle.exitonclick()
    

import turtle
turtle.speed('fastest')
turtle.penup()
turtle.goto(-50, 50)
def canisters1(radius):
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.forward(2 * radius + 5)

def moving():
    turtle.goto(-56, 0)

def canisters2(height, radius):
    turtle.pendown()
    turtle.forward(radius * 2)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(radius * 2)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.penup()
    turtle.forward(radius * 2 + 5)

for x in range(10):
    canisters1(12)

moving()

for x in range(10):
    canisters2(36, 6)

turtle.exitonclick()
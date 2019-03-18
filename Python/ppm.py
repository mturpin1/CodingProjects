import turtle
turtle.speed('fastest')
turtle.penup()
turtle.goto(-50, 50)
def canisters1(radius):
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.forward(2 * radius + 5)

def movement():
    turtle.goto(-62, 62)

def canisters2(height, radius):
    turtle.pendown()
    turtle.forward(int(radius) * 4)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(int(radius) * 4)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.penup()
    turtle.forward(int(radius) * 4 + 5)

def movement2():
    turtle.goto(-50, 14)

for x in range(10):
    canisters1(12)

movement()

for x in range(10):
    canisters2(36, 6)

movement2()

for x in range(10):
    canisters1(12)

turtle.exitonclick()
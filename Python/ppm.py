import turtle
turtle.screensize(3000, 2000)
turtle.speed('fastest')
turtle.penup()
turtle.right(90)
turtle.forward(305)
turtle.left(90)
turtle.pendown()
turtle.begin_fill()
turtle.circle(305)
turtle.end_fill()
turtle.penup()
turtle.left(90)
turtle.forward(305)
turtle.right(90)
turtle.left(155)
def canisters1(radius):
    turtle.pendown()
    turtle.forward(307)
    turtle.right(90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.left(90)
    turtle.backward(307)
    turtle.right(20)

for x in range(11):
    canisters1(24)

turtle.color('white')
turtle.goto(0, -100)
turtle.seth(0)
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.penup()
turtle.goto(0, -30)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()
turtle.penup()
turtle.goto(610, -305)
turtle.color('black')

for x in range(11):
    canisters1(24)

turtle.color('white')
turtle.goto(305, -252.5)
turtle.seth(0)
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.penup()
turtle.goto(305, -182.5)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()
turtle.penup()

turtle.exitonclick()
import turtle
turtle.speed('fastest')
turtle.circle(305)
turtle.penup()
turtle.goto(0, 305)
turtle.left(135)
def canisters1(radius):
    turtle.forward()
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(0, 25)
    turtle.right(20)

for x in range(10):
    canisters1(12)


turtle.exitonclick()
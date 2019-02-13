import turtle
while True:
    direction = input()
    if direction == 'w' or direction == 'a' or direction == 's' or direction == 'd':
        while direction == 'w':
            turtle.forward(1)
        while direction == 'a':
            turtle.left(1)
        while direction == 's':
            turtle.backward(1)
        while direction == 'd':
            turtle.right(1)
turtle.exitonclick()
    
import random
import turtle
turtle.colormode(255)
r = 0
g = 0
b = 0
x = 0
y = 0
def pick_color():
   global r
   global g
   global b
   r = random.randint(0, 255)
   g = random.randint(0, 255)
   b = random.randint(0, 255)
def pick_loc():
   global x
   global y
   x = random.randint(-150, 100)
   y = random.randint(-150, 100)
def draw_circle():
   turtle.speed(0)
   turtle.penup()
   turtle.goto(x , y)
   turtle.pendown()
   turtle.begin_fill()
   turtle.color(r , g , b)
   turtle.circle(random.randint(20 , 100))
   turtle.end_fill()
while True:
   for x in range(20):
       pick_loc()
       pick_color()
       draw_circle()
   turtle.reset()
turtle.exitonclick()

from turtle import *
from math import sin, pi

shape('turtle')
speed(100)

penup()
goto(150,0)
pendown()
left(90)


begin_fill()
for i in range(120) :
    forward(2*150*sin(pi/120))
    left(3)
color("yellow")
end_fill()


color("black")
penup()
goto(70,70)
pendown()
begin_fill()
for i in range(90):
    forward(1.4)
    left(4)
color("blue")
end_fill()


color("black")
penup()
goto(-35,70)
pendown()
begin_fill()
for i in range(90):
    forward(1.4)
    left(4)
color("green")
end_fill()


color("black")
penup()
goto(0,20)
pendown()
left(180)
width(15)
forward(40)


color("red")
penup()
goto(60,-30)
pendown()
for i in range(int(90/2)):
    forward(2*60*sin(pi/90))
    right(4)


mainloop()
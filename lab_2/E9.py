from turtle import *
from math import sin, pi

shape('turtle')
speed(100)
for i in range(3,13):
    left(90+180/i)
    forward(2*(20*(i-2))*sin(pi/i))
    for j in range(i-1):
        left(360/i)
        forward(2*(20*(i-2))*sin(pi/i))
    penup()
    goto(20*(i-2),0)
    pendown()
    right(90-180/i)
mainloop()
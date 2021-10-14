from turtle import *

shape('turtle')
speed(100)
penup()
goto(-300,0)
pendown()
left(90)
for j in range(1,6):
    for i in range(60):
        forward(3)
        right(3)
    for i in range(60):
        forward(0.5)
        right(3)

mainloop()
from turtle import *

shape('turtle')
speed(100)
left(90)
for j in range(1,10):
    for i in range(120):
        forward(2+j/3)
        left(3)
    for i in range(120):
        forward(2+j/3)
        right(3)
mainloop()
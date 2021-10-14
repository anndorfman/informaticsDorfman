from turtle import *

shape('turtle')
speed(100)
for j in 1,2,3:
    for i in range(45):
        forward(10)
        left(8)
    for i in range(45):
        forward(10)
        right(8)
    left(60)

mainloop()
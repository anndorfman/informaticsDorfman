from turtle import *

n=int(input("Введите число лап: "))
shape('turtle')
speed(4)
for i in range(n):
    forward(100)
    stamp()
    backward(100)
    left(360/n)
mainloop()
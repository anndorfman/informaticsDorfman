import math

def y(x):
    return math.log(math.e**(1/(math.sin(x)+1))/(5/4+x**(-15)) , 1+x**2)
y1=y(1)
y10=y(10)
y1000=y(1000)
print(y1,y10,y1000)
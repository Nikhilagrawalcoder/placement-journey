import math
x1=eval(input("enter coordinate x1"))
y1=eval(input("enter coordinate y1"))
x2=eval(input("enter coordinate x2"))
y2=eval(input("enter coordinate y2"))
x=x2-x1
y=y2-y1
out=x**2+y**2
distance=out**0.5
print(f'distance between coordinate({x1},{y1}) and ({x2},{y2}) is {distance:.5f}')
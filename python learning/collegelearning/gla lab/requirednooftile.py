import math
l1=eval(input("enter length of room"))
b1=eval(input("enter breadth of room"))
l2=eval(input("enter length of tile"))
b2=eval(input("enter breadth of tile"))
arearoom=l1*b1
areatile=l2*b2
no=(-arearoom//areatile)

print(f'no of tiles required {-no}')
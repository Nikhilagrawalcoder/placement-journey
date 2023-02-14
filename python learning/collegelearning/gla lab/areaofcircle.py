import math
#input section
r=eval(input("enter radius"))

#logic section
a=math.pi*r*r
area=round(a,3)
#display section
print(f'area of circleof radius {r}is{area:.2f}')
import math
r=5

h=10
v=15
volume= math.pi *h*r**2

time=eval(input("enter time"))
if(v*time<volume):
    print(f'underflow')
    print(f'filled height',(v*time)/math.pi*r**2)
    print(f'remaining height',(10-((v*time)/math.pi*r**2)))
elif(v*time==volume):
    print("full")
else:
    print(f'overflow volume is{v*time-(volume)}')        

a=int(input())
b=int(input())
c=int(input())
d=int(input())
max=a
if(b>max):
    if(c>max):
         if(d>max):
           max=d
         else:
            max=c
    else:
        max=b  
else:
    max=a             
print(max)
#pass is used as a continue in python


           
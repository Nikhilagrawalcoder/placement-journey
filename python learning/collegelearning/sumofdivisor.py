a=eval(input("enter no "))
c=0
for i in range(1,a+1):
    if(a%i==0):
        c=c+i
print(c)        
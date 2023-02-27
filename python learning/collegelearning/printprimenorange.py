def prime(n):
    c=0
    for i in range (1,n+1):
        if(n%i==0):
            c=c+1
    if(c==2):
        return 1
    else:
        return 0
a=eval(input("enter first no"))
b=eval(input("enter second no"))
for i in range(a,b+1):
    k=prime(i)
    if(k):
        print(i)
    else:
        continue    

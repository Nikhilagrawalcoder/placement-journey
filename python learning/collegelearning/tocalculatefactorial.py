def fact(n,sum,i):
    if(i <=n):
          fact(n,sum*i,i+1)
    else:
        return sum*i 

n =5
sum =1
i =1
print(fact(n,sum,i))
l =0
def fact(n,sum,i):
    if(i <=n):
        print(sum)
        l = l+sum
        fact(n,sum*i,i+1)
    else:
        return l

n =5
sum =1
i =1
print(fact(n,sum,i))
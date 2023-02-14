def compare(a,b):
    if(a>b):
        return a
    else:
        return b   
def avg(c,d):
    av=(c+d)/2
    return av

a=eval(input("enter no1"))
b=eval(input("enter no2"))
k=compare(a,b)
print(f'greatest no is {k}')
o=avg(a,b)
print(f'avg of {a} and {b} is {o}')
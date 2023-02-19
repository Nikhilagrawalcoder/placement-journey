a=eval(input("enter first number :"))
b=eval(input("enter second number :"))
c=eval(input("enter third number :"))
out=a if(a>=b and a>=c) else b if(b>=c and b>=a) else c
print(f'max number between three number between {a},{b},{c} is {out}')
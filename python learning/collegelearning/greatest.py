a=eval(input("enter first number"))
b=eval(input("enter second number"))
c=eval(input("enter third number"))
out=print(a) if a>=b and a>=c else print(b) if b>=c and b>=a else print(c)

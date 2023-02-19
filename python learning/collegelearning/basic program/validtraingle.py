a=eval(input("enter first side length:"))
b=eval(input("enter second side length:"))
c=eval(input("enter third side length:"))
if(a+b>c or a+c>b or b+c>a):
    print("triangle is valid")
else:
    print("triangle is not valid")    
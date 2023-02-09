import math
a = int(input("enter the number "))
c =a
b = math.log10(a)+1
print(b)
sum =0
while(a>0):
    d=a%10
    sum = sum +  (d**b)
    print(sum)
    a=a//10
    print(a)
if (sum == c):
    print("numebr is armsstrong")
else:
    print("number is not armstriong")
a=int(input())
b=int(input())
c=int(input())
k=(a+b+c)/3
if(k>100):
    print("invalidinput")
elif(k>=40):
    if(a>=33 and b>=33 and c>=33):
     print("pass")
else:
    print("Fail")

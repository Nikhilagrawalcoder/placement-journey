s={}
a=input()
b=input()
c=input()
d=input()
updict={
    "nikhil":a,
    "harsh":b,
    "deepanshu":c,
    "charchit":d
}
s.update(updict)
k=input()
print(s.get(k))
#if two freind have same name then it will update the value of that freind  not define all the values 
#if language of two freind are same then it will not affect as we gave input as a key which is not same for both
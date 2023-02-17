ls=[1,2,3,4,5,6,7,8]
i=0
for i in range (len(ls)):
    print(ls[i])
    i=i+1
# ls=[]
# i=0
# for i in range (5):
#     ls[i]=eval(input("enter"))
#     i=i+1
if 5 in ls:
    print(True)
else:
    print(False)
print(ls[1:5:2]) 
print(ls[1:-1])       
    
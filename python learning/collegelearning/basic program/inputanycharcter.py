a=eval(input("enter input: "))
if(a>="a" and  a<='z' or a<='Z'and a>='A'):
    print(f'{a} is alphabet')
elif(a>=0 and a<=9):
    print(f'{a} is number')
else:
    print(f'{a} is special character ')        
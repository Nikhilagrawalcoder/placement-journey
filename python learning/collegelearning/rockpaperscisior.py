a=input()
b=input()
c=input()
d=input()
if((c=='rock'and d=='scisoor') or (c=='paper' and d=='stone' ) or (c=='scisoor' and d=='paper')):
    print(f'{a} Win')
elif((c=='scisoor' and d=='rock') or (c=='stone' and d=='paper') or (c=='paper' and d=='scisoor')):
    print(f'{b} Win')
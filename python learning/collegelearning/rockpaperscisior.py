import random
a=(input("enter player 1 name"))
# b=(input("enter player 2 name "))
b="computer"
c=(input("enter player one choice"))


randno= random.randint(1, 3) 
if randno == 1:
    d = 'rock'
elif randno == 2:
    d= 'paper'
elif randno == 3:
    d = 'scisoor'






if((c== 'rock' and d=='scisoor') or (c=='scisoor' and d=='paper') or(c=='paper' and d=='rock')):
    print(f'{a}player wins')
if((d== 'rock' and c=='scisoor') or (d=='scisoor' and c=='paper') or(d=='paper' and c=='rock')):
    print(f'{b}player wins')    
else:
    print(f'{b} player tie with {a} player')



from builtins import int
import time

a=int(time.strftime("%H"))
b=time.strftime("%M")
c=time.strftime("%S")
if(a>=0 and a<=11):
    print("Good morning")
elif(a>=12 and a<=14):
    print("Good afternoon")
elif(a>=15 and a<=19):
    print("Good evening")
else:
    print("Good night")            

amount=eval(input("enter amount:"))
k=amount-100
a=k//2000
k=k-2000*a
b=k//500
k=k-500*b
c=k//200
k=k-200*c
d=k//100
print(f'current notes in amount {amount} is\n2000 {a}\n500is {b}\n200 is{c}\n100 is {d+1}')

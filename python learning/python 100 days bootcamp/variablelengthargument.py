def avg(*no):
    print(type(no))
    sum=0
    for i in no:
        sum=sum+i
        
    print(f'avg of number is {sum/len(no)}')

avg(5,6,7,5,6)        
# here * is unpacked the tupple
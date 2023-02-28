a=''
n=5
for i in range(n):
    a=a+chr(65+i)
for i in range(n):   
    print(a[:n-i])
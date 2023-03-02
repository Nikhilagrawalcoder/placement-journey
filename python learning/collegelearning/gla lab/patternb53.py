n=5
for i in range(n):
    if(i==0 or i==n-1):
        print(chr(65+i)*(i+1))
    else:
        print(chr(65+i),"  "*(i-1),chr(65+i),sep='') 
try:
    a=int(input("x="))
    b=int(input("y="))
    c=int(input("z="))

    for i in range (a,b+1,c):
        print(i)
except:
    print("Invalid input")


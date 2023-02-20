def func():
    try:
        l=[1,2,3,4]
        i=eval(input("enter index value:"))
        print(l[i])
        return 1
    except:
        print("Input error ocuured")
        return 0
    finally:
        print("i am always ready to be exceuted")
x=func()
print(x)                
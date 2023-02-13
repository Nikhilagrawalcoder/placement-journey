from builtins import int


a=int(input())
match a:
    case 0:
        print("Value of a  is 0")
    case _ if(a==1):
        print("value of a is 1")
    case _:
        print("value of a is ",a)    


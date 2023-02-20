a=(input("enter the number"))
print(f'multiplication table was ')
try:
    for i in range(1,11):
        print(f'int({a}) X {i}={int(a)*i}')
except Exception as e:
    print(e)
print("some imp line of code") 
print("end of program")   


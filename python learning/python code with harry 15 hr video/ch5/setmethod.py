a=set()
print(a)
a.add(5)
a.add(6)
print(a)
a.add((1,2,30))
print(a)
#cannot add dictionary and list as it is not hashable
print(len(a)) #length of set
# a.remove(5)
# print(a)
print(a.pop())
print(a.clear())

mydict={
    "fast":"in a quick manner",
  "harry":"it is good coder",
  "marks":[1,2,5],
  "anotherdict" :  {'harry':'coder'},
  1:2
}

# print(list(mydict.keys())) #print the keys of the dictionaries
# print(mydict.values()) #prints the value of all the keys 


print(mydict.items()) #print the key and value for all the content 

#update the value of dict 

updatedict={
"lovish":'freind',

}


mydict.update(updatedict)
print(mydict)
print(mydict.get("lovish2"))
#.get method give none in result
# square bracket return error






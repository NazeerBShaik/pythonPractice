# without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

#with list comprehension you can do all that with only one line code:
fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)        

# returns ture if conditon is ture
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#with no if statement
newlist = [x for x in fruits if x != "apple"]
newlist = [x for x in fruits]
print(newlist)

#iterable using range() function
newlist = [x for x in range(10)]
print(newlist)
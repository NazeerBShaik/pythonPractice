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
#iterable using range() with condition
newlist = [x for x in range(10) if x < 5]
print(newlist)
#expression 
newlist = [x.upper() for x in fruits]
newlist = [x.lower() for x in fruits]
newlist = [x.capitalize() for x in fruits]
print(newlist)
#we can set values to a new list 
newlist = ['hello' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]
newlist = [x for x in fruits if x == 'banana']
#sort list alphanumarically
newlist = ["apple","banana","cherry","kiwi","mango"]
newlist.sort()
newlist.sort( reverse = True)
print(newlist)
#Customize sort fuction
#sort the list based on how close the number is to 50
def myfunc(n):
    return abs(n-50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key= myfunc)
fruits = ["apple","banana","cherry","kiwi","mango"]
print(thislist)
# by default case sensitive sorting can give an unexpected result
thislist = ["banana","Orange","Kiwi","cherry"]
thislist.sort()
print(thislist)
#Perform a case-sensitive sort of the list
thislist = ["banana","Orange","Kiwi","cherry"]
thislist.sort(key= str.lower)
print(newlist)
#reverse order
thislist = ["banana","Orange","Kiwi","cherry"]
thislist.reverse()
print(thislist)
#copy a list
thislist = ["banana","Orange","Kiwi","cherry"]
mylist = thislist.copy()
print(mylist)
#another way to copy a list by using list()method
thislist = ["banana","Orange","Kiwi","cherry"]
mylist = list(thislist)
print(mylist)
#make a copy of a list with the [:]operator
thislist = ["banana","Orange","Kiwi","cherry"]
mylist = thislist[:]
print(mylist)
#join two lists
list1 = ["a","b","c"]
list2 = [1,2,3]

list3 = list1 + list2
print(list3)
#another way to add two lists by using append()method
list1 = ["a","b","c"]
list2 = [1,2,3]

for x in list2:
    list1.append(x)
print(list1)    
#we can use extend() method to add elements from one list to another list
list1 = ["a","b","c"]
list2 = [1,2,3]
list1.extend(list2)
print(list1)

















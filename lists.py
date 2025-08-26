mylist = ["apple","banana","cherry"]
print(mylist)
# To know the lenghe of a list
print(len(mylist))
# To know the type of a list
print(type(mylist))
# To access items
print(mylist[2])
# Check if item is exist
if "apple" in mylist:
    print("yes, 'apple' is in the fruits list")
# Change item value
mylist[1] = "blackcurrent" 
print(mylist)
# Change a range of item values
myList = ["apple","banana","cherry","orange","kiwi","mango"]
myList[1:3] = ["blackcurrent","watermelon"]
# To insert an item
myList.insert(2, "watermelon")
# To append items
myList.append("guva")
# To extend list
myList2 = ["sapota","grapes"]
myList.extend(myList2)
print(mylist)
# mylist.remove("banana")
myList.pop(1)
# del keyword also can remove specified index
#it can also deletes entire list
del myList[3]
# to clear the list 
myList.clear()
print(myList)

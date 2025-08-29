#dictionary using by key 
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1995
}
print(thisdict["brand"])
#using get() method
x = thisdict.get("model")
print(x)
#using keys() method
x = thisdict.keys()
print(x)
#add a new item to the dictionary
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
x = car.keys()
print(x)
car["color"] = "white"
print(x)
#get values
x = thisdict.values()
print(x)
#make change th original dictionary
car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
y = car.values()
car["year"] = 2020
print(y)
#get items using items()method
y = car.items()
car["year"] = 2022 #change the value
print(y)
#Check if keys exist
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
# update dictionary
thisdict.update({"year" : 2003})
print(thisdict)
#remove item by using pop() method removes by specified keynames
thisdict.pop("model")
print(thisdict)
#popitem() method removes last inserted item
thisdict.popitem()
print(thisdict)
#to clear a dictionary we use clear()method
# thisdict.clear()
print(thisdict)
#looping through dictionary
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1995
}
for x in thisdict:
    print(x)
#to print value in the dictionary one by one by using loop
for x in thisdict:
    print(thisdict[x])
#Loop through the both the keys and values by using items() method
for x, y in thisdict.items():
    print(x,y)
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
    print(x,y,"yes")
#copy dictionary
mydict = thisdict.copy()
print(mydict,"copy method") 
#copy dictionary by using dict() function   
mydict = dict(thisdict)
print(mydict,"dict function")
#Nested dictionaries
myfamily = {
    "child1" :{
        "name" : "Email",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" :{
        "name" : "Linus",
        "year" : 2011
    }
}
print(myfamily)
#If you want to add three dictionaries into a new dictionary
child1 = {
        "name" : "Email",
        "year" : 2004
}
child2 = {
        "name" : "Tobias",
        "year" : 2007
},
child3 = {
        "name" : "Linus",
        "year" : 2011
}
# myfamily = {
#    "child1" : child1,
#    "child2" : child2,
#    "child3" : child3
# }
# print(myfamily,"nested2")
#access items in nested dictionaries
print(myfamily["child1"]["year"])
#Loop through nested dictionaries using items()method
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ' :', obj[y])
#fromkeys(method)        

#clear()method
x = myfamily.clear()
print(x, "cleared dict")        

        
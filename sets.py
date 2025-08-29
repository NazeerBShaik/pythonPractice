#access set items
thisset = {"apple","banana","cherry"}

for x in thisset:
    print(x)
#check if banana is present in the set, its prints true if exist
thisset = {"apple","banana","cherry"}
print("banana" in thisset)    

#adding a new tiem to a set
thisset = {"apple","banana","cherry"}
thisset.add("orange")
print(thisset)
#adding sets
thisset = {"apple","banana","cherry"}
tropical = {"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)
#remove item
thisset = {"apple","banana","cherry"}
thisset.remove("apple")
print(thisset)

#join sets by using union() method
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)
#JOIN USING | OPERATOR
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1 | set2
print(set3)
#join multiple sets by using union() method
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = {"John","Elena"}
set4 = {"apple","bananas","cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
#join a set and a tuple
x = {"a","b","c"}
y = {1,2,3}

z = x.union(y)
print(z)
#join using update()METHOD
set1 = {"a","b",1,"c"}
set2 = {1,2,3,"c"}
set1.update(set2)
print(set1)
#join using intersection method
set1 = {1,2,3,4}
set2 = {2,5,6,7}
set3 = set1.intersection(set2) | (set1 & set2)
print(set3)
#using diffresnce() method the "|" operater refers the or meaning
set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set3 = set1.difference(set2) | set1 - set2
print(set3)
#symmetric_difference() method
set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set3 = set1.symmetric_difference(set2) | set1 ^ set2
print(set3)


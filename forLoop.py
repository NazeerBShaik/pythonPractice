# for loop example
fruits = ["apple","banana","cherry"]
for x in fruits: print(x)
#looping through a string 
for x in "fruits": print(x)
# The break statement we can stop the loop before it has looped through all the items
for x in fruits: 
    print(x)
    if x == "banana":
     break
#Exit the loop when x is "banana", but this time the break comes before the print:
for x in fruits: 
    if x == "banana":
     break   
    print(x)
#The continue statement we can stop the current iteration of the loop, and continue with the next
for x in fruits:
   if x == "banana":
      continue
   print(x)
#range() Function
for x in range(6): print(x)
# between two parameters
for x in range(2, 6): print(x)
# increment value by adding third parameter
for x in range(2, 30, 3):
   print(x)
#Else in For loop
for x in range(6):
   print(x)
else :
   print("Finally finished")
# Nested Loops
adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"] 

for x in adj:
   for y in fruits:
      print(x,y)
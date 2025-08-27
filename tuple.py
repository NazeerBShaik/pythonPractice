#example for tuple
thistuple = ("apple","ban"
"ana","cherry")
print(thistuple)
#type check
print(type(thistuple))
#How to change a tuple value
x = ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#add items to a tuple
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
#add tuple to a tuple
thistuple = ("apple","banana","cherry")
y = ("orange",)
thistuple += y
print(thistuple)
#remve items in tuple
thistuple = ("apple","banana","cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
#delete the tuple completely by using del keyword
thistuple = ("apple","banana","cherry")
del thistuple
# print(thistuple)
#unpacking
fruits = ("apple","banana","cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#asterisk another example
fruits = ("apple","banana","cherry","strawberry","rasberry")
(green, *yellow, red) = fruits
print(green)
print(yellow)
print(red)
#loop through tuple
fruits = ("apple","banana","cherry","strawberry","rasberry")
for x in fruits:
    print(x)
#loop through the index numbers
thistuple = ("apple","banana","cherry")
for i in range(len(thistuple)):
    print(thistuple[i])    
#using while loop
thistuple = ("apple","banana","cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1
    
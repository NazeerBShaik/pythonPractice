#stings are arrays , accessing elements in a string
a = "Hello World"
print(a[3])
#Looping through a string
for x in "banana":
    print(x)
#String length
a = "Hello World!"
print(len(a))
#Check String
txt = "The best things in life are free!"
print("free" in txt)
#Use it in an if statement
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present,")
#check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)
#use it in an if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
#slicing strings
b = "Hello, World!"
print(b[2:5])
#slice from the start
b = "Hello, World!"
print(b[:5])
#slice from the end
b = "Hello, World!"
print(b[3])


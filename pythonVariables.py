#examples of variables declearing
#integers
a=10
b=20
print(a+b)
#sting
a="nazeer"
b="rahul"
print(a+b)
#float
a=0.10
b=20.10
print(a+b)
#unpack a collection
fruits = ["apple","banana","cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)
#Global variables
X = "awsome"
def myfunc():
    print("Python is "+ X)

myfunc()
#Local variables
x = "awsome"

def myfunc():
    x = "factastic"
    print("python is " + x)

myfunc()
print("python is "+ x)
#global key word 
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is "+ x)
#to change the value of a global variable inside a functon
x = "awsome"

def myfunc():
    global x 
    x = "fantastic"

myfunc()
print("Python is "+ x)

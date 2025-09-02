# A function is defined using the def keyword
def my_func():
    print("Hello from a function")

my_func()
# Arguments 
def my_func(fname):
    print(fname + " Assigned")

my_func("nazeer")
my_func("basha")
# Arbitrary arguments or *args 
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("nazeer","habida","abbu")
#keyword arguments you can also send arguments with the key = value syntax
#this way the order of the argument doesnt matter
def my_funct(child3, child2, child1): 
    print("The youngest child is " + child3)

my_funct(child1="nazeer", child2="habida",child3="abbu")    
# Arbitrary Keyword Arguments, **kwargs / it will receive a dictionary if arguments
def my_func(**kid):
    print("His last name is " + kid["lname"])
my_func(fname = "nazeer", lname = "shaik")
#Default parameter value
def my_country(country = "Norway"):
    print("I am from " + country)

my_country("India")
my_country()
#Passing a list in an argument
def my_fuction(food):
    for x in food:
        print(x)

fruits = ["apple", "banana","cherry"]

my_fuction(fruits)
# Retrun a value
def math(x):
    return 5 * x
print(math(3))
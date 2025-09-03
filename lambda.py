# lambda function
x = lambda a : a + 10
print(x(5))
# it can take any number of arguments
x = lambda a,b : a * b
print(x(5, 6))
##############################
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
#double number
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
#triple the number
def myfunc(n):
    return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(22))
#same function definition to make both functions in the same program
def myfunc(n):
    return lambda a : a * n 

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(22))
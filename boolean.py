print(10>9)
print(10 == 9)
print(10<9)
print(bool("Hell0"))
print(bool(23))

a = 200
b = 33
if b>a:
    print("b is greater than a")
else:
    print("b is not greater thn a ")


#len function while using bool

class myclass():
    def _len_(self):
        return 0
myobj = myclass()
print(bool(myobj))    
        
def myFunction():
    return True
print(myFunction())
###########################
def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!") 
#############################
x = 200
print(isinstance(x, int))

#Python OOPs concept
#create a class named MyClass, with a property named x
class MyClass:
    x = 5

print(MyClass)
#create an object named p1, and print the value of x
p1 = MyClass()
print(p1.x)
#CREATE A CLASS NAMED PERSON USE THE _init_() METHOD TO ASSIGN VALUES FOR NAME AND AGE
class  Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# if condition
a = 30 
b= 300
if b > a: #if statement without indentation will rise an error
    print("b is greater than a")    
# Elif condition  means if the previous condition were not ture then try this
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")    
    
# Else cates anything which isnt caught by the preceding condition
a = 300
b = 33
if b > a:
    print("b is greater than a")    
elif a == b:
    print("a and b are equal")
else: print("a is greater than b") #shot hand wrighting       
#Shot hand If...Else
print('A') if a > b else print("B")
#You can also have multiple else statements in the same line
print("A") if a > b else print("=") if a == b else print("B")
# And keyword is a logical operator and is used to combine conditional statements
c = 400
if a > b and c > a: print("Both condition are True")
# Or keyword
if a > b or a > c:print("At least one of the condition id True")
# Not keyword
a = 33
b = 300
if not a > b: print("a is Not greater than b")
# You can have if statemt inside if statements this is called nested if statement
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!") 
    else: 
        print("but not above 20.")

#short hand for if else stat
print("and also above 20!") if x > 20 else print("but not above 20.")
# Pass Statement if statements cannot be empty but if you for some reason have an if statement with no content put in the pass statement to avoid getting an error
if b > a:
    pass

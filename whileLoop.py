# while loop
i = 1
while i < 6:
    print(i)
    i += 1 
#break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break #With the break statement we can stop the loop even if the while condition is true 
    i += 1     
#The continue statement
i = 1
while i < 6:
    i += 1     
    if i == 3:
        continue #we can stop the current iteration, and continue with the next
    print(i,"break")
#with else we can run a block of code once when the condition no longer is true
i = 1
while i < 6: 
    print(i)
    i += 1  
else:
    print("i is no longer less than 6") 
